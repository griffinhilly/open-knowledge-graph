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
