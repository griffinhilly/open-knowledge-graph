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

## Explainer

From your knowledge of balanced binary search trees, you know that keeping a tree balanced guarantees O(log n) search, insertion, and deletion. But in a BST, each node holds one key and has two children, so a tree with a million keys is about 20 levels deep (log₂ 1,000,000 ≈ 20). Each level requires following a pointer to a new node — and when that node lives on disk rather than in memory, each pointer-chase becomes a disk read that takes milliseconds instead of nanoseconds. Twenty disk reads per lookup is painfully slow. **B-trees** solve this by making each node hold many keys and many children, dramatically reducing the tree's height.

A B-tree of **order m** allows each node to hold up to m-1 keys and m children. The search property generalizes from BSTs: keys within a node are sorted, and each child pointer leads to a subtree whose keys fall between the surrounding parent keys. The critical insight is choosing m to match the disk block size. If a disk reads 4KB at a time and each key-pointer pair takes 40 bytes, you can fit about 100 entries per node — so m ≈ 100. A B-tree of order 100 containing one million keys has height at most log₁₀₀(1,000,000) ≈ 3. Three disk reads to find any key among a million — compared to twenty for a binary tree. This is why every major database (PostgreSQL, MySQL, SQLite) and file system (NTFS, ext4, HFS+) uses B-trees or their variant, B+ trees.

**Insertion** works by searching for the correct leaf and adding the new key. If the leaf is full (already has m-1 keys), it **splits** into two nodes, and the middle key is promoted to the parent. If the parent is also full, it splits too, potentially cascading up to the root. When the root splits, a new root is created, increasing the tree's height by one — this is the only way a B-tree grows taller, and it happens rarely. **Deletion** is the reverse: removing a key may cause a node to become too empty (below the minimum of ⌈m/2⌉ - 1 keys), triggering a **merge** with a sibling or a **redistribution** of keys from an adjacent sibling through the parent.

The variant most commonly used in practice is the **B+ tree**, where all actual data records (or pointers to records) are stored only in the leaves, and internal nodes contain only keys for navigation. The leaves are linked together in a doubly-linked list, which makes range queries (e.g., "find all records where price is between 10 and 50") extremely efficient — you find the starting leaf via the tree, then simply walk the linked list. This is why database indexes support both point queries and range scans efficiently. The combination of minimal tree height, disk-block-aligned nodes, and linked leaves makes B+ trees the single most important data structure in storage systems.
