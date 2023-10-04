line = input()
result = ""
counter = 0
for char in line:
    if char == ' ':
        result += line[counter - 1]
    counter += 1
#Добавляем последний символ строки, тк пробела в конце нет
result += line[len(line) - 1]
print(result)