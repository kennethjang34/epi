import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


# TC: O(h), SC: O(1)
def iterative(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node is None:
        return None
    if node.right is None:
        while node.parent is not None and node.parent.right is node:
            node = node.parent
        return node.parent
    else:
        node = node.right
        while node.left is not None:
            node = node.left
        return node


# TC: O(h), SC: O(h)
def recursive(node: BinaryTreeNode, ignore_right=False) -> Optional[BinaryTreeNode]:
    if node is None:
        return None
    elif node.right is None or ignore_right:
        if node.parent is not None and node.parent.right is node:
            return recursive(node.parent, ignore_right=True)
        else:
            return node.parent

    else:
        node = node.right
        while node.left is not None:
            node = node.left
        return node


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # return iterative(node)
    return recursive(node)


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "successor_in_tree.py", "successor_in_tree.tsv", find_successor_wrapper
        )
    )
