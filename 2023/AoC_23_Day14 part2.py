from file_reader import read_data
import numpy as np


def main():
    test_data = read_data("test.txt")
    raw_data = read_data("input23_14.txt")
    curr = raw_data
    states_of_platform = []
    total = 0
    platform = create_np_array(curr)
    np_platform = np.rot90(platform, k=1)
    for i in range(1000000000):
        # print(f"Cyklus {i}/1 000 000 000")
        np_platform = cycle(np_platform)
        if any(np.array_equal(np_platform, arr) for arr in states_of_platform):
            print(i)
            break
        else:
            states_of_platform.append(np_platform)
    for j, arr in enumerate(states_of_platform):
        if np.array_equal(np_platform, arr):
            cycle_start = j
            break
    
    cycle_lenght = len(states_of_platform) - cycle_start
    print(cycle_lenght)
    index_of_solution = cycle_start+(1000000000-cycle_start-1) % cycle_lenght
    print(index_of_solution)
    final_state = states_of_platform[index_of_solution]
    total = 0
    for line in final_state:
        weight = len(line)
        for char in line:
            if char == "O":
                total += weight
            weight -= 1
    
    print(total)


def cycle(np_platform):
    state = "NWSE"
    for i in range(4):
        # print(state[i])
        list_of_strings = rotate(np_platform)
        platform = create_np_array(list_of_strings)
        np_platform = np.rot90(platform, k=-1)
    return np_platform


def rotate(np_platform):
    list_of_strings = []
    for line in np_platform:
        to_string = "".join(line)
        to_list = to_string.split("#")
        new_line = []
        for el in to_list:
            el = sorted(el, reverse=True)
            el = "".join(el)
            new_line.append(el)
        new_line = "#".join(new_line)
        list_of_strings.append(new_line)
    return list_of_strings


def create_np_array(list_of_strings):
    platform = []
    for line in list_of_strings:
        platform_line = list(map(str, line.strip()))
        platform.append(platform_line)
    
    return platform

main()