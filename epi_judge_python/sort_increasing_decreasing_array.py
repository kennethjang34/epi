from typing import List

from test_framework import generic_test
import heapq


# TC: O(n*log(k)), where k: number of order change in A +1 (to include the start of the array) and n: number of total elements
# SC: O(k)
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if A is None or len(A) == 0:
        return []
    cur = [A[0]]
    increasing_lists = [cur]
    decreasing_lists = []
    prev = A[0]
    direction = True
    for n in A[1:]:
        if direction and prev > n:
            direction = False
            cur = []
            decreasing_lists.append(cur)
            cur.append(n)
        elif direction is False and prev < n:
            direction = True
            cur = []
            increasing_lists.append(cur)
            cur.append(n)
        else:
            cur.append(n)
        prev = n
    lists = increasing_lists + [ls[::-1] for ls in decreasing_lists]
    list_iters = [iter(ls) for ls in lists]
    min_heap = [(next(it), i) for i, it in enumerate(list_iters)]
    heapq.heapify(min_heap)
    res = []
    while len(min_heap):
        element, list_index = heapq.heappop(min_heap)
        res.append(element)
        to_push = next(list_iters[list_index], None)
        if to_push is not None:
            heapq.heappush(min_heap, (to_push, list_index))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_increasing_decreasing_array.py",
            "sort_increasing_decreasing_array.tsv",
            sort_k_increasing_decreasing_array,
        )
    )
