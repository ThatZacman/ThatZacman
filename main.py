import json
import os
import time

input_file = os.environ.get('INPUT_FILE')

if input_file:
    with open(input_file, 'r') as f:
        data = json.load(f)
        print(f"Processing {input_file}...")
else:
    print("No input file found.")

print("Creating output.txt file...")
timestamp = time.strftime("%Y%m%d-%H%M%S")
with open(f"output_{timestamp}.txt", "w") as outfile:
    if input_file:
        outfile.write(f"Data: {data}\n")
    else:
        outfile.write("No input file found.\n")
print("Done!")
