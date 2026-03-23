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
status: validated
---

# Binary Tree Structure and Node Representation

## Core Idea
A binary tree node contains a value and left/right child pointers. Trees can be represented as arrays (heap-like, for complete trees) or pointer structures. Understanding representation choices affects cache locality and memory usage.

## Questions

```yaml
- question: "A binary heap stores 7 nodes. The root is at index 0. What are the array indices of the root's two children?"
  type: multiple-choice
  options:
    - "Indices 1 and 2"
    - "Indices 2 and 3"
    - "Indices 0 and 1"
    - "It depends on the tree's height"
  answer: 0
  explanation: "In 0-based array representation, a node at index i has its left child at 2i+1 and right child at 2i+2. For the root (i=0): left child = 2(0)+1 = 1, right child = 2(0)+2 = 2. This formula encodes the tree structure purely through arithmetic — no pointers needed. This is why binary heaps use array representation: the formula is constant-time and the memory layout is contiguous."

- question: "You are building a binary search tree that handles frequent insertions and deletions of records in a database index. Which representation should you choose, and why?"
  type: multiple-choice
  options:
    - "Array-based, because it has better cache locality for all tree operations"
    - "Pointer-based, because the tree shape is unpredictable and restructuring only requires reassigning a few pointers"
    - "Array-based, because BSTs are always complete trees and the formula 2i+1, 2i+2 applies"
    - "Pointer-based, because it always uses less memory than an array"
  answer: 1
  explanation: "Array representation requires a complete tree to work efficiently — if the tree becomes sparse or deeply unbalanced (which BSTs can after many insertions and deletions), the array wastes exponential space. Pointer-based representation handles any shape: restructuring means reassigning a constant number of pointers regardless of tree size. BSTs are not guaranteed to be complete, making array representation inappropriate. Cache locality is a real advantage of arrays, but only when the tree shape justifies it."

- question: "In array-based binary tree representation, the parent of a node at index 5 (0-based) is at index 2."
  type: true-false
  answer: true
  explanation: "The parent formula (0-based) is ⌊(i-1)/2⌋. For i=5: ⌊(5-1)/2⌋ = ⌊4/2⌋ = ⌊2⌋ = 2. So yes, the parent of node at index 5 is at index 2. You can verify: node 2's children are at 2(2)+1=5 and 2(2)+2=6. This bidirectional formula is what makes array-based trees work without any pointers."

- question: "Pointer-based binary trees use more memory per node than array-based trees but always provide better performance for tree traversal due to flexibility."
  type: true-false
  answer: false
  explanation: "The first half is true — pointer-based nodes store left/right pointers in addition to the value, using more memory. But 'always better performance for traversal' is false. Array-based trees have *better* cache locality for complete trees: parent, left child, and right child are stored at adjacent indices, so the CPU cache loads them together. Pointer-based nodes can be scattered across memory, causing cache misses during traversal. The right choice depends on tree shape and access patterns."

- question: "Why does array-based tree representation become impractical for a sparse or highly unbalanced tree, even if the number of actual nodes is small?"
  type: short-answer
  answer: "The array must be large enough to hold every possible position at every depth level. A degenerate tree (a chain of n nodes) has depth n, requiring an array of size 2^n to accommodate the formula-encoded positions — even though only n slots are occupied. Almost all entries are empty, wasting exponential space."
  explanation: "Array representation encodes position implicitly: a node at depth d can be at any of 2^d positions, and all must be addressable. Complete trees use nearly all positions, so no space is wasted. But a right-skewed BST of 30 nodes would need an array of size ~2^30 (about 1 billion entries) to correctly index the deepest node. This makes array representation viable only when the tree is guaranteed to be complete or nearly complete."
```

## Explainer

A **binary tree** is built from nodes, and each node has a simple structure: it holds a value (or key) and has at most two children, conventionally called **left** and **right**. If you have worked with binary trees conceptually, this topic is about the concrete details of how those nodes are actually stored in memory — decisions that affect how fast your tree operations run in practice, not just in theory.

The most common representation is a **pointer-based (linked) structure**. Each node is an object or struct containing three fields: the stored value, a pointer (or reference) to the left child, and a pointer to the right child. If a child does not exist, its pointer is null. Building a tree means creating node objects and linking them together. This representation is flexible — inserting or deleting nodes requires only reassigning a few pointers, regardless of the tree's size. The downside is that nodes can be scattered across memory, so traversing the tree may cause many cache misses as the processor jumps between distant memory locations. For trees that change shape frequently (insertion-heavy workloads, for example), this tradeoff is usually worth it.

The alternative is an **array-based representation**, which works elegantly for **complete binary trees** (trees where every level is fully filled except possibly the last, which is filled left to right). The mapping is simple: the root goes at index 0 (or 1, depending on convention). For a node at index i, its left child is at index 2i + 1 and its right child is at 2i + 2 (using 0-based indexing). The parent of any node at index i is at index ⌊(i-1)/2⌋. No pointers are needed — the tree structure is encoded implicitly by array positions. This is why binary heaps use arrays: heaps are always complete, and the array layout gives excellent cache locality because parent and children are stored near each other in memory. However, if the tree is sparse or unbalanced, the array wastes significant space — a tree with n nodes but depth n (a degenerate chain) would need an array of size 2ⁿ, with almost every slot empty.

Choosing between these representations is a practical engineering decision. Use pointer-based trees when the tree shape is unpredictable, when nodes are inserted and deleted frequently, or when the tree may be highly unbalanced (as in a binary search tree). Use array-based trees when the tree is guaranteed to be complete or nearly complete, when you want maximum cache performance, or when you need fast index-based access to parent and children (as in heaps and certain segment trees). Understanding both representations lets you match the data structure to the workload rather than defaulting to one approach for all situations.
