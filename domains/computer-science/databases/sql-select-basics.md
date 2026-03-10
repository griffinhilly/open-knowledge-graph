---
id: sql-select-basics
title: SQL SELECT Basics
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: primary-and-foreign-keys
  type: soft
- id: boolean-logic-programming
  type: soft
builds-toward:
- sql-joins
- sql-aggregation
- sql-subqueries
- sql-views
tags:
- SQL
- SELECT
- WHERE
- ORDER BY
- DML
- declarative
stage: formal-systems
status: draft
---

# SQL SELECT Basics

## Core Idea
SQL's SELECT statement is the primary tool for querying relational databases, following the logical structure SELECT columns FROM table WHERE condition ORDER BY column LIMIT n. The WHERE clause filters rows using Boolean expressions, comparison operators, and predicates like BETWEEN, IN, LIKE, and IS NULL. SQL is a declarative language — you specify what data you want, not how to retrieve it; the database engine chooses the execution strategy. The logical processing order is FROM → WHERE → SELECT → ORDER BY, regardless of how the query is written.

## How It's Best Learned
Use a sandbox database (SQLite or PostgreSQL with sample data) to run queries immediately. Start with single-table queries, add WHERE filters, then ORDER BY and LIMIT. Practice writing queries from English-language descriptions before seeing the answer.

## Common Misconceptions
- SELECT * retrieves all columns on every call — in production systems this is a performance and security concern.
- WHERE filters happen before SELECT projections in the logical query order, even though SELECT is written first in the syntax.
- SQL is case-insensitive for keywords but case-sensitive for string comparisons on most databases.
