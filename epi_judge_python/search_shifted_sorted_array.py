from typing import List

from test_framework import generic_test


# TC: O(log n)
def search_smallest(A: List[int]) -> int:
    if len(A) == 0:
        return -1
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if A[l] > A[mid]:
            l = l + 1
            r = mid
        elif A[mid] > A[r]:
            l = mid + 1
        else:
            return l


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
