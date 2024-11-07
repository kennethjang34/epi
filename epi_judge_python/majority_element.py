import collections
from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    # return majority_search_collection_counter(stream)
    cand = None
    cand_count = 0
    for c in stream:
        if cand_count == 0:
            cand = c
            cand_count = 1
        elif cand == c:
            cand_count += 1
        else:
            cand_count -= 1
    return cand


def majority_search_collection_counter(stream: Iterator[str]) -> str:
    counts = collections.Counter(stream)
    return counts.most_common(1)[0][0]


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "majority_element.py", "majority_element.tsv", majority_search_wrapper
        )
    )
