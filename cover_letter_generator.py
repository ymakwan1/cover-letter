import os
from docx import Document
from docx.shared import Pt
from dotenv import load_dotenv
from docx2pdf import convert

# Load environment variables from .env file
load_dotenv()

def generate_cover_letter(position: str, company: str) -> None:
    template_path = os.getenv('COVER_LETTER_TEMPLATE_PATH')
    font_size_str = os.getenv('COVER_LETTER_FONT_SIZE')
    font_name = os.getenv('COVER_LETTER_FONT_NAME')

    if not template_path:
        print("Cover letter template path not found. Please set the COVER_LETTER_TEMPLATE_PATH environment variable.")
        return

    # Convert font size to integer
    font_size = int(font_size_str) if font_size_str else None

    # Load the cover letter template
    doc = Document(template_path)

    # Find and replace placeholders with actual values
    for paragraph in doc.paragraphs:
        if '[POSITION]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[POSITION]', position)
        if '[COMPANY NAME]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[COMPANY NAME]', company)

    # Apply font settings
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if font_size:
                run.font.size = Pt(font_size)
            if font_name:
                run.font.name = font_name

    # Define the output directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the modified document as DOC
    doc_path = os.path.join(output_dir, f"cover_letter_{company}_{position}.docx")
    doc.save(doc_path)

    # Convert the Word document to PDF
    pdf_path = os.path.join(output_dir, f"cover_letter_{company}_{position}.pdf")
    convert(doc_path, pdf_path)

    print(f"Cover letter generated and saved as: {pdf_path}")

if __name__ == "__main__":
    position: str = input("Enter the desired position for the cover letter: ")
    company: str = input("Enter the name of the company: ")
    generate_cover_letter(position, company)
