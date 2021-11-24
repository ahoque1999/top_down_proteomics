import re
import sys

extracted_toppic_file_name = sys.argv[1]
ms2_file_name = sys.argv[2]

# store annotation and charge from toppic results as a dictionary with scan number as key value
# note we did not have to store charge since we have charge in the ms2 file
annotation = {}
charge = {}

with open(extracted_toppic_file_name, 'r') as file:
    for line in file:
        split_results = line.split()
        annotation[split_results[0]] = split_results[2]
        charge[split_results[0]] = split_results[1]

regex_pattern = re.compile(r"^\d+\.\d.+")

id_count = 0
ids = []
# all lines
lines = []
masses = []
with open (ms2_file_name, 'r') as file:
    inside = False
    for line in file:
        if line[:6] == 'SCANS=':
            ID = line.split('=')[1][:-1]
            if ID not in annotation.keys():
                continue
            else:
                inside = True
                # note we append strings as a list so it is easier to add the peaks as part of this list
                # can be made better
                lines.append([f"Name: {annotation[ID]}/{charge[ID]}\n", f"Comment: Charge={charge[ID]}\n"])
                ids.append(ID)

        if inside:
            # store mass
            if line[:14] == "PRECURSOR_MASS":
                # same reasoning as peaks
                masses.append(line.split('=')[1][:-1])
            search_result = re.search(regex_pattern, line)  
            # store peaks
            if search_result:
                new_line = f"{line.split()[0]}\t{line.split()[1]}\n"
                # add each peak information into the previously generated new list
                lines[id_count].append(new_line)
        
        if line[:3] == "END" and inside:
            inside = False
            id_count += 1

# fix naming system
output_file_name = f"annotated_{ms2_file_name.split('.')[1][1:]}_using_{extracted_toppic_file_name.split('.')[1][1:]}.msp"

with open(output_file_name, 'w') as file:
    for id in range(id_count):
        num_lines = len(lines[id])
        # if no peaks then we can ignore it
        if num_lines == 2:
            continue
        for line in range(num_lines):
            # consequence of how we stored the lines and wanting to mimic the msp format to our best ability
            # can be improved
            if line == 1:
                file.write(f"MW: {masses[line]}\n")
            # same as above comment
            if line == 2:
                file.write(f"Num peaks: {num_lines - 2}\n")
            file.write(lines[id][line])
        file.write("\n")