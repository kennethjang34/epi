import functools
import random
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient,
    check_sequence_is_uniformly_random,
    compute_combination_idx,
    run_func_with_retries,
)
from test_framework.test_utils import enable_executor_hook


# TC: O(n), SC: O(k)
# Note:
# The probability of obtaining any subset S of length k is the same because each element has k/(length of elements seen so far, or len(samples)).
# However, the subsets are not independent from iteration to iteration. Successive subsets are different in at most one element!
# in the brute force method, they are indeed independent though. (brute force method will just make the whole new permutation of length k for each iteration over and over again)
# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    samples = []
    while True:
        packet = next(stream, None)
        if packet is None:
            break
        samples.append(packet)
        if len(samples) <= k:
            continue
        else:
            rand_idx = random.randint(0, len(samples) - 1)
            samples[rand_idx], samples[-1] = samples[-1], samples[rand_idx]
    return samples[:k]


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda: [online_random_sample(iter(stream), k) for _ in range(100000)]
        )

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes,
            0.01,
        )

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_sampling.py", "online_sampling.tsv", online_random_sample_wrapper
        )
    )
