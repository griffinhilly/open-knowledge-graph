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
- id: logarithms-intro
  type: soft
tags:
- AVL-tree
- balanced-BST
- rotations
- self-balancing
stage: formal-systems
status: validated
---

# AVL Trees

## Core Idea
An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one (the balance factor is in {−1, 0, +1}). After each insertion or deletion, the tree checks balance factors and performs rotations — single or double — to restore balance. This guarantees O(log n) worst-case time for all operations. AVL trees were the first self-balancing BST; red-black trees are often preferred in practice for slightly lower rotation overhead.

## How It's Best Learned
First master BST insertions, then study rotations in isolation. Implement AVL insertion with balance-factor tracking. The four rotation cases (LL, RR, LR, RL) are best understood through diagrams before translating to code.

## Common Misconceptions
- Rotations preserve the BST ordering property; they only restructure the tree shape without violating the BST invariant.
- AVL trees require rebalancing on deletion as well as insertion, which is often overlooked in initial implementations.

## Explainer

From your work with binary search trees, you know the fundamental problem: a BST's performance depends entirely on its shape. Insert elements in sorted order and you get a linked list with O(n) operations; insert them in a balanced way and you get O(log n). The trouble is that you rarely control the insertion order. An **AVL tree** solves this by automatically restructuring itself after every modification to guarantee that the tree stays approximately balanced — specifically, that no node's left and right subtrees differ in height by more than one.

Each node in an AVL tree tracks its **balance factor**: the height of its left subtree minus the height of its right subtree. A balance factor of 0 means the subtrees are the same height; +1 means the left is one taller; −1 means the right is one taller. All of these are acceptable. But after an insertion or deletion, some node might end up with a balance factor of +2 or −2 — that node's subtrees have become too uneven, and the tree must be corrected.

The correction mechanism is the **rotation**, which reshapes a local portion of the tree without violating the BST ordering invariant. There are four cases. If a node is left-heavy (+2) and its left child is also left-heavy or balanced (+1 or 0), a single **right rotation** fixes it: the left child moves up to take the unbalanced node's place, and the unbalanced node becomes the right child. The mirror case — right-heavy with right-heavy child — uses a single **left rotation**. The trickier cases arise when the imbalance zigzags: a left-heavy node with a right-heavy left child (or vice versa). These require a **double rotation** — first rotate the child to straighten the zigzag into a straight line, then rotate the unbalanced node. These four cases (LL, RR, LR, RL) cover every possible imbalance.

The height guarantee is what makes AVL trees powerful. Because every node's subtrees differ in height by at most one, the maximum height of an AVL tree with n nodes is approximately 1.44 log₂(n). Since every BST operation — search, insert, delete — takes time proportional to the tree's height, AVL trees guarantee **O(log n) worst-case** performance for all operations. The cost is that insertions and deletions require walking back up the tree to check balance factors and possibly perform rotations (at most O(log n) balance checks and at most two rotations per insertion, though deletions can cascade). In practice, red-black trees are often preferred because they require fewer rotations on average, but AVL trees produce more tightly balanced trees and are faster for lookup-heavy workloads.
