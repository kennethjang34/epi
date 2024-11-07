from typing import List, Set

from test_framework import generic_test


# O(n!)
def n_queens(n: int) -> List[List[int]]:
    ans = []
    col_pos = [0] * n

    def helper(row, col_pos, ans, n):
        if row == n:
            ans.append(col_pos.copy())
        else:
            for col in range(n):
                if all(
                    abs(col - c) not in (0, row - i)
                    for i, c in enumerate(col_pos[:row])
                ):
                    col_pos[row] = col
                    helper(row + 1, col_pos, ans, n)

    helper(0, col_pos, ans, n)
    return ans


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("n_queens.py", "n_queens.tsv", n_queens, comp))
