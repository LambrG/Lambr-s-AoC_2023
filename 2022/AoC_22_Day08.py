from file_reader import read_data


raw_data = read_data("2022\input22_08.txt")
test_data = read_data("2022\\test.txt")
curr = raw_data
forrest_map = []

for line in curr:
    forrest_map.append([int(x) for x in line.strip()])
row_len = len(forrest_map[0])
col_len = len(forrest_map)

total = 0
for row in range(row_len):
    for col in range(col_len):
        current = forrest_map[row][col]        
        left = all(forrest_map[row][x] < current for x in range(col))
        right = all(forrest_map[row][x] < current for x in range(col+1, col_len))
        up = all(forrest_map[x][col] < current for x in range(row))
        down = all(forrest_map[x][col] < current for x in range(row+1, row_len))
        if any([left, right, up, down]):
            total += 1

print(total)

total = 0
for row in range(row_len):
    for col in range(col_len):
        current = forrest_map[row][col]
        left = 0
        for x in range(col-1, -1, -1):
            left += 1
            if forrest_map[row][x] >= current:
                break
        right = 0
        for x in range(col+1, col_len):
            right += 1
            if forrest_map[row][x] >= current:
                break
        up = 0
        for x in range(row -1, -1, -1):
            up += 1
            if forrest_map[x][col] >= current:
                break 
        down = 0
        for x in range(row + 1, row_len):
            down += 1
            if forrest_map[x][col] >= current:
                break
        total = max(total, left*right*up*down)


print(total)
