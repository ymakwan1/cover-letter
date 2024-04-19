import argparse
import os
from docx import Document
from docx.shared import Pt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def setup(template_path):
    if not os.path.isfile(template_path):
        print(f"Template path {template_path} does not exist.")
        return

    os.environ['TEMPLATE_PATH'] = template_path
    print(f"Template path set to {template_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a cover letter")
    parser.add_argument('--setup', metavar='TEMPLATE_PATH', type=str, help='Set up the cover letter template path.')

    args = parser.parse_args()

    if args.setup:
        setup(args.setup)
    else:
        template_path = os.getenv('TEMPLATE_PATH')
        if not template_path:
            print("Please set up the template path first.")
            exit(1)

        print(f"Generating cover letter for {args.company} for the position of {args.position}")