import collections
import functools
from typing import Dict, List, Tuple

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # return optimum_subject_to_capacity_top_bottom(items, capacity)
    return optimum_subject_to_capacity_bottom_top(items, capacity)


# TC:O(n*w), SC: O(w), where n: number of items and w: weight capacity
def optimum_subject_to_capacity_bottom_top(items: List[Item], capacity: int) -> int:
    table = [[0] * (capacity + 1) for _ in range(2)]
    for item in items:
        for c in range(1, capacity + 1):
            w = item.weight
            v = item.value
            if w <= c:
                table[1][c] = max(table[0][c - w] + v, table[0][c])
            else:
                table[1][c] = table[0][c]
        table[0] = table[1]
        table[1] = [0] * (capacity + 1)
    return table[0][-1]


# TC, SC: O(n*w), where n: number of items and w: weight capacity
def optimum_subject_to_capacity_top_bottom(items: List[Item], capacity: int) -> int:
    def helper(items: List[Item], capacity: int, item_idx=0, table: Dict = {}):
        if item_idx >= len(items):
            return 0
        elif capacity <= 0:
            return 0
        elif (item_idx, capacity) in table:
            return table[(item_idx, capacity)]
        item = items[item_idx]
        cand_1 = 0
        if item.weight <= capacity:
            cand_1 = item.value + helper(
                items, capacity - item.weight, item_idx + 1, table
            )
        cand_2 = helper(items, capacity, item_idx + 1, table)
        ans = max(cand_1, cand_2)
        table[(item_idx, capacity)] = ans
        return ans

    table = {}
    return helper(items, capacity, 0, table)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
