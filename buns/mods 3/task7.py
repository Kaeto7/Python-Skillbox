list = input().split()
print(True if [True for i in range(len(list)) if list[i] == list[i-1]] else False)
