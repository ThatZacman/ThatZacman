import argparse
from docx import Document
import json

def create_doc(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to the input file")
    parser.add_argument("--output-file", required=True, help="Path to save the output document")
    args = parser.parse_args(args)

    # Load data from JSON file
    with open(args.input_file, 'r') as f:
        data = json.load(f)

    # Extract values from JSON data
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')

    # Create the Word document
    doc = Document()
    doc.add_paragraph(f"Name: {name}")
    doc.add_paragraph(f"Age: {age}")
    doc.add_paragraph(f"Email: {email}")
    
    return doc

if __name__ == '__main__':
    import sys

    args = sys.argv[1:]
    print(f"Input arguments: {args}")
    doc = create_doc(args)
    doc.save('document.docx')
    print("Document created successfully")
