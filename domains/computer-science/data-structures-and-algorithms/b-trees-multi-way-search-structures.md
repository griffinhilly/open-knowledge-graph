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

## Questions

```yaml
- question: "A database designer is choosing the order m for a B-tree index on a table with 10 million rows. Which criterion should guide the choice of m?"
  type: multiple-choice
  options:
    - "m should be chosen to minimize the number of key comparisons per search"
    - "m should be chosen to match the size of a disk block so each node fits in one I/O read"
    - "m should equal log₂(n) to keep the tree balanced"
    - "m should be as large as possible to minimize tree height regardless of disk structure"
  answer: 1
  explanation: "The whole point of B-trees is to minimize disk I/O, not key comparisons. If a disk block is 4KB and each key-pointer pair takes 40 bytes, fitting ~100 entries per node means one disk read fetches one full node. Option A confuses the metric: more keys per node means *more* comparisons per node, but far fewer disk reads overall. Option D is wrong because m is constrained by disk block size — a node larger than one block forces multiple reads."

- question: "For an in-memory data structure where all data fits in RAM, a B-tree of order 100 versus a balanced BST — which typically performs better for lookups?"
  type: multiple-choice
  options:
    - "The B-tree, because log₁₀₀(n) < log₂(n) means fewer pointer traversals"
    - "The BST, because cache lines are small and a BST node's single pointer chase fits efficiently in L1/L2 cache"
    - "They are identical because both are O(log n)"
    - "The B-tree, because it requires fewer key comparisons per lookup"
  answer: 1
  explanation: "B-trees are optimized for disk-block-sized nodes. In RAM, CPU cache lines are small (typically 64 bytes), so a B-tree node with 100 keys spans many cache lines and actually causes more cache misses than a BST. O(log n) hides the constant: a BST has fewer operations per level even if it has more levels. B-trees beat BSTs on disk; BSTs (and cache-optimized variants) often beat B-trees in memory. Option C is wrong because big-O hides constants that dominate in practice."

- question: "A B-tree of order 100 containing one million keys has height at most 3."
  type: true-false
  answer: true
  explanation: "log₁₀₀(1,000,000) = log₁₀₀(10⁶) = 6/2 = 3. Each level can branch into 100 children, so three levels of branching can accommodate 100³ = 1,000,000 leaf nodes. This is the critical insight: by matching node size to disk block size and allowing many children, B-trees reduce millions-of-record indexes to just 3–4 disk reads — versus 20 for a binary tree of the same size."

- question: "The primary advantage of B-trees over BSTs is that B-trees require fewer key comparisons during search."
  type: true-false
  answer: false
  explanation: "B-trees actually require *more* key comparisons per node visited (scanning through up to m-1 keys per node), but far fewer disk reads overall because each node holds many keys. The advantage is I/O efficiency, not comparison efficiency. A BST with 1M nodes requires ~20 pointer traversals; a B-tree of order 100 requires ~3 — but each B-tree traversal reads a full disk block. The benefit is measured in disk accesses, not comparisons."

- question: "Why is the order m of a B-tree chosen to match the disk block size rather than being derived from some mathematically optimal formula?"
  type: short-answer
  answer: "Because each node access in a B-tree corresponds to one disk I/O operation, and disk reads fetch data in fixed-size blocks (e.g., 4KB). By sizing a node to fill exactly one disk block, you guarantee that each I/O read retrieves a complete node — no disk read is wasted, and no node requires two reads. If m were smaller, each disk read would bring in a node with wasted space; if m were larger, one node access would require multiple reads. The optimization target is minimizing disk reads, not minimizing comparisons, so the disk architecture determines m."
  explanation: "This reveals why B-tree design is hardware-aware, not purely algorithmic. The formula log_m(n) gives the tree height, but m must be set by the storage medium's block size to make each level of the tree correspond to exactly one I/O. A B-tree is fundamentally a data structure designed around the gap between CPU speed and disk speed — every design decision flows from that constraint."
```

## Explainer

From your knowledge of balanced binary search trees, you know that keeping a tree balanced guarantees O(log n) search, insertion, and deletion. But in a BST, each node holds one key and has two children, so a tree with a million keys is about 20 levels deep (log₂ 1,000,000 ≈ 20). Each level requires following a pointer to a new node — and when that node lives on disk rather than in memory, each pointer-chase becomes a disk read that takes milliseconds instead of nanoseconds. Twenty disk reads per lookup is painfully slow. **B-trees** solve this by making each node hold many keys and many children, dramatically reducing the tree's height.

A B-tree of **order m** allows each node to hold up to m-1 keys and m children. The search property generalizes from BSTs: keys within a node are sorted, and each child pointer leads to a subtree whose keys fall between the surrounding parent keys. The critical insight is choosing m to match the disk block size. If a disk reads 4KB at a time and each key-pointer pair takes 40 bytes, you can fit about 100 entries per node — so m ≈ 100. A B-tree of order 100 containing one million keys has height at most log₁₀₀(1,000,000) ≈ 3. Three disk reads to find any key among a million — compared to twenty for a binary tree. This is why every major database (PostgreSQL, MySQL, SQLite) and file system (NTFS, ext4, HFS+) uses B-trees or their variant, B+ trees.

**Insertion** works by searching for the correct leaf and adding the new key. If the leaf is full (already has m-1 keys), it **splits** into two nodes, and the middle key is promoted to the parent. If the parent is also full, it splits too, potentially cascading up to the root. When the root splits, a new root is created, increasing the tree's height by one — this is the only way a B-tree grows taller, and it happens rarely. **Deletion** is the reverse: removing a key may cause a node to become too empty (below the minimum of ⌈m/2⌉ - 1 keys), triggering a **merge** with a sibling or a **redistribution** of keys from an adjacent sibling through the parent.

The variant most commonly used in practice is the **B+ tree**, where all actual data records (or pointers to records) are stored only in the leaves, and internal nodes contain only keys for navigation. The leaves are linked together in a doubly-linked list, which makes range queries (e.g., "find all records where price is between 10 and 50") extremely efficient — you find the starting leaf via the tree, then simply walk the linked list. This is why database indexes support both point queries and range scans efficiently. The combination of minimal tree height, disk-block-aligned nodes, and linked leaves makes B+ trees the single most important data structure in storage systems.
