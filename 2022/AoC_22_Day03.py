from file_reader import read_data

raw_data = read_data("2022\input22_03.txt")
groups = len(raw_data) // 3
total = 0

for i in range(groups):
    idx = i * 3
    set1 = set(raw_data[idx])
    set2 = set(raw_data[idx+1])
    set3 = set(raw_data[idx+2])
    first = set1.intersection(set2)
    second = first.intersection(set3)
    badge = "".join(second)
    value = ord(badge.swapcase())-64
    if value <= 26:
        total += value
    else:
        value -= 6
        total += value
    print(badge, " ", value)


print(groups)
print(total)
