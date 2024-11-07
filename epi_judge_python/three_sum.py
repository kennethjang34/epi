from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    # return has_three_sum_bf(A, t)
    return has_three_sum_hash(A, t)
    # return has_three_sum_space_optimal(A, t)


# TC: O(n^2), SC: O(1)
# A bit slower than the one using hashing but no extra space
def has_three_sum_space_optimal(A: List[int], t: int) -> bool:
    A = sorted(A)
    for a in A:
        i = 0
        j = len(A) - 1
        while i <= j:
            if t - a < A[i] + A[j]:
                j -= 1
            elif t - a > A[i] + A[j]:
                i += 1
            else:
                return True
    return False


# TC: O(n^2), SC: O(n)
# Fastest
def has_three_sum_hash(A: List[int], t: int) -> bool:
    hs = set(A)
    for i in range(len(A)):
        a = A[i]
        for j in range(i, len(A)):
            b = A[j]
            if t - a - b in hs:
                return True
    return False


# TC: O(n^3)
def has_three_sum_bf(A: List[int], t: int) -> bool:
    A = sorted(A)
    for i in range(len(A)):
        a = A[i]
        for j in range(i, len(A)):
            b = A[j]
            for k in range(j, len(A)):
                c = A[k]
                if a + b + c == t:
                    return True
    return False


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))
