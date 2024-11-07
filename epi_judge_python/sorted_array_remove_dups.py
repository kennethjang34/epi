import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# TC: O(n), SC: O(1)
# when it comes to filtering array eleemnts, often iterating through the array with write_index, where elements of arr[0:i] are all valid after filtering

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    cur = 0
    prev = None
    for n in A:
        if prev is None:
            cur = 1
        elif prev != n:
            A[cur] = n
            cur += 1
        prev = n
    return cur


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_array_remove_dups.py",
            "sorted_array_remove_dups.tsv",
            delete_duplicates_wrapper,
        )
    )
