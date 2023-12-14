from file_reader import read_data

test_data = read_data("test.txt")
raw_data = read_data("input23_14.txt")
curr = raw_data

platform = []

for line in curr:
    platform_line = list(map(str, line.strip()))
    platform.append(platform_line)

platform = list(zip(*platform))

lenght = len(platform[0])
total = 0
for line in platform:
    last_free = 0
    for idx, char in enumerate(line):
        if char == "O":
            total += lenght - last_free
            last_free += 1
        elif char == "#":
            last_free = idx + 1
        else:
            continue

print(total)