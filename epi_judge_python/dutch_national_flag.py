import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# TC: O(n), SC: O(1)
def two_single_passes(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    small = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[small], A[i] = A[i], A[small]
            small += 1
    bigger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[bigger], A[i] = A[i], A[bigger]
            bigger -= 1


# TC: O(n), SC: O(1)
## let smaller values be in: A[:smaller]
##     equal values be in: A[smaller:equal]
##     unconfirmed values be in: A[equal:bigger]
##     bigger values be in: A[bigger:]
def one_single_pass(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller, equal, bigger = 0, 0, len(A)
    # if equal == bigger, length of unconfirmed group: len(A[equal:bigger]) == 0
    while equal < bigger:
        # A[equal] is not evaluated yet
        next_val = A[equal]
        if next_val == pivot:
            equal += 1
        elif next_val < pivot:
            A[equal] = A[smaller]
            A[smaller] = next_val
            smaller += 1
            equal += 1
            # another alternative for next_val < pivot case:

            # the equal group is still empty, so no switching required

            # if smaller == equal:
            #     smaller += 1
            #     equal += 1

            # the equal group has at least one value, so switching required.

            # else:
            #     A[equal] = pivot # or A[equal] = A[smaller]
            #     A[smaller] = next_val
            #     smaller += 1
            #     equal += 1

        else:
            bigger -= 1
            A[equal] = A[bigger]
            A[bigger] = next_val


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # two_single_passes(pivot_index=pivot_index, A=A)
    one_single_pass(pivot_index=pivot_index, A=A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

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

    if i != len(A):
        raise TestFailure("Not partitioned after {}th element".format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
