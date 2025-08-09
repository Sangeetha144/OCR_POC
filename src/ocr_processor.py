import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path  
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_invoice_number(text):
    pattern = r"\b(?:Invoice|Document)\s+No\.?\s*[:\-]?\s*([\w/\-]+)"
    # Search line by line to reduce false positives
    for line in text.splitlines():
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None

def process_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
   
    text = ""
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        print(f"[INFO] Processing image: {file_path}")
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    elif file_path.lower().endswith('.pdf'):
        print(f"[INFO] Processing PDF: {file_path}")
        pages = convert_from_path(file_path, dpi=350)
        
        for i, page in enumerate(pages):
            print(f"[INFO] Processing page {i + 1} of PDF")
            page_text = pytesseract.image_to_string(page, config='--oem 3 --psm 6')
            text += page_text + "\n\n"
            return text
    else:
        raise ValueError("Unsupported file type. Please use an image or PDF.")
    
    invoice_number = extract_invoice_number(text)
    
    if invoice_number:
        print(f"Invoice Number: {invoice_number}")
    else:
        print("Invoice Number: Not found")

    return invoice_number
