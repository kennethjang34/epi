import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple("Interval", ("left", "right"))


# TC: O(n log n)
def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals = sorted(intervals, key=lambda intv: intv.right)
    i = 0
    ans = 0
    while i < len(intervals):
        intv = intervals[i]
        j = i + 1
        while j < len(intervals) and intervals[j].left <= intv.right:
            j += 1
        ans += 1
        i = j
    return ans


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_points_covering_intervals.py",
            "minimum_points_covering_intervals.tsv",
            find_minimum_visits_wrapper,
        )
    )
