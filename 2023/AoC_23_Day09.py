from file_reader import read_data

def main():
    raw_data = read_data("input23_09.txt")
    test_data = read_data("test.txt")

    total = 0
    total_part2 = 0
    step = 0
    for line in raw_data:
        sequence = get_sequence(line)
        prediction = get_prediction(sequence)
        sequence.reverse()
        history = get_prediction(sequence)
        total += prediction
        total_part2 += history
        step +=1
    print(total)
    print(total_part2)


def get_sequence(line):
    sequence = list(map(int, line.split()))
    return sequence


def get_prediction(numbers):
    previous = numbers
    next_step = get_next_step(previous)
    step_trace = [numbers[-1], next_step[-1]]
    while any(next_step) != 0:
        previous = next_step
        next_step = get_next_step(previous)
        step_trace.append(next_step[-1])
    last_digit = get_last_digit(step_trace)
    return last_digit


def get_next_step(numbers):
    next_numbers = []
    for i in range(len(numbers)-1):
        x = numbers[i+1] - numbers[i]
        next_numbers.append(x)
    return next_numbers


def get_last_digit(step_trace):
    step_trace.reverse()
    next_digit = step_trace[0]
    for i in range(len(step_trace)-1):
        next_digit += step_trace[i+1]
    return next_digit


main()