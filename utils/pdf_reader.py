from pypdf import PdfReader
from utils.ocr import extract_text_with_ocr


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    # OCR fallback if no text extracted
    if text.strip() == "":
        print("No text found. Using OCR...")
        text = extract_text_with_ocr(file_path)

    return text
