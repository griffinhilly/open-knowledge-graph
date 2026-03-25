---
id: btree-indexes
title: B-Tree Indexes
domain: computer-science
course: databases
prerequisites:
- id: index-types-btree-hash-bitmap
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

## Questions

```yaml
- question: "A database has a composite B+ tree index on (last_name, first_name). A query filters only on first_name. Will the index speed up this query?"
  type: multiple-choice
  options:
    - "Yes — the index covers both columns, so any query touching either column can use it"
    - "No — the B+ tree is sorted by last_name first; without a last_name filter, the index cannot narrow the search and a full index scan is needed"
    - "Yes — the leaf linked list allows the database to scan first_name values efficiently in sorted order"
    - "No — composite indexes never improve query performance; only single-column indexes do"
  answer: 1
  explanation: "A composite index sorts by the leftmost column first, exactly like a phone book sorted by last name. If you don't provide a last_name filter, you can't jump to the right part of the tree — you'd have to scan every leaf. This is the 'leftmost prefix rule': the index accelerates queries that filter on (last_name), (last_name, first_name), but not on (first_name) alone. Understanding this is essential for designing indexes that actually help rather than just consuming disk space."

- question: "Why does a B+ tree with branching factor 500 reach billion-row tables in only 4–5 levels, while a binary search tree would need roughly 30+ levels for the same data?"
  type: multiple-choice
  options:
    - "B+ trees use a different sorting algorithm than binary trees, making each comparison more powerful"
    - "Each B+ tree level eliminates 500 candidates (not 2), so 500⁴ ≈ 62.5 billion rows fit within 4 levels; a binary tree requires log₂(n) levels, which is ~30 for a billion rows"
    - "B+ trees cache their upper levels in memory, making higher levels invisible to the performance calculation"
    - "Binary trees require more disk space per node, forcing more levels"
  answer: 1
  explanation: "The branching factor is the key insight. At each level of a B+ tree, you eliminate 1/500th of remaining candidates rather than 1/2nd. Height grows as log₅₀₀(n) vs log₂(n). For n = 1 billion: log₂(1B) ≈ 30 levels; log₅₀₀(1B) ≈ 3.5 levels. Each level = one disk read, so this difference between 4 reads and 30 reads is enormous. The branching factor is why B-trees were designed: packing many keys per node matches the page-based I/O model of disks."

- question: "In a B+ tree as used by relational databases, data records are stored in both internal (non-leaf) nodes and leaf nodes."
  type: true-false
  answer: false
  explanation: "This is the defining characteristic of B+ trees (as opposed to plain B-trees). Internal nodes store only keys and child pointers — they function purely as a routing structure. All actual data records live exclusively in the leaf nodes. The leaves are then linked together as a sorted doubly-linked list, enabling efficient range scans. Keeping data only in leaves means internal nodes can hold more routing keys, maximizing branching factor."

- question: "A B+ tree index efficiently supports range queries (e.g., WHERE age BETWEEN 25 AND 40) because its leaf nodes are linked in sorted order."
  type: true-false
  answer: true
  explanation: "This is one of B+ trees' key advantages over hash indexes, which only support exact-match lookups. For a range query, the database traverses the tree to find the first matching leaf, then follows the leaf-level linked list forward until it passes the upper bound — no further tree traversal needed. This makes B+ trees the standard choice for any column that appears in range conditions, ORDER BY clauses, or inequality filters."

- question: "Why are B-trees used for database indexes instead of binary search trees? What property of storage systems drives this design choice?"
  type: short-answer
  answer: "Databases store data on disk, where the unit of access is a page (typically 4–16 KB). Each disk read is far slower than memory access. A binary tree node holds one key, wasting almost an entire page per read. B-trees pack hundreds of keys into each node (= each page), so one disk read eliminates hundreds of candidates rather than just one. This high branching factor reduces tree height to 3–5 levels for any practical table size, meaning at most 3–5 disk reads per lookup."
  explanation: "The design is driven by the I/O cost model: memory accesses are nanoseconds; disk reads are milliseconds — a million times slower. Any data structure that minimizes the number of disk accesses wins. B-trees are optimal for this model because they are designed around page size rather than individual keys. The insight is that the cost bottleneck is the number of disk reads, not CPU comparisons — so packing more work into each read is the right optimization."
```

## Explainer

From your study of binary search trees, you know that a balanced tree lets you find any key in O(log n) time by eliminating half the candidates at each level. But binary search trees are designed for in-memory operations where accessing any node is equally fast. Databases store data on disk, where each read fetches an entire **page** (typically 4–16 KB). A binary tree node holds one key and two pointers — wasting almost all of that page. A **B-tree** solves this by packing hundreds of keys into each node so that one disk read eliminates not half the candidates, but a much larger fraction. This is the fundamental insight: B-trees are search trees optimized for the page-based I/O model of storage systems.

In practice, databases use the **B+ tree** variant. The difference is architectural: in a B+ tree, internal nodes store only keys and child pointers (acting purely as a routing structure), while all actual data records live in the **leaf nodes**. The leaves are linked together in a sorted doubly-linked list. This separation is what makes range queries efficient — to find all customers with IDs between 1000 and 2000, you use the internal nodes to locate the leaf containing 1000, then walk the linked list forward until you pass 2000. No further tree traversal is needed. Point lookups work the same way as in any search tree: start at the root, compare the search key against the keys in each node, follow the appropriate child pointer, and repeat until you reach a leaf.

The **branching factor** — the number of children per internal node — is what gives B+ trees their remarkable scalability. If each node holds 500 keys, then a tree of height 3 can index 500³ = 125 million keys. A tree of height 4 handles over 60 billion. This means even for very large tables, a point lookup requires only 3–5 disk reads (one per tree level), and the root and upper levels are almost certainly cached in memory, reducing actual I/O to 1–2 reads. Compare this to a binary search tree, which would need log₂(125 million) ≈ 27 levels — 27 potential disk reads for the same lookup.

When you create an index with `CREATE INDEX` in SQL, the database almost always builds a B+ tree behind the scenes. The index maps the indexed column's values to the physical locations of corresponding rows. For a **composite index** on multiple columns (e.g., `(last_name, first_name)`), the B+ tree sorts by the first column, then by the second within ties — exactly like a phone book sorted by last name then first name. This means the index supports queries filtering on `last_name` alone or on both columns, but not on `first_name` alone (the leftmost prefix rule). Understanding this structure is essential for designing indexes that actually accelerate your queries rather than just consuming disk space and slowing down writes.
