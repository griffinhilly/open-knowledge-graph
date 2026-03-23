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
status: validated
---

# B-Trees: Multi-Level Indexing and Database Applications

## Core Idea
B-trees generalize BSTs to allow multiple keys per node (order t). Searches, insertions, and deletions are O(log n) and optimized for disk I/O—fewer seeks per operation. They're the standard for database indexes and file systems.

## Questions

```yaml
- question: "A balanced BST with 1 million keys has a height of roughly 20. A B-tree of order t=1000 with the same 1 million keys has a height of roughly 3. Why does the B-tree dramatically outperform the BST for on-disk lookups?"
  type: multiple-choice
  options:
    - "The B-tree uses binary search within each node, while BSTs use linear scan"
    - "Each BST traversal step costs one disk seek; the B-tree's high fanout means far fewer seek operations are needed"
    - "B-trees store duplicate keys, reducing the number of comparisons needed"
    - "BSTs are unbalanced, while B-trees are always perfectly balanced at the leaf level"
  answer: 1
  explanation: "The key insight is that every pointer traversal in a BST stored on disk costs one disk seek — an operation millions of times slower than an in-memory comparison. A height-20 BST requires 20 disk seeks per lookup. A B-tree with t=1000 stores up to 1999 keys per node (sized to fit one disk block), so its fanout is enormous and its height is tiny — 3 seeks instead of 20. Option D contains a partial truth (B-trees are height-balanced with all leaves at the same depth), but that alone doesn't explain the dramatic performance difference; the fanout is the key."

- question: "During B-tree insertion, a leaf node already contains 2t-1 keys (it is full). What must happen before the new key can be inserted?"
  type: multiple-choice
  options:
    - "The entire tree is rebuilt to redistribute keys evenly"
    - "The full node splits into two nodes of t-1 keys each, and the median key is pushed up to the parent"
    - "The new key is stored in an overflow page linked to the leaf"
    - "The insertion is rejected until a deletion creates room"
  answer: 1
  explanation: "When a full node must receive a new key, it splits: the 2t-1 keys are divided into two halves of t-1 keys each, and the middle key is promoted to the parent node. This splitting can cascade upward — if the parent is also full, it splits too. The only way the tree grows taller is when the root splits and a new root is created, which guarantees all leaves remain at the same depth."

- question: "In a B-tree, all leaf nodes are always at the same depth."
  type: true-false
  answer: true
  explanation: "This is a defining structural property of B-trees. The tree grows in height only when the root splits, which affects every path equally. Insertions cause local splits that preserve equal depth across all leaves. This is in contrast to unbalanced BSTs, where depth can vary dramatically across leaves. Equal depth means every search takes exactly the same number of disk seeks — no worst-case outliers."

- question: "Searching a B-tree with a billion keys requires examining every node in the tree."
  type: true-false
  answer: false
  explanation: "Search in a B-tree follows a single path from root to leaf — it never backtracks or examines sibling subtrees. At each node, you identify which child interval contains the target key and follow that one pointer. With t=1000, a billion-key B-tree has height ~3, meaning only 3 or 4 nodes are examined per search, regardless of how many total nodes exist. This logarithmic behavior (in terms of disk accesses) is the entire point of the structure."

- question: "Why does increasing a B-tree's order t (more keys per node) reduce the number of disk I/Os needed to find a key, and what practical factor limits how large t can be made?"
  type: short-answer
  answer: "Higher t means higher fanout — each node has more children — which reduces the tree's height. A shallower tree means fewer nodes to visit, and each node visit is one disk I/O. In practice, t is set so that a single node fits exactly in one disk block (typically 4KB–16KB). Making nodes larger than one disk block would force the OS to issue multiple I/O operations just to read a single node, eliminating the benefit. The optimal t matches node size to the disk block size."
  explanation: "The height of a B-tree is approximately log_t(n), so doubling t roughly halves the tree height. But the constraint is physical: each node must be read from disk in one operation. A disk block is fixed in size, so once your node fills a block, making it larger doesn't reduce I/Os per node read — it increases them. Database designers size t so node size ≈ disk block size (e.g., PostgreSQL uses 8KB pages), getting maximum fanout within the one-I/O-per-node constraint."
```

## Explainer

From binary search trees, you know how to organize data for efficient search: maintain a sorted structure where each comparison eliminates half the remaining candidates. BSTs achieve O(log n) search when balanced, but they are designed around a model where every operation — every pointer traversal, every comparison — costs roughly the same. On disk, this model breaks down completely. Reading from a hard drive or SSD involves a **seek** operation that is orders of magnitude slower than an in-memory comparison — perhaps 10 milliseconds for a disk seek versus 10 nanoseconds for a memory access, a factor of a million. A BST with a million keys has a height of about 20 when balanced, meaning 20 disk seeks per search. B-trees solve this by making each node hold many keys, dramatically reducing the tree's height and thus the number of disk seeks.

A **B-tree of order t** (sometimes called minimum degree t) stores between t-1 and 2t-1 keys in each node, with corresponding child pointers between them. A node with k keys has k+1 children, and the keys act as separators: all keys in the first child are less than the first key, all keys in the second child are between the first and second key, and so on. This is the same BST ordering principle, just extended to multiple keys per node. With t = 1000 (a common choice sized to match a disk block), each node holds up to 1999 keys and 2000 children. A tree with a billion keys would have a height of only 3 or 4 — meaning any key can be found with just 3 or 4 disk reads.

The operations — search, insert, and delete — maintain the B-tree's balanced structure through **splitting** and **merging** nodes. Search works like a multi-way binary search: at each node, you scan (or binary search) the keys to find the correct child, then follow that pointer. Insertion finds the correct leaf and adds the key; if the leaf is full (2t-1 keys), it **splits** into two nodes of t-1 keys each, pushing the median key up to the parent. This splitting can cascade upward, and if the root splits, a new root is created — this is the only way the tree grows taller, guaranteeing that all leaves remain at the same depth. Deletion is the inverse: if removing a key leaves a node with fewer than t-1 keys, it borrows from a sibling or merges with one.

The reason B-trees dominate **database indexing** and **file systems** comes down to this alignment with hardware. Each node is sized to fit in a single disk block (typically 4KB to 16KB), so reading a node requires exactly one disk I/O. The fanout (number of children per node) is enormous compared to a binary tree, which means the tree is very shallow. PostgreSQL, MySQL, SQLite, and virtually every major database engine use B-trees or their variant **B+ trees** (where all data lives in the leaves, and leaves are linked for efficient range scans) as their default index structure. When you create an index on a database column, you are almost certainly building a B-tree — and the performance you get from indexed queries versus full table scans is a direct consequence of the ideas you have just learned.
