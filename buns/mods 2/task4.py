number = float(input())

#for <dec
def number_system_swaper(n, divider):
    result = ''
    while n > 0:
        result = str(n % divider) + result
        n = n // divider
    return result

def my_hex(n):
    hex_digits = "0123456789ABCDEF"
    result = ''
    while n > 0:
        result = hex_digits[n % 16] + result
        n = n // 16
    return result
if number != int(number) or number < 0:
    print("Неверный ввод")
else:
    number = int(number)
    print(number_system_swaper(number, 2), number_system_swaper(number, 8), my_hex(number))


