from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


# Note bst cannot be rebuilt using inorder traversal only even if all the nodes have unique values/keys.
# BST can be reconstructed with either preorder or postorder sequence.
# TC: O(n)
def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    def helper(lower, upper, root_idx):
        if root_idx >= len(preorder_sequence) or not (
            lower <= preorder_sequence[root_idx] <= upper
        ):
            return (None, root_idx)
        else:
            subtree_root = BstNode(data=preorder_sequence[root_idx])
            subtree_root.left, root_idx = helper(lower, subtree_root.data, root_idx + 1)
            subtree_root.right, root_idx = helper(subtree_root.data, upper, root_idx)
            return (subtree_root, root_idx)

    root = helper(float("-inf"), float("inf"), 0)[0]
    return root


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_preorder.py", "bst_from_preorder.tsv", rebuild_bst_from_preorder
        )
    )
