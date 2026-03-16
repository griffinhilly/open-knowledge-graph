---
id: index-structure-performance
title: 'Database Indexing: Structures and Performance'
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: soft
builds-toward:
- index-selection-optimization
tags:
- index
- B-tree
- hash
- performance
- search
stage: formal-systems
status: draft
---

# Database Indexing: Structures and Performance

## Core Idea
Indexes are data structures that enable fast data retrieval by avoiding full table scans. B-tree indexes support range queries and sorted access. Hash indexes support fast equality lookups. Indexes trade query speed for storage space and update overhead. Understanding index types and their trade-offs is essential for database optimization.

## How It's Best Learned
Study B-tree and hash structure properties, understand when each is preferred, analyze query plans with and without indexes, and measure performance improvements from indexing.

## Explainer

Without an index, answering a query like "find the customer with ID 42857" requires scanning every row in the table — a **full table scan**. If the table has a million rows, the database reads a million rows to find one. An index is a separate data structure that maps column values to the physical locations of their rows, enabling the database to jump directly to matching rows. The concept is identical to a book's index: instead of reading every page to find mentions of "B-tree," you look up "B-tree" in the back and go straight to pages 47, 93, and 201.

The most common index structure is the **B-tree** (and its variant, the B+ tree). A B-tree is a balanced, multi-way search tree where each node contains multiple keys and child pointers, and all leaf nodes sit at the same depth. Because B-tree nodes are sized to match disk pages (typically 4-16 KB), a single disk read loads an entire node containing dozens or hundreds of keys. A B-tree with a branching factor of 100 can index 100 million rows in just four levels — meaning any lookup requires at most four disk reads. B-trees support both **equality queries** (find the row where ID = 42857) and **range queries** (find all rows where price BETWEEN 10 AND 50) because the keys are stored in sorted order.

**Hash indexes** take a different approach: they apply a hash function to the key and use the result to locate the row directly. For equality lookups, a hash index offers O(1) average-case performance — faster than a B-tree's O(log n). But hash indexes cannot answer range queries at all, because hashing destroys the ordering of keys. If you need `WHERE price > 100`, a hash index on price is useless. This makes B-trees the default choice in most databases, with hash indexes reserved for specific workloads dominated by exact-match lookups.

The fundamental tradeoff of indexing is **read speed versus write overhead and storage cost**. Every index must be updated whenever a row is inserted, deleted, or has its indexed column modified. A table with five indexes means every INSERT triggers five index updates in addition to the table write. Indexes also consume disk space — sometimes substantial amounts for large tables with many indexed columns. The art of index selection is choosing indexes that accelerate your most critical queries without creating an unsustainable write-time or storage burden. Tools like `EXPLAIN` or `EXPLAIN ANALYZE` let you inspect the database's **query plan** to verify whether an index is actually being used and how much it reduces the work.
