import copy
import functools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook


def get_rand(n):
    return random.randint(0, n - 1)


# TC: O(n*log(n)) <- reference: coupon collector's problem. In short, it's same as expected number of buying a product with a coupon from an urn until all unique colors are chosen with replacement. (or coupons)
# SC: O(n), for the hashset and returned list
def brute_force(n: int) -> List[int]:
    used = set({})
    ans = []
    while len(used) < n:
        next = get_rand(n)
        while next in used:
            next = get_rand(n)
        used.add(next)
        ans.append(next)
    return ans


# TC: O(n), SC: O(n) (only for the returned list)
def optimized(n: int) -> List[int]:
    ans = [i for i in range(n)]
    for i in range(n):
        rand_idx = get_rand(n - i)
        ans[i], ans[rand_idx] = ans[rand_idx], ans[i]
    return ans


def compute_random_permutation(n: int) -> List[int]:
    # return brute_force(n)
    return optimized(n)


@enable_executor_hook
def compute_random_permutation_wrapper(executor, n):
    def compute_random_permutation_runner(executor, n):
        def permutation_index(perm):
            p = copy.deepcopy(perm)
            idx = 0
            n = len(p)
            while p:
                a = p.pop(0)
                idx += a * math.factorial(n - 1)
                for i, b in enumerate(p):
                    if b > a:
                        p[i] -= 1
                n -= 1
            return idx

        result = executor.run(
            lambda: [compute_random_permutation(n) for _ in range(1000000)]
        )

        return check_sequence_is_uniformly_random(
            [permutation_index(perm) for perm in result], math.factorial(n), 0.01
        )

    run_func_with_retries(
        functools.partial(compute_random_permutation_runner, executor, n)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "random_permutation.py",
            "random_permutation.tsv",
            compute_random_permutation_wrapper,
        )
    )
