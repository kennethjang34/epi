from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    h = 0
    arr = sorted(citations)
    n = len(arr)
    for i, e in enumerate(arr):
        if n - i <= e:
            return n - i


def h_index_reverse_sorted(citations: List[int]) -> int:
    if len(citations) < 1:
        return 0
    arr = sorted(citations, reverse=True)
    if arr[0] == 0:
        return 0
    for i, h_cand in enumerate(arr):
        if i + 1 == h_cand:
            return i + 1
        elif i + 1 > h_cand:
            return i
    return len(citations)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("h_index.py", "h_index.tsv", h_index))
