---
id: hash-indexes
title: Hash Indexes
domain: computer-science
course: databases
prerequisites:
- id: index-types-btree-hash-bitmap
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

## Questions

```yaml
- question: "A database table has a hash index on the 'email' column. A developer runs the query: SELECT * FROM users WHERE created_at > '2024-01-01'. Why won't the hash index help with this query?"
  type: multiple-choice
  options:
    - "Hash indexes only work on string columns, not date columns"
    - "Hash indexes require an exact key value to hash; the ordering information needed to find all dates above a threshold is destroyed by the hash function"
    - "Hash indexes are only used when the table has fewer than 1000 rows"
    - "The hash index would actually work fine for this range query"
  answer: 1
  explanation: "The hash function maps key values to bucket positions without preserving any sorted order. Two keys adjacent in value (e.g., '2024-01-01' and '2024-01-02') may hash to completely different buckets. To answer a range query like > '2024-01-01', the database would need to scan all buckets — which negates the benefit of the index entirely. A B-tree index, which stores keys in sorted order in its leaf nodes, handles range queries naturally."

- question: "For which of the following query types does a hash index provide a genuine performance advantage over a B-tree index?"
  type: multiple-choice
  options:
    - "SELECT * FROM orders WHERE amount BETWEEN 100 AND 500"
    - "SELECT * FROM users WHERE name LIKE 'Ali%'"
    - "SELECT * FROM sessions WHERE session_token = 'abc123xyz'"
    - "SELECT * FROM products ORDER BY price ASC"
  answer: 2
  explanation: "Hash indexes excel at exact equality lookups — they compute a hash of the search key and jump directly to the matching bucket in O(1) average time, avoiding tree traversal. The other three queries all require ordered access: BETWEEN needs a range scan, LIKE 'Ali%' needs prefix matching on sorted keys, and ORDER BY requires sorted output. For all three, the hash's destroyed ordering makes it useless, while a B-tree handles them naturally."

- question: "Hash indexes cannot support range queries because the hash function does not preserve the ordering relationship between key values."
  type: true-false
  answer: true
  explanation: "This is the defining limitation of hash indexes. Two keys that are adjacent in sorted order (like 5 and 6, or 'alice' and 'bob') may hash to entirely different buckets, so there is no way to scan 'all keys between X and Y' without checking every bucket. B-trees store keys in sorted order, which is why they handle range queries naturally at the cost of slightly slower equality lookups."

- question: "Hash indexes are generally faster than B-tree indexes for all types of database query operations."
  type: true-false
  answer: false
  explanation: "Hash indexes are faster only for equality lookups (WHERE col = value), where they achieve O(1) average time vs. O(log n) for B-tree traversal. For range queries, prefix searches, ORDER BY, and any operation requiring sorted key access, hash indexes provide no benefit and must fall back to a full table scan. B-trees are slightly slower for equality but handle the full range of query types, which is why they are the default index type in most databases."

- question: "Why can't a hash index answer the query WHERE salary > 50000, even if there is a hash index on the salary column?"
  type: short-answer
  answer: "The hash function maps salary values to bucket positions without preserving their numeric order. To find all salaries greater than 50000, you would need to examine all salaries in sorted order starting from 50000. But the hash function may scatter nearby salary values (50001, 50002, 50003) into completely different buckets with no predictable relationship. The only way to answer the query would be to check every bucket, which is equivalent to a full table scan and provides no index benefit."
  explanation: "This is the fundamental tradeoff that makes hash indexes a specialized tool rather than a universal one. They trade ordering for speed on exact matches. Understanding this helps explain why B-trees remain the default: the O(log n) penalty for equality lookups is worth it in exchange for supporting the full range of query types that real applications need."
```

## Explainer

You already know the two core ideas behind hash indexes from your prerequisites: indexing speeds up queries by avoiding full table scans, and hash tables map keys to positions using a hash function. A **hash index** applies this same principle to database storage — instead of scanning every row to find where `email = 'alice@example.com'`, the database hashes the search key, jumps directly to the corresponding bucket, and finds matching rows in O(1) average time.

The mechanics work like an in-memory hash table, adapted for disk. A hash function takes the indexed column's value and produces a bucket number. Each bucket stores pointers to the actual rows on disk (or the rows themselves in some implementations). When you execute `SELECT * FROM users WHERE email = 'alice@example.com'`, the database hashes `'alice@example.com'`, looks up the bucket, and follows the pointer to the row. No tree traversal, no binary search — just a direct lookup. For **equality queries** (exact match on a key), this is faster than a B-tree, which requires traversing multiple levels of a tree structure.

The critical limitation is that hashing **destroys ordering**. Two keys that are adjacent in sort order (like `'alice'` and `'bob'`) might hash to completely different buckets. This means hash indexes are useless for range queries (`WHERE age > 30`), prefix searches (`WHERE name LIKE 'Ali%'`), or anything requiring sorted output (`ORDER BY`). A B-tree preserves key order in its leaf nodes and handles all these operations naturally. This is why B-trees remain the default index type in most databases — they're slightly slower for equality lookups but vastly more versatile.

As your dataset grows, a static hash table with a fixed number of buckets becomes inefficient — too many entries per bucket degrade lookups. **Dynamic hashing** schemes solve this. **Extendible hashing** uses a directory of pointers to buckets, doubling the directory and splitting only the overflowing bucket when needed. **Linear hashing** splits buckets one at a time in a round-robin fashion, spreading the cost of growth evenly over insertions. Both approaches let the index grow smoothly without the stop-the-world cost of rehashing every key at once — an important property for databases that must remain responsive during writes.
