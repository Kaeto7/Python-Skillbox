line = input()
vowelsList = "ёуыеаоияэю"
vowels = consonants = 0
for char in line:
    if char != ' ' and char != 'ъ' and char != 'ь' :
        if vowelsList.find(char) != -1: vowels += 1
        else: consonants += 1
print(vowels, consonants)