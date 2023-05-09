import argparse
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="path to the input file")
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    data = json.load(f)
    print(f"Processing {args.input_file}...")
    print(f"Data: {data}")
    print("Creating output.txt file...")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open(f"output_{timestamp}.txt", "w") as outfile:
        outfile.write(f"Data: {data}\n")
    print("Done!")
