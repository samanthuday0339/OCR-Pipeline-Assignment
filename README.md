# Handwritten OCR + PII Extraction Pipeline

This project implements a complete end-to-end pipeline for extracting text and detecting **Personally Identifiable Information (PII)** from handwritten documents (JPEG images).

The system is robust enough to handle:
* **Doctor / clinic notes**
* **Slightly tilted pages**
* **Different handwriting styles**

---

## 🔄 End-to-End Flow

The pipeline processes images through the following stages:

1. **Input Image** (JPEG)
2. **Pre-processing** (Deskewing, CLAHE, Adaptive Thresholding)
3. **OCR** (Tesseract Engine)
4. **Text Cleaning**
5. **PII Detection** (Regex patterns + spaCy NER)
6. **Redaction** (Visual masking of PII on the original image)

---

## 📂 Project Structure

```
handwritten-ocr-pii-pipeline/
│── README.md                      # Project documentation
│── pipeline.py                    # Main pipeline code
│── requirements.txt               # Python dependencies
│── data/
│     └── samples/                 # Place your handwritten input images here
│── results/                       # Generated outputs
│     ├── *_ocr.txt                # Raw extracted text
│     ├── *_clean.txt              # Cleaned text
│     ├── *_preprocessed.png       # Debug image (thresholded)
│     └── *_redacted.png           # Final image with PII blacked out
│── pipeline_summary.json          # JSON summary of findings
```

---

## 🚀 How to Run

### 0. System Prerequisites

You must have the **Tesseract OCR engine** installed on your system before running the Python code.

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download the installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki).

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### 1. Install Python Dependencies

Install the required libraries and the English language model for spaCy.

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Setup Data

Place your handwritten JPEG images inside the `data/samples/` folder.

```bash
mkdir -p data/samples
# Copy your images here
```

### 3. Run the Pipeline

Execute the main pipeline script:

```bash
python pipeline.py
```

The pipeline will process all images found in the samples folder and save the results in the `/results` directory.

---

## 📋 Requirements File

Create a `requirements.txt` file with the following dependencies:

```
opencv-python==4.8.1.78
pytesseract==0.3.10
spacy==3.7.2
numpy==1.24.3
Pillow==10.0.0
matplotlib==3.7.2
```

---

## 🧠 Technologies Used

- **Python 3.x** - Programming language
- **OpenCV** - Image pre-processing (deskewing, noise removal, thresholding)
- **Tesseract OCR** - Core engine for extracting text from images
- **spaCy** - Natural Language Processing for Named Entity Recognition (names, organizations)
- **Regex** - Pattern matching for structured PII (emails, phone numbers, dates)
- **Pillow** - Image manipulation and redaction
- **Matplotlib** - Image visualization

---

## 📊 Outputs

For every input image, the following files are generated in the `results/` folder:

| File | Description |
|------|-------------|
| `*_ocr.txt` | Raw extracted text directly from Tesseract |
| `*_clean.txt` | Cleaned and normalized text |
| `*_preprocessed.png` | Binary preprocessed image (useful for debugging OCR quality) |
| `*_redacted.png` | Original image with black boxes over detected PII |
| `pipeline_summary.json` | Structured JSON log with all detected PII entities |

---

## ✨ Features

### Robust Pre-processing
Automatically corrects orientation for slightly tilted handwritten documents. Applies CLAHE (Contrast Limited Adaptive Histogram Equalization) for better contrast. Uses adaptive thresholding to handle varying lighting conditions.

### Multi-Style Handwriting Support
Works on cursive handwriting, block letters, and mixed writing styles.

### Comprehensive PII Detection

**Regex-based Detection:**
- 📧 **Emails** - `user@example.com`
- 📞 **Phone Numbers** - `(123) 456-7890`, `123-456-7890`
- 📅 **Dates** - `MM/DD/YYYY`, `MM-DD-YYYY`
- 🔐 **Social Security Numbers** - `XXX-XX-XXXX`
- 💳 **Credit Cards** - `XXXX-XXXX-XXXX-XXXX`

**Named Entity Recognition (spaCy):**
- 👤 **Person Names**
- 🏢 **Organization Names**
- 📍 **Geographic Locations**
- 📆 **Date Entities**

### Visual Redaction
Automatically calculates bounding boxes for detected PII words. Draws black boxes over PII directly on the original image. Preserves image quality and readability of non-sensitive content.

