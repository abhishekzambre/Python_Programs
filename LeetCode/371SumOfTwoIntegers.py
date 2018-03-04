def getSum(a, b):
    print(bin(a))
    for i in range(b):
        if i % 2 == 0:
            a = a << 1
            print(bin(a))
        else:
            a = a | 1
            print(bin(a))

    return a


print(getSum(2, 3))
