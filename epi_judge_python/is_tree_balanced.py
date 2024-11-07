from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# using post order traversal
# TC: O(n)
# SC: O(h), or: O(log n) if not skewed, O(n) if skewed
def helper(root):
    if root is None:
        return (True, -1)
    if root.left is None and root.right is None:
        return (True, 0)
    elif root.right is None:
        if root.left.left is None and root.left.right is None:
            return (True, 1)
        else:
            return (False, -1)
    elif root.left is None:
        if root.right.left is None and root.right.right is None:
            return (True, 1)
        else:
            return (False, -1)
    else:
        left_res = helper(root.left)
        if left_res[0] is False:
            return (False, -1)
        right_res = helper(root.right)
        if right_res[0] is False:
            return (False, -1)
        if abs(left_res[1] - right_res[1]) <= 1:
            return (True, max(left_res[1], right_res[1]))
        else:
            return (False, -1)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return helper(tree)[0]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
