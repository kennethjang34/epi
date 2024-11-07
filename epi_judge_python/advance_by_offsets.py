from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    i = 0
    stretch = 0
    while True:
        stretch = max(stretch, i + A[i])
        if stretch >= len(A) - 1:
            return True
        if i + 1 <= stretch:
            i += 1
        else:
            break
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end
        )
    )
