def add_digits(n):
    f = n % 10
    n = n // 10
    t = f
    while n != 0:
        s = n % 10
        t = f + s
        if t > 9:
            t = t % 10 + t // 10
        n = n // 10
        f = t
    return t


def add_digits2(n):
    return n % 9 or 9 if n else 0


print("38 :", add_digits(38))
print("123 :", add_digits(123))
print("0 :", add_digits(0))
print("12345 :", add_digits(12345))
print("1 :", add_digits(1))
