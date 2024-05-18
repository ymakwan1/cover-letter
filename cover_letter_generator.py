import os

def generate_cover_letter(position: str, company: str) -> None:
    template_path = os.getenv('COVER_LETTER_TEMPLATE_PATH')
    if not template_path:
        raise ValueError('COVER_LETTER_TEMPLATE_PATH environment variable is not set')
    
    print(f'Generating cover letter for {position} at {company} using template at {template_path}')

if __name__ == '__main__':
    generate_cover_letter('Software Engineer', 'Google')