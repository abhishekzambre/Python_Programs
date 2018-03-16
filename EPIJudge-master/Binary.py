def nega(num):
    res = []
    while num != 0:
        remainder = abs(num) % 2
        res.append(str(remainder))
        if num < 0 and remainder:
            num -= 1
        num = int(num / -2)

    print(res)


print(nega(-12))
