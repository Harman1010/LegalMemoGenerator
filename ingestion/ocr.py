import pdfplumber
from paddleocr import PaddleOCR
import os

ocr_engine = PaddleOCR()

def extract_pdf_text(pdf_path):

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages, start=1):

            text = page.extract_text()

            if text:
                pages.append({"page": page_num,"text": text})

    return pages

def extract_image_text(image_path):

    result = ocr_engine.predict(image_path)

    extracted_text = []

    try:
        for line in result[0]["rec_texts"]:
            extracted_text.append(line)

    except Exception:
        pass

    return [
        {
            "page": 1,
            "text": "\n".join(extracted_text)
        }
    ]


def process_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        pages = extract_pdf_text(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:

        pages = extract_image_text(file_path)

    else:

        raise ValueError(f"Unsupported file type: {extension}")

    return {
        "source": os.path.basename(file_path),
        "pages": pages
    }