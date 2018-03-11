from test_framework.test_failure_exception import TestFailureException
from test_framework.test_utils import enable_timer_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # Implement this placeholder.

    pivot = A[pivot_index]

    smaller = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

    return


@enable_timer_hook
def dutch_flag_partition_wrapper(timer, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    timer.start()
    dutch_flag_partition(pivot_idx, A)
    timer.stop()

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A) or any(count):
        raise TestFailureException("Invalid output")


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('dutch_national_flag.tsv',
                                              dutch_flag_partition_wrapper)
