def robot(steps):
    x = y = 0
    i = 1
    k = -1
    while steps > 0:
        if steps / (2 * i) >= 1:
            x += i * k
            y = x
            steps -= 2 * i
            i += 1
            k *= -1
        else:
            if steps / i <= 1:
                x += steps * k
            else:
                x += i * k
                y += steps % i * k
            k *= -1
            break
    return x, y


print(robot(int(input())))
