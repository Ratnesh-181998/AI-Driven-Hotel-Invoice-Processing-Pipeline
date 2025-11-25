import sys
import os
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    doc = fitz.open(pdf_path)
    img_count = 0
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"page{page_index+1}_img{img_index}.{image_ext}"
            image_path = os.path.join(output_dir, image_name)
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            img_count += 1
    print(f"Extracted {img_count} images to {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_images.py <pdf_path> <output_dir>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    extract_images_from_pdf(pdf_path, output_dir)
