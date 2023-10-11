a = input()
print(bin(int(a))[2:], oct(int(a))[2:], hex(int(a))[2:]) if (a.isdigit()) else print("Неверный ввод")
