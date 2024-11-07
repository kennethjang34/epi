import collections
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TC: O(n), SC: O(h=log n)
    # BST can be defined to be a binary tree
    # where each node's left subtree is either empty or less than or equal to that node,
    # and right subtree is either empty or greater than or equal to that node.
    # This means if a binary tree's both subtrees are BST and if the maximum value of the left subtree is <= root.value and right subtree's minimum value >= root.value,
    # we can conclude the tree is BST.
    def recursive_check(node, lower=-math.inf, upper=math.inf):
        return node is None or (
            lower <= node.data <= upper
            and recursive_check(node.left, lower, node.data)
            and recursive_check(node.right, node.data, upper)
        )

    # TC: O(n), SC: O(h=log n)
    # Note: if inorder traversal of a binary tree gives sorted array, then the tree is BST. The converse is also true.
    def inorder(node, prev=None):
        if node is None:
            return (True, None)
        else:
            if node.left is None:
                if prev is not None and node.data < prev:
                    return (False, node.data)
            else:
                left = inorder(node.left, prev)
                if not left[0] or left[1] > node.data:
                    return (False, node.data)
            if node.right is None:
                return (True, node.data)
            right = inorder(node.right, node.data)
            if not right[0] or right[1] < node.data:
                return right
            else:
                return (True, right[1])

    # TC: O(n), SC: O(n)
    # Instead of DFS methods, BFS method can detect the binary search tree constraint violation
    # at an earlier level of the binary tree at the expense of extra space (O(n) instead of O(h=log n)).
    def bfs(tree):
        QueueEntry = collections.namedtuple("QueueEntry", ("node", "lower", "upper"))
        if tree is None:
            return True
        q = collections.deque([QueueEntry(tree, -math.inf, math.inf)])
        while len(q) > 0:
            node, lower, upper = q.popleft()
            if node.data < lower or node.data > upper:
                return False
            else:
                if node.left is not None:
                    q.append(QueueEntry(node.left, lower=lower, upper=node.data))
                if node.right is not None:
                    q.append(QueueEntry(node.right, lower=node.data, upper=upper))
        return True

    return recursive_check(tree)
    # return inorder(tree)[0]
    # return bfs(tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
