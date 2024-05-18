import os
from docx import Document

def generate_cover_letter(position: str, company: str) -> None:
    template_path = os.getenv('COVER_LETTER_TEMPLATE_PATH')
    if not template_path:
        raise ValueError('COVER_LETTER_TEMPLATE_PATH environment variable is not set')
    
    doc = Document(template_path)

    for paragraph in doc.paragraphs:
        if '[POSITION]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[POSITION]', position)
        if '[COMPANY NAME]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[COMPANY NAME]', company)
        print(paragraph.text)
    
    print(f'Generating cover letter for {position} at {company} using template at {template_path}')

if __name__ == '__main__':
    generate_cover_letter('Software Engineer', 'Google')