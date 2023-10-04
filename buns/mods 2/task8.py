line = input()
i = line[len(line) - 1:]
s = line[:len(line) - 2]
counter = 0
for char in s:
    if char == i: counter += 1
    else: break
print(counter)