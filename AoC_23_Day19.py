from file_reader import read_data
import re
from collections import deque


def get_approval(part, next):
    if next == "A":
        return True
    if next == "R":
        return False

    fallback = codex[next][1]
    for cond in codex[next][0]:
        i = id.index(cond[0][0])
        expression = f"{part[i]}{cond[0][1:]}"
        if eval(expression):
            return get_approval(part, cond[1])

    return get_approval(part, fallback)


test_data = read_data("test.txt")
raw_data = read_data("input23_19.txt")
curr = raw_data
id = "xmas"                 # to get index of current evaluated letter
idx = curr.index("")        # import of data gets list of strings, instructions and parts are separated by empty string
instructions = curr[:idx]   # getting first part of input data - instructions (workflows)

# creating codex - dictionary of instructions (workflows)
codex = {}

for instruction in instructions:
    name, rest = instruction[:-1].split("{")
    conditions = rest.split(",")
    fallback = conditions.pop(-1)
    rules = []
    for condition in conditions:
        rule, next = condition.split(":")
        rules.append((rule, next))
    codex[name] = [rules, fallback]


part_list = curr[idx+1:]    # getting second part of input data - parts

# creating part list
parts = []

for part in part_list:
    x,m,a,s = map(int, re.findall("\d+", part))
    parts.append((x, m, a, s))


# PART 1
evaluated = []

for part in parts:
    if get_approval(part, "in"):
        evaluated.append(sum(part))

print(sum(evaluated))


# PART 2
def eval_range(part_range, next):
    if next == "R":
        return False
    if next == "A":
        return True
    
    conditions, fallback = codex[next]
    for condition in conditions:
        key, mark, number, next_step = condition[0][0], condition[0][1], int(condition[0][2:]), condition[1]
        # if condition limit is inside evaluated range, we split the range in 2 and send both ranges into queue
        if part_range[key][0] < number < part_range[key][1]:
            part_range_1 = part_range.copy()
            part_range_1[key] = (part_range[key][0], number - 1 if mark == "<" else number)
            part_range_2 = part_range.copy()
            part_range_2[key] = (number if mark == "<" else number + 1, part_range[key][1])
            queu.append(part_range_1)
            queu.append(part_range_2)
            break # and we don't want to continue evaluating
        # we compare upper boundary of range if mark is "<" 
        # or lower boundary of range if mark is ">" and if passed, 
        # we continue evaluating next condition
        elif mark == "<":
            if eval(f"{part_range[key][1]}{mark}{number}"):
                return eval_range(part_range, next_step)
        else:
            if eval(f"{part_range[key][0]}{mark}{number}"):
                return eval_range(part_range, next_step)
    # and if everything fails, we evaluate fallback for current range
    else:
        return eval_range(part_range, fallback)


queu = deque()          # initialize Q
part_range = {
    "x" : (1, 4000),
    "m" : (1, 4000),
    "a" : (1, 4000),
    "s" : (1, 4000)
}
queu.append(part_range) # create whole range and add it to Q
total = 0               # Part 2 total initialize, 0 for addition

# main loop
while len(queu) > 0:
    curr_range = queu.popleft()                     # get the range from Q
    if eval_range(curr_range, "in"):                # if range is valid
        subtotal = 1                                # initialize subtotal, 1 for multiplication
        for min_r, max_r in curr_range.values():    # count product of range sizes 
            subtotal *= max_r - min_r + 1           # +1 to include both boundaries
        total += subtotal

print(total)