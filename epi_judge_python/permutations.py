from typing import List, Set

from test_framework import generic_test, test_utils


# TC: O(n*n!), SC: O(n)
def permutations(A: List[int]) -> List[List[int]]:
    ans = []
    l = len(A)

    def helper(chars: Set, cur: List[int]):
        if len(chars) == 0:
            ans.append(cur)
            return
        else:
            idx = (len(chars) - l) % l
            cur_chars = list(chars)
            for ch in cur_chars:
                chars.remove(ch)
                cur[idx] = ch
                helper(chars, cur)
                chars.add(ch)

    chars = set(A)
    helper(chars, [0] * l)
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
