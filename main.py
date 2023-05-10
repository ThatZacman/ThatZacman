import json
import os
import time

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

print("Creating output.txt file...")
timestamp = time.strftime("%Y%m%d-%H%M%S")
output_file = f"output_{timestamp}.txt"
with open(output_file, "w") as outfile:
    if input_file:
        outfile.write(f"Data: {data}\n")
    else:
        outfile.write("No input file found.\n")
print("Done!")
