---
id: binary-trees
title: Binary Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: linked-lists
  type: hard
- id: recursion-basics
  type: hard
- id: trees-in-graph-theory
  type: soft
builds-toward:
- tree-traversals
- binary-search-trees
- heaps-and-priority-queues
tags:
- binary-tree
- nodes
- root
- leaf
- height
stage: formal-systems
status: validated
---

# Binary Trees

## Core Idea
A binary tree is a hierarchical data structure where each node has at most two children, called the left and right child. The tree starts at a root node; nodes with no children are leaves. Important properties include height (the longest root-to-leaf path), completeness (all levels fully filled except possibly the last), and balance (heights of left and right subtrees differ by at most a constant). Binary trees form the foundation for binary search trees, heaps, and expression parsers.

## How It's Best Learned
Implement a BinaryTree class with Node objects containing left, right, and value fields. Draw many tree examples and practice identifying height, depth of specific nodes, and whether a tree is complete or balanced before touching code.

## Common Misconceptions
- Height and depth are often confused: height is a property of the whole tree or a subtree rooted at a node, while depth is the distance from the root to a specific node.
- A full binary tree (every node has 0 or 2 children) is distinct from a complete binary tree (all levels filled left-to-right).
