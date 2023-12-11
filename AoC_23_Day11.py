from file_reader import read_data
import numpy as np


def create_star_list(map):
    star_list = []
    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if col == "#":
                star_list.append((r, c))
    return star_list


def find_empty(data):
    empty_rows = []
    for row, line in enumerate(data):
        if "#" not in line:
            empty_rows.append(row)
    return empty_rows


def count_distance(star1, star2, expansion_rate):
    r1, c1 = star1
    r2, c2 = star2
    distance = abs(r2-r1) + abs(c2 - c1)
    for col in empty_cols:
        if col in range(min(c1+1, c2+1), max(c1+1,c2+1)):
            distance += expansion_rate-1
    for row in empty_rows:
        if row in range(min(r1+1, r2+1), max(r1+1,r2+1)):
            distance += expansion_rate-1
    return distance


test_data = read_data("test.txt")
raw_data = read_data("input23_11.txt")
curr = raw_data
for i, line in enumerate(curr):
    line = [char for char in line]
    curr[i] = line


star_map = curr
empty_rows = find_empty(star_map)
star_map = np.rot90(star_map, k=-1)
star_map = star_map.tolist()
empty_cols = find_empty(star_map)
star_map = np.rot90(star_map, k=1)
star_map = star_map.tolist()

star_list = create_star_list(star_map)
total_distance_1 = 0
expansion_rate1 = 2
total_distance_2 = 0
expansion_rate2 = 1000000
pair_stars = star_list[1:]

for star in star_list:
    for pair_star in pair_stars:
        total_distance_1 += count_distance(star, pair_star, expansion_rate1)
        total_distance_2 += count_distance(star, pair_star, expansion_rate2)
    pair_stars = pair_stars[1:]

print(total_distance_1)
print(total_distance_2)