from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# ex: 2,3,5,3,2 becomes 5,3,2,2,3


# TC: O(n), SC: O(1)
# Note: if k >= n, where n: length of the linked list, then it's the same as given k=k%n, as the list shifts right in a cyclic way.
def cyclically_right_shift_list(L, k: int) -> Optional[ListNode]:
    if L is None:
        return L
    tail = L
    l = 1
    while tail.next is not None:
        l += 1
        tail = tail.next
    # # the following line should come before 'new_tail.next'=None, in case tail==new_tail, i.e. new_tail==tail and so new_tail.next should be the original head (this is the case when k=0)
    tail.next = L
    k = k % l
    new_tail = L
    for _ in range(l - k - 1):
        new_tail = new_tail.next
    head = new_tail.next
    new_tail.next = None
    return head


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "list_cyclic_right_shift.py",
            "list_cyclic_right_shift.tsv",
            cyclically_right_shift_list,
        )
    )
