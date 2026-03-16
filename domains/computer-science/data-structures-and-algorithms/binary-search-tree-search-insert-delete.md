---
id: binary-search-tree-search-insert-delete
title: 'Binary Search Trees: Search, Insertion, Deletion'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-tree-properties-height-balance-completeness
  type: hard
- id: binary-search-trees
  type: soft
builds-toward:
- avl-tree-balance-rotations-maintenance
- b-tree-multi-level-indexing
tags:
- bst
- search
- insertion
stage: formal-systems
status: draft
---

# Binary Search Trees: Search, Insertion, Deletion

## Core Idea
A BST maintains the invariant: left subtree < node < right subtree, enabling O(h) search and insertion. Deletion is trickier—removing a node with two children requires finding the successor. Unbalanced trees degrade to O(n).

## How It's Best Learned
Implement insertion and deletion from scratch. Trace each operation: insert elements to create an unbalanced tree, then delete various nodes (leaf, one child, two children). Measure tree height to see performance degradation.

## Common Misconceptions
- A BST is always efficient—unbalanced trees can be O(n) per operation.
- Deletion is easier than insertion—actually, deletion with two children is the hardest case.
- The successor is always the right-most node in the right subtree (true, but must find it iteratively or recursively).

## Explainer

You already know that a binary tree organizes data hierarchically and that properties like height and balance affect performance. A **binary search tree (BST)** adds one crucial rule: for every node, all values in its left subtree are smaller and all values in its right subtree are larger. This single invariant turns the tree into a searchable structure — at each node, you know which half of the remaining data to explore, much like binary search on a sorted array.

**Searching** is the most natural operation. Start at the root and compare your target value to the current node. If it matches, you are done. If the target is smaller, go left; if larger, go right. Each comparison eliminates an entire subtree, so search takes O(h) time where h is the tree's height. In a balanced tree with n nodes, h ≈ log₂(n), giving you the same logarithmic efficiency as binary search on an array. **Insertion** follows the same path: search for where the new value *would* be, and when you reach a null pointer (a missing child), attach the new node there. The new node always becomes a leaf, and the BST property is automatically maintained because you placed it exactly where the search ordering dictates.

**Deletion** is where things get interesting, because removing a node from the middle of the tree must preserve the BST invariant. There are three cases of increasing difficulty. Deleting a **leaf** (no children) is trivial — just remove it. Deleting a node with **one child** is almost as easy — replace the node with its single child, and the ordering is preserved because the child's entire subtree was already on the correct side. The hard case is deleting a node with **two children**. You cannot simply remove it without orphaning two subtrees. The solution is to find the node's **in-order successor** — the smallest value in its right subtree (found by going right once, then left as far as possible). This successor has at most one child (it cannot have a left child, or it would not be the leftmost node). Copy the successor's value into the node being deleted, then delete the successor node, which falls into the easy one-child or leaf case.

The critical performance caveat is that all three operations — search, insert, delete — are O(h), not O(log n). If you insert already-sorted data into an empty BST, each new value goes to the rightmost position, producing a degenerate tree that is effectively a linked list with h = n. In this worst case, every operation takes O(n) time. This is why balanced BST variants like AVL trees and red-black trees exist: they perform rotations after modifications to keep h close to log₂(n), guaranteeing logarithmic performance regardless of insertion order.
