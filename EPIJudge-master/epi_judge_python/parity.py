def parity(x):
    # Implement this placeholder.
    result = 0

    # while x != 0:
    #     result ^= x & 1
    #     x >>= 1

    while x:
        result ^= 1
        x &= x-1

    return result


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('parity.tsv', parity)
