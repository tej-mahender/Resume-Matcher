import PyPDF2
import docx
import re
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_text_from_pdf(file_path):
    """
    Extract text from PDF. First tries PyPDF2; if empty, uses OCR via pdf2image + pytesseract.
    """
    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print("PyPDF2 error:", e)

    # If PyPDF2 extraction failed or returned empty, fallback to OCR
    if not text.strip():
        text = ocr_pdf(file_path)
    return text

def ocr_pdf(file_path):
    """
    Extract text from PDF using OCR (pdf2image + pytesseract).
    """
    text = ""
    poppler_path = r"C:\poppler-25.07.0\Library\bin" 
    # convert_from_path will automatically find poppler if it's in system PATH
    pages = convert_from_path(file_path, poppler_path=poppler_path)
    for page in pages:
        text += pytesseract.image_to_string(page) + "\n"
    return text

def extract_text_from_docx(file_path):
    """
    Extract text from DOCX file.
    """
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        return text
    except Exception as e:
        print("DOCX error:", e)
        return ""

def normalize_text_readable(text):
    """
    Normalize text: lowercase, remove extra spaces, remove special characters (except +, ., #).
    """
    lines = text.split("\n")
    normalized_lines = []
    for line in lines:
        line = line.strip().lower()
        line = re.sub(r"\s+", " ", line)
        line = re.sub(r"[^a-z0-9+.# ]", "", line)
        if line:
            normalized_lines.append(line)
    return "\n".join(normalized_lines)

def extract_resume_text(file_path):
    """
    Main function to extract text from a resume (PDF or DOCX) and normalize it.
    """
    if file_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
    normalized_text = normalize_text_readable(raw_text)
    return normalized_text
