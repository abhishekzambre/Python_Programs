def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


print('2^13 =', power(2, 13))
print('[1,2,3,4,5]', binary_sum([1, 2, 3, 4, 5], 0, 5))
