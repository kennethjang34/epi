from typing import List

from test_framework import generic_test


# TC: O(n^2)
def transpose_and_reverse(square_matrix: List[List[int]]) -> None:
    for i in range(len(square_matrix)):
        for j in range(i):
            square_matrix[i][j], square_matrix[j][i] = (
                square_matrix[j][i],
                square_matrix[i][j],
            )
    for i in range(len(square_matrix)):
        for j in range(len(square_matrix) // 2):
            square_matrix[i][j], square_matrix[i][len(square_matrix[0]) - 1 - j] = (
                square_matrix[i][len(square_matrix[0]) - 1 - j],
                square_matrix[i][j],
            )

# TC: O(n^2)
def layer_by_layer(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)
    if n < 1:
        return
    # actually since the given matrix is square, m==n
    m = len(square_matrix[0])
    for i in range(n // 2):
        for j in range(i, m - 1 - i):
            (
                square_matrix[i][j],
                square_matrix[~j][i],
                square_matrix[~i][~j],
                square_matrix[j][~i],
            ) = (
                square_matrix[~j][i],
                square_matrix[~i][~j],
                square_matrix[j][~i],
                square_matrix[i][j],
            )
            for i in range(len(square_matrix)):
                print(square_matrix[i])


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # transpose_and_reverse(square_matrix)
    layer_by_layer(square_matrix)


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_rotation.py", "matrix_rotation.tsv", rotate_matrix_wrapper
        )
    )
