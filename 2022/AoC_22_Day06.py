from file_reader import read_data

raw_data = str(read_data("2022\input22_06.txt")[0])
test = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

right = 0
marker = ""
stop = len(raw_data)
while right < stop:
    char = raw_data[right]
    right += 1
    if char in marker:
        j = marker.index(char)
        marker = marker[j+1:]
    marker += char
    if len(marker) == 14:
        break

print(right)