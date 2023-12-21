from file_reader import read_data
import numpy as np

def find_reflection(mirror):
    for i in range(1, len(mirror)):
        difference = 0
        mirror1 = mirror[:i][::-1]
        mirror2 = mirror[i:]

        # part 1
        """        
        if mirror1 == mirror2:
            return i
        """
        # part 2
        for row1, row2 in zip(mirror1, mirror2):
            for a, b in zip(row1, row2):
                if a != b:
                    difference += 1
        if difference == 1:
            return i
        # part 2 end
    return 0

def show(mirror):
    for line in mirror:
        print("".join(line))
    print()


test_data = read_data("test.txt")
raw_data = read_data("input23_13.txt")
curr = raw_data

mirrors = []
mirror = []
total = 0

for line in curr:
    if ("." not in line and "#" not in line):
        mirrors.append(mirror)
        mirror = []
    else:
        mirror_line = list(map(str, line.strip()))
        mirror.append(mirror_line)
mirrors.append(mirror)

for mirror in mirrors:
    row, col = 0, 0
    row = find_reflection(mirror)
    mirror = list(zip(*mirror))
    col = find_reflection(mirror)
    total += 100*row + col
print(total)