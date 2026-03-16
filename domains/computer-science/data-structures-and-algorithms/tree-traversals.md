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
status: validated
---

# Tree Traversals

## Core Idea
Tree traversal visits every node in a tree exactly once. Depth-first traversals include inorder (left → root → right), preorder (root → left → right), and postorder (left → right → root); each visits nodes in a different order suited to different applications. Breadth-first (level-order) traversal visits nodes level by level using a queue. Inorder traversal of a binary search tree yields elements in sorted order, making it especially useful for validation and enumeration.

## How It's Best Learned
Implement all four traversals both recursively and iteratively (using an explicit stack or queue). For each, predict the output order by hand before running the code, then verify.

## Common Misconceptions
- Recursive implementations are elegant but can cause stack overflow on very deep or degenerate trees; iterative versions using explicit stacks are safer for production use.
- Inorder traversal yields sorted output ONLY for binary search trees, not arbitrary binary trees.

## Explainer

You already understand binary trees — each node has at most two children, called left and right. A **tree traversal** is a systematic way to visit every node exactly once, and the order in which you visit them determines what the traversal is useful for. There are four standard traversals, three depth-first and one breadth-first, and each answers a different question about the tree's contents.

The three **depth-first** traversals differ only in when they process the current node relative to its children. **Preorder** (root, left, right) visits the current node first, then recurses into the left subtree, then the right. This naturally produces a top-down view — you see parents before children, making preorder ideal for copying a tree or producing a prefix representation of an expression. **Inorder** (left, root, right) recurses into the left subtree first, then visits the current node, then the right subtree. For a binary search tree, this visits nodes in ascending sorted order — the left subtree contains smaller values, the root is next, and the right subtree contains larger values. **Postorder** (left, right, root) recurses into both subtrees before visiting the current node, giving a bottom-up view — you process children before parents, making it natural for computing aggregate properties (like subtree size or height) and for safely deleting a tree.

**Breadth-first** (level-order) traversal visits all nodes at depth 0, then depth 1, then depth 2, and so on. Instead of recursion, it uses a queue: enqueue the root, then repeatedly dequeue a node, process it, and enqueue its children. This produces a left-to-right, top-to-bottom sweep of the tree and is useful when you need to process nodes by level — for example, finding the shallowest node satisfying some condition, or printing a tree level by level.

The recursive implementations are concise — each depth-first traversal is about three lines of code. But recursion uses the call stack, and a deeply unbalanced tree (essentially a linked list) can cause stack overflow. The **iterative** versions use an explicit stack (for depth-first) or queue (for breadth-first), giving you direct control over memory. For iterative inorder, you push nodes as you go left, pop when there's nothing left to push, process the popped node, then move right. Mastering both recursive and iterative forms is important because the iterative versions reveal what the recursion is actually doing — managing a frontier of nodes yet to be visited — which is the same pattern you will encounter in graph traversal algorithms like depth-first search and breadth-first search.
