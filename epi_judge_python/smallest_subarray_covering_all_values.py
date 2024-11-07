import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple("Subarray", ("start", "end"))

import math


# TC: O(n), SC: O(m), where n: len(paragraph), m: len(keywords)
def find_smallest_sequentially_covering_subset(
    paragraph: List[str], keywords: List[str]
) -> Subarray:
    res = Subarray(-1, math.inf)
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_loc = [-1] * len(keywords)
    shortest_subarr_len = [math.inf] * len(keywords)
    shortest_dist = math.inf
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarr_len[keyword_idx] = 1
            elif shortest_subarr_len[keyword_idx - 1] < math.inf:
                dist_to_prev = i - latest_loc[keyword_idx - 1]
                shortest_subarr_len[keyword_idx] = (
                    dist_to_prev + shortest_subarr_len[keyword_idx - 1]
                )
            latest_loc[keyword_idx] = i
            if (
                keyword_idx == len(keywords) - 1
                and shortest_subarr_len[-1] < shortest_dist
            ):
                shortest_dist = shortest_subarr_len[-1]
                res = Subarray(i - shortest_dist + 1, i)
    return res if res.end - res.start <= len(paragraph) else Subarray(-1, -1)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph, keywords):
    result = executor.run(
        functools.partial(
            find_smallest_sequentially_covering_subset, paragraph, keywords
        )
    )

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError("Subarray start index is negative")

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            "smallest_subarray_covering_all_values.tsv",
            find_smallest_sequentially_covering_subset_wrapper,
        )
    )
