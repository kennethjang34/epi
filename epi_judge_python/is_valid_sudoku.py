from typing import List

from test_framework import generic_test


# TC: O(9*9), as partial_assignment is a 9 x 9 matrix
# SC: O((9 * 9) * 3), as each row,col,subgrid has a set of max length 9 and there are 9 rows,cols,subgrids
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    row_sets = [set({}) for _ in range(9)]
    col_sets = [set({}) for _ in range(9)]
    subgrid_sets = [set({}) for _ in range(9)]
    for i in range(9):
        for j in range(9):
            r_set = row_sets[i]
            c_set = col_sets[j]
            sg_set_idx = (i // 3) * 3 + (j // 3)
            sg_set = subgrid_sets[sg_set_idx]
            n = partial_assignment[i][j]
            if n == 0:
                continue
            if n in r_set or n in c_set or n in sg_set:
                return False
            r_set.add(n)
            c_set.add(n)
            sg_set.add(n)
    return True




if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
