from typing import List

from test_framework import generic_test


# O(log n)
def search_first_of_k(A: List[int], k: int) -> int:
    i = 0
    j = len(A) - 1
    while i < j:
        mid = i + (j - i) // 2
        if A[mid] < k:
            i = mid + 1
        else:
            j = mid
    if i == j and A[i] == k:
        return i
    else:
        return -1


## a variant question, TC: O(log n)
## similar leetcode: https://leetcode.com/problems/find-peak-element/description/
def find_local_min(A: List[int]) -> int:
    i = 1
    j = len(A) - 2
    while i <= j:
        mid = i + (j - i) // 2
        if A[mid - 1] >= A[mid] <= A[mid + 1]:
            return mid
        elif A[mid - 1] <= A[mid]:
            j = mid - 1
        else:
            i = mid
    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
