import argparse
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', required=True, help='Path to the input JSON file')
args = parser.parse_args()

input_file = args.input_file

print(f"Input file: {input_file}")
if os.path.exists(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
else:
    print("Input file not found.")

print("Creating output.txt file...")
timestamp = time.strftime("%Y%m%d-%H%M%S")
with open(f"output_{timestamp}.txt", "w") as outfile:
    if os.path.exists(input_file):
        outfile.write(f"Data: {data}\n")
    else:
        outfile.write("No input file found.\n")
    outfile.write("Additional content for the artifact.\n")  # Add some content
print("Done!")
