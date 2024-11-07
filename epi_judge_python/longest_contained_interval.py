from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    # return longest_contained_range_subopt(A)
    return longest_contained_range_optimal(A)


# TC: O(n), SC: O(n)
def longest_contained_range_optimal(A: List[int]) -> int:
    ans = 0
    to_process = set(A)
    while len(to_process) > 0:
        e = to_process.pop()
        lower_bound = e - 1
        while lower_bound in to_process:
            to_process.remove(lower_bound)
            lower_bound -= 1
        upper_bound = e + 1
        while upper_bound in to_process:
            to_process.remove(upper_bound)
            upper_bound += 1
        ans = max(ans, upper_bound - lower_bound - 1)
    return ans


# TC: O(n), SC: O(n)
def longest_contained_range_subopt(A: List[int]) -> int:
    pos = {}
    for i, e in enumerate(A):
        pos[e] = i
    visited = {}
    rans = {}
    for i, e in enumerate(A):
        if e not in visited:
            rans[e] = e
            visited[e] = e
            orig = e
            e = e + 1
            while e in pos and e not in visited:
                visited[e] = orig
                rans[orig] = e
                e += 1
    ans = 0
    for e, ran in rans.items():
        cur = ran - e + 1
        ans = max(ans, cur)
        e = e - 1
        while e in visited:
            orig = visited[e]
            ran2 = rans[orig]
            cur += ran2 - orig + 1
            ans = max(ans, cur)
            e = orig - 1
            if e == orig:
                break
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_contained_interval.py",
            "longest_contained_interval.tsv",
            longest_contained_range,
        )
    )
