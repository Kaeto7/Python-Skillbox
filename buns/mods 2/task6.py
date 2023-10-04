line = input()
a = b = c = ""
a = line[:line.find('.')]
line = line[line.find('.') + 1:]
b = line[:line.find('.')]
c = line[line.find('.') + 1:]
print(c)
print(b)
print(a)