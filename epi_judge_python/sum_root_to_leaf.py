from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# TC: O(n), SC: O(h)
def pre_order(root, cur=0):
    if root is None:
        return 0
    cur = (cur << 1) + root.data
    # if node is a leaf then return current value
    if root.left is None and root.right is None:
        return cur
    # if node is not a leaf then return the sum of its leaves' values
    else:
        return pre_order(root.left, cur=cur) + pre_order(root.right, cur=cur)


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    return pre_order(tree, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
