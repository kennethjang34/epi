from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


# TC: O(n), SC: O(1)
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    ans = []
    if tree is None:
        return ans
    node = tree
    while node is not None:
        while node.left is not None:
            node = node.left
        ans.append(node.data)
        if node.right is not None:
            node = node.right
            continue
        elif node.parent is None:
            return ans
        else:
            while node:
                parent = node.parent
                if parent is None or parent.right is node:
                    node = parent
                else:
                    ans.append(parent.data)
                    if parent.right is not None:
                        node = parent.right
                        break
                    else:
                        node = parent
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
