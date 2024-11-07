from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# TC: O(n), SC: O(n)
def with_visited_set(tree: BinaryTreeNode) -> List[int]:
    ans = []
    if tree is None:
        return []
    stk = [tree]
    visited = set()
    while len(stk) != 0:
        cur = stk[-1]
        if cur.left is not None and cur.left not in visited:
            stk.append(cur.left)
            visited.add(cur.left)
        else:
            ans.append(cur.data)
            stk.pop()
            if cur.right is not None and cur.right not in visited:
                stk.append(cur.right)
                visited.add(cur.right)
    return ans


# TC: O(n), SC: O(h)
def optimized_1(tree: BinaryTreeNode) -> List[int]:
    ans = []
    if tree is None:
        return []
    stk = []
    cur = tree
    while cur is not None:
        stk.append(cur)
        cur = cur.left
    while len(stk) != 0:
        cur = stk.pop()
        ans.append(cur.data)
        cur = cur.right
        while cur is not None:
            stk.append(cur)
            cur = cur.left
    return ans


# TC: O(n), SC: O(h)
def optimized_2(tree: BinaryTreeNode) -> List[int]:
    ans = []
    if tree is None:
        return []
    stk = []
    cur = tree
    while cur is not None or len(stk) != 0:
        if cur is not None:
            stk.append(cur)
            cur = cur.left
        else:
            cur = stk.pop()
            ans.append(cur.data)
            cur = cur.right
    return ans


# TC: O(n), SC: O(h)
def imitate_callstack(tree) -> List[int]:
    ans = []
    if tree is None:
        return []
    stk = [(tree, 0)]
    while len(stk) != 0:
        cur_node, cur_state = stk.pop()
        if cur_node is not None:
            if cur_state == 0:
                stk.append((cur_node, 1))
                stk.append((cur_node.left, 0))
            else:
                ans.append(cur_node.data)
                stk.append((cur_node.right, 0))
    return ans


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # return with_visited_set(tree)
    # return optimized_1(tree)
    # return optimized_2(tree)
    return imitate_callstack(tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_inorder.py", "tree_inorder.tsv", inorder_traversal
        )
    )
