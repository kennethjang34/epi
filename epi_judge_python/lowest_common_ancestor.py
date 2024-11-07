import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# traverse the tree twice
# TC: O(n*log(n)), SC: O(h)
def bruteforce(root: BinaryTreeNode, left, right):
    if left is right:
        return left
    if root is None or left is None or right is None:
        return None

    def find_node(cursor, node, path=[]):
        if cursor is node:
            return node
        if cursor is None or node is None:
            return None
        path.append(cursor)
        new_path = path[:]
        left_res = find_node(cursor.left, node, new_path)
        if left_res is not None:
            path[:] = new_path[:]
            return left_res
        else:
            return find_node(cursor.right, node, path)

    left_path = []
    right_path = []
    find_node(root, left, left_path)
    left_path.append(left)
    find_node(root, right, right_path)
    right_path.append(right)
    i = 0
    while i < min(len(left_path), len(right_path)):
        if left_path[i] is not right_path[i]:
            return left_path[i - 1]
        i += 1

    if len(left_path) < len(right_path):
        return left_path[i - 1]
    else:
        return right_path[i - 1]


# TC: O(n), SC: O(h)
def optimized(root, left, right):
    if root is None or left is None or right is None:
        return (0, None)
    if left is right:
        return (2, left)
    left_found_count, left_lca_node = optimized(root.left, left, right)
    if left_found_count == 2:
        return (2, left_lca_node)
    right_found_count, right_lca_node = optimized(root.right, left, right)
    if right_found_count == 2:
        return (2, right_lca_node)
    total_count = left_found_count + right_found_count + (left, right).count(root)
    if total_count == 2:
        return (2, root)
    if left_found_count == 1:
        return (total_count, left_lca_node)
    elif right_found_count == 1:
        return (total_count, right_lca_node)
    else:
        return (total_count, root)


def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    # return bruteforce(tree, node0, node1)
    return optimized(tree, node0, node1)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
