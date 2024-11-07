import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def generate_all_binary_trees(num_nodes: int) -> List[Optional[BinaryTreeNode]]:
    return generate_all_binary_trees_pythonic(num_nodes)
    # return generate_all_binary_trees_v1(num_nodes)


def generate_all_binary_trees_v1(num_nodes: int) -> List[Optional[BinaryTreeNode]]:
    def helper(num_nodes) -> List[Optional[BinaryTreeNode]]:
        res = []
        if num_nodes == 0:
            return [None]
        if num_nodes == 1:
            return [BinaryTreeNode()]
        if num_nodes == 2:
            root_1 = BinaryTreeNode()
            root_2 = BinaryTreeNode()
            res = [root_1, root_2]
            root_1.left = BinaryTreeNode()
            root_2.right = BinaryTreeNode()
        else:
            res = []
            for i in range(num_nodes):
                left_subtrees = helper(i)
                right_subtrees = helper(num_nodes - (i + 1))
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = BinaryTreeNode()
                        res.append(root)
                        root.left = left_subtree
                        root.right = right_subtree
        return res

    return helper(num_nodes=num_nodes)


# TC: O(3^(n)+(combination(2n,n))/(n+1))
# Number of recursive calls R(n) can be approximated by O(3^(n)) since R(n)=sum of (R(n-1-i)+R(i)) for i=0..=n-1
# Number of total subtree combinations C(n), which dominates the merge step, is (combination(2n,n))/(n+1), since C(n)=sum of (C(n-1-i)*C(i)) for i=0..=n-1


def generate_all_binary_trees_pythonic(
    num_nodes: int,
) -> List[Optional[BinaryTreeNode]]:
    if num_nodes == 0:
        return [None]
    result: List[Optional[BinaryTreeNode]] = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - (1 + num_left_tree_nodes)
        left_subtrees = generate_all_binary_trees_pythonic(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees_pythonic(num_right_tree_nodes)
        result += [
            BinaryTreeNode(0, left, right)
            for left in left_subtrees
            for right in right_subtrees
        ]
    return result


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_trees.py",
            "enumerate_trees.tsv",
            generate_all_binary_trees_wrapper,
        )
    )
