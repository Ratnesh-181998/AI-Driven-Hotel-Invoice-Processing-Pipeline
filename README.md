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

Project Link: https://github.com/Ratnesh-181998

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)

  
---


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**Licensed under the MIT License** - Feel free to fork and build upon this innovation! 🚀

---

# 📞 **CONTACT & NETWORKING** 📞


### 💼 Professional Networks

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RatneshS16497)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rattudacsit2021gate)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/32068937/ratnesh-kumar)

### 🚀 AI/ML & Data Science
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/RattuDa98)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/rattuda)

### 💻 Competitive Programming (Including all coding plateform's 5000+ Problems/Questions solved )
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ratnesh_1998/)
[![HackerRank](https://img.shields.io/badge/HackerRank-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black)](https://www.hackerrank.com/profile/rattudacsit20211)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/ratnesh_181998)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Ratnesh_181998)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/ratnesh1998)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@ratnesh138/)
[![InterviewBit](https://img.shields.io/badge/InterviewBit-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.interviewbit.com/profile/rattudacsit2021gate_d9a25bc44230/)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)





<img 
  src="https://streak-stats.demolab.com?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4"
  alt="GitHub Streak Stats"
width="48%"/>





<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">


