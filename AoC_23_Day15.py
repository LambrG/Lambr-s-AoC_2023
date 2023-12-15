from file_reader import read_data
import re

def word_value(word):
    curr_val = 0
    for char in word: 
        curr_val += ord(char)
        curr_val *= 17
        curr_val = curr_val%256
    #print(f"word: {word}, value: {curr_val}")
    return curr_val
    
    
def analyze_instruction(word):
    label, operation, focus = re.findall(r'([A-Za-z]+)([=-])(\d?)', word)[0]
    return word_value(label), label, operation, int(focus) if focus else False
    

def find_lens(label, box):
    for i, lens in enumerate(box):
        if lens[0] == label:
        return i
    return None
    
    
test_data = read_data("test.txt")
raw_data = read_data("input23_15.txt")
curr = raw_data
curr = "".join(curr)
curr += ","

# PART 1

word = ""
total = 0

for char in curr:
    if char == ",":
        total += word_value(word)
        word = ""
    else:
        word += char
  
print(total)


# PART 2

laboratory = {}
curr = curr.split(",")[:-1]

for instruction in curr:
    box, label, operation, focus = analyze_instruction(instruction)
    if box in laboratory.keys():
        curr_box = laboratory[box]
    else:
        curr_box = []
    lens = (label, focus)
    if operation == "=": 
        idx = find_lens(label, curr_box)
        if idx is None:
            curr_box.append(lens)
        else:
            curr_box[idx] = lens
        laboratory[box] = curr_box
    elif operation == "-":
        idx = find_lens(label, curr_box)
        if idx is None:
            pass
        else:
            del curr_box[idx]
        laboratory[box] = curr_box
    else:
        print("Wrong instruction")
        exit()
        
total = 0
keys = sorted(list(laboratory.keys()))
for key in keys:
  if len(laboratory[key]) == 0:
    pass
  else:
    curr_box = laboratory[key]
    for i, lens in enumerate(curr_box):
      lens_power = (key+1) * (i+1) * lens[1]

      total += lens_power

print(total)


