from file_reader import read_data
import re


test_data = read_data("test.txt")
raw_data = read_data("input23_06.txt")
total = 1

current = raw_data
times = [int(x) for x in re.findall("\d+", current[0].split(":")[1])]
distances = [int(x) for x in re.findall("\d+", current[1].split(":")[1])]
races = list(zip(times, distances))

def single_race_input(input):
    digit_list = re.findall("\d+", input.split(":")[1])
    return int("".join(digit_list))


time = single_race_input(current[0])
distance = single_race_input(current[1])
single_race = (time, distance)
print(time)


def count_possibilities(race):
    min_left = 0
    min_right = race[0]//2 + 1
    max_left = race[0]//2 
    max_right = race[0]
    while min_left < min_right:
        mid = (min_left + min_right) // 2
        distance = (race[0] - mid)*mid
        if distance > race[1]:
            min_right = mid
        else:
            min_left = mid + 1
    while max_left < max_right:
        mid = (max_left + max_right) // 2
        distance = (race[0] - mid)*mid
        if distance > race[1]:
            max_left = mid + 1
        else:
            max_right = mid
    return max_left - min_left

for race in races:
    total *= count_possibilities(race)

print(total)

print(count_possibilities(single_race)


