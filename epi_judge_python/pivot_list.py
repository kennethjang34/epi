import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting_without_dummy_heads(L, k: int):
    lh = lt = None
    mh = mt = None
    rh = rt = None
    curr = L
    while curr is not None:
        val = curr.data
        if val < k:
            if lt is None:
                lh = lt = curr
            else:
                lt.next = curr
                lt = lt.next
        elif val == k:
            if mt is None:
                mh = mt = curr
            else:
                mt.next = curr
                mt = mt.next
        else:
            if rt is None:
                rh = rt = curr
            else:
                rt.next = curr
                rt = rt.next
        tmp = curr
        curr = curr.next
        tmp.next = None
    ## the order of concatenating matters because if mh.next == mt.next == None, then lt.next will just become None, regardless of rh.next is None or not
    head = lh
    if head is None:
        head = mh
        if head is None:
            head = rh
        else:
            assert mt is not None
            mt.next = rh
    else:
        assert lt is not None
        if mt is None:
            lt.next = rh
        else:
            lt.next = mh
            mt.next = rh
    return head


def list_pivoting_with_dummy_heads(L: ListNode, k: int) -> Optional[ListNode]:
    lh = lt = ListNode()
    mh = mt = ListNode()
    rh = rt = ListNode()
    curr = L
    while curr is not None:
        val = curr.data
        if val < k:
            lt.next = curr
            lt = lt.next
        elif val == k:
            mt.next = curr
            mt = mt.next
        else:
            rt.next = curr
            rt = rt.next
        tmp = curr
        curr = curr.next
        tmp.next = None
    ## the order of concatenating matters because if mh.next == mt.next == None, then lt.next will just become None, regardless of rh.next is None or not
    mt.next = rh.next
    lt.next = mh.next
    return lh.next


# TC: O(n)
def list_pivoting(L: ListNode, k: int) -> Optional[ListNode]:
    # return list_pivoting_with_dummy_heads(L, k)
    return list_pivoting_without_dummy_heads(L, k)


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure("List is not pivoted")
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure("List is not pivoted")

    if sorted(original) != sorted(pivoted):
        raise TestFailure("Result list contains different values")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pivot_list.py", "pivot_list.tsv", list_pivoting_wrapper
        )
    )
