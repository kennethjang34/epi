import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# TC: O(n^2), as it takes O(n) to insert/delete an element in the middle of a list
def brute_force(size: int, s: List[str]) -> int:
    last_idx = size
    i = 0
    while i < last_idx:
        ch = s[i]
        if ch == "a":
            s[i] = "d"
            s.insert(i, "d")
            last_idx += 1
            i += 1
        i += 1
    i = 0
    while i < last_idx:
        ch = s[i]
        if ch == "b":
            del s[i]
            last_idx -= 1
            continue
        i += 1
    return last_idx

# TC: O(n)
def optimized(size: int, s: List[str]) -> int:
    write_idx = 0
    a_count = 0
    for ch in s[:size]:
        if ch != "b":
            if ch == "a":
                a_count += 1
            s[write_idx] = ch
            write_idx += 1
    final_size = write_idx + a_count
    idx = final_size - 1
    for ch in reversed(s[:write_idx]):
        if ch == "a":
            s[idx] = "d"
            s[idx - 1] = "d"
            idx -= 1
        else:
            s[idx] = ch
        idx -= 1
    return final_size


def replace_and_remove(size: int, s: List[str]) -> int:
    # return brute_force(size, s)
    return optimized(size, s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
