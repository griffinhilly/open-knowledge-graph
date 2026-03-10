---
id: avl-trees
title: AVL Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: time-space-complexity
  type: soft
tags:
- AVL-tree
- balanced-BST
- rotations
- self-balancing
stage: formal-systems
status: draft
---

# AVL Trees

## Core Idea
An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one (the balance factor is in {−1, 0, +1}). After each insertion or deletion, the tree checks balance factors and performs rotations — single or double — to restore balance. This guarantees O(log n) worst-case time for all operations. AVL trees were the first self-balancing BST; red-black trees are often preferred in practice for slightly lower rotation overhead.

## How It's Best Learned
First master BST insertions, then study rotations in isolation. Implement AVL insertion with balance-factor tracking. The four rotation cases (LL, RR, LR, RL) are best understood through diagrams before translating to code.

## Common Misconceptions
- Rotations preserve the BST ordering property; they only restructure the tree shape without violating the BST invariant.
- AVL trees require rebalancing on deletion as well as insertion, which is often overlooked in initial implementations.
