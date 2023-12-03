from file_reader import read_data
import re

raw_data = read_data("2022\input22_05.txt")
# test_data = read_data("2022\\test.txt")
warehouse = ["" for _ in range(9)]
warehouse2 = ["" for _ in range(9)]
idx = 0
while idx < 8:
    for i, char in enumerate(raw_data[idx]):
        if char.isalpha():
            j = i//4
            warehouse[j] = char + warehouse[j]
            warehouse2[j] = char + warehouse2[j]
    
    idx += 1


final = ""
final2 = ""

for idx in range(10, 511):
    numbers = re.findall("\d+", raw_data[idx])
    crates = int(numbers[0])
    source = int(numbers[1]) - 1
    target = int(numbers[2]) - 1

    for i in range(crates):
        char = warehouse[source][-1]
        warehouse[source] = warehouse[source][:-1]
        warehouse[target] += char
    
    stack = warehouse2[source][crates*-1:]
    warehouse2[source] = warehouse2[source][:crates*-1]
    warehouse2[target] += stack


for stack in warehouse:
    final += stack[-1]

for stack in warehouse2:
    final2 += stack[-1]

print(final)
print(final2)