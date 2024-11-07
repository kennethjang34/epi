import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def preorder_left_exterior(node, is_exterior, res=[]):
    if node is None:
        return
    elif is_exterior:
        res.append(node)
        if node.left is None:
            preorder_left_exterior(node.right, True, res)
        else:
            preorder_left_exterior(node.left, is_exterior, res)
            preorder_left_exterior(node.right, not is_exterior, res)
    elif node.left is None and node.right is None:
        res.append(node)
    else:
        preorder_left_exterior(node.left, False, res)
        preorder_left_exterior(node.right, False, res)


def postorder_right_exterior(node, is_exterior, res=[]):
    if node is None:
        return
    elif is_exterior:
        if node.right is None:
            postorder_right_exterior(node.left, True, res)
        else:
            postorder_right_exterior(node.left, not is_exterior, res)
            postorder_right_exterior(node.right, is_exterior, res)
        res.append(node)
    elif node.left is None and node.right is None:
        res.append(node)
    else:
        postorder_right_exterior(node.left, False, res)
        postorder_right_exterior(node.right, False, res)


# TC: O(n), SC: O(h)
def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    res = []
    if tree is None:
        return res
    res.append(tree)
    preorder_left_exterior(tree.left, True, res)
    postorder_right_exterior(tree.right, True, res)
    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure("Resulting list contains None")
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_exterior.py", "tree_exterior.tsv", create_output_list_wrapper
        )
    )
