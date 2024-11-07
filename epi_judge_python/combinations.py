from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def helper(n, k):
        ans = []
        if k == 0:
            return [[]]
        if n < k:
            return []
        sub_comb = helper(n - 1, k - 1)
        for l in sub_comb:
            l.append(n)
        with_cur = sub_comb
        ans.extend(with_cur)
        without_cur = helper(n - 1, k)
        ans.extend(without_cur)
        return ans

    returned = helper(n, k)
    return returned


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            "combinations.tsv",
            combinations,
            comparator=test_utils.unordered_compare,
        )
    )
