from typing import List
import heapq

from test_framework import generic_test


# TC: O(n*log(k)), where k: number of arrays and n: number of total elements
# method uses max heap to pop from the end of each list, but we can just use min heap if we don't pop but just use iterator
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    max_heap = [(-(arr.pop(-1)), i) for i, arr in enumerate(sorted_arrays)]
    heapq.heapify(max_heap)

    next_e = heapq.heappop(max_heap)
    reversed_list = []
    while next_e is not None:
        reversed_list.append(-next_e[0])
        replacement = (
            -sorted_arrays[next_e[1]].pop(-1)
            if len(sorted_arrays[next_e[1]]) != 0
            else None
        )
        if replacement is not None:
            next_e = heapq.heappushpop(max_heap, (replacement, next_e[1]))
        else:
            try:
                next_e = heapq.heappop(max_heap)
            except:
                next_e = None

    return reversed_list[::-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
