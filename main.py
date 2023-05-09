import json
import os
import time

input_file = os.environ.get('INPUT_FILE')

if not os.path.exists(input_file):
    print(f"No input file found at {input_file}")
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
