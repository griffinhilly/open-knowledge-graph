---
id: hash-indexes
title: Hash Indexes
domain: computer-science
course: databases
prerequisites:
- id: indexing-concepts
  type: hard
- id: hash-tables
  type: soft
builds-toward:
- query-optimization
tags:
- hash index
- equality lookup
- hash table
- index structure
- point query
stage: formal-systems
status: validated
---

# Hash Indexes

## Core Idea
Hash indexes use a hash function to map key values to bucket locations, enabling O(1) average-case equality lookups that are faster than B-tree traversals for point queries. However, because the hash function destroys key ordering, hash indexes cannot support range queries, prefix matching, or ordered scans. Dynamic hashing schemes (extendible hashing, linear hashing) allow the index to grow and shrink without a full rebuild as the dataset changes.

## How It's Best Learned
Implement a simple extendible hash index on a mock dataset and test equality lookups vs. range scans. Compare execution plans between a B-tree-indexed column and a hash-indexed column for both equality and range queries.

## Common Misconceptions
- Hash indexes are faster than B-trees for equality but completely unsuitable for range scans or ORDER BY operations.
- Hash collisions are expected and handled by chaining — they don't cause corruption, only slight performance degradation at high load.
- Many older database versions limited hash indexes to in-memory use due to WAL recovery complications.
