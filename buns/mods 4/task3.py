text = input().split()

def NOD(a, b):
    if a == 0 or b == 0:
        print(a + b)
    elif a > b: NOD(a - b, b)
    else: NOD(a, b - a)


NOD(int(text[0]), int(text[1]))
