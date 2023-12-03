from file_reader import read_data


def part_1(data):
    total = 0
    for i in range(1, len(data)-1):
        total += line_value(data[i-1], data[i], data[i+1], i)
    return total

def part_2(data):
    total = 0
    for i,j in star_locations:
        gear = extract_gears(data[i-1], data[i], data[i+1], j)
        print(gear)
        total += gear_value(gear)
    return total


def extract_gears(line1, line2, line3, index):
    values = []
    values.append(crawl(line1, index))
    values.append(crawl(line2, index))
    values.append(crawl(line3, index))
    return values

def crawl(text, index):
    start = index
    end = index
    if text[index].isdigit():
        while text[start-1].isdigit():
            start -= 1
        while text[end+1].isdigit():
            end += 1
        return text[start:end+1]
    left = text[index-1].isdigit()
    right = text[index+1].isdigit()
    left_str = ""
    right_str = ""
    if left:
        end = index
        start = end
        while text[start-1].isdigit() and start > 0:
            start -= 1
        left_str = text[start:end]
    if right:
        text += "."
        start = index + 1
        end = start
        while text[end].isdigit() and end < line_lenght:
            end += 1
        right_str = text[start:end]
    return ".".join([left_str,right_str])

def gear_value(gear):
    value = []
    total = 0
    for number in gear:
        try:
            value.append(int(number))
        except:
            number = number.split(".")
            for num in number:
                try:
                    value.append(int(num))
                except:
                    continue
    if len(value) == 2:
        total = value[0] * value[1]
    return total


def line_value(prev_line, evaluated_line, next_line, idx):
    line_value = 0
    current_number = ""
    add_number = False
    carry_symbol = False
    line_index = idx
    for i in range(line_lenght):
        char = evaluated_line[i]
        is_symbol = prev_line[i] in symbols or evaluated_line[i] in symbols or next_line[i] in symbols
        if char == "*":
            star_locations.append((line_index, i))
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

star_locations = []
data, symbols, line_lenght = prepare_data()
print(part_1(data))
print(part_2(data))
print(symbols)