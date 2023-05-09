import os
import sys

if __name__ == '__main__':
    input_file = sys.argv[0]
    filename = os.path.basename(input_file)
    print(f"Processing {filename}")
    
    with open('output.txt', 'w') as f:
        f.write(filename)
