---
id: tree-node-structure-properties
title: Tree Structure and Node Properties
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: arrays-and-indexed-collections
  type: soft
builds-toward:
- binary-trees
- binary-search-trees
- avl-tree-rotations-balancing
- tree-traversals
tags:
- trees
- graph-theory
- hierarchy
- nodes
- edges
- terminology
stage: formal-systems
status: draft
---

# Tree Structure and Node Properties

## Core Idea
A tree is a connected acyclic graph with a hierarchical structure: a root at the top, internal nodes in the middle, and leaves at the bottom. Key properties include height (longest root-to-leaf path), depth (distance from root), degree (number of children), and balance. Understanding these properties is essential for analyzing tree algorithms and designing balanced structures.

## How It's Best Learned
Draw several tree structures and label height, depth, degree, and parent-child relationships. Calculate these properties by hand on various trees. Study the relationship between height, node count, and branching degree (e.g., a binary tree of height h has at most 2^(h+1) - 1 nodes).

## Common Misconceptions
- All balanced trees are equivalent (balance improves search cost, but binary search trees perform well with random insertion order). - Height and depth are the same (height measures from node to furthest leaf; depth measures from root to node).

## Questions

```yaml
- question: "A node v in a binary tree has depth 4. What is the height of node v?"
  type: multiple-choice
  options:
    - "4, because height and depth are measured along the same path from the root"
    - "The tree's total height minus 4, because depth and height always sum to the tree's height"
    - "Cannot be determined — height depends on v's subtree below it, not its distance from the root"
    - "0, because nodes at even depth are always leaves"
  answer: 2
  explanation: "Depth measures edges from the root down to a node — it tells you how far below the root the node sits. Height measures the longest path from a node down to any of its leaves — it tells you how deep the subtree rooted at that node extends. These are independent: a node at depth 4 could have height 0 (if it is a leaf) or height 10 (if it has a large subtree below it). They sum to the tree's total height only for nodes that lie on the single longest root-to-leaf path."

- question: "Integer keys 1, 2, 3, 4, 5 are inserted in order into an initially empty binary search tree. What is the height of the resulting tree, and what does this reveal?"
  type: multiple-choice
  options:
    - "Height 2; the BST insertion algorithm automatically balances after each insertion"
    - "Height 4; the tree degenerates into a right-leaning chain, giving O(n) search time instead of O(log n)"
    - "Height 3; BST insertion always produces a tree of height ⌈log₂ n⌉ for n elements"
    - "Height 5; each new node always becomes a leaf at the maximum possible depth"
  answer: 1
  explanation: "Inserting sorted keys into a BST is the worst case: each new key is larger than all previous ones, so it always becomes the right child of the current rightmost node. The result is effectively a linked list with height n − 1 = 4. Search now takes O(n) time rather than O(log n). This is why self-balancing structures (AVL trees, red-black trees) exist: they enforce the invariant that height stays O(log n) regardless of insertion order, using rotations to maintain balance after each operation."

- question: "The height of a tree equals the depth of its deepest leaf."
  type: true-false
  answer: true
  explanation: "True. The height of a tree is defined as the height of the root, which equals the length of the longest path from the root to any leaf. The deepest leaf is at the end of this longest path, and its depth equals the number of edges from the root to it — the same count as the tree's height. So height of tree = depth of deepest leaf."

- question: "In a binary tree, every internal node has exactly 2 children."
  type: true-false
  answer: false
  explanation: "False. 'Binary tree' means each node has *at most* 2 children (degree 0, 1, or 2). A tree is called 'full' if every internal node has exactly 2 children, and 'perfect' if it is full and all leaves are at the same depth — but these are special cases. A binary tree with height h can have as few as h + 1 nodes (a chain where each internal node has exactly one child) or as many as 2^(h+1) − 1 nodes (a perfect tree)."

- question: "Explain why an unbalanced binary search tree can degrade to O(n) search time, and why this makes the tree's height the critical structural property for performance."
  type: short-answer
  answer: "In a BST, search works by comparing the target key to the current node and moving left or right. The number of comparisons is at most the height of the tree — the length of the longest root-to-leaf path. In a balanced tree, height is O(log n), so any element can be found in at most log₂(n) comparisons. But if the tree is unbalanced — for example, all nodes in a right-leaning chain from sorted insertion — height is O(n) and search degenerates to a linear scan. Balance ensures the exponential capacity of trees (2^h nodes at height h) is fully exploited, keeping height logarithmic in the number of elements."
  explanation: "Height directly determines worst-case search cost. A perfectly balanced binary tree of height 20 can hold over a million nodes and find any element in at most 20 comparisons. The same million-node tree inserted in sorted order has height ~1,000,000 and may require a million comparisons in the worst case. This is why AVL trees, red-black trees, and B-trees enforce balance invariants: they guarantee O(log n) height regardless of insertion order by performing rotations or rebalancing after each modification."
```

## Explainer

If arrays give you a flat line of elements and linked lists give you a chain, a **tree** gives you a branching hierarchy. Picture an organizational chart: one person at the top (the CEO), with subordinates branching out below, each of whom may have their own subordinates. In computer science, the person at the top is called the **root**, the branching connections are **edges**, and every person in the chart is a **node**. Nodes with no subordinates — no children — are called **leaves**. Everything else is an **internal node**. Unlike the arrays and indexed collections you already know, trees naturally represent data with parent-child relationships and nested structure.

Every node in a tree has a precise location described by two measurements. **Depth** counts how many edges you must travel downward from the root to reach that node — the root itself has depth 0, its children have depth 1, and so on. **Height** works in the opposite direction: it measures the longest path from a node down to any of its leaves. A leaf has height 0, and the height of the tree as a whole is the height of the root. These are easy to confuse because both involve counting edges along paths, but depth looks upward toward the root and height looks downward toward the leaves.

The **degree** of a node is simply how many children it has. In a binary tree, every node has degree 0, 1, or 2. In a general tree, nodes can have any number of children. The maximum degree across all nodes, combined with the tree's height, determines the tree's capacity. A binary tree of height h can hold at most 2^(h+1) - 1 nodes — so a tree of height 3 can hold at most 15 nodes, while a tree of height 20 can hold over a million. This exponential relationship between height and capacity is precisely why trees are so powerful for search: if the tree is **balanced** (meaning all leaves are at roughly the same depth), you can store n elements in a tree of height approximately log₂(n) and reach any element in at most that many steps.

Balance is the single most important structural property for performance. An unbalanced tree can degenerate into a chain — imagine inserting already-sorted data into a binary search tree, where each new element becomes the right child of the previous one. The result is effectively a linked list with O(n) search time instead of O(log n). This is why later topics on AVL trees and other self-balancing structures exist: they enforce balance through rotations after each insertion or deletion, guaranteeing that the height stays logarithmic. Before studying those mechanisms, you need to be comfortable identifying root, leaves, depth, height, and degree by sight — these are the vocabulary every tree algorithm builds upon.
