line = input()
current = ''
index = 1
for char in line:

    if char != ' ':
        current += char
        if index == 1 and current != '-':
            a = int(current)
        elif index == 2 and current != '-':
            b = int(current)
        elif index == 3 and current != '-':
            c = int(current)
    else:
        index += 1
        current = ''
if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)