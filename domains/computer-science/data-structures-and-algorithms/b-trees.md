---
id: b-trees
title: B-Trees and Multi-Way Search Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: tree-node-structure-properties
  type: hard
- id: binary-trees
  type: soft
builds-toward:
- btree-indexes
tags:
- b-trees
- multi-way
- external-storage
- database-indexes
- disk-based
stage: formal-systems
status: draft
---

# B-Trees and Multi-Way Search Trees

## Core Idea
A B-tree of degree m is a multi-way search tree where internal nodes have 2 to m children and store multiple keys, minimizing height. Each disk read retrieves an entire node, making B-trees ideal for external storage (databases, file systems). Height is O(log_m n), which is dramatically smaller than binary trees for large m.

## How It's Best Learned
Trace insertions and splits on a B-tree of order 3 by hand. Understand why the branching factor reduces height (crucial for disk-based systems). Implement insertion with node splitting and the median key 'bubbling up' to parent nodes.

## Common Misconceptions
- B-trees are only for databases (the principles apply to any external-memory algorithm). - Every node must have exactly m children (nodes can have fewer; the range is flexible).

## Explainer

From binary trees, you know that search performance depends on tree height — every level you descend costs one comparison. A binary search tree with n keys has height O(log₂ n), which is fine when every comparison is cheap. But when your data lives on disk rather than in memory, each node access means a disk read, and disk reads are roughly 100,000 times slower than memory accesses. A binary tree with a million keys has height ~20, meaning 20 disk reads per search. A **B-tree** solves this by making nodes wide instead of tall: each node stores dozens or hundreds of keys with correspondingly many children, dramatically reducing height.

A B-tree of **order m** (also called degree or branching factor m) allows each internal node to have up to m children and store up to m−1 keys. Keys within a node are sorted, and the children between them point to subtrees containing keys in the corresponding range — just like a binary search tree, but with multiple partitions per node instead of two. The minimum occupancy rule ensures nodes stay at least half full: internal nodes must have at least ⌈m/2⌉ children. This guarantee keeps the tree balanced and prevents degenerate chains. The height of a B-tree with n keys is O(log_m n), so with m = 1000, a tree holding a billion keys is only 3 levels deep — 3 disk reads versus 30 for a binary tree.

**Insertion** works by searching for the correct leaf, inserting the key, and splitting if the leaf overflows. When a node exceeds m−1 keys, it splits into two nodes, and the **median key** is promoted to the parent. If the parent also overflows, the split propagates upward — in the worst case, all the way to the root, which splits to create a new root and increases the tree height by one. This bottom-up splitting is why B-trees grow at the top, not the bottom, and why they stay perfectly balanced: every leaf is always at the same depth. Deletion is the mirror image, merging or redistributing keys when nodes become too empty.

The reason B-trees dominate in databases and file systems comes down to matching the data structure to the hardware. A disk read fetches an entire block (typically 4–16 KB) regardless of how much data you need from it. By sizing B-tree nodes to match the disk block size, each read brings in hundreds of keys at once — you binary-search within the node in memory (fast), then follow one pointer to the next level (one more disk read). This is why the branching factor m is chosen to be as large as a disk block can hold. The result is that B-tree operations cost O(log_m n) disk I/Os, and since m is large, the practical number of reads for even massive datasets is tiny. Every relational database index you have ever used is built on a variant of this idea.
