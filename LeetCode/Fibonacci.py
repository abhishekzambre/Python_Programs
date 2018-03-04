def fibonacci(n):
    arr = [0, 1, 1]
    if n < 3:
        print(n, n, arr)
        return arr[n]
    else:
        for i in range(3, n+1):
            print(n, i, arr)
            arr[i % 3] = arr[(i-1) % 3] + arr[(i-2) % 3]
        return arr[n % 3]


def fibonacci2(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, y+x

    return x


print("output:", fibonacci2(8))
