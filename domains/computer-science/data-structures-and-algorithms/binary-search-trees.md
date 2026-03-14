---
id: binary-search-trees
title: Binary Search Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: tree-traversals
  type: hard
- id: time-space-complexity
  type: soft
- id: binary-search-algorithm
  type: soft
builds-toward:
- avl-trees
tags:
- BST
- binary-search-tree
- ordered-tree
- search
stage: formal-systems
status: validated
---
# Binary Search Trees

## Core Idea
A binary search tree (BST) is a binary tree where, for every node, all values in the left subtree are less than the node's value and all values in the right subtree are greater. This property allows searching, insertion, and deletion in O(h) time where h is the height. For a balanced tree, h = O(log n), giving efficient O(log n) operations. However, inserting sorted data produces a degenerate (linear) tree with h = O(n), making it no better than a linked list.

## How It's Best Learned
Implement BST search, insert, and delete from scratch. Pay close attention to the three cases in deletion: leaf node, one child, two children. Test with sorted and random insertion orders to observe the impact on tree shape.

## Common Misconceptions
- BSTs are not inherently balanced; their performance depends entirely on the distribution of insertions.
- Deletion is the trickiest operation: the two-child case requires finding the in-order successor (or predecessor) to replace the deleted node.
