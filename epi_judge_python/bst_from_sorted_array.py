import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import binary_tree_height, generate_inorder
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# TC: O(n), as T(n)=2T(n/2)+O(1),
# or recursive call happens once for each node taking O(1) each time, resulting in a total of n O(1) calls=O(n).
def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    if A is None or len(A) == 0:
        return None
    mid_idx = len(A) // 2
    mid = A[mid_idx]
    root = BstNode(data=mid)
    left = A[0:mid_idx]
    right = None
    if mid_idx + 1 < len(A):
        right = A[mid_idx + 1 :]
    left_tree = build_min_height_bst_from_sorted_array(left)
    right_tree = build_min_height_bst_from_sorted_array(right)
    root.left = left_tree
    root.right = right_tree
    return root


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py",
            "bst_from_sorted_array.tsv",
            build_min_height_bst_from_sorted_array_wrapper,
        )
    )
