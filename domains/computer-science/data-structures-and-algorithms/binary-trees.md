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

## Questions

```yaml
- question: "A programmer inserts one million records into a binary tree in sorted ascending order. Search operations are far slower than expected — comparable to a linked list. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Binary trees cannot store sorted data; the records should have been stored in a hash table"
    - "Inserting in sorted order creates a degenerate tree where each node has only one child, giving height n instead of log₂(n)"
    - "The tree exceeded its memory allocation and switched to disk-based storage"
    - "Binary tree search is inherently O(n) for datasets above a certain size"
  answer: 1
  explanation: "When sorted values are inserted into a plain binary tree, each new value is the largest seen so far and attaches to the rightmost position — creating a single chain with no branching. The tree degrades to a linked list with height n, so search is O(n) instead of O(log n). This is the central motivation for self-balancing variants like AVL trees and red-black trees, which restructure after insertions to keep height at O(log n) regardless of insertion order."

- question: "A binary tree has 7 nodes arranged so every level is completely filled. What is the height of this tree (measured as the depth of the deepest node, with the root at depth 0)?"
  type: multiple-choice
  options:
    - "7 — one unit of height per node"
    - "3 — the number of fully filled levels"
    - "6 — the depth of the deepest node counted starting from 1"
    - "2 — the depth of the deepest node counted starting from 0"
  answer: 3
  explanation: "A completely filled tree with 7 nodes has 3 levels: root at depth 0, two children at depth 1, four grandchildren at depth 2. Height = 2 (depth of the deepest node). Option B confuses height with the number of levels (height + 1). Off-by-one errors in height are common: if height counts edges from root to deepest leaf, a 7-node complete tree has height 2; if it counts nodes along that path, it's 3. The convention used here counts depth from 0."

- question: "The height of a node in a binary tree is defined as its distance from the root."
  type: true-false
  answer: false
  explanation: "Distance from the root is the node's DEPTH, not its height. Height of a node is the length of the longest path from that node DOWN to a leaf — or equivalently, the height of the subtree rooted at that node. Height of the entire tree equals the depth of the deepest leaf. This confusion is one of the most common binary tree errors: depth measures position going down from the root; height measures how far down the subtree extends further."

- question: "A full binary tree (most node has 0 or 2 children) is typically also a complete binary tree (most levels filled left-to-right)."
  type: true-false
  answer: false
  explanation: "Full and complete are independent properties. A full tree only requires that every internal node has exactly 2 children (no nodes with just 1 child). A complete tree requires every level to be fully filled except possibly the last, filled left-to-right. Example of a full but not complete tree: a root with two children where the left child has two grandchildren and the right child has none. Every node has 0 or 2 children (full), but the levels are not uniformly filled (not complete)."

- question: "Why does the shape of a binary tree — balanced versus degenerate — matter so much for the performance of operations like search and insertion?"
  type: short-answer
  answer: "Most binary tree operations visit nodes along a root-to-target path. The height of the tree determines the maximum length of this path. In a balanced tree, each level doubles the number of nodes, so a tree with n nodes has height approximately log₂(n) — about 20 levels for a million nodes. In a degenerate tree (all nodes in a single chain), height equals n. The difference between O(log n) and O(n) is enormous: searching a million records takes ~20 steps when balanced, up to ~1,000,000 steps when degenerate."
  explanation: "A tree storing identical data in a balanced versus degenerate arrangement has the same information content but wildly different performance. This is why self-balancing tree variants exist: they add structural constraints that guarantee O(log n) height by automatically restructuring after insertions and deletions, preventing the degenerate case regardless of input order."
```

## Explainer

You've already worked with linked lists — chains of nodes connected by pointers, where each node points to the next. A **binary tree** generalizes this idea: instead of each node having one "next" pointer, each node has up to two child pointers, called **left** and **right**. This branching structure creates a hierarchy rather than a sequence, and that hierarchy is what makes binary trees powerful. The topmost node is the **root** (the entry point to the tree), and nodes with no children are called **leaves** (the endpoints).

To build intuition, think of a family tree or an organizational chart. The CEO sits at the root, with two direct reports below, each of whom has their own reports. The **depth** of any person is how many levels down from the CEO they sit — the CEO has depth 0, direct reports have depth 1, and so on. The **height** of the tree is the depth of the deepest node. These structural properties matter because they determine performance: most binary tree operations (searching, inserting, traversing) visit nodes along a path from root to leaf, so the height of the tree directly controls how long these operations take.

The shape of a binary tree matters enormously. A **balanced** binary tree keeps its height close to log₂(n), where n is the number of nodes — because each level doubles the number of nodes, you only need about 20 levels to store a million nodes. But a degenerate tree — where every node has only one child — looks exactly like a linked list, with height n. The difference between O(log n) and O(n) operations is the central motivation for balanced variants like AVL trees and red-black trees, which you'll encounter soon. Two other shape categories are important: a **full** binary tree is one where every node has either 0 or 2 children (never just 1), and a **complete** binary tree fills every level fully from left to right, with the possible exception of the last level.

Your recursion prerequisite is essential here because binary trees are inherently recursive structures. Every node is the root of its own subtree, and its left and right children are roots of smaller subtrees. This means nearly every binary tree algorithm — computing height, counting nodes, checking balance — follows the same recursive pattern: solve the problem for the left subtree, solve it for the right subtree, then combine the results. For example, the height of a tree is 1 + max(height of left subtree, height of right subtree), with a base case of -1 for an empty tree. Once you see this pattern, binary tree problems become exercises in recursive decomposition, and the data structure serves as the foundation for search trees, heaps, expression parsers, and many other structures you'll build next.
