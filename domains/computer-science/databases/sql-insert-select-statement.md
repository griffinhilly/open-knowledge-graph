---
id: sql-insert-select-statement
title: 'INSERT...SELECT: Populating Tables from Queries'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-bulk-insert-operations
tags:
- sql
- dml
- data-loading
stage: formal-systems
status: draft
---

# INSERT...SELECT: Populating Tables from Queries

## Core Idea
INSERT...SELECT allows inserting rows derived from a SELECT query directly into a table, avoiding manual INSERT statements and enabling bulk data migration and transformation.

## How It's Best Learned
Practice inserting filtered or aggregated data from one table to another, then use with JOINs to combine data from multiple sources.
