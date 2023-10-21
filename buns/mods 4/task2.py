a = input().split()

def fast_pow(a, n):
    if n == 0: return 1
    elif n % 2 == 0: return fast_pow(a ** 2, n / 2)
    else: return a * fast_pow(a, n - 1)

print(fast_pow(int(a[0]), int(a[1])))
