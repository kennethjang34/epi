import collections
import functools
from typing import DefaultDict, List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import math

Subarray = collections.namedtuple("Subarray", ("start", "end"))


def find_smallest_subarray_covering_set(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    # return find_smallest_subarray_covering_set_time_optimal(paragraph, keywords)
    return find_smallest_subarray_covering_set_space_optmial(paragraph, keywords)


def find_smallest_subarray_covering_set_space_optmial(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    class DoublyLinkedListNode:
        def __init__(self, data=None) -> None:
            self.data = data
            self.next = self.prev = None

    class LinkedList:
        def __init__(self) -> None:
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def append(self, value):
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -= 1

    loc = LinkedList()
    d = {keyword: None for keyword in keywords}
    res = Subarray(-1, math.inf)
    for idx, word in enumerate(paragraph):
        if word in d:
            it = d[word]
            if it is not None:
                loc.remove(it)
            loc.append(idx)
            d[word] = loc.tail
            if len(loc) == len(keywords):
                if idx - loc.head.data < res[1] - res[0]:
                    res = Subarray(loc.head.data, idx)
    return res


def find_smallest_subarray_covering_set_time_optimal(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    res = Subarray(-1, math.inf)
    l = 0
    counts = collections.Counter(keywords)
    remaining_to_cover = len(keywords)
    for r, word in enumerate(paragraph):
        counts[word] -= 1
        if counts[word] == 0:
            remaining_to_cover -= 1
        while remaining_to_cover == 0:
            if r - l < res.end - res.start:
                res = Subarray(l, r)
            left_word = paragraph[l]
            if left_word in keywords:
                counts[left_word] += 1
                if counts[left_word] > 0:
                    remaining_to_cover += 1
            l += 1
    return res


def find_smallest_subarray_covering_set_slow(
    paragraph: List[str], keywords: Set[str]
) -> Subarray:
    def helper(paragraph, keywords, i, j, mem):
        if (i, j) in mem:
            return Subarray(i, j)
        if i > j:
            return Subarray(0, math.inf)
        sublist = paragraph[i : j + 1]
        subset = set(sublist)
        res4 = Subarray(i, j)
        if len(keywords - subset) == 0:
            mem[(i, j)] = True
            res0 = helper(paragraph, keywords, i + 1, j, mem)
            res1 = helper(paragraph, keywords, i, j - 1, mem)
            res2 = helper(paragraph, keywords, i + 1, j - 1, mem)
            if res0.end - res0.start < res1.end - res1.start:
                if res0.end - res0.start < res2.end - res2.start:
                    res = res0
                else:
                    res = res2
            elif res1.end - res1.start < res2.end - res2.start:
                res = res1
            else:
                res = res2
            if res.end - res.start > j - i:
                res = res4
        else:
            res = Subarray(0, math.inf)
        return res

    return helper(paragraph, keywords, 0, len(paragraph) - 1, {})


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph, keywords)
    )

    if (
        start < 0
        or start >= len(paragraph)
        or end < 0
        or end >= len(paragraph)
        or start > end
    ):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper,
        )
    )
