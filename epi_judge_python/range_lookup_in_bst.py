import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple("Interval", ("left", "right"))


# TC: O(h+m), where h: height of input tree and m: the number of nodes that have keys in the input interval.
# Note, we visit nodes that appear in path to interval.left and to interval.right and nodes between the two paths.
# These nodes are not necessarily within the input interval and there are O(h) nodes from both paths.
# However, those between the two paths are always included in the result, and there are O(m) such nodes.
def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    ans = []
    if tree is None:
        return ans
    min_val = interval.left
    max_val = interval.right
    if tree.data < min_val:
        ans.extend(range_lookup_in_bst(tree.right, Interval(min_val, max_val)))
    elif tree.data > max_val:
        ans.extend(range_lookup_in_bst(tree.left, Interval(min_val, max_val)))
    else:
        if min_val <= tree.data <= max_val:
            ans.extend(range_lookup_in_bst(tree.left, Interval(min_val, max_val)))
            ans.append(tree.data)
            ans.extend(range_lookup_in_bst(tree.right, Interval(min_val, max_val)))
    return ans


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "range_lookup_in_bst.py",
            "range_lookup_in_bst.tsv",
            range_lookup_in_bst_wrapper,
        )
    )
