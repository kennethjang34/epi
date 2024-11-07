from typing import Iterator, List

from test_framework import generic_test


# Q: given a sequence, if arr[i] > for any arr[j], j > i then include in the list
# ex: [1,3,7,5,2] -> [1,0] for 3,1 (should return in the reversed order)


# TC: O(n^2)
def brute_force(sequence: Iterator[int]) -> List[int]:
    res = []
    l = list(sequence)
    for i in range(len(l)):
        h1 = l[i]
        for j in range(i + 1, len(l)):
            h2 = l[j]
            if h1 <= h2:
                break
        else:
            res.append(i)

    return res[::-1]


# TC: O(n)
# SC: O(n), as it requires constructing list from sequence to iterate in the reversed order
def optimized_reverse_traversal(sequence: Iterator[int]) -> List[int]:
    res = []
    max_h = 0
    l = list(sequence)
    length = len(l)
    for i, h in enumerate(reversed(l)):
        i = length - 1 - i
        if h > max_h:
            res.append(i)
            max_h = h
    return res


# TC: O(n)
# SC: O(n) in the worst case, but O(1) in the best case. Overall better space complexity than those that need to construct new list for reverse traversal
def optimized_with_stk(sequence: Iterator[int]) -> List[int]:
    stk = []
    for i, h in enumerate(sequence):
        while len(stk) > 0 and stk[-1][1] <= h:
            stk.pop()
        stk.append((i, h))
    res = []
    while len(stk) > 0:
        res.append(stk.pop()[0])
    return res


# Q: given a sequence, if arr[i] > for any arr[j], j > i then include in the list
# ex: [1,3,7,5,2] -> [1,0] for 3,1 (should return in the reversed order)
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # return brute_force(sequence=sequence)
    # return optimized_reverse_traversal(sequence=sequence)
    return optimized_with_stk(sequence=sequence)


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sunset_view.py", "sunset_view.tsv", examine_buildings_with_sunset
        )
    )
