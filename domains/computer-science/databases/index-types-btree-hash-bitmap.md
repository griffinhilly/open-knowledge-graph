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
- physical-storage-pages-records
- index-design-selection
tags:
- index-types
- B-tree
- hash
- bitmap
- tradeoffs
stage: formal-systems
status: draft
---

# Index Types: B-Trees, Hash Indexes, and Bitmap Indexes

## Core Idea
B-tree indexes provide sorted access supporting range queries through multi-level balanced tree structures; hash indexes use hash functions for fast exact-match lookups but don't support range queries; bitmap indexes use bit arrays for low-cardinality columns, excelling in data warehouse environments. Each type has different I/O characteristics, space requirements, and INSERT/UPDATE/DELETE costs.

## Explainer

You already understand B-trees and hash indexes individually — now the question is when to use which. The choice of index type is one of the most impactful decisions in physical database design, because it determines how efficiently the database can answer different query patterns. Each index type is optimized for a different access pattern, and choosing wrong means either wasted space or queries that scan far more data than necessary.

**B-tree indexes** are the default workhorse of relational databases. Their balanced tree structure keeps all leaf nodes at the same depth, guaranteeing O(log n) lookups. But their real advantage is that leaf nodes are linked together in sorted order, making them excellent for **range queries** (WHERE price BETWEEN 10 AND 50), **prefix matching** (WHERE name LIKE 'Sm%'), and **ORDER BY** operations. When the database walks the B-tree to find the start of a range and then scans sequentially through linked leaf pages, it minimizes random I/O. This versatility is why B-trees are the default index type in PostgreSQL, MySQL, and most other systems — if you're unsure what index to use, a B-tree is almost always a reasonable choice.

**Hash indexes** trade versatility for speed on a single operation: **exact-match lookups**. A hash function maps the search key directly to a bucket containing the matching records, achieving O(1) average-case lookup — faster than a B-tree's O(log n). But hash indexes cannot answer range queries, cannot return results in sorted order, and do not support partial key matching. They are ideal for join keys and equality predicates on high-cardinality columns (like UUIDs or email addresses) where you never need ranges. In many database systems, hash indexes also don't support unique constraints as robustly as B-trees, which further limits their use cases.

**Bitmap indexes** take a completely different approach, optimized for columns with **low cardinality** — columns that take on only a few distinct values, like gender, status codes, or boolean flags. For each distinct value, a bitmap index stores a bit array with one bit per row: 1 if the row has that value, 0 otherwise. Queries on these columns become bitwise AND/OR operations across bitmaps, which modern CPUs execute extremely fast. Bitmap indexes shine in **data warehouse** environments where tables are large, queries involve multiple low-cardinality filters (WHERE region = 'West' AND status = 'Active' AND year = 2024), and writes are infrequent. They are poorly suited to OLTP workloads because every INSERT or UPDATE requires modifying the bit arrays, which can cause contention. The rule of thumb: B-trees for general-purpose OLTP, hash for equality-only lookups at high cardinality, bitmaps for analytical queries on low-cardinality columns.
