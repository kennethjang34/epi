import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import time


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    return lca_fast(node0, node1)
    # return lca_slow(node0, node1)
    # (parent0, elapsed0) = measure_runtime(lambda: lca_fast(node0, node1))
    # (parent1, elapsed1) = measure_runtime(lambda: lca_slow(node0, node1))
    # assert parent0 == parent1
    # if elapsed0 < elapsed1:
    #     print()
    #     print("fast one took:", elapsed0)
    #     print("slow one took:", elapsed1)
    # return parent0


def measure_runtime(f, quite=True):
    start = time.time()
    returned = f()
    end = time.time()
    elapsed = end - start
    if not quite:
        print("time elapsed:", elapsed)
    return (returned, elapsed)


# TC: O(h0+h1), where h0: depth of node0 and h1: depth of node1, SC: O(1)
def lca_slow(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node0 is node1:
        return node0

    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    if depth1 > depth0:
        node0, node1 = node1, node0
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


# TC, SC: O(D0+D1), where D0: distance from lca to node0 and D1: from lca to node1.
def lca_fast(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node0 is node1:
        return node0
    left = set()
    right = set()
    left.add(node0)
    right.add(node1)
    while node0.parent is not None or node1.parent is not None:
        if node0.parent is not None:
            node0 = node0.parent
            left.add(node0)
            if node0 in right:
                return node0
        if node1.parent is not None:
            node1 = node1.parent
            right.add(node1)
            if node1 in left:
                return node1
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1))
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
