---
id: red-black-trees
title: Red-Black Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: tree-node-structure-properties
  type: soft
tags:
- red-black-trees
- self-balancing
- binary-search
- balancing
- rotations
stage: formal-systems
status: draft
---

# Red-Black Trees

## Core Idea
Red-black trees are self-balancing binary search trees where each node is colored red or black, subject to five invariants: root is black, leaves are black, red nodes have only black children, all paths have equal black-node counts, and no two consecutive red nodes exist. These properties guarantee O(log n) height while requiring fewer rotations than AVL trees during insertion and deletion.

## How It's Best Learned
Study the five properties and understand why they imply logarithmic height (the proof is subtle). Trace insertion with recoloring and rotations. Compare to AVL trees: red-black has fewer rebalancing operations but is less tightly balanced. Implement insertion algorithm carefully.

## Common Misconceptions
- Red-black properties directly imply height bounds (they do, but the proof requires careful analysis). - Red-black trees are always better than AVL (red-black has fewer rotations; AVL is more balanced; choice depends on use case).

## Explainer

You already know that a binary search tree (BST) keeps elements in sorted order, allowing O(h) search, insertion, and deletion where h is the tree's height. The problem is that an unbalanced BST can degenerate into a linked list with h = n. A **red-black tree** solves this by attaching a color — red or black — to every node and enforcing invariants that prevent the tree from becoming too lopsided. The result is a guaranteed height of at most 2 log₂(n + 1), ensuring O(log n) worst-case operations.

The five **red-black properties** are: (1) every node is either red or black, (2) the root is black, (3) every null leaf is considered black, (4) a red node's children must both be black (no two consecutive reds on any path), and (5) every path from a given node to any of its descendant null leaves contains the same number of black nodes. Property 5 is the most important — it defines the **black-height** of the tree. Because no path can have consecutive red nodes (property 4) and all paths have the same black-height (property 5), the longest possible path (alternating red-black-red-black...) is at most twice the length of the shortest path (all black). This 2:1 ratio is what bounds the height.

When you insert a new node, you color it red (to preserve black-height) and then fix any violations of property 4 — the "no consecutive reds" rule. The fix involves **recoloring** nodes and performing **rotations**. A rotation is a local restructuring that shifts one node up and another down while preserving the BST ordering. There are two cases: if the new node's uncle (parent's sibling) is red, you can fix the violation by recoloring without rotation. If the uncle is black, you perform one or two rotations plus recoloring. The fix propagates upward at most O(log n) levels but requires at most two rotations total per insertion — this is fewer than AVL trees, which may rotate at every level.

Deletion is more complex but follows the same pattern: remove the node using standard BST deletion, then fix any black-height violations with recoloring and rotations (at most three per deletion). The practical significance of red-black trees is enormous — they are the implementation behind `std::map` and `std::set` in C++, Java's `TreeMap` and `TreeSet`, and the Linux kernel's process scheduler. They offer a pragmatic balance: slightly less rigidly balanced than AVL trees (so lookups may touch a few more nodes), but with cheaper insertions and deletions due to fewer rotations. For workloads dominated by modifications rather than pure lookups, red-black trees are typically the better choice.
