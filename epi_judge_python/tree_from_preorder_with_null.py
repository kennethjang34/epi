import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# TC: O(n), assuming list.pop(0) takes O(1), although it is not necessarily true, it can made it into O(1) by using Double-ended queue
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    if preorder is None or len(preorder) == 0 or preorder[0] is None:
        return None
    root = BinaryTreeNode(preorder.pop(0))
    stk = [root]
    left = True
    while len(preorder) != 0:
        next_value = preorder.pop(0)
        if next_value is None:
            if left is False:
                stk.pop(-1)
            else:
                left = False
        else:
            next_node = BinaryTreeNode(next_value)
            if left:
                parent = stk[-1]
                parent.left = next_node
            else:
                parent = stk.pop(-1)
                parent.right = next_node
                left = True
            stk.append(next_node)
    return root


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == "null" else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_with_null.py",
            "tree_from_preorder_with_null.tsv",
            reconstruct_preorder_wrapper,
        )
    )
