from test_framework import generic_test
import math


# TC: O(log x/s), s: tolerance
def square_root(x: float) -> float:
    l, r = (x, 1.0) if x < 1 else (1.0, x)
    while not math.isclose(l, r):
        mid = l + (r - l) / 2
        mid_sq = mid**2
        if mid_sq > x:
            r = mid
        else:
            l = mid
    # mid = l + (r - l) / 2
    # while l < mid and mid < r:
    #     mid_sq = mid**2
    #     if x < mid_sq:
    #         r = mid
    #     else:
    #         l = mid
    #     mid = l + (r - l) / 2
    return l


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "real_square_root.py", "real_square_root.tsv", square_root
        )
    )
