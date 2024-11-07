import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple("Endpoint", ("is_closed", "val"))

Interval = collections.namedtuple("Interval", ("left", "right"))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    # return union_of_intervals_initial_attempt(intervals)
    return union_of_intervals_optimized(intervals)


# TC: O(n log n)
def union_of_intervals_optimized(intervals: List[Interval]) -> List[Interval]:
    ans = []
    sorted_intervals = sorted(
        intervals,
        key=lambda intv: (
            intv.left.val if intv.left.is_closed else intv.left.val + 0.1
        ),
    )
    cur_intv = None
    for intv in sorted_intervals:
        if cur_intv is None:
            cur_intv = intv
        else:
            if cur_intv.right.val > intv.left.val or (
                cur_intv.right.val == intv.left.val
                and (cur_intv.right.is_closed or intv.left.is_closed)
            ):
                if cur_intv.right.val < intv.right.val or (
                    cur_intv.right.val == intv.right.val and intv.right.is_closed
                ):
                    cur_intv = Interval(cur_intv.left, intv.right)
            else:
                ans.append(cur_intv)
                cur_intv = intv
    if cur_intv is not None:
        ans.append(cur_intv)
    return ans


def union_of_intervals_initial_attempt(intervals: List[Interval]) -> List[Interval]:
    def merge_interval(i1: Interval, i2: Interval):
        closed_i1 = get_closed_version(i1)
        closed_i2 = get_closed_version(i2)
        i1_l: Endpoint = closed_i1.left
        i1_r: Endpoint = closed_i1.right
        i2_l: Endpoint = closed_i2.left
        i2_r: Endpoint = closed_i2.right
        left = None
        right = None

        if (
            i1_l <= i2_r
            and i2_l <= i1_r
            or (i1.right.is_closed and i1.right.val == i2.left.val)
            or (i2.left.is_closed and i2.left.val == i1.right.val)
        ):
            if i1_l < i2_l:
                left = i1.left
            elif i1_l == i2_l:
                left = i1.left if not i1.left.is_closed else i2.left
            else:
                left = i2.left
            if i1_r > i2_r:
                right = i1.right
            elif i1_r == i2_r:
                right = i1.right if not i1.right.is_closed else i2.right
            else:
                right = i2.right
            return Interval(left, right)
        else:
            return None

    def get_closed_version(intv: Interval):
        left: Endpoint = intv.left
        right: Endpoint = intv.right
        if not left.is_closed:
            left = Endpoint(True, left.val + 0.1)
        if not right.is_closed:
            right = Endpoint(True, right.val - 0.1)
        return Interval(left, right)

    ans = []
    sorted_intervals = sorted(
        intervals,
        key=lambda intv: (
            intv.left.val if intv.left.is_closed else intv.left.val + 0.1
        ),
    )
    cur_intv = None
    for intv in sorted_intervals:
        if cur_intv is None:
            cur_intv = intv
        else:
            merged = merge_interval(cur_intv, intv)
            if merged is None:
                ans.append(cur_intv)
                cur_intv = intv
            else:
                cur_intv = merged
    if cur_intv is not None:
        ans.append(cur_intv)
    return ans


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [
        (i.left.val, i.left.is_closed, i.right.val, i.right.is_closed) for i in result
    ]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intervals_union.py", "intervals_union.tsv", union_of_intervals_wrapper
        )
    )
