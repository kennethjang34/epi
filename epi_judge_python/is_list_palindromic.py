from list_node import ListNode
from test_framework import generic_test


def reverse_list(head):
    if head is None:
        return head
    new_head = head
    curr = head.next
    new_head.next = None
    while curr is not None:
        tmp = curr.next
        curr.next = new_head
        new_head = curr
        curr = tmp
    return new_head


# TC: O(n),
# SC: O(n), as it stores left half of the list
def brute_force(L) -> bool:
    if L is None or L.next is None:
        return True
    left = []
    slow = fast = L
    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
            left.append(slow.data)
            slow = slow.next
        else:
            slow = slow.next
            break
    for i in reversed(list(range(len(left)))):
        if slow.data != left[i]:
            return False
        slow = slow.next
    return True


# TC: O(n), SC: O(1)
# instead of creating a new array to store a half of the list, reverse the right half.
# to prevent unexpected side effects, reverse the reversed half again to restore the original list before return
def optimized(L) -> bool:
    if L is None or L.next is None:
        return True
    slow = fast = L
    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        else:
            break
    old_left_tail = slow
    right = reverse_list(slow.next)
    slow.next = None
    new_right_head = right
    left = L
    while right is not None:
        if left.data != right.data:
            old_left_tail.next = reverse_list(new_right_head)
            return False
        right = right.next
        left = left.next
    old_left_tail.next = reverse_list(new_right_head)
    new = []
    n = L
    while n is not None:
        new.append(n.data)
        n = n.next
    return True


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # return brute_force(L)
    return optimized(L)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
