import argparse
from docx import Document
import json

def create_doc(data):
    doc = Document()
    doc.add_paragraph(f"Name: {data['name']}")
    doc.add_paragraph(f"Age: {data['age']}")
    doc.add_paragraph(f"Email: {data['email']}")
    return doc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to the input file")
    parser.add_argument("--output-file", required=True, help="Path to save the output document")
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        data = json.load(f)

    doc = create_doc(data)
    doc.save(args.output_file)
    print("Document created successfully")

if __name__ == '__main__':
    main()
