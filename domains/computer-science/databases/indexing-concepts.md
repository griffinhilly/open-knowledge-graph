---
id: indexing-concepts
title: Database Indexing
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: file-system-concepts
  type: soft
- id: time-space-complexity
  type: soft
- id: database-schema-design
  type: soft
builds-toward:
- btree-indexes
- hash-indexes
- query-execution-plans
tags:
- indexing
- performance
- clustered index
- secondary index
- selectivity
stage: formal-systems
status: validated
---
# Database Indexing

## Core Idea
A database index is a supplementary data structure that allows the engine to locate rows matching a condition without scanning every row in the table, trading write overhead and storage for faster reads. Clustered indexes determine the physical storage order of rows (only one per table); secondary (non-clustered) indexes maintain a separate structure with pointers to rows. Index selectivity — the fraction of rows matching a condition — determines whether using an index is worth it. Indexes are most beneficial on columns used in WHERE, JOIN, and ORDER BY clauses.

## How It's Best Learned
Run EXPLAIN/EXPLAIN ANALYZE on queries before and after creating an index to observe the execution plan change. Experiment with high-selectivity (unique ID) vs. low-selectivity (boolean flag) indexes to understand when indexes help vs. hurt.

## Common Misconceptions
- Indexing every column does not make a database faster — it increases write cost and storage use.
- An index is not automatically used just because it exists; the query planner decides based on statistics and selectivity estimates.
- Primary key columns are automatically indexed in most databases, but foreign key columns generally are not.

## Explainer

Imagine a textbook with no index at the back. To find every mention of "B-tree," you would have to read every page from cover to cover — a **full table scan** in database terms. Now imagine the textbook has an alphabetical index that lists "B-tree: pages 42, 107, 215." You jump straight to those pages. A **database index** works the same way: it is a separate data structure that maps column values to the physical locations of matching rows, letting the database engine skip directly to relevant data instead of scanning every row.

The tradeoff is straightforward and mirrors what you know from time-space complexity analysis. An index speeds up reads (SELECT queries with WHERE, JOIN, or ORDER BY on the indexed column) but slows down writes (INSERT, UPDATE, DELETE), because every modification to the table must also update the index. An index also consumes additional storage. This means indexing every column in a table is counterproductive — the write overhead and storage cost outweigh the read benefit for columns that are rarely queried. The goal is to index selectively, targeting columns that appear frequently in query predicates and join conditions.

**Selectivity** is the key concept that determines whether an index is worth using for a given query. A highly selective condition matches a small fraction of rows — for example, looking up a user by their unique email address matches exactly one row out of millions. The index is extremely valuable here because it avoids scanning millions of irrelevant rows. A low-selectivity condition, like filtering on a boolean `is_active` column that is TRUE for 90% of rows, gains little from an index — the database would spend time traversing the index only to end up reading most of the table anyway. In such cases, a sequential scan is faster. The query planner makes this decision automatically based on statistics about value distributions in each column.

A **clustered index** determines the physical order in which rows are stored on disk — the table's data is literally sorted by the clustered index key. Because data can only be physically sorted one way, a table can have at most one clustered index (in many systems, this is the primary key by default). A **secondary (non-clustered) index** is a separate structure that stores the indexed column's values along with pointers back to the corresponding rows in the main table. When a query uses a secondary index, the database first looks up matching entries in the index, then follows the pointers to fetch the actual rows — a two-step process called a **bookmark lookup**. If the query only needs columns that are stored in the index itself (a **covering index**), the second step is skipped entirely, which is why thoughtful index design can dramatically improve query performance.
