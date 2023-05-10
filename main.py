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

artifact_dir = os.path.join(os.environ["GITHUB_WORKSPACE"], "artifacts")
os.makedirs(artifact_dir, exist_ok=True)

output_file = os.path.join(artifact_dir, "output.txt")
print(f"Creating {output_file}...")
timestamp = time.strftime("%Y%m%d-%H%M%S")
with open(output_file, "w") as outfile:
    if input_file:
        outfile.write(f"Data: {data}\n")
    else:
        outfile.write("No input file found.\n")
print("Done!")
