from typing import List

from bintrees import RBTree

from test_framework import generic_test
from math import sqrt


class Number:
    def __init__(
        self,
        a,
        b,
    ) -> None:
        self.a, self.b = a, b
        self.val = a + b * sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    # return generate_first_k_a_b_sqrt2_bst(k)
    return generate_first_k_a_b_sqrt2_opt(k)


# TC: O(k log k), SC: O(k)
def generate_first_k_a_b_sqrt2_bst(k: int) -> List[float]:
    ans = []
    # Val of nodes not needed. Set it to None
    # Note a duplicate item can be inserted twice (e.g., 1+sqrt(2) can be inserted from incrementing 1 by sqrt(2) and sqrt(2) by 1)
    # To ensure no duplicate items inserted, we must be extra careful with the equality of keys,
    # so that even if a duplicate item is inserted twice, both insertions are with the same key so it just replaces the previous one.
    # two duplicate items might have different keys because of floating point issue without extra care.
    # Also note that if one number has been popped, its duplicate cannot be inserted later, since we are only adding numbers bigger than the popped ones.
    cands = RBTree([(Number(0, 0), None)])
    while len(ans) < k:
        next_smallest = cands.pop_min()[0]
        ans.append(next_smallest.val)
        cands[Number(next_smallest.a + 1, next_smallest.b)] = None
        cands[Number(next_smallest.a, next_smallest.b + 1)] = None
    return ans


# TC: O(n), SC: O(1)
def generate_first_k_a_b_sqrt2_opt(k: int) -> List[float]:
    res = [Number(0, 0)]
    i = 0
    j = 0
    while len(res) < k:
        cand_i_plus_1 = Number(res[i].a + 1, res[i].b)
        cand_j_plus_sqrt2 = Number(res[j].a, res[j].b + 1)
        if cand_i_plus_1 > cand_j_plus_sqrt2:
            res.append(cand_j_plus_sqrt2)
            j += 1
        elif cand_i_plus_1 < cand_j_plus_sqrt2:
            res.append(cand_i_plus_1)
            i += 1
        else:
            res.append(cand_i_plus_1)
            i += 1
            j += 1
    return [n.val for n in res]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
