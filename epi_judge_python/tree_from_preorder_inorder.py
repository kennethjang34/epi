from argparse import ArgumentError
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# TC: O(n), SC: O(h)
def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode:
    preorder = preorder.copy()
    inorder = inorder.copy()
    if len(preorder) == 0:
        return None
    elif len(preorder) != len(inorder):
        raise ArgumentError
    root = BinaryTreeNode(preorder.pop(0))
    # stk has nodes that have been visited in preorder but have not yet been found by inorder[0]
    stk = [root]
    prev_node = None
    while len(preorder) != 0:
        node = stk.pop()
        # pointer to the last node that was found in inorder[0]
        prev_node = None
        next_node = BinaryTreeNode(preorder.pop(0))
        ## assuming each node has distinct values
        while node.data == inorder[0]:
            inorder.pop(0)
            prev_node = node
            if len(stk) != 0:
                node = stk.pop(-1)
            else:
                break
        stk.append(node)
        if prev_node is not None:
            prev_node.right = next_node
        else:
            node.left = next_node
        stk.append(next_node)
    return root


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
