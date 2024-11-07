from typing import List

from test_framework import generic_test


# TC: O(len(A) + len(B))
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    inter = []
    l = 0
    r = 0
    # return sorted(list(set(A).intersection(B)))
    while l < len(A) and r < len(B):
        a = A[l]
        b = B[r]
        if a == b:
            if l == 0 or a != A[l - 1]:
                inter.append(a)
            l += 1
            r += 1
        elif a < b:
            l += 1
        else:
            r += 1

    return inter


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )
