import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


# TC: O(h), SC: O(h)
def recursive(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    if tree is None or k < 1:
        return None
    if tree.left is None:
        if k == 1:
            return tree
        else:
            return find_kth_node_binary_tree(tree.right, k - 1)
    else:
        left_size = tree.left.size
        if left_size >= k:
            return find_kth_node_binary_tree(tree.left, k)
        elif left_size + 1 == k:
            return tree
        else:
            return find_kth_node_binary_tree(tree.right, k - left_size - 1)


# TC: O(h), SC: O(1)
def iterative(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    if tree is None or k < 1:
        return None
    while tree:
        # the following condition does not work as inorder traversal visites left subtree before current root!
        # if k == 1:
        #     return tree
        left_size = tree.left.size if tree.left else 0
        if left_size >= k:
            tree = tree.left
        elif left_size + 1 == k:
            return tree
        else:
            tree = tree.right
            k = k - left_size - 1
    return None


def find_kth_node_binary_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    # return recursive(tree, k)
    return iterative(tree, k)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_node_in_tree.py",
            "kth_node_in_tree.tsv",
            find_kth_node_binary_tree_wrapper,
        )
    )
