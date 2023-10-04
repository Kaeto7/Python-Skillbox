line = input()
counter = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in line:
    if char == ',':
        letter = line[:counter]
        step = int(line[counter + 2:])
    counter += 1
index = alphabet.find(letter)
print(alphabet[(index + step) % 26])