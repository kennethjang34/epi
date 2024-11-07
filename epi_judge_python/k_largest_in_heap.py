from collections import namedtuple
import heapq
from typing import List

from test_framework import generic_test, test_utils


# TC: O(k log k), SC: O(log k)
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    Node = namedtuple("Node", ["negval", "idx"])
    hp = [Node(-A[0], 0)]
    res = []
    for i in range(k):
        node = heapq.heappop(hp)
        val = -node.negval
        idx = node.idx
        res.append(val)
        if idx * 2 + 1 < len(A):
            heapq.heappush(hp, Node(-A[idx * 2 + 1], idx * 2 + 1))
        if idx * 2 + 2 < len(A):
            heapq.heappush(hp, Node(-A[idx * 2 + 2], idx * 2 + 2))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare,
        )
    )
