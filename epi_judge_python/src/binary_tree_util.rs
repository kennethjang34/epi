use std::{cell::RefCell, fmt::Display, rc::Rc};

use crate::test_failure::{Property, PropertyName};

#[derive(Debug, Clone)]
struct TreePath {
    prev: Option<Rc<RefCell<Self>>>,
    to_left: bool,
}

impl TreePath {
    fn new() -> Self {
        TreePath {
            prev: None,
            to_left: false,
        }
    }

    fn with_left(self) -> Self {
        TreePath {
            prev: Some(Rc::new(RefCell::new(self))),
            to_left: true,
        }
    }

    fn with_right(self) -> Self {
        TreePath {
            prev: Some(Rc::new(RefCell::new(self))),
            to_left: false,
        }
    }

    fn to_string(&self) -> String {
        let mut result = Vec::new();
        let mut node = self;
        let mut next_node = Rc::new(RefCell::new(node.clone()));
        while let Some(prev) = next_node.clone().borrow().prev.clone() {
            result.push(if node.to_left { "->left" } else { "->right" });
            next_node = prev.clone();
        }

        result.reverse();
        result[0] = "root";

        result.concat()
    }
}

#[derive(Debug, Clone)]
struct BinaryTreeNode<T> {
    data: T,
    left: Option<Box<BinaryTreeNode<T>>>,
    right: Option<Box<BinaryTreeNode<T>>>,
}

impl<T> BinaryTreeNode<T> {
    fn new(
        data: T,
        left: Option<Box<BinaryTreeNode<T>>>,
        right: Option<Box<BinaryTreeNode<T>>>,
    ) -> Self {
        BinaryTreeNode { data, left, right }
    }
}

fn generate_preorder<T>(tree: &Option<Box<BinaryTreeNode<T>>>) -> Vec<T>
where
    T: Clone,
{
    let mut result = Vec::new();
    let mut stack = Vec::new();

    if let Some(node) = tree {
        stack.push(node);

        while let Some(node) = stack.pop() {
            result.push(node.data.clone());
            if let Some(right) = &node.right {
                stack.push(right);
            }
            if let Some(left) = &node.left {
                stack.push(left);
            }
        }
    }

    result
}

fn generate_inorder<T>(tree: &Option<Box<BinaryTreeNode<T>>>) -> Vec<T>
where
    T: Clone,
{
    let mut result = Vec::new();
    let mut stack = Vec::new();
    let mut initial = true;

    if let Some(mut node) = tree.clone() {
        stack.push(node);

        while let Some(mut node) = stack.pop() {
            if initial {
                initial = false;
            } else {
                result.push(node.data.clone());
                if let Some(right) = node.right.take() {
                    stack.push(right);
                }
                node = node.left.take().unwrap();
            }

            while let Some(left) = node.left.take() {
                stack.push(node);
                node = left;
            }
        }
    }

    result
}

fn generate_postorder<T>(tree: &Option<Box<BinaryTreeNode<T>>>) -> Vec<T>
where
    T: Clone,
{
    let mut result = Vec::new();
    let mut stack = Vec::new();

    if let Some(node) = tree {
        stack.push(node);

        while let Some(node) = stack.pop() {
            result.push(node.data.clone());
            if let Some(left) = &node.left {
                stack.push(left);
            }
            if let Some(right) = &node.right {
                stack.push(right);
            }
        }

        result.reverse();
    }

    result
}

fn find_node<T>(tree: &Option<Box<BinaryTreeNode<T>>>, val: T) -> Option<&Box<BinaryTreeNode<T>>>
where
    T: PartialEq,
{
    let mut stack = Vec::new();

    if let Some(node) = tree {
        stack.push(node);

        while let Some(node) = stack.pop() {
            if node.data == val {
                return Some(node);
            }
            if let Some(right) = &node.right {
                stack.push(right);
            }
            if let Some(left) = &node.left {
                stack.push(left);
            }
        }
    }

    None
}

fn must_find_node<T: Display + Clone>(
    tree: &Option<Box<BinaryTreeNode<T>>>,
    val: T,
) -> &Box<BinaryTreeNode<T>>
where
    T: PartialEq,
{
    find_node(tree, val.clone()).expect(&format!("{} was not found in the tree", val))
}

fn equal_binary_trees<T>(
    tree1: &Option<Box<BinaryTreeNode<T>>>,
    tree2: &Option<Box<BinaryTreeNode<T>>>,
) -> bool
where
    T: PartialEq,
{
    let mut stack = Vec::new();
    stack.push((tree1, tree2));

    while let Some((node1, node2)) = stack.pop() {
        match (node1, node2) {
            (Some(n1), Some(n2)) => {
                if n1.data != n2.data {
                    return false;
                }
                stack.push((&n1.left, &n2.left));
                stack.push((&n1.right, &n2.right));
            }
            (None, None) => {}
            _ => return false,
        }
    }

    true
}

#[derive(Debug)]
#[allow(unused_lifetimes)]
struct TestFailure {
    properties: Vec<Property>,
    description: String,
}

impl TestFailure {
    fn new(description: &str) -> Self {
        TestFailure {
            properties: Vec::new(),
            description: description.to_string(),
        }
    }

    fn with_property(&mut self, name: PropertyName, value: String) {
        self.properties.push(Property { name, value });
    }

    fn with_mismatch_info(&mut self, path: &TreePath, expected_item: String, result_item: String) {
        self.with_property(PropertyName::MismatchIndex, path.to_string());
        self.with_property(PropertyName::Expected, expected_item);
        self.with_property(PropertyName::Result, result_item);
    }
}

// fn main() {
//     // Example usage
//     let tree = BinaryTreeNode::new(
//         1,
//         Some(Box::new(BinaryTreeNode::new(
//             2,
//             Some(Box::new(BinaryTreeNode::new(4, None, None))),
//             Some(Box::new(BinaryTreeNode::new(
//                 5,
//                 Some(Box::new(BinaryTreeNode::new(8, None, None))),
//                 None,
//             ))),
//         ))),
//         Some(Box::new(BinaryTreeNode::new(
//             3,
//             Some(Box::new(BinaryTreeNode::new(
//                 6,
//                 None,
//                 Some(Box::new(BinaryTreeNode::new(9, None, None))),
//             ))),
//             Some(Box::new(BinaryTreeNode::new(
//                 7,
//                 None,
//                 Some(Box::new(BinaryTreeNode::new(
//                     10,
//                     Some(Box::new(BinaryTreeNode::new(11, None, None))),
//                     Some(Box::new(BinaryTreeNode::new(12, None, None))),
//                 ))),
//             ))),
//         ))),
//     );
//
//     assert_eq!(
//         generate_inorder(&Some(Box::new(tree.clone()))),
//         vec![4, 2, 8, 5, 1, 6, 9, 3, 7, 11, 10, 12]
//     );
//     assert_eq!(
//         generate_preorder(&Some(Box::new(tree.clone()))),
//         vec![1, 2, 4, 5, 8, 3, 6, 9, 7, 10, 11, 12]
//     );
//     assert_eq!(
//         generate_postorder(&Some(Box::new(tree.clone()))),
//         vec![4, 8, 5, 2, 9, 6, 11, 12, 10, 7, 3, 1]
//     );
//
//     let path = TreePath::new()
//         .with_left()
//         .with_left()
//         .with_right()
//         .with_left();
//     assert_eq!(path.to_string(), "root->left->left->right->left");
// }
