from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    merge_two_sorted_arrays_from_back(A, m, B, n)
    # merge_two_sorted_arrays_move_to_back_first(A, m, B, n)


# TC: O(n+m)
def merge_two_sorted_arrays_from_back(
    A: List[int], m: int, B: List[int], n: int
) -> None:
    i = m + n - 1
    j = m - 1
    k = n - 1
    while i >= 0:
        if k >= 0:
            if j >= 0 and A[j] >= B[k]:
                A[i] = A[j]
                j -= 1
            else:
                A[i] = B[k]
                k -= 1
        i -= 1


# TC: O(n+m)
def merge_two_sorted_arrays_move_to_back_first(
    A: List[int], m: int, B: List[int], n: int
) -> None:
    for i in range(m - 1, -1, -1):
        A[i + n] = A[i]
    i = 0
    j = n
    k = 0
    while i < m + n:
        if k < n:
            if j < m + n and A[j] <= B[k]:
                A[i] = A[j]
                j += 1
            else:
                A[i] = B[k]
                k += 1
        i += 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
