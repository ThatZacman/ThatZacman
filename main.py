import json
import os
import time
import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input-file", required=True, help="Path to the input file")
args = parser.parse_args()

input_file = args.input_file

print(f"Input file: {input_file}")
if input_file:
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
else:
    print("No input file found.")

# Prepare the content to be written to stdout
output_content = ""
if input_file:
    output_content = f"Data: {data}\n"
else:
    output_content = "No input file found.\n"

# Write the output content to stdout
sys.stdout.write(output_content)
