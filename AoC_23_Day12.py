# https://advent-of-code.xavd.id/writeups/2023/day/12/
# this helped me understand the solution
# I have written the comments myself

from file_reader import read_data
from functools import cache

@cache
def count_possibilities(pattern, lengths):
    # base cases:
    # if no pattern left, leghts of groups of # needs to be empty
    if not pattern:
        return len(lengths) == 0
    # if no leghth of groups, then in the rest of the pattern no # allowed
    if not lengths:
        return "#" not in pattern
    
    # lets split the pattern for char and the rest
    char, rest = pattern[0], pattern[1:]

    # first check for . - it is simpler, just ignore and continue
    if char == ".":
        return count_possibilities(rest, lengths)
    
    # check for # - must be first char of the group, because in the 
    # middle of the group it would be skipped by checking of the validity of group:
    if char == "#":
        group = lengths[0]
        # group is valid:
        if (
            # pattern is long enough
            len(pattern) >= group
            # no . in current potential group
            and "." not in pattern[:group]
            # if it is not end of patter then the next character can't be #
            and (len(pattern) == group or pattern[group] != "#")
        ):
            # if valid, we filled the group and we can check rest with one less group
            return count_possibilities(rest[group:], lengths[1:])
        # if not valid:
        return 0
    
    if char == "?":
        # try solution for both possibilities
        return count_possibilities("#" + rest, lengths) + count_possibilities("." + rest, lengths)


test_data = read_data("test.txt")
raw_data = read_data("input23_12.txt")

work_data = raw_data
total = 0

for line in work_data:
    springs, sequence = line.split()
    sequence = tuple(map(int, sequence.split(",")))
    subtotal = count_possibilities(springs, sequence)
    total += subtotal
      
print(total)

# Part 2
total = 0

for line in work_data:
    springs, sequence = line.split()
    sequence = tuple(map(int, sequence.split(",")))
    springs = "?".join([springs] * 5)
    sequence *= 5
    subtotal = count_possibilities(springs, sequence)
    total += subtotal
      
print(total)

