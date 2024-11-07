import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


# TC: O(h)=O(log n) in worst case, O(d) on average,
# where h: height of the BST and d: difference between depths of the ancestor and descendant
# when they are indeed proper ancestor and descendant.
def pair_includes_ancestor_and_descendant_of_m(
    possible_anc_or_desc_0: BstNode,
    possible_anc_or_desc_1: BstNode,
    middle: BstNode,
) -> bool:
    p1, p2 = possible_anc_or_desc_0, possible_anc_or_desc_1
    while (
        (p1 is not None or p2 is not None)
        and (p1 is not middle)
        and (p2 is not middle)
        and (p1 is not p2)
    ):
        if p1 is not None:
            p1 = p1.left if p1.data > middle.data else p1.right
        if p2 is not None:
            p2 = p2.left if p2.data > middle.data else p2.right
    if (p1 is not middle and p2 is not middle) or p1 is p2:
        return False
    child = None
    p = middle
    if p1 is middle:
        child = possible_anc_or_desc_1
    elif p2 is middle:
        child = possible_anc_or_desc_0
    else:
        return False
    p = middle
    while p is not None and p is not child:
        p = p.left if p.data > child.data else p.right
    return p is child


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
    executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1, middle_idx
):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(
            pair_includes_ancestor_and_descendant_of_m,
            candidate0,
            candidate1,
            middle_node,
        )
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            "descendant_and_ancestor_in_bst.tsv",
            pair_includes_ancestor_and_descendant_of_m_wrapper,
        )
    )
