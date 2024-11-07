import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient,
    check_sequence_is_uniformly_random,
    compute_combination_idx,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook


# concept very similar to creating a random permutation of length k when given list of [0..n-1]. We are creating the input list outselves
# TC: O(n), as it takes O(n) to create list of [0,1,..n-1]. SC: O(n) for the initially created list
def as_permutation(n: int, k: int) -> List[int]:
    subset = [i for i in range(n)]
    for i in range(k):
        next = random.randrange(i, n)
        subset[i], subset[next] = subset[next], subset[i]
    return subset[:k]


# concept very similar to creating a random permutation of length k when given list of [0..n-1],
# but we don't really have and create such a list.
# Instaed, track the swapped elements only in a hashmap
# and assume if the hashmap does not contain index i, it means the value corresponding to the index is the index itself.
# TC: O(k)
# SC: O(k)
def with_reduced_space(n: int, k: int) -> List[int]:
    subset = []
    swapped = {}
    for i in range(k):
        next_idx = random.randrange(i, n)
        subset.append(swapped.get(next_idx, next_idx))
        swapped[next_idx] = swapped.get(i, i)
    return subset


def random_subset(n: int, k: int) -> List[int]:
    # return as_permutation(n, k)
    return with_reduced_space(n, k)


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes,
            0.01,
        )

    run_func_with_retries(functools.partial(random_subset_runner, executor, n, k))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "random_subset.py", "random_subset.tsv", random_subset_wrapper
        )
    )
