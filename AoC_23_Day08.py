from file_reader import read_data
import re
from math import lcm

def main():
    test_data = read_data("test.txt")
    raw_data = read_data("input23_08.txt")
    cur = raw_data


    instructions = cur[0]
    sand_map = cur[2:]
    sand_map_dict, starts = constuct_map(sand_map)
    step_counts = []
    total = 1
    for start in starts:
        x = find_way_second(sand_map_dict, instructions, start)
        step_counts.append(x)

    for count in step_counts:
        total = lcm(total, count)

    print(find_way(sand_map_dict, instructions))
    print(total)



def constuct_map(sand_map):
    dictionary = {}
    pattern = re.compile(r'\b[a-zA-Z]{3}\b')
    starts = []

    for node in sand_map:

        point, left, right = pattern.findall(node)

        dictionary[point] = (left, right)
        if point.endswith("A"):
            starts.append(point)
    
    return dictionary, starts

def find_way(map, instructions):
    steps = 0
    next = "AAA"
    while next != "ZZZ":
        direction = instructions[0]
        instructions = instructions[1:] + direction
        if direction == "L":
            next = map[next][0]
        elif direction == "R":
            next = map[next][1]
        else:
            return "chyba"
        steps += 1
    return steps

def find_way_second(map, instructions, start):
    steps = 0
    next = start
    while not next.endswith("Z"):
        direction = instructions[0]
        instructions = instructions[1:] + direction
        if direction == "L":
            next = map[next][0]
        elif direction == "R":
            next = map[next][1]
        else:
            return "chyba"
        steps += 1
    return steps





main()