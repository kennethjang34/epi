from typing import List

from test_framework import generic_test
from bintrees import RBTree


# TC: O(n log k), where n: total number of elements in the input arrays and k the number of sorted arrays. Here k=3, therefore TC: O(n)
def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    tree = RBTree()
    for idx, arr in enumerate(sorted_arrays):
        it = iter(arr)
        first_min = next(it, None)
        if first_min is not None:
            tree.insert((first_min, idx), it)
    ans = float("inf")
    while True:
        min_e = tree.pop_min()
        max_e = tree.max_item()
        ans = min(ans, max_e[0][0] - min_e[0][0])
        it = min_e[1]
        next_min = next(it, None)
        if next_min is None:
            return ans
        else:
            tree.insert(
                (next_min, min_e[0][1]),
                it,
            )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_distance_3_sorted_arrays.py",
            "minimum_distance_3_sorted_arrays.tsv",
            find_closest_elements_in_sorted_arrays,
        )
    )
