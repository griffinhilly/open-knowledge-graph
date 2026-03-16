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
status: draft
---

# Index Design and Selection Strategy

## Core Idea
Effective indexing requires choosing which columns to index based on query patterns, selectivity (uniqueness), and update frequency. Composite indexes on multiple columns can optimize multi-condition queries. Over-indexing wastes space and slows writes. Index selection must balance query performance against storage and maintenance costs.

## How It's Best Learned
Analyze query patterns in a real application, identify high-cardinality columns in WHERE/JOIN predicates, create composite indexes in order of selectivity, and validate that queries use intended indexes.

## Explainer

You already understand how indexes work — tree structures (typically B-trees) that let the database find rows without scanning entire tables. The harder question is **which columns to index and in what combinations**. Creating an index is not free: each index consumes disk space, and every INSERT, UPDATE, or DELETE must maintain all affected indexes. A table with ten indexes might have fast reads but painfully slow writes. Index selection is the art of finding the sweet spot between read performance and write overhead, guided by actual query patterns rather than guesswork.

The most important concept in index selection is **selectivity** — how many distinct values a column has relative to the total number of rows. A column like `user_id` with millions of unique values is highly selective: an index lookup returns very few rows. A column like `status` with three possible values (active, inactive, suspended) is low-selectivity: an index lookup still returns roughly a third of the table, at which point a full table scan might actually be faster. The general rule is to index columns that appear in WHERE clauses and JOIN conditions, prioritizing those with high selectivity. An index on a low-selectivity column rarely helps because the database cannot meaningfully narrow down the result set.

**Composite indexes** (indexes on multiple columns) unlock major performance gains for queries that filter on several columns simultaneously. A composite index on `(country, city, zip_code)` can efficiently serve queries that filter on `country` alone, `country AND city`, or all three — but not queries that filter only on `city` or `zip_code`. This is because B-tree indexes are ordered left to right: the index sorts first by country, then by city within each country, then by zip code within each city. This **leftmost prefix** rule means column order in a composite index matters enormously. Put the most selective columns that appear in equality conditions first, followed by range conditions, to maximize the index's filtering power.

When selecting indexes, examine the application's actual query workload rather than indexing every column that looks important. Use `EXPLAIN` or `EXPLAIN ANALYZE` to verify that the database uses your indexes as intended — sometimes the query optimizer decides a sequential scan is cheaper, indicating the index is not helpful for that query. Watch for **covering indexes**, where the index contains all the columns a query needs, allowing the database to answer the query entirely from the index without touching the table data. Periodically review indexes for ones that are never used (most databases track index usage statistics) and drop them to reclaim space and reduce write overhead. Good index design is an ongoing conversation between your query patterns and your write volume, not a one-time decision made during schema creation.
