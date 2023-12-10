from file_reader import read_data

def construct_map(data):
    pipes_map = [["" for x in range(boundary_x[1])] for y in range(boundary_y[1])]
    start = ()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            pipes_map[y][x] = char
            if char == "S":
                start = (x, y)
    return pipes_map, start


def find_connector(node):
    x, y = node
    if pipes_map[y][x] in pipes:
        for direct in list(directions.keys()):
            try:
                i, j = directions[direct]
                next = pipes_map[x+i, y+j]
                if next in pipes:
                    break
            except:
                continue
    return direct
    

def get_next_node(source, direction):
    x, y = source[0] + directions[direction][0], source[1] + directions[direction][1]
    return (x, y)

def get_next_direction(source_direction, current):
    key = pipes_map[current[1], current[0]] + source_direction
    combinations = {
        "-E" : "E", "-W" : "W", 
        "|N" : "N", "|S" : "S", 
        "7N" : "W", "7E" : "S", 
        "JS" : "W", "JE" : "N",
        "FN" : "E", "FW" : "S",
        "LS" : "E", "LW" : "N"
    }
    return combinations[key]


test_data = read_data("test.txt")
raw_data = read_data("input23_10.txt")

directions = {
    "N" : (0, -1),
    "W" : (1, 0),
    "S" : (0, 1),
    "E" : (-1, 0),
}
pipes = "|-J7FL"
boundary_x = [-1, len(test_data[0])]
boundary_y = [-1, len(test_data)]
pipes_map, start = construct_map(test_data)

steps = 0
current = (-1, -1)
direction = find_connector(start)
next_node = get_next_node(start, direction)


while current != start:
    steps += 1
    current = next_node
    direction = get_next_direction(direction, next_node)
    next_node = get_next_node(current, direction)

print(steps/2)