from file_reader import read_data
from copy import deepcopy


def construct_map(data):
    pipes_map = [["" for x in range(boundary_x+1)] for y in range(boundary_y+1)]
    start = ()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            pipes_map[y][x] = char
            if char == "S":
                start = (x, y)
                pipes_map[y][x] = "F"
    return pipes_map, start


def find_connector(node):
    where = deepcopy(directions)
    x, y = node
    if x == 0:
        del where["W"]
    if x == boundary_x:
        del where["E"]
    if y == 0:
        del where["N"]
    if y == boundary_y:
        del where["S"]
    output = ""
    for direct in list(where.keys()):
        i, j = directions[direct]
        connect_node = (x+i, y+j)
        next_value = get_map_value(connect_node)
        if next_value in pipes:
                output = get_next_direction(direct, connect_node)
                break
    return output
    

def get_next_node(source, direction):
    x, y = source[0] + directions[direction][0], source[1] + directions[direction][1]
    return (x, y)


def get_next_direction(source_direction, current):
    combinations = {
        "-E" : "E", "-W" : "W", 
        "|N" : "N", "|S" : "S", 
        "7N" : "W", "7E" : "S", 
        "JS" : "W", "JE" : "N",
        "FN" : "E", "FW" : "S",
        "LS" : "E", "LW" : "N"
    }
    key = get_map_value(current) + source_direction
    return combinations[key]


def get_map_value(node):
    x, y = node[0], node[1]
    if x == 0 or x == boundary_x:
        return ""
    if y == 0 or y == boundary_y:
        return ""
    return pipes_map[y][x]


test_data = read_data("test.txt")
raw_data = read_data("input23_10.txt")
data = raw_data
directions = {"S" : (0, 1), "E" : (1, 0), "N" : (0, -1), "W" : (-1, 0)}
pipes = "|-J7FL"
boundary_x = len(data[0])-1
boundary_y = len(data)-1
pipes_map, start = construct_map(data)
steps = 0
current = start
direction = find_connector(start)
next_node = get_next_node(start, direction)
loop = []

while next_node != start:
    steps += 1
    loop.append(current)
    current = next_node
    direction = get_next_direction(direction, next_node)
    next_node = get_next_node(current, direction)
else:
    steps += 1
    loop.append(current)
    current = next_node
    direction = get_next_direction(direction, next_node)
    next_node = get_next_node(current, direction)

for y in range(len(pipes_map)):
    for x in range(len(pipes_map[0])):
        if (x,y) not in loop:
            pipes_map[y][x] = "."

print(len(loop)//2)


count = 0
last_loop = ""

for line in pipes_map:
    inside = False
    for char in line:
        if char == "." and inside:
            count += 1
        if char in pipes[2:]:
            last_loop += char
            if len(last_loop) == 2:
                if last_loop in ["FJ", "L7"]:
                    inside = not inside
                last_loop = ""
        if char == "|":
            inside = not inside

print(count)