line = input()
counter = 0
for char in line:
    if char == ',':
        first = int(line[:counter])
        second = int(line[counter + 2:])
    counter += 1
print(first % second)
