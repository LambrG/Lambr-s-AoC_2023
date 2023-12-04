from file_reader import read_data
import re

#test_data = read_data("test.txt")
raw_data = read_data("input23_04.txt")
total = 0
total_cards = 0
card_count = [0 for x in range(len(raw_data))]

for i, line in enumerate(raw_data):
    
    card_count[i] += 1
    winning_numbers = set(re.findall("\d+", line[8:].split("|")[0]))
    scrachted_numbers = set(re.findall("\d+", line[8:].split("|")[1]))
    numbers_in_both = winning_numbers.intersection(scrachted_numbers)
    exp = (len(numbers_in_both))

    if exp == 0:
        total += 0
    elif exp == 1:
        total += 1
        for h in range(card_count[i]):
            card_count[i+1] += 1
    else:
        total += 2**(len(numbers_in_both)-1)
        for h in range(card_count[i]):
            for j in range(exp):
                card_count[i+j+1] += 1

print(total)
print(sum(card_count))

