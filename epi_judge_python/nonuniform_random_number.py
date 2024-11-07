import bisect
import collections
import functools
import itertools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


# TC: O(n). O(n) for constructing cumulative probability list + O(log(n)) for binary search for the corresponding interval. O(n) dominates the overall TC
# SC: O(n)
def nonuniform_random_number_generation(
    values: List[int], probabilities: List[float]
) -> int:
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    ## or using for loop like below. Note using itertools.accumulate function is faster due to implementation difference although they are essentially doing the same
    ## and the TCs are therefore also the same
    ##

    # prefix_sum_of_probabilities = [probabilities[0]]
    # for i in range(1, len(probabilities)):
    #     prefix_sum_of_probabilities.append(
    #         prefix_sum_of_probabilities[i - 1] + probabilities[i]
    #     )
    x = random.random()
    value_idx = bisect.bisect_left(prefix_sum_of_probabilities, x)
    return values[value_idx]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values, probabilities):
    def nonuniform_random_number_generation_runner(executor, values, probabilities):
        N = 10**6
        result = executor.run(
            lambda: [
                nonuniform_random_number_generation(values, probabilities)
                for _ in range(N)
            ]
        )

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(
            nonuniform_random_number_generation_runner, executor, values, probabilities
        )
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nonuniform_random_number.py",
            "nonuniform_random_number.tsv",
            nonuniform_random_number_generation_wrapper,
        )
    )
