---
id: btree-indexes
title: B-Tree Indexes
domain: computer-science
course: databases
prerequisites:
- id: indexing-concepts
  type: hard
- id: binary-search-trees
  type: soft
- id: binary-search-algorithm
  type: soft
builds-toward:
- query-optimization
tags:
- B-tree
- B+ tree
- balanced tree
- range queries
- disk I/O
stage: formal-systems
status: draft
---

# B-Tree Indexes

## Core Idea
B-trees are the standard index structure in relational databases, generalizing binary search trees to have many children per node in order to minimize disk I/O — each node corresponds to a disk page and stores hundreds of keys. B+ trees (the variant used in practice) store all data records in leaf nodes, which are linked as a sorted doubly-linked list, supporting both point lookups in O(log n) and efficient range scans. Their high branching factor (often 100–1000) means even billion-row tables require only 4–5 levels, making lookups extremely fast.

## How It's Best Learned
Trace insertions into a B+ tree by hand, observing splits and the propagation of separator keys upward. Then relate node size to disk page size (typically 8KB) to understand why branching factor dominates performance.

## Common Misconceptions
- B-trees in databases are almost always B+ trees — all data lives in leaf nodes, not internal nodes.
- B-trees do not help with leading-wildcard queries (LIKE '%suffix') because key ordering is irrelevant when the prefix is unknown.
- A large branching factor keeps tree height at 3–5 levels for millions of rows, not the O(log₂ n) height of a binary tree.
