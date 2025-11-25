import os
import pathlib
import sys

# Add project root to import path
PROJECT_ROOT = pathlib.Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

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
    preprocessed = preprocess_image(image_path)
    raw_text = ocr_image(preprocessed)
    fields = extract_fields(raw_text)
    df_items = parse_line_items(raw_text)
    warnings = validate_data(fields, df_items)
    if warnings:
        print(f"[{os.path.basename(image_path)}] Validation warnings:")
        for w in warnings:
            print(f"  - {w}")
    img_name = pathlib.Path(image_path).stem
    out_path = os.path.join(out_root, img_name)
    export_results(fields, df_items, output_path=out_path)
    print(f"✅ Finished {os.path.basename(image_path)} → {out_path}\n")

def main():
    images_dir = os.path.join(PROJECT_ROOT, "extracted_images")
    output_root = os.path.join(PROJECT_ROOT, "output_one_by_one")
    os.makedirs(output_root, exist_ok=True)

    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for idx, img_file in enumerate(image_files, start=1):
        img_path = os.path.join(images_dir, img_file)
        print(f"--- Processing [{idx}/{len(image_files)}]: {img_file} ---")
        process_image(img_path, output_root)
        input("Press Enter to continue to the next image...\n")

    print("\n✅ All images processed one‑by‑one. Results are in:")
    print(output_root)

if __name__ == "__main__":
    main()
