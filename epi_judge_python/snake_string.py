from test_framework import generic_test

import itertools


# TC: O(n), SC: O(n) (excluding space for return value. this implementation needs a temporary 2D array with 3 rows)
def using_2d_arr(s: str) -> str:
    l = len(s)
    rows = [[], [], []]
    cycle = itertools.cycle([1, 0, 1, 2])
    for c in s:
        row = rows[cycle.__next__()]
        row.append(c)
    return "".join([c for r in rows for c in r])


# TC: O(n), SC: O(1) (excluding space for return value)
def using_loops(s: str) -> str:
    l = len(s)
    arr = []
    for i in range(1, l, 4):
        arr.append(s[i])
    for i in range(0, l, 2):
        arr.append(s[i])
    for i in range(3, l, 4):
        arr.append(s[i])
    return "".join(arr)


def snake_string(s: str) -> str:
    # return using_2d_arr(s)
    return using_loops(s)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "snake_string.py", "snake_string.tsv", snake_string
        )
    )
