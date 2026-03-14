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
