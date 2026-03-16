---
id: binary-tree-structure-node-representation
title: Binary Tree Structure and Node Representation
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: soft
builds-toward:
- binary-tree-properties-height-balance-completeness
tags:
- binary-tree
- structure
- representation
stage: formal-systems
status: draft
---

# Binary Tree Structure and Node Representation

## Core Idea
A binary tree node contains a value and left/right child pointers. Trees can be represented as arrays (heap-like, for complete trees) or pointer structures. Understanding representation choices affects cache locality and memory usage.

## Explainer

A **binary tree** is built from nodes, and each node has a simple structure: it holds a value (or key) and has at most two children, conventionally called **left** and **right**. If you have worked with binary trees conceptually, this topic is about the concrete details of how those nodes are actually stored in memory — decisions that affect how fast your tree operations run in practice, not just in theory.

The most common representation is a **pointer-based (linked) structure**. Each node is an object or struct containing three fields: the stored value, a pointer (or reference) to the left child, and a pointer to the right child. If a child does not exist, its pointer is null. Building a tree means creating node objects and linking them together. This representation is flexible — inserting or deleting nodes requires only reassigning a few pointers, regardless of the tree's size. The downside is that nodes can be scattered across memory, so traversing the tree may cause many cache misses as the processor jumps between distant memory locations. For trees that change shape frequently (insertion-heavy workloads, for example), this tradeoff is usually worth it.

The alternative is an **array-based representation**, which works elegantly for **complete binary trees** (trees where every level is fully filled except possibly the last, which is filled left to right). The mapping is simple: the root goes at index 0 (or 1, depending on convention). For a node at index i, its left child is at index 2i + 1 and its right child is at 2i + 2 (using 0-based indexing). The parent of any node at index i is at index ⌊(i-1)/2⌋. No pointers are needed — the tree structure is encoded implicitly by array positions. This is why binary heaps use arrays: heaps are always complete, and the array layout gives excellent cache locality because parent and children are stored near each other in memory. However, if the tree is sparse or unbalanced, the array wastes significant space — a tree with n nodes but depth n (a degenerate chain) would need an array of size 2ⁿ, with almost every slot empty.

Choosing between these representations is a practical engineering decision. Use pointer-based trees when the tree shape is unpredictable, when nodes are inserted and deleted frequently, or when the tree may be highly unbalanced (as in a binary search tree). Use array-based trees when the tree is guaranteed to be complete or nearly complete, when you want maximum cache performance, or when you need fast index-based access to parent and children (as in heaps and certain segment trees). Understanding both representations lets you match the data structure to the workload rather than defaulting to one approach for all situations.
