from file_reader import read_data
import re

raw_data = read_data("2022\input22_08.txt")

forrest = []

for line in raw_data:
    forrest.append(re.findall("\d", line))
    

print(forrest)