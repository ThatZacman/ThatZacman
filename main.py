import json
import os
import sys
import time

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print(f"No input file found: {input_file}")
else:
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
        print(f"Data: {data}")
        print("Creating output.txt file...")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        with open(f"output_{timestamp}.txt", "w") as outfile:
            outfile.write(f"Data: {data}\n")
        print("Done!")
        print(f"Output file: output_{timestamp}.txt")
