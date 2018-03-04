def reverse(x):
    minus = False
    if x < 0:
        minus = True
        x = x * -1

    t = x % 10
    x = x // 10

    while x > 0:
        d = x % 10
        t = t * 10 + d
        x = x // 10

    if t > pow(2, 31) - 1:
        t = 0
    return t * -1 if minus else t


print(reverse(123))
print(reverse(-123))

print(reverse(0))
print(reverse(1563847412))
