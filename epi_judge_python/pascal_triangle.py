from typing import List

from test_framework import generic_test


# TC: O(n^2), SC: O(n^2)
# for both TC and SC: O(1+2+3+...+n) = O(n^2)
def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n < 1:
        return []
    ans = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
