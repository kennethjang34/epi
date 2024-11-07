from typing import Iterator, List
from heapq import heappush, heappop, heapify, heappushpop

from test_framework import generic_test


## TC: n log k, SC: O(k)
def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    ans = []
    hp = []
    ele = next(sequence)
    while True:
        try:
            if len(hp) == k:
                ans.append(heappushpop(hp, ele))
            else:
                heappush(hp, ele)
            ele = next(sequence)
        except StopIteration:
            while len(hp) != 0:
                ans.append(heappop(hp))
            break
    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
