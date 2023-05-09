import json
import sys
import os

# Get the path to the input JSON file
input_file = sys.argv[1]

# Construct the path to the output file
output_file = os.path.join(os.path.dirname(input_file), 'doc.txt')

# If the output file doesn't exist, create it
if not os.path.exists(output_file):
    with open(output_file, 'w'):
        pass

# Process the input JSON file and write the output to the output file
with open(input_file, 'r') as f:
    data = json.load(f)
    output = process_data(data)
    with open(output_file, 'w') as out_f:
        out_f.write(output)

# Print the path to the output file
print(f'Output written to {output_file}')
