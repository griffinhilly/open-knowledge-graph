---
id: tree-traversals
title: Tree Traversals
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: stacks-data-structure
  type: soft
- id: queues-data-structure
  type: soft
builds-toward:
- binary-search-trees
- depth-first-search
- breadth-first-search
tags:
- traversal
- inorder
- preorder
- postorder
- level-order
stage: formal-systems
status: draft
---

# Tree Traversals

## Core Idea
Tree traversal visits every node in a tree exactly once. Depth-first traversals include inorder (left → root → right), preorder (root → left → right), and postorder (left → right → root); each visits nodes in a different order suited to different applications. Breadth-first (level-order) traversal visits nodes level by level using a queue. Inorder traversal of a binary search tree yields elements in sorted order, making it especially useful for validation and enumeration.

## How It's Best Learned
Implement all four traversals both recursively and iteratively (using an explicit stack or queue). For each, predict the output order by hand before running the code, then verify.

## Common Misconceptions
- Recursive implementations are elegant but can cause stack overflow on very deep or degenerate trees; iterative versions using explicit stacks are safer for production use.
- Inorder traversal yields sorted output ONLY for binary search trees, not arbitrary binary trees.
