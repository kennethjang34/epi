from typing import Set
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from bintrees import RBTree


class ClientsCreditsInfo:
    def __init__(self) -> None:
        self.offset = 0
        self.credit_tree = RBTree()
        self.client_dict = {}

    # TC: O(log n)
    def insert(self, client_id: str, c: int) -> None:
        self.client_dict[client_id] = c - self.offset
        self.credit_tree.set_default(c - self.offset, set()).add(client_id)

    # TC: O(log n)
    def remove(self, client_id: str) -> bool:
        if client_id in self.client_dict:
            credit = self.client_dict.pop(client_id)
            client_set: Set = self.credit_tree.get(credit)
            client_set.remove(client_id)
            if len(client_set) == 0:
                self.credit_tree.remove(credit)
            return True
        else:
            return False

    # TC: O(1)
    def lookup(self, client_id: str) -> int:
        if client_id in self.client_dict:
            credit = self.client_dict[client_id]
            return credit + self.offset
        else:
            return -1

    # TC: O(1)
    def add_all(self, C: int) -> None:
        self.offset += C

    # TC: O(log n) or O(1). O(log n) with naive implementation but bintree uses caching for max element
    def max(self) -> str:
        s: Set = self.credit_tree.max_item()[1]
        return s[0]


# very slow
# class ClientsCreditsInfoBaseNodes:
#     class Client:
#         def __init__(self, client_id, c, base) -> None:
#             self.client_id = client_id
#             self.credit = c
#             self.base = base
#
#         def __lt__(self, another):
#             return self.get_credit() < another.get_credit()
#
#         def __eq__(self, another):
#             return self.client_id == another.client_id
#
#         def get_credit(self):
#             total = self.credit + self.base.get_total()
#             return total
#
#     class Base:
#         def __init__(self, amount=0) -> None:
#             self.amount = amount
#             self.next = None
#
#         def get_total(self):
#             s = 0
#             base = self
#             while base is not None:
#                 s += base.amount
#                 base = base.next
#             return s
#
#         def append(self, amount):
#             self.next = ClientsCreditsInfoBaseNodes.Base(amount)
#
#     def __init__(self) -> None:
#         self.base = ClientsCreditsInfoBaseNodes.Base(0)
#         self.client_tree = RBTree()
#         self.client_dict = {}
#
#     def insert(self, client_id: str, c: int) -> None:
#         self.base.append(0)
#         self.base = self.base.next
#         client = ClientsCreditsInfoBaseNodes.Client(client_id, c, self.base)
#         self.client_dict[client_id] = client
#         self.client_tree.insert(client, client)
#
#     def remove(self, client_id: str) -> bool:
#         if client_id in self.client_dict:
#             client = self.client_dict.pop(client_id)
#             self.client_tree.discard(client)
#             return True
#         else:
#             return False
#
#     def lookup(self, client_id: str) -> int:
#         if client_id in self.client_dict:
#             client = self.client_dict[client_id]
#             return client.get_credit()
#         else:
#             return -1
#
#     def add_all(self, C: int) -> None:
#         self.base.amount += C
#
#     def max(self) -> str:
#         return self.client_tree.max_item()[1].client_id


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == "ClientsCreditsInfo":
            pass
        if op == "max":
            result = cr.max()
            if result != s_arg:
                raise TestFailure("Max: return value mismatch")
        elif op == "remove":
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure("Remove: return value mismatch")
        elif op == "insert":
            cr.insert(s_arg, i_arg)
        elif op == "add_all":
            cr.add_all(i_arg)
        elif op == "lookup":
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure("Lookup: return value mismatch")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "adding_credits.py", "adding_credits.tsv", client_credits_info_tester
        )
    )
