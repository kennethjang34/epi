from typing import List

from test_framework import generic_test
import numpy as np


def matrix_search_bf(A: List[List[int]], x: int) -> bool:
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == x:
                return True
    return False


def matrix_search_slow_recursive(A: List[List[int]], x: int) -> bool:
    if len(A) == 0 or len(A[0]) == 0:
        return False
    elif len(A) == 1 and len(A[0]) == 1:
        return A[0][0] == x
    elif len(A) == 1:
        if A[0][0] < x:
            return matrix_search_slow_recursive([A[0][1:]], x)
        elif A[0][0] == x:
            return True
        else:
            return False
    elif len(A[0]) == 1:
        if A[0][0] < x:
            return matrix_search_slow_recursive([A[1:][0]], x)
        elif A[0][0] == x:
            return True
        else:
            return False
    else:
        if A[0][0] > x:
            return False
        elif A[0][0] == x:
            return True
        else:
            return (
                matrix_search_slow_recursive([A[1:][0]], x)
                or matrix_search_slow_recursive([A[0][1:]], x)
                or matrix_search_slow_recursive(A[1:][1:], x)
            )


# TC: O(m+n)
def matrix_search(A: List[List[int]], x: int) -> bool:
    i = 0
    if len(A) == 0:
        return False
    j = len(A[0]) - 1
    while i < len(A) and j >= 0:
        cur = A[i][j]
        if cur == x:
            return True
        elif cur > x:
            j -= 1
        elif cur < x:
            i += 1
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
