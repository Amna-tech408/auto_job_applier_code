# import os
# from fpdf import FPDF

# def save_cover_letter_to_pdf(text, filename):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     for line in text.split("\n"):
#         pdf.multi_cell(0, 10, line)
#     os.makedirs(os.path.dirname(filename), exist_ok=True)
#     pdf.output(filename)

# def log_application(jobs):
#     print(f"📄 Logged {len(jobs)} applications")

import os
from fpdf import FPDF
import PyPDF2

def save_cover_letter_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf.output(filename)

def log_application(jobs):
    print(f"📄 Logged {len(jobs)} applications")

def extract_content(file_path):
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type. Only .pdf or .txt allowed.")
