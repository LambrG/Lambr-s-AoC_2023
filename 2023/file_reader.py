def read_data(file):
    data = []
    with open(file) as text_file:
        for line in text_file.readlines():
            line = line.strip()
            data.append(line)
    return data

