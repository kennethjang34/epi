from typing import List

import random


from test_framework import generic_test


# TC: O(n) on average, O(n^2) in the worst case, SC: O(n)
def find_kth_largest_extra_mem(k: int, A: List[int]) -> int:
    while k >= 1:
        pivot = A[random.randint(0, len(A) - 1)]
        lesser = []
        greater = []
        for e in A:
            if e < pivot:
                lesser.append(e)
            else:
                greater.append(e)
        if len(greater) > k:
            A = greater
        elif len(greater) == k:
            return pivot
        else:
            k = k - len(greater)
            A = lesser


# TC: O(n) on average, O(n^2) in the worst case, SC: O(1)
def find_kth_largest_space_optimized(k: int, A: List[int]) -> int:
    def partition_around_pivot(A, left, right, piv_idx):
        pivot = A[piv_idx]
        new_piv_idx = left
        A[piv_idx], A[left] = A[left], pivot
        for i in range(left + 1, right + 1):
            e = A[i]
            if e > pivot:
                new_piv_idx += 1
                A[i], A[new_piv_idx] = A[new_piv_idx], A[i]
        A[left], A[new_piv_idx] = A[new_piv_idx], A[left]
        return new_piv_idx

    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_piv_idx = partition_around_pivot(A, left, right, pivot_idx)
        if new_piv_idx == k - 1:
            return A[new_piv_idx]
        elif new_piv_idx > k - 1:
            right = new_piv_idx - 1
        else:
            left = new_piv_idx


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    return find_kth_largest_space_optimized(k, A)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py", "kth_largest_in_array.tsv", find_kth_largest
        )
    )
