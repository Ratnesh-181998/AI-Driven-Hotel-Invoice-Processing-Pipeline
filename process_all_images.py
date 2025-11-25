import os
import sys
import pathlib

# Add the project folder to the import path so we can import from run_pipeline.py
PROJECT_ROOT = pathlib.Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

# Import the core functions from your existing pipeline
from run_pipeline import (
    preprocess_image,
    ocr_image,
    extract_fields,
    parse_line_items,
    validate_data,
    export_results,
)

def process_image(image_path: str, out_root: str):
    """Run the full pipeline on a single image and store results in a dedicated folder."""
    # 1️⃣ Pre‑process
    preprocessed = preprocess_image(image_path)

    # 2️⃣ OCR
    raw_text = ocr_image(preprocessed)

    # 3️⃣ Extract deterministic fields
    fields = extract_fields(raw_text)

    # 4️⃣ Parse line items
    df_items = parse_line_items(raw_text)

    # 5️⃣ Validation
    warnings = validate_data(fields, df_items)
    if warnings:
        print(f"[{os.path.basename(image_path)}] Validation warnings:")
        for w in warnings:
            print(f"  - {w}")

    # 6️⃣ Export – each image gets its own sub‑folder
    img_name = pathlib.Path(image_path).stem
    out_path = os.path.join(out_root, img_name)
    export_results(fields, df_items, output_path=out_path)

def main():
    images_dir = os.path.join(PROJECT_ROOT, "extracted_images")
    output_root = os.path.join(PROJECT_ROOT, "output_all")

    os.makedirs(output_root, exist_ok=True)

    # Process every PNG/JPEG image in the folder
    for fname in os.listdir(images_dir):
        if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(images_dir, fname)
            print(f"\n=== Processing {fname} ===")
            process_image(img_path, output_root)

    print("\n✅ All images processed! Results are in the folder:")
    print(output_root)

if __name__ == "__main__":
    main()
