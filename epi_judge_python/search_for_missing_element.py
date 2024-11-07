import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple(
    "DuplicateAndMissing", ("duplicate", "missing")
)


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    missing_xor_dup = 0
    n = len(A)
    for i in range(n):
        missing_xor_dup ^= i ^ A[i]
    lsb = missing_xor_dup & (-missing_xor_dup)
    cand = 0
    for i in range(n):
        if i & lsb > 0:
            cand ^= i
        if A[i] & lsb > 0:
            cand ^= A[i]
    mis, dup = None, None
    for i in range(n):
        if A[i] == cand:
            mis = missing_xor_dup ^ cand
            dup = cand
    if mis is None:
        mis = cand
        dup = missing_xor_dup ^ cand
    return DuplicateAndMissing(missing=mis, duplicate=dup)


def res_printer(prop, value):
    def fmt(x):
        return "duplicate: {}, missing: {}".format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED, PropertyName.RESULT) else value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            "find_missing_and_duplicate.tsv",
            find_duplicate_missing,
            res_printer=res_printer,
        )
    )
