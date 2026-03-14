---
id: sql-view-virtual-tables-management
title: 'SQL: Views and Virtual Tables'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- denormalization-strategy
tags:
- SQL
- view
- virtual table
- materialized view
stage: formal-systems
status: draft
---

# SQL: Views and Virtual Tables

## Core Idea
A view is a virtual table defined by a SELECT query stored in the database. Views simplify complex queries, provide security by limiting column access, and enable logical data independence. Materialized views store query results physically for performance.
