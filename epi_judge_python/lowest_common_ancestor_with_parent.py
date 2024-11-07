import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# TC: O(h), SC: O(h)
# traverse the tree only once, but need to store past parents
def time_optimized(n1, n2) -> Optional[BinaryTreeNode]:
    if n1 is None or n2 is None:
        return None
    elif n1 is n2:
        return n1
    p1s = set()
    p1s.add(n1)
    p2s = set()
    p2s.add(n2)
    while n1 is not None and n2 is not None:
        n1 = n1.parent
        n2 = n2.parent
        if n1 is n2:
            return n1
        if n1 in p2s:
            return n1
        if n2 in p1s:
            return n2
        p1s.add(n1)
        p2s.add(n2)
    if n1 is None:
        while n2 is not None:
            if n2 in p1s:
                return n2
            n2 = n2.parent
    if n2 is None:
        while n1 is not None:
            if n1 in p2s:
                return n1
            n1 = n1.parent
    return None


# TC: O(h), SC: O(1)
# traverse the tree two more times than time optimized solution in order to get the depth of each node
# However, this solution doesn't use extra memory
def space_optimized(n1, n2) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node is not None:
            node = node.parent
            depth += 1
        return depth

    n1_d = get_depth(n1)
    n2_d = get_depth(n2)
    lower = n1
    upper = n2
    if n1_d < n2_d:
        lower, upper = upper, lower
    for _ in range(abs(n1_d - n2_d)):
        lower = lower.parent
    while lower is not upper:
        lower = lower.parent
        upper = upper.parent
    return lower


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # return time_optimized(node0, node1)
    return space_optimized(node0, node1)


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
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
