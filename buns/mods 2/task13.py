line = input()
flag = True
odd = 0
even = 0
for char in line:
    if flag:
        odd += int(char)
        flag = False
    else:
        even += int(char)
        flag = True
print
if (odd + 3 * even) % 10 == 0: print("yes")
else: print("no")

