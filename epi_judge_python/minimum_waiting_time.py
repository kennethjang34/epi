from typing import List

from test_framework import generic_test


# TC: O(n log n)
def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times = sorted(service_times)
    ans = 0
    cur = 0
    for t in service_times[:-1]:
        cur += t
        ans += cur
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_waiting_time.py",
            "minimum_waiting_time.tsv",
            minimum_total_waiting_time,
        )
    )
