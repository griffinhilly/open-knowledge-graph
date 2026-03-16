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

## Explainer

You already know the two core ideas behind hash indexes from your prerequisites: indexing speeds up queries by avoiding full table scans, and hash tables map keys to positions using a hash function. A **hash index** applies this same principle to database storage — instead of scanning every row to find where `email = 'alice@example.com'`, the database hashes the search key, jumps directly to the corresponding bucket, and finds matching rows in O(1) average time.

The mechanics work like an in-memory hash table, adapted for disk. A hash function takes the indexed column's value and produces a bucket number. Each bucket stores pointers to the actual rows on disk (or the rows themselves in some implementations). When you execute `SELECT * FROM users WHERE email = 'alice@example.com'`, the database hashes `'alice@example.com'`, looks up the bucket, and follows the pointer to the row. No tree traversal, no binary search — just a direct lookup. For **equality queries** (exact match on a key), this is faster than a B-tree, which requires traversing multiple levels of a tree structure.

The critical limitation is that hashing **destroys ordering**. Two keys that are adjacent in sort order (like `'alice'` and `'bob'`) might hash to completely different buckets. This means hash indexes are useless for range queries (`WHERE age > 30`), prefix searches (`WHERE name LIKE 'Ali%'`), or anything requiring sorted output (`ORDER BY`). A B-tree preserves key order in its leaf nodes and handles all these operations naturally. This is why B-trees remain the default index type in most databases — they're slightly slower for equality lookups but vastly more versatile.

As your dataset grows, a static hash table with a fixed number of buckets becomes inefficient — too many entries per bucket degrade lookups. **Dynamic hashing** schemes solve this. **Extendible hashing** uses a directory of pointers to buckets, doubling the directory and splitting only the overflowing bucket when needed. **Linear hashing** splits buckets one at a time in a round-robin fashion, spreading the cost of growth evenly over insertions. Both approaches let the index grow smoothly without the stop-the-world cost of rehashing every key at once — an important property for databases that must remain responsive during writes.
