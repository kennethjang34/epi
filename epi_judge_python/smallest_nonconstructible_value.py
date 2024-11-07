from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    return smallest_nonconstructible_value_opt(A)
    # return smallest_nonconstructible_value_extra_space(A)
# TC: O(nlogn)
def smallest_nonconstructible_value_opt(A: List[int]) -> int:
    max_found = 0
    for i in sorted(A):
        if i <= max_found + 1:
            max_found = max_found + i
        else:
            return max_found + 1
    return max_found + 1


def smallest_nonconstructible_value_extra_space(A: List[int]) -> int:
    coins = sorted(A)
    found = set()
    found.add(0)
    ls = [0]
    for i in coins:
        cur_len = len(ls)
        for j in range(cur_len):
            prev = ls[j]
            cur = prev + i
            if cur not in found:
                found.add(cur)
                ls.append(cur)
            if ls[-1] - ls[-2] > 1:
                return ls[-2] + 1
    return ls[-1] + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_nonconstructible_value.py",
            "smallest_nonconstructible_value.tsv",
            smallest_nonconstructible_value,
        )
    )
