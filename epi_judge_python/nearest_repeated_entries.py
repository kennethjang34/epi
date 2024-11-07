from typing import DefaultDict, List

from test_framework import generic_test

import math


# TC: O(n), SC: O(d), d: number of distinct entries/words in input paragraph
def find_nearest_repetition(paragraph: List[str]) -> int:
    memory = DefaultDict(lambda: -math.inf)
    res = math.inf
    for pos, word in enumerate(paragraph):
        res = min(res, pos - memory[word])
        memory[word] = pos
    return res if res != math.inf else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
