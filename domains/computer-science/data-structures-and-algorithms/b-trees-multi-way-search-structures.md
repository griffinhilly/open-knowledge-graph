---
id: b-trees-multi-way-search-structures
title: 'B-Trees: Multi-Way Search Trees for Disk Access'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-tree-balance-properties
  type: hard
tags:
- trees
- indexing
- disk
- database
stage: formal-systems
status: draft
---

# B-Trees: Multi-Way Search Trees for Disk Access

## Core Idea
B-trees generalize BSTs to have many children per node (order m). Each node holds m-1 keys and m children, keeping trees very shallow (log_m n). This is critical for databases and file systems where disk block access dominates cost, not key comparisons.

## How It's Best Learned
Understand why a B-tree of order 100 with one million keys has depth ≤ 3. Implement insertion with splitting when nodes are full, observing how shallow trees minimize disk I/O.

## Common Misconceptions
- Thinking B-trees are just 'wide' binary trees; the order m is chosen to match disk block size.
- Forgetting that each node access may require disk I/O, making shallow trees essential.
- Not recognizing that B-trees' main benefit is cache/disk efficiency, not algorithmic complexity.
