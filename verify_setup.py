"""
Verification script to ensure all components are working before GitHub upload.
Run this script to perform a complete system check.
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    exists = os.path.exists(filepath)
    status = "OK" if exists else "FAIL"
    print(f"  [{status}] {description}: {filepath}")
    return exists

def check_directory_exists(dirpath, description):
    """Check if a directory exists and print status."""
    exists = os.path.isdir(dirpath)
    status = "OK" if exists else "FAIL"
    print(f"  [{status}] {description}: {dirpath}")
    return exists

def main():
    print("=" * 60)
    print("AI-DRIVEN HOTEL INVOICE PROCESSING PIPELINE")
    print("GitHub Upload Verification")
    print("=" * 60)
    
    root = Path(__file__).parent
    all_checks_passed = True
    
    # Check core scripts
    print("\n1. CORE SCRIPTS")
    scripts = [
        ("run_pipeline.py", "Main pipeline script"),
        ("process_all_images.py", "Batch processing script"),
        ("process_one_by_one.py", "Interactive processing script"),
        ("extract_images.py", "PDF extraction script"),
        ("combine_all.py", "Result aggregation script"),
    ]
    for script, desc in scripts:
        if not check_file_exists(root / script, desc):
            all_checks_passed = False
    
    # Check documentation
    print("\n2. DOCUMENTATION")
    docs = [
        ("README.md", "Main README"),
        ("PROJECT_SUMMARY.md", "Project summary"),
        ("GITHUB_UPLOAD_GUIDE.md", "Upload guide"),
        ("LICENSE", "License file"),
        (".gitignore", "Git ignore file"),
    ]
    for doc, desc in docs:
        if not check_file_exists(root / doc, desc):
            all_checks_passed = False
    
    # Check dependencies
    print("\n3. DEPENDENCIES")
    if not check_file_exists(root / "requirements.txt", "Requirements file"):
        all_checks_passed = False
    
    # Check sample data
    print("\n4. SAMPLE DATA")
    if not check_file_exists(root / "sample_invoice.png", "Sample invoice"):
        all_checks_passed = False
    if not check_directory_exists(root / "extracted_images", "Extracted images folder"):
        all_checks_passed = False
    else:
        img_count = len(list((root / "extracted_images").glob("*")))
        print(f"      Found {img_count} sample images")
    
    # Check output folder
    print("\n5. OUTPUT FOLDER")
    if check_directory_exists(root / "output", "Output folder"):
        output_files = list((root / "output").glob("*"))
        print(f"      Contains {len(output_files)} files")
    
    # Check Python version
    print("\n6. PYTHON VERSION")
    py_version = sys.version_info
    if py_version.major >= 3 and py_version.minor >= 11:
        print(f"  [OK] Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    else:
        print(f"  [FAIL] Python {py_version.major}.{py_version.minor}.{py_version.micro} (3.11+ required)")
        all_checks_passed = False
    
    # Check Tesseract
    print("\n7. TESSERACT OCR")
    try:
        import pytesseract
        tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        if os.path.exists(tesseract_path):
            print(f"  [OK] Tesseract found at: {tesseract_path}")
        else:
            print(f"  [WARN] Tesseract not found at default path")
            print(f"      Update path in run_pipeline.py if needed")
    except ImportError:
        print("  [FAIL] pytesseract not installed")
        all_checks_passed = False
    
    # Check required packages
    print("\n8. REQUIRED PACKAGES")
    
    import_map = {
        "opencv-python": "cv2",
        "pytesseract": "pytesseract",
        "pandas": "pandas",
        "numpy": "numpy",
        "scikit-learn": "sklearn",
        "Pillow": "PIL",
        "openpyxl": "openpyxl",
        "pymupdf": "fitz"
    }
    
    for package, module_name in import_map.items():
        try:
            __import__(module_name)
            print(f"  [OK] {package}")
        except ImportError:
            print(f"  [FAIL] {package} - NOT INSTALLED")
            all_checks_passed = False
    
    # Final summary
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("SUCCESS: ALL CHECKS PASSED - READY FOR GITHUB UPLOAD!")
        print("\nNext steps:")
        print("1. Review GITHUB_UPLOAD_GUIDE.md")
        print("2. Update README.md with your GitHub username")
        print("3. Update LICENSE with your name")
        print("4. Initialize git and push to GitHub")
    else:
        print("ERROR: SOME CHECKS FAILED - PLEASE FIX ISSUES BEFORE UPLOAD")
        print("\nReview the errors above and:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Ensure all required files are present")
        print("3. Run this script again to verify")
    print("=" * 60)
    
    return 0 if all_checks_passed else 1

if __name__ == "__main__":
    sys.exit(main())
