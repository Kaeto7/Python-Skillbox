line = input()
digits = "0123456789"
number = "+"
for char in line:
    if digits.find(char) != - 1: number += char
    else: continue
print(number)
