from typing import List

from test_framework import generic_test


## works only for square matrix
# TC: O(n^2) SC: O(n^2)
def with_loops(square_matrix: List[List[int]]) -> List[int]:
    start = [0, 0]
    n = len(square_matrix)
    ans = []
    while n > 0:
        if n == 1:
            ans.append(square_matrix[start[0]][start[1]])
        for j in range(n - 1):
            ans.append(square_matrix[start[0]][start[1] + j])
        for i in range(n - 1):
            ans.append(square_matrix[start[0] + i][start[1] + n - 1])
        for j in range(n - 1):
            ans.append(square_matrix[start[0] + n - 1][start[1] + n - 1 - j])
        for i in range(n - 1):
            ans.append(square_matrix[start[0] + n - 1 - i][start[1]])
        start[0] += 1
        start[1] += 1
        n -= 2
    return ans


# Given matrix of shape: n x m
# TC: O(n^m) or O(n^n) for square matrix, SC: O(n * m)
def with_rotation(matrix: List[List[int]]):
    if len(matrix) == 0:
        return []
    else:
        popped = matrix.pop(0)
        return popped + with_rotation([list(z) for z in zip(*matrix)][::-1])


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # return using_loops(square_matrix)
    return with_rotation(square_matrix)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
