def plus_one(A):
    # Implement this placeholder.

    c = 0
    last = 0
    A[len(A) - 1] += 1
    for i in reversed(range(len(A))):
        A[i] += c
        if A[i] >= 10:
            c = 1
            A[i] = 0
        else:
            c = 0

        last = i

    if c != 0 and last != -1:
        A.insert(0, c)

    return A


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("int_as_array_increment.tsv",
                                              plus_one)
