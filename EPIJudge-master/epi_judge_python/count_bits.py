def count_bits(x):
    # Implement this placeholder.
    count = 0

    while x != 0:
        count += x & 1
        x >>= 1

    return count


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('count_bits.tsv', count_bits)
