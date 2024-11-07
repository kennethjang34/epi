from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # return find_k_largest_in_bst_recursive(tree, k)
    return find_k_largest_in_bst_iterative(tree, k)


# TC: O(h+k), SC: O(h)
def find_k_largest_in_bst_iterative(root: BstNode, k: int) -> List[int]:
    ans = []
    stk = []
    cur = root
    if k > 0:
        while len(ans) < k and (cur is not None or len(stk) > 0):
            if cur is not None:
                stk.append(cur)
                cur = cur.right
            else:
                cur = stk.pop()
                ans.append(cur.data)
                cur = cur.left

    return ans


# TC: O(h+k), SC: O(h)
def find_k_largest_in_bst_recursive(node: BstNode, k: int) -> List[int]:
    ans = []
    if node is None or k < 1:
        return ans
    if node.right is None:
        ans.append(node.data)
        if len(ans) < k:
            ans.extend(find_k_largest_in_bst_recursive(node.left, k - 1))
    else:
        ans.extend(find_k_largest_in_bst_recursive(node.right, k))
        if len(ans) < k:
            ans.append(node.data)
        if len(ans) < k:
            ans.extend(find_k_largest_in_bst_recursive(node.left, k - len(ans)))
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
