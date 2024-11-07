import itertools
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    num_bucket = 1 << 16
    buckets = [0] * num_bucket
    stream, stream_cp = itertools.tee(stream)
    for addr in stream_cp:
        buckets[addr >> 16] += 1
    cand = next(i for i, c in enumerate(buckets) if c < num_bucket)
    mp = [0] * num_bucket
    for addr in stream:
        if (addr >> 16) == cand:
            mp[addr & ((1 << 16) - 1)] = 1
    ans = (cand << 16) | (next(i for i, v in enumerate(mp) if v == 0))
    return ans


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure("{} appears in stream".format(res))
    except ValueError:
        raise TestFailure("Unexpected no missing element exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "absent_value_array.py",
            "absent_value_array.tsv",
            find_missing_element_wrapper,
        )
    )
