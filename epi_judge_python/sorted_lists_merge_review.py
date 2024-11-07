from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# TC: O(n+m), where n: len(L1), m: len(L2)
def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    R_0 = None
    # i_1, j_1=1
    # represents i_k-th node of L1
    i = L1
    # represents j_k-th node of L2
    j = L2
    if i.data <= j.data:
        R_0 = i
        i = i.next
    else:
        R_0 = j
        j = j.next
    # represents k-th node of R
    k = R_0
    while i is not None and j is not None:
        if i.data <= j.data:
            k.next = i
            i = i.next
        else:
            k.next = j
            j = j.next
        k = k.next
    if i is not None:
        k.next = i
    elif j is not None:
        k.next = j
    return R_0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
