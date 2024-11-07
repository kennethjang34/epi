import collections
from typing import DefaultDict, List

from test_framework import generic_test


# TC, SC: O(n)
def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    res = 0
    l = 0
    latest_occ = {}
    for r, c in enumerate(A):
        if c in latest_occ and latest_occ[c] >= l:
            l = latest_occ[c] + 1
        latest_occ[c] = r
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            "longest_subarray_with_distinct_values.tsv",
            longest_subarray_with_distinct_entries,
        )
    )
