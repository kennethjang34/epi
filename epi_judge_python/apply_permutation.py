from typing import List

from test_framework import generic_test


# TC: O(n), SC: O(n)
def brute_force(perm: List[int], A: List[int]) -> None:
    elements = A.copy()
    for i, pos in enumerate(perm):
        A[pos] = elements[i]


# TC: O(n), SC: O(1)
def without_extra_mem_1(perm: List[int], A: List[int]) -> None:
    for idx in range(len(A)):
        i = idx
        ch = A[idx]
        while perm[i] != -1:
            pos = perm[i]
            ch, A[pos] = A[pos], ch
            perm[i] = -1
            i = pos


# TC: O(n), SC: O(1)
# swap two of A's elements for each iteration, updating perm array with new permutation locations
def without_extra_mem_2(perm: List[int], A: List[int]) -> None:
    for i in range(len(perm)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]


# TC: O(n), SC: O(1)
def without_modifying_perm(perm: List[int], A: List[int]) -> None:
    idx = 0
    n = len(A)
    for i in range(n - 1):
        idx = perm[i]
        while idx < i:
            idx = perm[idx]
        A[i], A[idx] = A[idx], A[i]

def apply_permutation(perm: List[int], A: List[int]) -> None:
    # brute_force(perm, A)
    # without_extra_mem_1(perm, A)
    # without_extra_mem_2(perm, A)
    without_modifying_perm(perm,A)


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "apply_permutation.py", "apply_permutation.tsv", apply_permutation_wrapper
        )
    )
