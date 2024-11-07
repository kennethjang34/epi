from typing import Optional

from list_node import ListNode
from test_framework import generic_test
import math


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    return stable_sort_list_opt(L)
    # return stable_sort_list_brute_force(L)


# TC: O(n log n), SC: O(log n). no explicitly allocated extra memory, but call stack depth can reach O(log n) for merge sort.
def stable_sort_list_opt(L: ListNode) -> Optional[ListNode]:
    def merge_two_sorted_list(L1: ListNode, L2: ListNode):
        i = L1
        j = L2
        if i.data > j.data:
            i, j = j, i
        dummy_head = ListNode(-math.inf, None)
        head = dummy_head
        while i and j:
            if i.data < j.data:
                head.next = i
                i = i.next
                head.next.next = None
            else:
                head.next = j
                j = j.next
                head.next.next = None
            head = head.next
        while i:
            head.next = i
            i = i.next
            head = head.next
        while j:
            head.next = j
            j = j.next
            head = head.next
        return dummy_head.next

    if L is None or L.next is None:
        return L
    pre_slow, slow, fast = None, L, L
    while fast is not None and fast.next is not None:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next
    pre_slow.next = None
    return merge_two_sorted_list(stable_sort_list_opt(L), stable_sort_list_opt(slow))


# TC: O(n^2)
def stable_sort_list_brute_force(L: ListNode) -> Optional[ListNode]:
    flag = False
    orig_head = ListNode(-math.inf, L)
    head = L
    prev = orig_head
    while not flag:
        flag = True
        prev = orig_head
        head = prev.next
        while head is not None and head.next is not None:
            if head.data > head.next.data:
                prev.next = head.next
                head.next = head.next.next
                prev.next.next = head
                prev = prev.next

                flag = False
            else:
                prev = prev.next
                head = prev.next
    return orig_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_list.py", "sort_list.tsv", stable_sort_list
        )
    )
