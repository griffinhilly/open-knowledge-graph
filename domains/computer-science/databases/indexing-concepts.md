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
