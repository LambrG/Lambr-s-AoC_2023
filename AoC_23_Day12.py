from file_reader import read_data

test_data = read_data("test.txt")
raw_data = read_data("input23_12.txt")

work_data = test_data
fib = [1, 1, 2, 3, 5, 8, 13, 21]
for line in test_data:
    i = 0

    springs, sequence = line.split()
    springs = springs.split(".")
    sequence = [int(x) for x in sequence.split(",")]
    print(springs, sequence)
    total = 0
    ways = []
    for spring in springs:        
        curr_spr = len(spring)
        curr_seq = sequence[i]
        spaces = 0
        while curr_seq < curr_spr:
            if i >= len(sequence)-1:
                break
            i += 1
            spaces += 1
            curr_seq += 1 + sequence[i]
        idx = curr_spr - curr_seq + spaces
        print(idx)
        ways.append(0 if idx < 0 else fib[idx])
    print(ways)
    input()
    total += max(ways)
    print(total)         
print(total)
input()
