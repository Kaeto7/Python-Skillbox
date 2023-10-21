text = input().split()
if len(set(text)) == 1: print("Все числа равны")
elif len(set(text)) == len(text) : print("Все числа разные")
else: print("Есть равные и неравные числа")