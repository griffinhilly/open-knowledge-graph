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
status: validated
---

# Database Indexing: Structures and Performance

## Core Idea
Indexes are data structures that enable fast data retrieval by avoiding full table scans. B-tree indexes support range queries and sorted access. Hash indexes support fast equality lookups. Indexes trade query speed for storage space and update overhead. Understanding index types and their trade-offs is essential for database optimization.

## How It's Best Learned
Study B-tree and hash structure properties, understand when each is preferred, analyze query plans with and without indexes, and measure performance improvements from indexing.

## Questions

```yaml
- question: "A database table receives hundreds of thousands of INSERT operations per hour and is rarely queried. A developer proposes adding five separate indexes to speed up the occasional read queries. What is the main risk of this approach?"
  type: multiple-choice
  options:
    - "The indexes will consume too much RAM during query execution"
    - "Each INSERT will trigger five additional index updates, significantly increasing write-time overhead"
    - "Five indexes exceeds the maximum allowed by most database systems"
    - "Hash indexes cannot be maintained during high-volume inserts"
  answer: 1
  explanation: "Each index must be updated whenever a row is inserted, so five indexes mean five extra write operations per INSERT. On a write-heavy table, this overhead can severely degrade overall performance — illustrating the core tradeoff: indexes speed up reads but impose real costs on writes and storage. The common misconception is that indexes are purely beneficial; they are always a tradeoff."

- question: "A database has a hash index on the 'price' column. A query asks for all rows WHERE price BETWEEN 10 AND 50. What will the database most likely do?"
  type: multiple-choice
  options:
    - "Use the hash index to quickly locate all prices between 10 and 50"
    - "Use the hash index only for the boundary values 10 and 50, then scan between them"
    - "Ignore the hash index and perform a full table scan instead"
    - "Convert the range query to a series of equality lookups using the hash index"
  answer: 2
  explanation: "A hash index maps column values to row locations via a hash function, which destroys ordering. There is no way to navigate from hash(10) to hash(50) — hashed entries have no sorted relationship. For range queries, the database must fall back to a full table scan (or use a different index if one exists). Hash indexes are only useful for exact equality lookups."

- question: "A B-tree index can answer both equality queries (WHERE id = 42) and range queries (WHERE price BETWEEN 10 AND 50)."
  type: true-false
  answer: true
  explanation: "Because B-trees store keys in sorted order across their leaf nodes, the database can efficiently locate the first matching value and scan forward to collect the full range. Sorted storage is the property that makes range queries possible — and is precisely what hash indexes sacrifice in exchange for faster equality lookups."

- question: "Adding an index to a column always improves the performance of queries that filter on that column."
  type: true-false
  answer: false
  explanation: "The query optimizer may choose a full table scan over an index if the index is not selective enough (e.g., a boolean column with only 'Y'/'N' values). It may also skip the index if the table is small. Moreover, every index imposes write overhead — the improvement on reads is never free. The art of index selection is choosing indexes where the read gains outweigh the write costs."

- question: "Why is the B-tree the default index structure in most databases rather than the hash index, even though hash indexes offer faster average-case equality lookups?"
  type: short-answer
  answer: "B-trees support both equality and range queries because keys are stored in sorted order, making them versatile for the full range of query patterns. Hash indexes only support equality lookups — they cannot answer range queries at all because hashing destroys key ordering. Since most real-world workloads include range queries, sorting, and ordering, the B-tree's versatility makes it the better general-purpose default despite the slightly higher O(log n) cost for equality lookups."
  explanation: "Hashing deliberately discards ordering information to achieve O(1) lookup — a good tradeoff for pure equality workloads but catastrophic for range queries. B-trees accept O(log n) to preserve ordering, enabling a much broader class of queries. The hash index is a specialized tool, not a replacement."
```

## Explainer

Without an index, answering a query like "find the customer with ID 42857" requires scanning every row in the table — a **full table scan**. If the table has a million rows, the database reads a million rows to find one. An index is a separate data structure that maps column values to the physical locations of their rows, enabling the database to jump directly to matching rows. The concept is identical to a book's index: instead of reading every page to find mentions of "B-tree," you look up "B-tree" in the back and go straight to pages 47, 93, and 201.

The most common index structure is the **B-tree** (and its variant, the B+ tree). A B-tree is a balanced, multi-way search tree where each node contains multiple keys and child pointers, and all leaf nodes sit at the same depth. Because B-tree nodes are sized to match disk pages (typically 4-16 KB), a single disk read loads an entire node containing dozens or hundreds of keys. A B-tree with a branching factor of 100 can index 100 million rows in just four levels — meaning any lookup requires at most four disk reads. B-trees support both **equality queries** (find the row where ID = 42857) and **range queries** (find all rows where price BETWEEN 10 AND 50) because the keys are stored in sorted order.

**Hash indexes** take a different approach: they apply a hash function to the key and use the result to locate the row directly. For equality lookups, a hash index offers O(1) average-case performance — faster than a B-tree's O(log n). But hash indexes cannot answer range queries at all, because hashing destroys the ordering of keys. If you need `WHERE price > 100`, a hash index on price is useless. This makes B-trees the default choice in most databases, with hash indexes reserved for specific workloads dominated by exact-match lookups.

The fundamental tradeoff of indexing is **read speed versus write overhead and storage cost**. Every index must be updated whenever a row is inserted, deleted, or has its indexed column modified. A table with five indexes means every INSERT triggers five index updates in addition to the table write. Indexes also consume disk space — sometimes substantial amounts for large tables with many indexed columns. The art of index selection is choosing indexes that accelerate your most critical queries without creating an unsustainable write-time or storage burden. Tools like `EXPLAIN` or `EXPLAIN ANALYZE` let you inspect the database's **query plan** to verify whether an index is actually being used and how much it reduces the work.
