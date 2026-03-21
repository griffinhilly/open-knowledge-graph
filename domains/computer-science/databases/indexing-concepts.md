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

## Questions

```yaml
- question: "A table has a 'status' column with values 'active' (95% of rows) and 'inactive' (5% of rows). A query runs WHERE status = 'active'. What will the query planner most likely do with an index on 'status'?"
  type: multiple-choice
  options:
    - "Use the index — that is exactly what indexes are for"
    - "Use the index only for the primary key lookup following the index scan"
    - "Perform a full table scan instead of using the index"
    - "Rebuild the index statistics before deciding"
  answer: 2
  explanation: "This tests index selectivity. When a condition matches 95% of rows, the index barely narrows the search — the database would traverse the index structure, then follow pointers to nearly every row in the table anyway. A sequential full table scan is often faster in this case because it reads data in order with lower overhead than the random I/O of index-then-lookup. The query planner estimates selectivity from column statistics and skips the index when it wouldn't help. Low-selectivity columns (booleans, status flags) are the classic case where indexes don't pay off."

- question: "A developer adds indexes on every column of a large write-heavy table to ensure the fastest possible query performance. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "All queries run faster because the optimizer always has the best possible index to choose from"
    - "Read queries run faster; write queries are unaffected since indexes are separate structures"
    - "Write performance degrades significantly, and storage use increases, without proportional read gains"
    - "The database automatically drops unused indexes to manage the overhead"
  answer: 2
  explanation: "Every index on a table must be updated on every INSERT, UPDATE, and DELETE. A table with 20 indexes requires 20 index updates per write operation. For write-heavy tables, this overhead can dominate performance — making the database slower overall even if individual SELECT queries benefit. The correct approach is selective indexing: target columns that appear frequently in WHERE, JOIN, and ORDER BY clauses, especially high-selectivity ones. More indexes is not always better."

- question: "A covering index — one that contains all columns needed by a query — can answer the query entirely from the index without accessing the main table."
  type: true-false
  answer: true
  explanation: "When an index contains all columns referenced in a query (both the filter columns and the output columns), the database can satisfy the query entirely by scanning the index, skipping the 'bookmark lookup' step of following pointers to the main table rows. This is especially valuable for read-heavy analytical queries on large tables. Thoughtful index design — including covering indexes for frequent query patterns — can dramatically reduce I/O."

- question: "In most database systems, adding a foreign key constraint on a column automatically creates an index on that column."
  type: true-false
  answer: false
  explanation: "Primary key columns are automatically indexed in most databases, but foreign key columns generally are not. This is a common source of slow JOIN performance: a query joining on a foreign key column with no index forces the database to scan the entire table for matching rows. Developers must explicitly create indexes on foreign key columns. Some databases (like MySQL/InnoDB) do create them automatically, but PostgreSQL and SQL Server do not — making this a genuine gotcha for schema designers."

- question: "Why is selectivity the key concept in deciding whether an index will improve query performance, rather than simply asking whether the column appears in a WHERE clause?"
  type: short-answer
  answer: "An index is worth using only when it significantly reduces the number of rows the database must read. High selectivity (e.g., a unique email column) means the index eliminates almost all rows immediately — the query touches a handful of rows instead of millions. Low selectivity (e.g., a boolean column true for 90% of rows) means the index barely narrows the result set, so the cost of index traversal plus random-access row fetches often exceeds the cost of a simple sequential scan. Appearing in a WHERE clause is necessary but not sufficient for an index to help."
  explanation: "The query planner makes this evaluation automatically based on column statistics, which is why running ANALYZE (to update statistics) matters for performance. Understanding selectivity also explains why composite indexes (indexing multiple columns together) can be more selective than any single-column index, and why the leading column of a composite index should be the most selective one."
```

## Explainer

Imagine a textbook with no index at the back. To find every mention of "B-tree," you would have to read every page from cover to cover — a **full table scan** in database terms. Now imagine the textbook has an alphabetical index that lists "B-tree: pages 42, 107, 215." You jump straight to those pages. A **database index** works the same way: it is a separate data structure that maps column values to the physical locations of matching rows, letting the database engine skip directly to relevant data instead of scanning every row.

The tradeoff is straightforward and mirrors what you know from time-space complexity analysis. An index speeds up reads (SELECT queries with WHERE, JOIN, or ORDER BY on the indexed column) but slows down writes (INSERT, UPDATE, DELETE), because every modification to the table must also update the index. An index also consumes additional storage. This means indexing every column in a table is counterproductive — the write overhead and storage cost outweigh the read benefit for columns that are rarely queried. The goal is to index selectively, targeting columns that appear frequently in query predicates and join conditions.

**Selectivity** is the key concept that determines whether an index is worth using for a given query. A highly selective condition matches a small fraction of rows — for example, looking up a user by their unique email address matches exactly one row out of millions. The index is extremely valuable here because it avoids scanning millions of irrelevant rows. A low-selectivity condition, like filtering on a boolean `is_active` column that is TRUE for 90% of rows, gains little from an index — the database would spend time traversing the index only to end up reading most of the table anyway. In such cases, a sequential scan is faster. The query planner makes this decision automatically based on statistics about value distributions in each column.

A **clustered index** determines the physical order in which rows are stored on disk — the table's data is literally sorted by the clustered index key. Because data can only be physically sorted one way, a table can have at most one clustered index (in many systems, this is the primary key by default). A **secondary (non-clustered) index** is a separate structure that stores the indexed column's values along with pointers back to the corresponding rows in the main table. When a query uses a secondary index, the database first looks up matching entries in the index, then follows the pointers to fetch the actual rows — a two-step process called a **bookmark lookup**. If the query only needs columns that are stored in the index itself (a **covering index**), the second step is skipped entirely, which is why thoughtful index design can dramatically improve query performance.
