# AI-Driven Hotel Invoice Processing Pipeline

An automated invoice processing system that uses OCR and machine learning to extract structured data from hotel invoice images.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- **Image Preprocessing**: Automatic deskewing, denoising, and binarization
- **OCR Integration**: Tesseract OCR for text extraction
- **Field Extraction**: Regex-based extraction of invoice numbers, dates, amounts
- **Line Item Parsing**: ML-based categorization of line items
- **Financial Validation**: Automatic validation of subtotals, tax, and totals
- **Multi-Format Export**: CSV, Excel (XLSX), and JSON outputs
- **Batch Processing**: Process multiple invoices automatically
- **PDF Support**: Extract and process images from PDF documents

## 📋 Prerequisites

- Python 3.11 or higher
- Tesseract OCR installed on your system

### Installing Tesseract OCR

**Windows:**
```powershell
winget install --id=UB-Mannheim.TesseractOCR
```

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hotel-invoice-pipeline.git
cd hotel-invoice-pipeline
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Verify Tesseract installation:
```bash
tesseract --version
```

## 💻 Usage

### Process a Single Invoice

```bash
python run_pipeline.py path/to/invoice.png
```

**Output:**
- `output/line_items.csv` - Line items in CSV format
- `output/line_items.xlsx` - Line items in Excel format
- `output/summary.json` - Extracted invoice fields

### Batch Process Multiple Images

```bash
python process_all_images.py
```

Processes all images in the `extracted_images/` folder and creates individual output folders for each.

### Extract Images from PDF

```bash
python extract_images.py "path/to/invoice.pdf" "output_directory"
```

### Combine All Results

```bash
python combine_all.py
```

Creates master files:
- `master_line_items.csv` - All line items combined
- `all_summaries.json` - All invoice summaries

## 📊 Example Output

### Extracted Fields (JSON)
```json
{
  "invoice_no": "102345",
  "date": "01/05/2023",
  "subtotal": "245.50",
  "tax": "24.55",
  "total": "270.05"
}
```

### Line Items (CSV)
```csv
description,category,price
Room Charge,service,200.00
Mini Bar,minibar,15.50
Laundry,laundry,30.00
```

## 🏗️ Project Structure

```
hotel-invoice-pipeline/
├── run_pipeline.py              # Core pipeline script
├── process_all_images.py        # Batch processing
├── process_one_by_one.py        # Interactive processing
├── extract_images.py            # PDF image extraction
├── combine_all.py               # Result aggregation
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── PROJECT_SUMMARY.md           # Detailed documentation
├── extracted_images/            # Sample invoice images
└── output/                      # Processing results
```

## 🔧 Configuration

Edit `run_pipeline.py` to customize:

- **Tesseract Path**: Update `pytesseract.pytesseract.tesseract_cmd`
- **Regex Patterns**: Modify `REGEX_PATTERNS` dictionary for different invoice formats
- **ML Classifier**: Adjust training examples in `train_dummy_classifier()`

## 📈 Pipeline Workflow

1. **Image Preprocessing**
   - Convert to grayscale
   - Denoise using fastNlMeansDenoising
   - Binarize with adaptive thresholding
   - Deskew using minAreaRect

2. **OCR Processing**
   - Extract text using Tesseract OCR
   - Page segmentation mode 3 (fully automatic)

3. **Data Extraction**
   - Regex-based field extraction
   - Line item parsing with price detection
   - ML-based categorization

4. **Validation**
   - Subtotal vs. calculated total comparison
   - Tax consistency verification
   - Warning generation for discrepancies

5. **Export**
   - CSV format for data analysis
   - Excel format for manual review
   - JSON format for API integration

## 🧪 Testing

Run the complete test suite:

```bash
# Test single invoice processing
python run_pipeline.py sample_invoice.png

# Test batch processing
python process_all_images.py

# Test result aggregation
python combine_all.py
```

## 🐛 Troubleshooting

### Tesseract Not Found Error
- Ensure Tesseract is installed
- Update the path in `run_pipeline.py`:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```

### Empty Output Files
- Check image quality (resolution, clarity)
- Verify invoice format matches regex patterns
- Review OCR text output for accuracy

### Unicode Encoding Errors (Windows)
- The script automatically configures UTF-8 encoding
- If issues persist, run PowerShell as Administrator

## 🔮 Future Enhancements

- [ ] Deep learning models (LayoutLM, BERT) for better extraction
- [ ] Table structure recognition for complex line items
- [ ] Web interface (Flask/FastAPI)
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] REST API for invoice upload
- [ ] Real-time processing dashboard
- [ ] Multi-language support
- [ ] Cloud deployment (AWS/Azure/GCP)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Your Name - Linkedin -https://www.linkedin.com/in/ratneshkumar1998/

Project Link: [https://github.com/yourusername/hotel-invoice-pipeline](https://github.com/yourusername/hotel-invoice-pipeline)

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
