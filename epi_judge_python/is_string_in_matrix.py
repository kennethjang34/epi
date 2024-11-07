from typing import List, Set

from test_framework import generic_test


# TC: O(m*n*l), where m: len(grid), n: len(grid[0]), l: len(pattern)
def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    table = [
        [[None] * (len(grid[0])) for _ in range(len(grid))]
        for _ in range(len(pattern) + 1)
    ]

    def helper(
        grid,
        pattern,
        i,
        j,
        table,
    ):
        ans = False
        if len(pattern) == 0:
            return True
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if table[len(pattern)][i][j] is not None:
            return table[len(pattern)][i][j]
        elif grid[i][j] == pattern[0]:
            sub_pattern = pattern[1:]
            ans = (
                helper(grid, sub_pattern, i + 1, j, table)
                or helper(grid, sub_pattern, i - 1, j, table)
                or helper(grid, sub_pattern, i, j + 1, table)
                or helper(grid, sub_pattern, i, j - 1, table)
            )
        table[len(pattern)][i][j] = ans
        return ans

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if helper(grid, pattern, i, j, table):
                return True
    return False


def is_pattern_contained_in_grid2(grid: List[List[int]], pattern: List[int]) -> bool:
    table = [
        [[None] * (len(grid[0])) for _ in range(len(grid))]
        for _ in range(len(pattern) + 1)
    ]

    def helper(grid, pattern, i, j, table, visited=set()):
        ans = False
        if len(pattern) == 0:
            return True
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if table[len(pattern)][i][j] is not None:
            return table[len(pattern)][i][j] is not None
        if grid[i][j] == pattern[0]:
            sub_pattern = pattern[1:]
            ans = (
                helper(grid, sub_pattern, i + 1, j, table, visited)
                or helper(grid, sub_pattern, i - 1, j, table, visited)
                or helper(grid, sub_pattern, i, j + 1, table, visited)
                or helper(grid, sub_pattern, i, j - 1, table, visited)
            )
            table[len(pattern)][i][j] = ans
        return ans

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if helper(grid, pattern, i, j, table):
                return True
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_in_matrix.py",
            "is_string_in_matrix.tsv",
            is_pattern_contained_in_grid,
        )
    )
