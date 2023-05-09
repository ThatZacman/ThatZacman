import json
import os
import time

input_file = os.environ.get('INPUT_FILE')

if input_file:
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
        print(f"Data: {data}")
        print("Creating output.txt file...")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        with open(f"output_{timestamp}.txt", "w") as outfile:
            outfile.write(f"Data: {data}\n")
        print("Done!")
else:
    print("No input file specified!")
