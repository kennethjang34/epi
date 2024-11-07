from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# TC: O(n) SC: O(k)
def with_extra_space(L, k: int) -> Optional[ListNode]:
    if L.next is None:
        return None
    ptr = L
    cache = []
    k_2 = k
    if k == 1:
        k_2 = 2
    for _ in range(k_2):
        cache.append(ptr)
        ptr = ptr.next
    while ptr is not None:
        cache.append(ptr)
        ptr = ptr.next
        cache.pop(0)
    vals = []
    for p in cache:
        if p is not None:
            vals.append(p.data)
        else:
            vals.append(p)
    to_delete = cache[0]
    if k != 1:
        if to_delete.next is not None:
            to_delete.data = to_delete.next.data
            to_delete.next = to_delete.next.next
        else:
            to_delete.next = None
    else:
        to_delete.next = None
    return L


# TC: O(n), SC: O(1):
# Not bad but can have multiple disc accesses if list is too long to fit in memory all at once
def brute_force(L, k: int) -> Optional[ListNode]:
    if L.next is None:
        return None
    l = 0
    ptr = L
    while ptr is not None:
        if k == 1 and ptr.next.next is None:
            ptr.next = None
            return L
        ptr = ptr.next
        l += 1
    ptr = L
    for _ in range(l - k):
        ptr = ptr.next
    ptr.data = ptr.next.data
    ptr.next = ptr.next.next
    return L


# TC: O(n), SC: O(1)
# Better than brute_force in the cases where k is small enough that we can keep nodes between the two pointers in memory, while the list is too big to fit in memory.
# two-pointer approach halves the number of disc accesses
def two_pointers(L, k: int) -> Optional[ListNode]:
    if L.next is None:
        return None
    first = second = L
    for _ in range(k):
        first = first.next
    while first is not None:
        if k == 1 and second.next is not None and second.next.next is None:
            second.next = None
            break
        first = first.next
        second = second.next
    if second.next is not None:
        if second.next is not None:
            second.data = second.next.data
            second.next = second.next.next
        else:
            second.next = None
    return L


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k: int) -> Optional[ListNode]:
    return brute_force(L, k)
    # return with_extra_space(L, k)
    # return two_pointers(L, k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
