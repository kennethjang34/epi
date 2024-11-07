from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def check_symmetric(left, right) -> bool:
    if left is None and right is None:
        return True
    elif left is None:
        return False
    elif right is None:
        return False
    else:
        if left.data == right.data:
            return check_symmetric(left.left, right.right) and check_symmetric(
                left.right, right.left
            )
        else:
            return False


# TC: O(n), SC: O(h) from call stack
def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True
    return check_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
