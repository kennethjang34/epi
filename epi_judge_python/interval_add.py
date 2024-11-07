import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple("Interval", ("left", "right"))


# Assume disjoint_intervals are sorted by intervals' left values
# TC: O(n)
def add_interval(
    disjoint_intervals: List[Interval], new_interval: Interval
) -> List[Interval]:
    # not needed because of pre-sortedness of input
    # disjoint_intervals=sorted(disjoint_intervals)
    i = 0
    ans = []
    while i < len(disjoint_intervals):
        cur_intv = disjoint_intervals[i]
        if new_interval is not None:
            if (
                cur_intv.left <= new_interval.right
                and cur_intv.right >= new_interval.left
            ):
                new_interval = Interval(
                    min(cur_intv.left, new_interval.left),
                    max(cur_intv.right, new_interval.right),
                )
            else:
                if cur_intv.left >= new_interval.left:
                    ans.append(new_interval)
                    new_interval = None
                ans.append(cur_intv)
        else:
            ans.append(cur_intv)
        i += 1
    if new_interval is not None:
        ans.append(new_interval)
    return ans


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals, Interval(*new_interval))
    )


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            "interval_add.tsv",
            add_interval_wrapper,
            res_printer=res_printer,
        )
    )
