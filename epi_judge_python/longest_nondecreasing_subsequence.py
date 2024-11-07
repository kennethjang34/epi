from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    # return longest_nondecreasing_subsequence_length_top_down(A)
    return longest_nondecreasing_subsequence_length_bottom_up(A)


# TC: O(n^2), SC: O(n)
def longest_nondecreasing_subsequence_length_top_down(A: List[int]):
    def helper(A: List[int], i, mem):
        if i >= len(A):
            return 0
        if i in mem:
            return mem[i]
        cand = 1
        for it in range(i + 1, len(A)):
            e = A[it]
            if e >= A[i]:
                cand = max(cand, 1 + helper(A, it, mem))
        mem[i] = cand
        return cand

    mem = {}
    return max(helper(A, i, mem) for i in range(len(A)))


# TC: O(n^2), SC: O(n)
def longest_nondecreasing_subsequence_length_bottom_up(A: List[int]):
    max_lengths = [1] * len(A)
    for i in range(1, len(A)):
        max_lengths[i] = 1 + max(
            max_lengths[j] if A[j] <= A[i] else 0 for j in range(i)
        )
    return max(max_lengths)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            "longest_nondecreasing_subsequence.tsv",
            longest_nondecreasing_subsequence_length,
        )
    )
