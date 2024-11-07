from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    # return minimum_path_weight_recursive(triangle)
    return minimum_path_weight_iterative(triangle)


# TC: O(n^2), SC: O(n^2)
def minimum_path_weight_recursive(triangle: List[List[int]]) -> int:
    def helper(i, j, rows, table={}):
        if i == len(rows):
            return 0
        elif (i, j) in table:
            return table[(i, j)]
        else:
            ans = min(helper(i + 1, j, rows), helper(i + 1, j + 1, rows)) + rows[i][j]
            table[(i, j)] = ans
            return ans

    return helper(0, 0, triangle)


# TC: O(n^2), SC: O(n)
def minimum_path_weight_iterative(triangle: List[List[int]]) -> int:
    prev = [0]
    for i in range(1, len(triangle) + 1):
        cur = []
        for j in range(i):
            if j == 0:
                cur.append(prev[j] + triangle[i - 1][j])
            elif j == len(triangle[i - 1]) - 1:
                cur.append(prev[j - 1] + triangle[i - 1][j])
            else:
                cur.append(min(prev[j], prev[j - 1]) + triangle[i - 1][j])
        prev = cur
    return min(prev)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_weight_path_in_a_triangle.py",
            "minimum_weight_path_in_a_triangle.tsv",
            minimum_path_weight,
        )
    )
