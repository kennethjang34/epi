import collections
import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    Placement = collections.namedtuple("Placement", ["value", "row", "col"])
    board = partial_assignment

    def is_valid(
        board: List[List[int]],
        placement: Placement,
    ):
        board_size = len(board)
        n = placement.value
        row = placement.row
        col = placement.col
        if n in board[row]:
            return False
        for i in range(board_size):
            if n == board[i][col]:
                return False
        region_size = int(math.sqrt(board_size))
        region_row_idx = row // region_size
        region_col_idx = col // region_size
        for i in range(3 * region_row_idx, 3 * region_row_idx + 3):
            for j in range(3 * region_col_idx, 3 * region_col_idx + 3):
                if (i != row or j != col) and board[i][j] == n:
                    return False
        return True

    def is_empty(val):
        return val == 0

    def helper(board: List[List[int]], i, j):
        if i == len(board):
            if j == len(board[0]) - 1:
                return True
            else:
                i = 0
                j += 1
        if is_empty(board[i][j]):
            for n in range(1, len(board) + 1):
                if is_valid(board, Placement(n, i, j)):
                    board[i][j] = n
                    if helper(board, i + 1, j):
                        return True
                    else:
                        board[i][j] = 0
                else:
                    board[i][j] = 0
            return False
        else:
            return helper(board, i + 1, j)

    res = helper(board, 0, 0)
    return res


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure("Cell left uninitialized")
        if x < 0 or x > len(seq):
            raise TestFailure("Cell value out of range")
        if x in seen:
            raise TestFailure("Duplicate value in section")
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j]
        for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure("Initial cell assignment has been changed")

    for br, sr in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure("Initial cell assignment has been changed")
        for bcell, scell in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure("Initial cell assignment has been changed")

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sudoku_solve.py", "sudoku_solve.tsv", solve_sudoku_wrapper
        )
    )
