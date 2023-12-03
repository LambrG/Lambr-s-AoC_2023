from file_reader import read_data


def part_1(data, line_lenght):
    total = 0
    for i in range(1, len(data)-1):
        total += line_value(data[i-1], data[i], data[i+1], line_lenght)
    return total

def line_value(prev_line, evaluated_line, next_line, line_lenght):
    line_value = 0
    current_number = ""
    add_number = False
    carry_symbol = False
    for i in range(line_lenght):
        char = evaluated_line[i]
        is_symbol = prev_line[i] in symbols or evaluated_line[i] in symbols or next_line[i] in symbols
        if char.isdigit():
            current_number += char
            add_number = add_number or carry_symbol or is_symbol
        else:
            add_number = add_number or carry_symbol or is_symbol
            is_number = len(current_number) > 0
            if add_number and is_number:
                line_value += int(current_number)
            add_number = False
            current_number = ""
        carry_symbol = is_symbol
    add_number = add_number or carry_symbol or is_symbol
    is_number = len(current_number) > 0
    if add_number and is_number:
        line_value += int(current_number)
    return line_value            



def prepare_data():
    raw_data = read_data("input23_03.txt")
    symbols = get_symbols(raw_data)
    lenght = len(raw_data[0])
    dotted_line = line_of_dots(lenght)
    raw_data.insert(0, dotted_line)
    raw_data.append(dotted_line)
    return raw_data, symbols, lenght


def line_of_dots(lenght):
    dotted_line = ""
    for i in range(lenght):
        dotted_line += "."
    return dotted_line


def get_symbols(data):
    symbols = ".0123456789"
    for line in data:
        for char in line:
            if char not in symbols:
                symbols += char
    return symbols[11:]       


data, symbols, line_lenght = prepare_data()
print(part_1(data, line_lenght))
print(symbols)