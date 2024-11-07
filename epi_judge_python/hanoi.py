import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


# TC: O(n^2), as T(n) = T(n-1)+1+T(n-1)=2*T(n)+1, so T(n) = 1+2+4+...2^k*T(n-k) = 2^n -1 = O(n^2)
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def helper(from_peg, to_peg, mid_peg, num_rings):
        if num_rings == 1:
            return [[from_peg, to_peg]]
        else:
            res = []
            res.extend(helper(from_peg, mid_peg, to_peg, num_rings - 1))
            res.append([from_peg, to_peg])
            res.extend(helper(mid_peg, to_peg, from_peg, num_rings - 1))
            return res

    return helper(0, 1, 2, num_rings)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure(
                "Illegal move from {} to {}".format(
                    pegs[from_peg][-1], pegs[to_peg][-1]
                )
            )
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "hanoi.py", "hanoi.tsv", compute_tower_hanoi_wrapper
        )
    )
