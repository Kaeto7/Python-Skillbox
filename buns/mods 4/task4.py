text = input()

def palindrom(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    middle = ""
    side = ""
    for char, value in dict.items():
        if value % 2 == 1:
            middle += char
        side += char * (value // 2)

    if len(middle)> 1: return("Это не палиндром")

    return(side + middle + side[::-1])

print(palindrom(text))