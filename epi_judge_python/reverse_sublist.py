from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# TC: O(n)
def reverse_sublist(L, start: int, finish: int) -> Optional[ListNode]:
    if L is None or start == 0:
        return L
    head = L
    prev_head = head
    left_tail = None
    for i in range(start - 1):
        if left_tail is None:
            left_tail = head
        if i < start - 2:
            left_tail = left_tail.next
        prev_head = prev_head.next
    curr = prev_head.next
    original_sh = prev_head
    for _ in range(start, finish):
        forward = curr.next
        curr.next = prev_head
        prev_head = curr
        original_sh.next = forward
        curr = forward

    if left_tail is not None:
        left_tail.next = prev_head
        return head
    else:
        return prev_head


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
