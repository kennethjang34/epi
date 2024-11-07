from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# TC: O(n), SC: O(1)
def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    p = L
    while p is not None:
        next_node = p.next
        while next_node and next_node.data == p.data:
            next_node = next_node.next
        p.next = next_node
        p = next_node
    return L


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            "remove_duplicates_from_sorted_list.tsv",
            remove_duplicates,
        )
    )
