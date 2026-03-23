---
id: index-types-btree-hash-bitmap
title: 'Index Types: B-Trees, Hash Indexes, and Bitmap Indexes'
domain: computer-science
course: databases
prerequisites:
- id: b-trees
  type: hard
- id: hash-indexes
  type: hard
- id: indexing-concepts
  type: hard
builds-toward:
  - index-design-selection
tags:
- index-types
- B-tree
- hash
- bitmap
- tradeoffs
stage: formal-systems
status: validated
---
# Index Types: B-Trees, Hash Indexes, and Bitmap Indexes

## Core Idea
B-tree indexes provide sorted access supporting range queries through multi-level balanced tree structures; hash indexes use hash functions for fast exact-match lookups but don't support range queries; bitmap indexes use bit arrays for low-cardinality columns, excelling in data warehouse environments. Each type has different I/O characteristics, space requirements, and INSERT/UPDATE/DELETE costs.

## Questions

```yaml
- question: "A data warehouse table has 50 million rows with a 'region' column containing 8 distinct values (North, South, East, West, etc.). Analysts frequently query WHERE region = 'West' AND status = 'Active'. Which index type is best suited for this column?"
  type: multiple-choice
  options:
    - "B-tree, because it handles equality predicates efficiently"
    - "Hash index, because equality lookups are O(1) on a hash"
    - "Bitmap index, because the low cardinality makes bitwise AND operations across columns extremely fast"
    - "No index — a sequential scan is faster when matching a large fraction of rows"
  answer: 2
  explanation: "With only 8 distinct values in 50M rows, 'region' is a classic low-cardinality column tailor-made for bitmap indexes. A bitmap stores one bit per row for each distinct value; combining filters like WHERE region = 'West' AND status = 'Active' becomes a single bitwise AND operation, which CPUs execute in bulk. B-trees and hash indexes handle point queries but cannot efficiently combine multi-column low-cardinality filters the way bitmaps can. Option D might be competitive, but for analytical queries in a write-infrequent warehouse, bitmap excels."

- question: "An application needs to look up user records by UUID (a globally unique 128-bit identifier) using only exact-match queries. The table has 100 million rows. Which index would give the best lookup performance?"
  type: multiple-choice
  options:
    - "B-tree, because it is the default and handles all query types"
    - "Hash index, because UUIDs are high-cardinality and only equality lookups are needed, giving O(1) average performance"
    - "Bitmap index, because UUIDs have high cardinality and low repetition"
    - "No index — UUID lookups are always sequential scans"
  answer: 1
  explanation: "Hash indexes achieve O(1) average-case lookup for exact matches, beating B-tree's O(log n) for this specific use case. UUIDs are high-cardinality (nearly every row has a unique value), which is exactly where bitmaps fail (they'd need one bit-array per unique UUID — essentially the entire table size). The key is recognizing that hash indexes trade away range and sort capabilities for maximum equality-lookup speed, which is the right tradeoff when range queries will never be issued."

- question: "A hash index on a column cannot be used to satisfy an ORDER BY clause on that column."
  type: true-false
  answer: true
  explanation: "Hash indexes map keys to buckets via a hash function that deliberately scatters values — the storage order has no relationship to the key's sort order. Retrieving results in sorted order would require fetching all matching rows and sorting them afterward, defeating any index benefit. B-tree indexes, by contrast, store leaf pages in sorted key order linked in a list, so ORDER BY can be satisfied by a sequential scan of the leaf level without any additional sort step."

- question: "Bitmap indexes are ideal for high-write OLTP systems because the compact bit-array format reduces storage overhead during frequent updates."
  type: true-false
  answer: false
  explanation: "Bitmap indexes are poorly suited to OLTP workloads with frequent writes. Every INSERT, UPDATE, or DELETE requires modifying the bit arrays — potentially locking many rows simultaneously and causing heavy contention. Their strength is in read-heavy analytical environments (data warehouses) where data is loaded in bulk and queried extensively. The 'compact storage' of bitmaps becomes a liability under frequent writes, not an asset."

- question: "Why can't a hash index support range queries, and what structural property of B-tree indexes allows them to do so efficiently?"
  type: short-answer
  answer: "A hash index maps each key through a hash function to a bucket — the storage location has no relationship to the key's natural order. To answer WHERE price BETWEEN 10 AND 50, you would need to compute a hash for every possible value in the range, which is impossible for continuous or large-domain values. B-tree indexes store keys in sorted order in their leaf pages, and those leaf pages are linked together in a doubly-linked list. To answer a range query, the database finds the start of the range via the tree structure (O(log n)), then scans forward through the sorted leaf pages — accessing only the relevant rows in order, without touching unrelated data."
  explanation: "The structural difference is order preservation: B-trees preserve sort order at every level, enabling both point lookups (top-down traversal) and range scans (leaf-level sequential scan). Hash functions deliberately destroy order to achieve uniform distribution across buckets — this is why they excel at equality and fail at ranges. Understanding this tradeoff is the core of index selection."
```

## Explainer

You already understand B-trees and hash indexes individually — now the question is when to use which. The choice of index type is one of the most impactful decisions in physical database design, because it determines how efficiently the database can answer different query patterns. Each index type is optimized for a different access pattern, and choosing wrong means either wasted space or queries that scan far more data than necessary.

**B-tree indexes** are the default workhorse of relational databases. Their balanced tree structure keeps all leaf nodes at the same depth, guaranteeing O(log n) lookups. But their real advantage is that leaf nodes are linked together in sorted order, making them excellent for **range queries** (WHERE price BETWEEN 10 AND 50), **prefix matching** (WHERE name LIKE 'Sm%'), and **ORDER BY** operations. When the database walks the B-tree to find the start of a range and then scans sequentially through linked leaf pages, it minimizes random I/O. This versatility is why B-trees are the default index type in PostgreSQL, MySQL, and most other systems — if you're unsure what index to use, a B-tree is almost always a reasonable choice.

**Hash indexes** trade versatility for speed on a single operation: **exact-match lookups**. A hash function maps the search key directly to a bucket containing the matching records, achieving O(1) average-case lookup — faster than a B-tree's O(log n). But hash indexes cannot answer range queries, cannot return results in sorted order, and do not support partial key matching. They are ideal for join keys and equality predicates on high-cardinality columns (like UUIDs or email addresses) where you never need ranges. In many database systems, hash indexes also don't support unique constraints as robustly as B-trees, which further limits their use cases.

**Bitmap indexes** take a completely different approach, optimized for columns with **low cardinality** — columns that take on only a few distinct values, like gender, status codes, or boolean flags. For each distinct value, a bitmap index stores a bit array with one bit per row: 1 if the row has that value, 0 otherwise. Queries on these columns become bitwise AND/OR operations across bitmaps, which modern CPUs execute extremely fast. Bitmap indexes shine in **data warehouse** environments where tables are large, queries involve multiple low-cardinality filters (WHERE region = 'West' AND status = 'Active' AND year = 2024), and writes are infrequent. They are poorly suited to OLTP workloads because every INSERT or UPDATE requires modifying the bit arrays, which can cause contention. The rule of thumb: B-trees for general-purpose OLTP, hash for equality-only lookups at high cardinality, bitmaps for analytical queries on low-cardinality columns.
