from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # return find_maximum_subarray_slow(A)
    # return find_maximum_subarray_fast_big_space(A)
    return find_maximum_subarray_fast_small_space(A)


# TC: O(n), SC: O(1)
def find_maximum_subarray_fast_small_space(A: List[int]) -> int:
    prev_subarr_max = 0
    max_found = 0
    i = 0
    while i < len(A):
        prev_subarr_max = max(prev_subarr_max + A[i], A[i])
        max_found = max(max_found, prev_subarr_max)
        i += 1
    return max_found


# TC: O(n), SC: O(n)
def find_maximum_subarray_fast_big_space(A: List[int]) -> int:
    subarray_maxes = [0] * (len(A))
    max_found = 0
    i = 0
    while i < len(subarray_maxes):
        subarray_maxes[i] = max(subarray_maxes[i - 1] + A[i], A[i])
        max_found = max(max_found, subarray_maxes[i])
        i += 1
    return max_found


# TC: O(n^2)
def find_maximum_subarray_slow(A: List[int]) -> int:
    sums = [0] * (len(A) + 1)
    s = 0
    for i, n in enumerate(A):
        s += n
        sums[i + 1] = s
    max_found = 0
    for i in range(len(sums)):
        for j in range(0, i):
            max_found = max(max_found, sums[i] - sums[j])
    return max_found


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_sum_subarray.py", "max_sum_subarray.tsv", find_maximum_subarray
        )
    )
