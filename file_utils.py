import os, zipfile
from PyPDF2 import PdfReader
import docx

def extract_zip(uploaded_zip, extract_to):
    with zipfile.ZipFile(uploaded_zip, "r") as zip_ref:
        zip_ref.extractall(extract_to)

def read_resume_texts(folder_path):
    """Returns dict: filename -> text"""
    texts = {}
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.lower().endswith(".pdf"):
            texts[file] = extract_text_from_pdf(file_path)
        elif file.lower().endswith(".docx"):
            texts[file] = extract_text_from_docx(file_path)
        # skip anything else
    return texts

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)
