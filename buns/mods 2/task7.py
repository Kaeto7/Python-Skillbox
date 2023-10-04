line = input()
counter = 0
for char in line:
    if char == "1": counter += 1
    else: counter -= 1
if counter == 0: print("yes")
else: print("no")

