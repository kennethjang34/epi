from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# TC: O(n+m), where n: length of L1, m: length of L2
def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    ans = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = tail.next.next
        else:
            tail.next = L2
            L2 = tail.next.next
        tail = tail.next
    tail.next = L1 or L2
    return ans.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
