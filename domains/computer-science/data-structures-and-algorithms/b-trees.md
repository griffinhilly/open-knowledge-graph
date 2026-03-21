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

## Questions

```yaml
- question: "A database engineer doubles the branching factor of a B-tree from m=100 to m=200. What is the primary performance benefit for a dataset stored on disk?"
  type: multiple-choice
  options:
    - "Each node now stores more keys, so the tree height decreases and fewer disk reads are needed per search"
    - "Node splits become more frequent, keeping the tree more balanced"
    - "Insertions no longer require propagating splits upward to the root"
    - "The tree can now store twice as many keys in the same number of nodes"
  answer: 0
  explanation: "The height of a B-tree is O(log_m n). Doubling m roughly halves the height for large datasets: log_200(n) < log_100(n). Since each level corresponds to one disk read, fewer levels means fewer disk I/Os per search — and disk I/Os dominate the cost. This is why m is tuned to be as large as a disk block can hold: the branching factor directly determines how many disk reads a lookup requires."

- question: "Why does the B-tree minimum occupancy rule require internal nodes to have at least ⌈m/2⌉ children?"
  type: multiple-choice
  options:
    - "To prevent any single node from holding more keys than fit in a disk block"
    - "To guarantee the tree remains balanced so all leaves stay at the same depth"
    - "To ensure the tree never needs to perform node splits during insertion"
    - "To match the number of keys in each node to the number of disk sectors"
  answer: 1
  explanation: "Without a minimum occupancy rule, deletions could leave nodes nearly empty, degenerating the tree into something resembling a linked list with O(n) height. The minimum of ⌈m/2⌉ children ensures that even after many deletions, nodes stay at least half full, bounding the height at O(log_m n). Crucially, this rule also guarantees balance: since every leaf is at the same depth and internal nodes must have enough children, the tree cannot become lopsided."

- question: "In a B-tree, all leaves are always at the same depth because the tree grows upward by splitting the root when it overflows."
  type: true-false
  answer: true
  explanation: "True. Unlike binary search trees that grow at the bottom (insertions always go to a leaf), B-trees grow at the top. Insertions find the appropriate leaf and insert there; if the leaf overflows, it splits and the median key is promoted to the parent. This split propagation can reach the root, and when the root splits, a new root is created — increasing the tree height by one. Because height increases only at the root and all new leaves are created at the current leaf level, every leaf stays at the same depth. This 'perfect balance' is the invariant that gives B-trees their guaranteed O(log_m n) performance."

- question: "B-trees are only useful for database indexing and have no advantage in other contexts."
  type: true-false
  answer: false
  explanation: "False. B-trees are valuable for any external-memory algorithm — any situation where data lives on a slower storage medium than the processor's cache. This includes file system directory structures (many OS file systems use B-tree variants), external sorting, geographic information systems, and any large-scale key-value store. The core principle — minimize the number of slow storage accesses by maximizing branching factor — applies wherever there is a significant latency gap between two storage layers, whether disk vs. RAM, RAM vs. cache, or even across network boundaries."

- question: "Why is the branching factor m in a B-tree typically chosen to match the disk block size rather than, say, optimizing for CPU cache performance?"
  type: short-answer
  answer: "Each disk read fetches an entire block regardless of how much data you actually need from it. By making B-tree nodes exactly the size of a disk block, each read fills one node completely — all m−1 keys and m child pointers are loaded in a single I/O. Binary search within the node happens in memory (fast), and only one more disk read is needed per level. This maximizes the 'useful work' per disk I/O. If nodes were smaller than a disk block, each read would waste most of the fetched bytes; if larger, one node access would require multiple disk reads."
  explanation: "The design principle is to match the data structure's unit of access (one node traversal) to the hardware's unit of access (one disk block). When these are aligned, the tree minimizes the number of disk I/Os, which dominate performance by a factor of ~100,000 over RAM accesses. This is a general principle in systems design: identify the bottleneck (disk I/O here), then design the data structure to minimize operations at that bottleneck."
```

## Explainer

From binary trees, you know that search performance depends on tree height — every level you descend costs one comparison. A binary search tree with n keys has height O(log₂ n), which is fine when every comparison is cheap. But when your data lives on disk rather than in memory, each node access means a disk read, and disk reads are roughly 100,000 times slower than memory accesses. A binary tree with a million keys has height ~20, meaning 20 disk reads per search. A **B-tree** solves this by making nodes wide instead of tall: each node stores dozens or hundreds of keys with correspondingly many children, dramatically reducing height.

A B-tree of **order m** (also called degree or branching factor m) allows each internal node to have up to m children and store up to m−1 keys. Keys within a node are sorted, and the children between them point to subtrees containing keys in the corresponding range — just like a binary search tree, but with multiple partitions per node instead of two. The minimum occupancy rule ensures nodes stay at least half full: internal nodes must have at least ⌈m/2⌉ children. This guarantee keeps the tree balanced and prevents degenerate chains. The height of a B-tree with n keys is O(log_m n), so with m = 1000, a tree holding a billion keys is only 3 levels deep — 3 disk reads versus 30 for a binary tree.

**Insertion** works by searching for the correct leaf, inserting the key, and splitting if the leaf overflows. When a node exceeds m−1 keys, it splits into two nodes, and the **median key** is promoted to the parent. If the parent also overflows, the split propagates upward — in the worst case, all the way to the root, which splits to create a new root and increases the tree height by one. This bottom-up splitting is why B-trees grow at the top, not the bottom, and why they stay perfectly balanced: every leaf is always at the same depth. Deletion is the mirror image, merging or redistributing keys when nodes become too empty.

The reason B-trees dominate in databases and file systems comes down to matching the data structure to the hardware. A disk read fetches an entire block (typically 4–16 KB) regardless of how much data you need from it. By sizing B-tree nodes to match the disk block size, each read brings in hundreds of keys at once — you binary-search within the node in memory (fast), then follow one pointer to the next level (one more disk read). This is why the branching factor m is chosen to be as large as a disk block can hold. The result is that B-tree operations cost O(log_m n) disk I/Os, and since m is large, the practical number of reads for even massive datasets is tiny. Every relational database index you have ever used is built on a variant of this idea.
