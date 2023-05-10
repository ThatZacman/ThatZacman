import json
import os
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input-file", required=True, help="Path to the input file")
parser.add_argument("--output-path", required=True, help="Path to save the output file")
args = parser.parse_args()

input_file = args.input_file
output_path = args.output_path

print(f"Input file: {input_file}")
if input_file:
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
else:
    print("No input file found.")

print(f"Creating output file at {output_path}...")
timestamp = time.strftime("%Y%m%d-%H%M%S")
with open(output_path, "w") as outfile:
    if input_file:
        outfile.write(f"Data: {data}\n")
    else:
        outfile.write("No input file found.\n")
print("Done!")
