---
id: b-tree-multi-level-indexing
title: 'B-Trees: Multi-Level Indexing and Database Applications'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-tree-search-insert-delete
  type: hard
builds-toward:
- database-schema-design
tags:
- b-tree
- indexing
- database
stage: formal-systems
status: draft
---

# B-Trees: Multi-Level Indexing and Database Applications

## Core Idea
B-trees generalize BSTs to allow multiple keys per node (order t). Searches, insertions, and deletions are O(log n) and optimized for disk I/O—fewer seeks per operation. They're the standard for database indexes and file systems.

## Explainer

From binary search trees, you know how to organize data for efficient search: maintain a sorted structure where each comparison eliminates half the remaining candidates. BSTs achieve O(log n) search when balanced, but they are designed around a model where every operation — every pointer traversal, every comparison — costs roughly the same. On disk, this model breaks down completely. Reading from a hard drive or SSD involves a **seek** operation that is orders of magnitude slower than an in-memory comparison — perhaps 10 milliseconds for a disk seek versus 10 nanoseconds for a memory access, a factor of a million. A BST with a million keys has a height of about 20 when balanced, meaning 20 disk seeks per search. B-trees solve this by making each node hold many keys, dramatically reducing the tree's height and thus the number of disk seeks.

A **B-tree of order t** (sometimes called minimum degree t) stores between t-1 and 2t-1 keys in each node, with corresponding child pointers between them. A node with k keys has k+1 children, and the keys act as separators: all keys in the first child are less than the first key, all keys in the second child are between the first and second key, and so on. This is the same BST ordering principle, just extended to multiple keys per node. With t = 1000 (a common choice sized to match a disk block), each node holds up to 1999 keys and 2000 children. A tree with a billion keys would have a height of only 3 or 4 — meaning any key can be found with just 3 or 4 disk reads.

The operations — search, insert, and delete — maintain the B-tree's balanced structure through **splitting** and **merging** nodes. Search works like a multi-way binary search: at each node, you scan (or binary search) the keys to find the correct child, then follow that pointer. Insertion finds the correct leaf and adds the key; if the leaf is full (2t-1 keys), it **splits** into two nodes of t-1 keys each, pushing the median key up to the parent. This splitting can cascade upward, and if the root splits, a new root is created — this is the only way the tree grows taller, guaranteeing that all leaves remain at the same depth. Deletion is the inverse: if removing a key leaves a node with fewer than t-1 keys, it borrows from a sibling or merges with one.

The reason B-trees dominate **database indexing** and **file systems** comes down to this alignment with hardware. Each node is sized to fit in a single disk block (typically 4KB to 16KB), so reading a node requires exactly one disk I/O. The fanout (number of children per node) is enormous compared to a binary tree, which means the tree is very shallow. PostgreSQL, MySQL, SQLite, and virtually every major database engine use B-trees or their variant **B+ trees** (where all data lives in the leaves, and leaves are linked for efficient range scans) as their default index structure. When you create an index on a database column, you are almost certainly building a B-tree — and the performance you get from indexed queries versus full table scans is a direct consequence of the ideas you have just learned.
