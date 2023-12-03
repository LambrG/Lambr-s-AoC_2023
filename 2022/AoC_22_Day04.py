from file_reader import read_data

raw_data = read_data("2022\input22_04.txt")
test_data = read_data("2022\\test.txt")
count_part1 = 0
count_part2 = 0
for line in raw_data:
    first, second = line.split(",")
    first = first.split("-")
    second = second.split("-")
    if first[0] == second[0] or first[1] == second[1]:
        count_part1 += 1
        count_part2 += 1
    else:
        if int(first[0]) > int(second[0]):
            first, second = second, first
        if int(first[1]) > int(second[1]):
            count_part1 += 1
        if int(first[1]) >= int(second[0]):
            count_part2 += 1


print(count_part1)
print(count_part2)