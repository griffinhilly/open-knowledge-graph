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
status: validated
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

## Explainer

From your study of binary search trees, you know that a balanced tree lets you find any key in O(log n) time by eliminating half the candidates at each level. But binary search trees are designed for in-memory operations where accessing any node is equally fast. Databases store data on disk, where each read fetches an entire **page** (typically 4–16 KB). A binary tree node holds one key and two pointers — wasting almost all of that page. A **B-tree** solves this by packing hundreds of keys into each node so that one disk read eliminates not half the candidates, but a much larger fraction. This is the fundamental insight: B-trees are search trees optimized for the page-based I/O model of storage systems.

In practice, databases use the **B+ tree** variant. The difference is architectural: in a B+ tree, internal nodes store only keys and child pointers (acting purely as a routing structure), while all actual data records live in the **leaf nodes**. The leaves are linked together in a sorted doubly-linked list. This separation is what makes range queries efficient — to find all customers with IDs between 1000 and 2000, you use the internal nodes to locate the leaf containing 1000, then walk the linked list forward until you pass 2000. No further tree traversal is needed. Point lookups work the same way as in any search tree: start at the root, compare the search key against the keys in each node, follow the appropriate child pointer, and repeat until you reach a leaf.

The **branching factor** — the number of children per internal node — is what gives B+ trees their remarkable scalability. If each node holds 500 keys, then a tree of height 3 can index 500³ = 125 million keys. A tree of height 4 handles over 60 billion. This means even for very large tables, a point lookup requires only 3–5 disk reads (one per tree level), and the root and upper levels are almost certainly cached in memory, reducing actual I/O to 1–2 reads. Compare this to a binary search tree, which would need log₂(125 million) ≈ 27 levels — 27 potential disk reads for the same lookup.

When you create an index with `CREATE INDEX` in SQL, the database almost always builds a B+ tree behind the scenes. The index maps the indexed column's values to the physical locations of corresponding rows. For a **composite index** on multiple columns (e.g., `(last_name, first_name)`), the B+ tree sorts by the first column, then by the second within ties — exactly like a phone book sorted by last name then first name. This means the index supports queries filtering on `last_name` alone or on both columns, but not on `first_name` alone (the leftmost prefix rule). Understanding this structure is essential for designing indexes that actually accelerate your queries rather than just consuming disk space and slowing down writes.
