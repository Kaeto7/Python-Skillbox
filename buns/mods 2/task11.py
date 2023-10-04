line = input()
idk = ""
flag = False
for char in line:
    if char == ' ': continue
    else:
        if idk.find(char) != - 1:
            flag = True
            break
        else:
            idk += char
print(flag)
