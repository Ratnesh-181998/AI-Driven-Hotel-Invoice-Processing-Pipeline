import argparse
import os
import re
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import pytesseract
import sys
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Ensure UTF-8 output on Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Path to Tesseract executable (installed via winget)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# ------------------- Extraction Patterns -------------------
REGEX_PATTERNS = {
    "invoice_no": r"Invoice\s+No[:\s]*\s*(\d+)",
    "date": r"Date[:\s]*\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})",
    "tax_reg": r"Tax\s+Registered\s*No[:\s]*\s*(\d+)",
    "subtotal": r"Sub\s*[Tt]otal[:\s]*\s*([\d,]+\.?\d{0,2})",
    "tax": r"(?:GST|Tax)[:\s]*\s*([\d,]+\.?\d{0,2})",
    "total": r"(?:Grand\s+)?Total[:\s]*\s*([\d,]+\.?\d{0,2})",
}

# ------------------- Helper Functions -------------------

def preprocess_image(image_path):
    """Deskew, denoise and binarize the input image for better OCR."""
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=30)
    binarized = cv2.adaptiveThreshold(
        denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
    )
    # Deskew
    coords = np.column_stack(np.where(binarized > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = binarized.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    deskewed = cv2.warpAffine(binarized, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return deskewed

def ocr_image(image):
    """Run Tesseract OCR on the pre‑processed image and return raw text.
    Uses page segmentation mode 3 (fully automatic) for robustness.
    """
    try:
        pil_img = Image.fromarray(image)
        custom_config = r"--oem 3 --psm 3"
        text = pytesseract.image_to_string(pil_img, config=custom_config)
        return text
    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return ""

def extract_fields(text):
    """Extract deterministic fields from OCR text using regex patterns."""
    data = {}
    for key, pattern in REGEX_PATTERNS.items():
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            data[key] = match.group(1).strip()
    return data

# ------------------- Simple ML Classifier -------------------
def train_dummy_classifier():
    examples = [
        "Room Service - Breakfast",
        "Mini Bar - Soda",
        "Laundry Service",
        "Food & Beverage",
    ]
    labels = ["service", "minibar", "laundry", "food"]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(examples)
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, labels)
    return vectorizer, clf

def classify_line(line, vectorizer, clf):
    X = vectorizer.transform([line])
    return clf.predict(X)[0]

# ------------------- Line‑Item Parsing -------------------
def parse_line_items(text):
    """Parse lines ending with a price into structured items.
    Handles optional quantity column.
    """
    lines = text.splitlines()
    items = []
    vectorizer, clf = train_dummy_classifier()
    price_pattern = re.compile(r"([\d,]+\.?\d{0,2})$")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        price_match = price_pattern.search(line)
        if price_match:
            try:
                price = float(price_match.group(1).replace(",", ""))
                description_raw = line[: price_match.start()].strip()
                parts = description_raw.split()
                # Remove trailing quantity if it's a pure integer
                if parts and parts[-1].isdigit():
                    parts = parts[:-1]
                description = " ".join(parts)
                if description:  # Only add if description is not empty
                    category = classify_line(description, vectorizer, clf)
                    items.append({"description": description, "category": category, "price": price})
            except ValueError:
                continue
    return pd.DataFrame(items)

# ------------------- Validation -------------------
def safe_float(val):
    if isinstance(val, (int, float)):
        return float(val)
    try:
        return float(str(val).replace(",", ""))
    except Exception:
        return 0.0

def validate_data(fields, df_items):
    """Check subtotal, tax and total consistency. Return list of warnings."""
    warnings = []
    try:
        subtotal = safe_float(fields.get("subtotal", 0))
        total = safe_float(fields.get("total", 0))
        tax = safe_float(fields.get("tax", 0))
        calculated_subtotal = df_items["price"].sum() if not df_items.empty else 0.0
        if abs(calculated_subtotal - subtotal) > 0.01:
            warnings.append(f"Subtotal mismatch: OCR {subtotal} vs calculated {calculated_subtotal:.2f}")
        if abs(subtotal + tax - total) > 0.01:
            warnings.append(f"Total mismatch: subtotal+tax {subtotal+tax:.2f} vs total {total}")
    except Exception as e:
        warnings.append(f"Validation error: {e}")
    return warnings

# ------------------- Export -------------------
def export_results(fields, df_items, output_path="output"):
    os.makedirs(output_path, exist_ok=True)
    items_csv = os.path.join(output_path, "line_items.csv")
    items_excel = os.path.join(output_path, "line_items.xlsx")
    df_items.to_csv(items_csv, index=False)
    df_items.to_excel(items_excel, index=False)
    summary_file = os.path.join(output_path, "summary.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=2)
    print(f"✅ Exported line items to {items_csv} and {items_excel}")
    print(f"✅ Exported summary to {summary_file}")

# ------------------- Main -------------------
def main():
    parser = argparse.ArgumentParser(description="Run the hotel invoice processing pipeline.")
    parser.add_argument("image_path", help="Path to the invoice image (jpg/png/tif)")
    args = parser.parse_args()

    preprocessed = preprocess_image(args.image_path)
    raw_text = ocr_image(preprocessed)
    print("--- OCR TEXT START ---")
    if raw_text.strip():
        print(raw_text)
    else:
        print("[No OCR text extracted]")
    print("--- OCR TEXT END ---")

    fields = extract_fields(raw_text)
    print("Extracted fields:")
    for k, v in fields.items():
        print(f"  {k}: {v}")

    df_items = parse_line_items(raw_text)
    print(f"Parsed {len(df_items)} line items")

    warnings = validate_data(fields, df_items)
    if warnings:
        print("Validation warnings:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("Validation passed")

    export_results(fields, df_items)

if __name__ == "__main__":
    main()
