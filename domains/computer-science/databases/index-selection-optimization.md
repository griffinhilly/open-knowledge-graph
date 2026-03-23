---
id: index-selection-optimization
title: Index Design and Selection Strategy
domain: computer-science
course: databases
prerequisites:
- id: index-structure-performance
  type: hard
builds-toward:
- execution-plan-query-optimization
tags:
- index selection
- index design
- composite index
- selectivity
stage: formal-systems
status: validated
---

# Index Design and Selection Strategy

## Core Idea
Effective indexing requires choosing which columns to index based on query patterns, selectivity (uniqueness), and update frequency. Composite indexes on multiple columns can optimize multi-condition queries. Over-indexing wastes space and slows writes. Index selection must balance query performance against storage and maintenance costs.

## How It's Best Learned
Analyze query patterns in a real application, identify high-cardinality columns in WHERE/JOIN predicates, create composite indexes in order of selectivity, and validate that queries use intended indexes.

## Questions

```yaml
- question: "A table has a composite index on (country, city). A query filters only on city. How will the database handle this?"
  type: multiple-choice
  options:
    - "It will use the composite index efficiently, since city is one of the indexed columns"
    - "It will use only the city portion of the composite index, skipping the country portion"
    - "It will likely not use the composite index, since the leftmost prefix (country) is not in the query"
    - "It will use the index but only if the city column has high selectivity"
  answer: 2
  explanation: "B-tree composite indexes are ordered left to right: (country, city) sorts first by country, then by city within each country. A filter on city alone cannot navigate this structure efficiently — the database would need to examine every country's entries. This leftmost prefix rule means the composite index on (country, city) is effectively useless for city-only queries. To support city-only queries, a separate index on city is needed. Column order in a composite index is one of the most important and commonly misunderstood aspects of index design."

- question: "A table has 1 million rows and a 'status' column with three possible values: 'active' (60%), 'inactive' (35%), 'suspended' (5%). A developer adds an index on status to speed up queries filtering by status. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "The index will dramatically speed up all queries filtering by status"
    - "The index will be most useful for status = 'suspended' queries but may not help for 'active' or 'inactive'"
    - "The index will slow down reads because the database must scan the entire index before the table"
    - "The index will have no effect because it was added after the table was populated"
  answer: 1
  explanation: "Selectivity determines whether an index helps. 'active' and 'inactive' each return hundreds of thousands of rows — a third or more of the table — at which point a full table scan can be faster than following index pointers to scattered row locations. But 'suspended' (5%) returns 50,000 rows, a narrow result where the index meaningfully reduces work. Low-selectivity columns make poor index candidates for common values. This is why the general rule is to prioritize high-selectivity columns — those with many distinct values relative to row count."

- question: "Adding more indexes to a frequently-written table can improve overall database performance by caching more data in memory."
  type: true-false
  answer: false
  explanation: "More indexes slow writes, not improve them. Every INSERT, UPDATE, or DELETE must update all indexes on the affected columns — the more indexes a table has, the more work each write operation requires. Indexes also consume disk space and memory buffer pool capacity. Over-indexing is a real problem in production systems: tables with ten or twenty indexes can have dramatically slower write throughput. The right number of indexes balances read performance gains against write overhead and storage costs, guided by the actual query workload."

- question: "A covering index can answer a query entirely from the index structure without accessing the underlying table rows."
  type: true-false
  answer: true
  explanation: "A covering index is one that contains all the columns a query needs — the SELECT columns, WHERE filters, and JOIN keys. When the index covers the query, the database can return results directly from the index without a 'table lookup' (also called a heap fetch or bookmark lookup). This is a major performance win because index pages are much smaller than table pages, so the same data fits in far fewer I/O operations. Identifying opportunities for covering indexes is one of the highest-leverage query optimization techniques."

- question: "Explain the leftmost prefix rule for composite indexes and why column order in a composite index matters enormously."
  type: short-answer
  answer: "A composite index on columns (A, B, C) is stored sorted first by A, then by B within each A value, then by C within each (A, B) pair. The database can only use the index efficiently for queries that filter on a prefix of this left-to-right order: A alone, A and B together, or A, B, and C together. Queries filtering only on B or C cannot navigate the index structure, because the values of B are interleaved across all A values with no useful global ordering. Column order should place the most selective equality-condition columns first, followed by range condition columns, to maximize the proportion of the index that narrows the search."
  explanation: "The leftmost prefix rule has a practical design implication: a single composite index on (user_id, created_at) can serve both 'show all records for user X' queries and 'show all records for user X after date Y' queries, but not 'show all records after date Y' queries without knowing the user. Designing composite indexes requires analyzing the query workload to identify which column combinations appear together most often, then ordering those columns to support as many query patterns as possible with a single index."
```

## Explainer

You already understand how indexes work — tree structures (typically B-trees) that let the database find rows without scanning entire tables. The harder question is **which columns to index and in what combinations**. Creating an index is not free: each index consumes disk space, and every INSERT, UPDATE, or DELETE must maintain all affected indexes. A table with ten indexes might have fast reads but painfully slow writes. Index selection is the art of finding the sweet spot between read performance and write overhead, guided by actual query patterns rather than guesswork.

The most important concept in index selection is **selectivity** — how many distinct values a column has relative to the total number of rows. A column like `user_id` with millions of unique values is highly selective: an index lookup returns very few rows. A column like `status` with three possible values (active, inactive, suspended) is low-selectivity: an index lookup still returns roughly a third of the table, at which point a full table scan might actually be faster. The general rule is to index columns that appear in WHERE clauses and JOIN conditions, prioritizing those with high selectivity. An index on a low-selectivity column rarely helps because the database cannot meaningfully narrow down the result set.

**Composite indexes** (indexes on multiple columns) unlock major performance gains for queries that filter on several columns simultaneously. A composite index on `(country, city, zip_code)` can efficiently serve queries that filter on `country` alone, `country AND city`, or all three — but not queries that filter only on `city` or `zip_code`. This is because B-tree indexes are ordered left to right: the index sorts first by country, then by city within each country, then by zip code within each city. This **leftmost prefix** rule means column order in a composite index matters enormously. Put the most selective columns that appear in equality conditions first, followed by range conditions, to maximize the index's filtering power.

When selecting indexes, examine the application's actual query workload rather than indexing every column that looks important. Use `EXPLAIN` or `EXPLAIN ANALYZE` to verify that the database uses your indexes as intended — sometimes the query optimizer decides a sequential scan is cheaper, indicating the index is not helpful for that query. Watch for **covering indexes**, where the index contains all the columns a query needs, allowing the database to answer the query entirely from the index without touching the table data. Periodically review indexes for ones that are never used (most databases track index usage statistics) and drop them to reclaim space and reduce write overhead. Good index design is an ongoing conversation between your query patterns and your write volume, not a one-time decision made during schema creation.
