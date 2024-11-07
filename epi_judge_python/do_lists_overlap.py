import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def detect_cycle(head):
    if head is None:
        return None
    fast = slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        # cycle detected!
        t = 0
        if fast is slow:
            last = head
            while last is not slow:
                last = last.next
                slow = slow.next
            p = last.next
            t = 1
            while p is not last:
                t += 1
                p = p.next
            return last
    return None


# no cycle exists on either of l1,l2
def detect_overlap(l1, l2):
    if l1 is None or l2 is None:
        return None
    p1 = l1
    p2 = l2
    while p1 is not None and p2 is not None:
        p1 = p1.next
        p2 = p2.next
    longer = l1
    shorter = l2
    longer_current = p1
    if p2 is not None:
        longer = l2
        shorter = l1
        longer_current = p2
    while longer_current is not None:
        longer_current = longer_current.next
        longer = longer.next
    while longer is not None or shorter is not None:
        if longer is shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


# TC: O(n)
def overlapping_lists(l1, l2):
    if l1 is None or l2 is None:
        return None
    if l1 is l2:
        return l1
    c1 = detect_cycle(l1)
    c2 = detect_cycle(l2)
    if c1 is None and c2 is None:
        return detect_overlap(l1, l2)

    else:
        if c2 is None or c1 is None:
            return None
        if c1 is c2:
            return c1
        p1 = c1.next
        while p1 is not c1:
            if p1 is c2:
                return c2
            p1 = p1.next
        return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_lists_overlap.py", "do_lists_overlap.tsv", overlapping_lists_wrapper
        )
    )
