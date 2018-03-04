def hammingDistance(x, y):
    total = 0
    while x > 0 or y > 0:
        print(x & 1, y & 1)
        if (x & 1) - (y & 1) != 0:
            total += 1
        x >>= 1
        y >>= 1
    print(total)


def hammingDistance2(x, y):
    print(bin(x ^ y).count('1'))


hammingDistance(4, 1)
hammingDistance2(4, 1)
