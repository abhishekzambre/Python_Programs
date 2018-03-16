def binary_sum(S, start, stop, side):

    print(S, start, stop, side)
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        # mid = start + ((stop - start) // 2)
        mid = (start + stop) // 2
        return binary_sum(S, start, mid, "left") + binary_sum(S, mid, stop, "right")


num = [1, 2]
# num = [1, 3, 2, 4, 6]

print(binary_sum(num, 0, len(num), "initial"))
print(sum(num))