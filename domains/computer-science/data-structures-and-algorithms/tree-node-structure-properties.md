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

## Explainer

If arrays give you a flat line of elements and linked lists give you a chain, a **tree** gives you a branching hierarchy. Picture an organizational chart: one person at the top (the CEO), with subordinates branching out below, each of whom may have their own subordinates. In computer science, the person at the top is called the **root**, the branching connections are **edges**, and every person in the chart is a **node**. Nodes with no subordinates — no children — are called **leaves**. Everything else is an **internal node**. Unlike the arrays and indexed collections you already know, trees naturally represent data with parent-child relationships and nested structure.

Every node in a tree has a precise location described by two measurements. **Depth** counts how many edges you must travel downward from the root to reach that node — the root itself has depth 0, its children have depth 1, and so on. **Height** works in the opposite direction: it measures the longest path from a node down to any of its leaves. A leaf has height 0, and the height of the tree as a whole is the height of the root. These are easy to confuse because both involve counting edges along paths, but depth looks upward toward the root and height looks downward toward the leaves.

The **degree** of a node is simply how many children it has. In a binary tree, every node has degree 0, 1, or 2. In a general tree, nodes can have any number of children. The maximum degree across all nodes, combined with the tree's height, determines the tree's capacity. A binary tree of height h can hold at most 2^(h+1) - 1 nodes — so a tree of height 3 can hold at most 15 nodes, while a tree of height 20 can hold over a million. This exponential relationship between height and capacity is precisely why trees are so powerful for search: if the tree is **balanced** (meaning all leaves are at roughly the same depth), you can store n elements in a tree of height approximately log₂(n) and reach any element in at most that many steps.

Balance is the single most important structural property for performance. An unbalanced tree can degenerate into a chain — imagine inserting already-sorted data into a binary search tree, where each new element becomes the right child of the previous one. The result is effectively a linked list with O(n) search time instead of O(log n). This is why later topics on AVL trees and other self-balancing structures exist: they enforce balance through rotations after each insertion or deletion, guaranteeing that the height stays logarithmic. Before studying those mechanisms, you need to be comfortable identifying root, leaves, depth, height, and degree by sight — these are the vocabulary every tree algorithm builds upon.
