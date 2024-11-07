from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# TC: O(n+m), SC: O(1), as nodes are reused for the result. If new nodes created then O(max(n,m))
def add_two_numbers(L1, L2) -> Optional[ListNode]:
    p1 = L1
    p2 = L2
    carry = 0
    head = L1

    if p1 is None:
        return p2
    if p2 is None:
        return p1
    while True:
        val1 = p1.data
        val2 = p2.data
        summ = val1 + val2 + carry
        carry = summ // 10
        p1.data = summ % 10
        if p1.next is None:
            p2 = p2.next
            if p2 is None and carry != 0:
                p1.next = ListNode(data=carry)
                carry = 0
            else:
                p1.next = p2
                p1 = p2
            break
        elif p2.next is None:
            if p1.next is None and carry != 0:
                p1.next = ListNode(data=carry)
                carry = 0
            else:
                p1 = p1.next
            break
        p1 = p1.next
        p2 = p2.next
    while carry != 0:
        assert p1 is not None
        summ = p1.data + carry
        p1.data = summ % 10
        carry = summ // 10
        if p1.next is None and carry != 0:
            p1.next = ListNode(data=carry)
            carry = 0
        p1 = p1.next
    return head


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_list_add.py", "int_as_list_add.tsv", add_two_numbers
        )
    )
