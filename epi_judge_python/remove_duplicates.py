import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (
            self.first_name < other.first_name
            if self.first_name != other.first_name
            else self.last_name < other.last_name
        )


def eliminate_duplicate(A: List[Name]) -> None:
    # eliminate_duplicate_with_extra_space(A)
    # eliminate_duplicate_no_extra_space_slow(A)
    eliminate_duplicate_opt(A)


# TC: O(n log n), SC: O(1)
# no popping. reuse the array A for saving new values
def eliminate_duplicate_opt(A: List[Name]) -> None:
    A.sort()
    i = 0
    write_idx = 0
    while i < len(A) - 1:
        if A[i].first_name == A[i + 1].first_name:
            i += 1
        else:
            A[write_idx] = A[i]
            i += 1
            write_idx += 1
    del A[write_idx:]


# TC: O(n log n), but can be O(n) with hashtable from the beginning (no need to sort actually), SC: O(n)
def eliminate_duplicate_with_extra_space(A: List[Name]) -> None:
    A.sort()
    i = 0
    s = set()
    while i < len(A) - 1:
        if A[i].first_name == A[i + 1].first_name:
            s.add(i)
        i += 1
    a2 = [A[i] for i in range(len(A)) if i not in s]
    A[:] = a2


# TC: O(n log n) or O(n^2) depending on A.pop() implementation because popping might cause all the elements to be moved each time, SC: O(1)
def eliminate_duplicate_no_extra_space_slow(A: List[Name]) -> None:
    A.sort()
    i = 0
    while i < len(A) - 1:
        if A[i].first_name == A[i + 1].first_name:
            A.pop(i + 1)
        else:
            i += 1


@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates.py",
            "remove_duplicates.tsv",
            eliminate_duplicate_wrapper,
            comp,
        )
    )
