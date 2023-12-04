from file_reader import read_data

raw_data = read_data("2022\input22_07.txt")
# test_data = read_data("2022\\test.txt")

class Directory:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.directories = {}
        self.files = []
    
    def add_directory(self, name, parent):
        self.directories[name] = Directory(name, parent)

    def add_file(self, size, name):
        self.files.append(File(size, name))

    def count_dir_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories.values():
            size += directory.get_size()
        return size
    
    def get_size(self):
        return self.count_dir_size()

class File:
    def __init__(self, size, name) -> None:
        self.name = name
        self.size = int(size)

def construct_disk(current_directory):
    for line in raw_data:

        if line[0] == "$":
            order, name = line[2:4], line[5:]      
            if order.startswith("cd"):
                if name == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.directories[name]

        if line.startswith("dir"):
            name = line[4:]
            current_directory.add_directory(name, current_directory)

        if line[0].isdigit():
            size, name = line.split(" ")
            current_directory.add_file(size, name)

def part_one(directory):
    if len(directory.directories) == 0:
        return 0
    sum = 0
    for dir in directory.directories.values():
        sum += part_one(dir)
        if dir.get_size() < 100000:
            sum += dir.get_size()
    return sum

def part_two(directory, minimum_size, closest_size):
    current_size = directory.get_size()
    if current_size >= minimum_size and current_size < closest_size:
        closest_size = current_size
    for dir in directory.directories.values():
        closest_size = part_two(dir, minimum_size, closest_size)
    return closest_size


root = Directory("root", None)
root.add_directory("/", root)

construct_disk(root)
MINIMUM = 30000000 - (70000000 - root.get_size())
print(part_one(root))
print(part_two(root, MINIMUM, 70000000))