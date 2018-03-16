def power(x, n):

    result = 1
    if n == 0:
        return 1

    for i in range(n):
        print("power call")
        result = result * x

    return result


def power2(x, n):
    result = 1
    if n == 0:
        return 1

    for i in range(n):
        print(i // 2)
        print(i)


def powerRecursion(x, n):
    print("power call recursive 1")
    if n == 0:
        return 1
    else:
        return x * powerRecursion(x, n-1)


def powerRecursion2(x, n):
    print("power call recursive 2")
    if n == 0:
        return 1
    else:
        partial = powerRecursion2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


print(power2(2, 5))
# print(powerRecursion(2, 5))
# print(powerRecursion2(2, 5))
