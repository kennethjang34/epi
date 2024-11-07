import heapq
from typing import Iterator, List

from test_framework import generic_test


#TC: O(log n), SC: O(n)
def online_median(sequence: Iterator[int]) -> List[float]:
    l_hp = []
    r_hp = []
    medians = []
    for v in sequence:
        if len(l_hp) == len(r_hp):
            heapq.heappush(r_hp, -heapq.heappushpop(l_hp, -v))
            medians.append(r_hp[0])
        else:
            heapq.heappush(l_hp, -heapq.heappushpop(r_hp, v))
            medians.append((r_hp[0] - l_hp[0]) / 2)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
