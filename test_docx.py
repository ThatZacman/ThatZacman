import argparse
from docx import Document

def create_doc(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True, help="Path to the input file")
    parser.add_argument("--output-file", required=True, help="Path to save the output document")
    args = parser.parse_args(args)

    # Your code to create the Word document goes here
    doc = Document()
    doc.add_paragraph("Hello, World!")
    
    return doc

if __name__ == '__main__':
    import sys

    args = sys.argv[1:]
    print(f"Input arguments: {args}")
    doc = create_doc(args)
    doc.save('document.docx')
    print("Document created successfully")
