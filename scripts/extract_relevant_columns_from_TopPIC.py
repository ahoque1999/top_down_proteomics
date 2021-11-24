import sys
import re

toppic_file = sys.argv[1]

# look for fr3
regex_pattern = r".+fr3"

lines = []
with open(toppic_file, 'r') as file:
    for line in file:
        if re.match(regex_pattern, line):
            new_line = line.split()
            new_line = f"{new_line[1]}\t{new_line[2]}\t{new_line[6]}"
            lines.append(new_line)

output_file_name = f"extracted_{toppic_file[2:]}"

with open(output_file_name, 'w') as file:
    for line in lines:
        file.write(f"{line}\n")