import os
from typing import List

from test_framework import generic_test
import heapq

from test_framework.test_utils import split_tsv_file

from sort_increasing_decreasing_array import sort_k_increasing_decreasing_array as ex


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    inc = []
    dec = []
    prev = 0
    ans = []
    direction = True
    for i, e in enumerate(A[1:], 1):
        prev_e = A[i - 1]
        if direction:
            if prev_e > e:
                inc.append((prev, i))
                prev = i
                direction = False
                if i == len(A) - 1:
                    dec.append((prev, i + 1))
            elif i == len(A) - 1:
                inc.append((prev, i + 1))
        else:
            if prev_e < e:
                dec.append((prev, i))
                prev = i
                direction = True
                if i == len(A) - 1:
                    inc.append((prev, i + 1))
            elif i == len(A) - 1:
                dec.append((prev, i + 1))

    indicies = [start for start, _ in inc + dec]
    for start, end in dec:
        A[start:end] = A[start:end][::-1]
    arrays = inc + dec
    pq = [(A[start], i) for i, (start, _) in enumerate(arrays)]
    heapq.heapify(pq)
    while len(pq):
        popped = heapq.heappop(pq)
        el = popped[0]
        arr = popped[1]
        ans.append(el)
        index = indicies[arr]
        index += 1
        indicies[arr] = index
        if index < arrays[arr][1]:
            heapq.heappush(pq, (A[index], arr))

    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_increasing_decreasing_array.py",
            "sort_increasing_decreasing_array.tsv",
            sort_k_increasing_decreasing_array,
        )
    )
