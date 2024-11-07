from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    ans = []
    if tree is None:
        return []
    next_lvl = [tree]
    while len(next_lvl) != 0:
        cur = next_lvl
        next_lvl = []
        cur_values = []
        for node in cur:
            cur_values.append(node.data)
            if node.left is not None:
                next_lvl.append(node.left)
            if node.right is not None:
                next_lvl.append(node.right)
        ans.append(cur_values)

    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
