from file_reader import read_data
import numpy as np

def find_reflection(mirror):
    valid = False
    for i in range(len(mirror)-1):
        if np.array_equal(mirror[i], mirror[i+1]):
            valid = is_valid(mirror, i)
            if valid:
                break
    return i+1 if valid else 0


def is_valid(mirror, i):
    mirror1 = mirror[:i+1][::-1]
    mirror2 = mirror[i+1:]
    mirror1 = mirror1[:len(mirror2)]
    mirror2 = mirror2[:len(mirror1)]
    return mirror1 == mirror2


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
    mirror = np.rot90(mirror, k=-1)
    mirror = mirror.tolist()
    col = find_reflection(mirror)
    total += 100*row + col
print(total)