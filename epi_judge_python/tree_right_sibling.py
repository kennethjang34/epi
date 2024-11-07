import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


# TC: O(n)
# SC: O(2^h)
def construct_right_sibling(tree: BinaryTreeNode) -> None:
    if tree is None:
        return
    q = [tree]
    next_q = []
    prev_node = None
    while len(q) != 0 or len(next_q) != 0:
        if len(q) == 0:
            q = next_q
            next_q = []
            prev_node = None
        node = q.pop(0)
        if node.left is not None:
            next_q.append(node.left)
        if node.right is not None:
            next_q.append(node.right)
        if prev_node is not None:
            prev_node.next = node
        prev_node = node


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)] for level in traverse_left(cloned)]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_right_sibling.py",
            "tree_right_sibling.tsv",
            construct_right_sibling_wrapper,
        )
    )
