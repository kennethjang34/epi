import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# TC: O(n), where n: max(len(l1),len(l2))
def overlapping_no_cycle_lists(l1, l2):
    if l1 is None or l2 is None:
        return None
    p1 = l1
    p2 = l2
    while p1 is not None and p2 is not None:
        p1 = p1.next
        p2 = p2.next
    longer = l1
    shorter = l2
    if p1 is None:
        longer = l2
        shorter = l1
    while p1 is not None or p2 is not None:
        if p1 is not None:
            p1 = p1.next
        else:
            p2 = p2.next
        longer = longer.next
    while shorter is not None and longer is not None:
        if shorter is longer:
            return shorter
        shorter = shorter.next
        longer = longer.next
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
