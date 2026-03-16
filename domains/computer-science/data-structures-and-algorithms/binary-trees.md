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

## Explainer

You've already worked with linked lists — chains of nodes connected by pointers, where each node points to the next. A **binary tree** generalizes this idea: instead of each node having one "next" pointer, each node has up to two child pointers, called **left** and **right**. This branching structure creates a hierarchy rather than a sequence, and that hierarchy is what makes binary trees powerful. The topmost node is the **root** (the entry point to the tree), and nodes with no children are called **leaves** (the endpoints).

To build intuition, think of a family tree or an organizational chart. The CEO sits at the root, with two direct reports below, each of whom has their own reports. The **depth** of any person is how many levels down from the CEO they sit — the CEO has depth 0, direct reports have depth 1, and so on. The **height** of the tree is the depth of the deepest node. These structural properties matter because they determine performance: most binary tree operations (searching, inserting, traversing) visit nodes along a path from root to leaf, so the height of the tree directly controls how long these operations take.

The shape of a binary tree matters enormously. A **balanced** binary tree keeps its height close to log₂(n), where n is the number of nodes — because each level doubles the number of nodes, you only need about 20 levels to store a million nodes. But a degenerate tree — where every node has only one child — looks exactly like a linked list, with height n. The difference between O(log n) and O(n) operations is the central motivation for balanced variants like AVL trees and red-black trees, which you'll encounter soon. Two other shape categories are important: a **full** binary tree is one where every node has either 0 or 2 children (never just 1), and a **complete** binary tree fills every level fully from left to right, with the possible exception of the last level.

Your recursion prerequisite is essential here because binary trees are inherently recursive structures. Every node is the root of its own subtree, and its left and right children are roots of smaller subtrees. This means nearly every binary tree algorithm — computing height, counting nodes, checking balance — follows the same recursive pattern: solve the problem for the left subtree, solve it for the right subtree, then combine the results. For example, the height of a tree is 1 + max(height of left subtree, height of right subtree), with a base case of -1 for an empty tree. Once you see this pattern, binary tree problems become exercises in recursive decomposition, and the data structure serves as the foundation for search trees, heaps, expression parsers, and many other structures you'll build next.
