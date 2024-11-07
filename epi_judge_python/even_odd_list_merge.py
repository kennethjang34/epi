from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# TC: O(n), SC: O(1)
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L
    even_tail = L
    odd_head = odd_tail = L.next
    curr = L.next.next
    # alternating using flag: turn
    # note: make sure odd_tail.next is None at the end!

    # tails = [even_tail, odd_tail]
    # turn = 0
    # while curr is not None:
    #     tails[turn].next = curr
    #     tails[turn] = curr
    #     curr = curr.next
    #     turn ^= 1
    # tails[1].next = None
    # tails[0].next = odd_head
    while curr is not None:
        even_tail.next = curr
        odd_tail.next = curr.next
        even_tail = even_tail.next
        odd_tail = odd_tail.next
        if curr.next is None:
            break
        curr = curr.next.next
    even_tail.next = odd_head
    return L


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "even_odd_list_merge.py", "even_odd_list_merge.tsv", even_odd_merge
        )
    )
