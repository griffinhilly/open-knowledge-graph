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
- id: boolean-logic
  type: soft
- id: relational-algebra
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
status: validated
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

## Questions

```yaml
- question: "In what logical order does a database engine process the clauses of: SELECT name FROM employees WHERE department = 'Sales' ORDER BY name?"
  type: multiple-choice
  options: ["SELECT → FROM → WHERE → ORDER BY", "FROM → SELECT → WHERE → ORDER BY", "FROM → WHERE → SELECT → ORDER BY", "WHERE → FROM → SELECT → ORDER BY"]
  answer: 2
  explanation: "The logical processing order is FROM (identify the table) → WHERE (filter rows) → SELECT (project columns) → ORDER BY (sort results). This is why you cannot reference a SELECT alias in a WHERE clause — WHERE executes before SELECT resolves those aliases. The written syntax with SELECT first is a historical convention that does not reflect actual execution order."

- question: "SQL keywords like SELECT, WHERE, and FROM are case-sensitive and must be written in uppercase to work correctly."
  type: true-false
  answer: false
  explanation: "SQL keywords are case-insensitive — select, SELECT, and Select are all equivalent. The convention of writing keywords in uppercase is a readability standard, not a requirement. However, string values compared in WHERE clauses ARE case-sensitive on most databases (e.g., 'Sales' ≠ 'sales' in PostgreSQL), which is a separate and important distinction."

- question: "Why is SELECT * generally discouraged in production database queries?"
  type: short-answer
  answer: "SELECT * retrieves every column on every execution, which is wasteful when only a few columns are needed. It also breaks when table schemas change (added or reordered columns can shift results in application code), and prevents the database optimizer from using index-only scans that serve queries without touching the main table."
  explanation: "In development and exploration, SELECT * is convenient. In production, explicitly naming columns is better for three reasons: (1) performance — retrieving only needed columns reduces I/O, network transfer, and memory; (2) robustness — schema changes won't silently alter query results; (3) optimizer efficiency — the query planner can use covering indexes that contain exactly the requested columns without a full table access."
```

## Explainer

SQL is a declarative language: you describe the data you want, and the database engine determines how to retrieve it efficiently. SELECT is the heart of this — it lets you specify columns, filter rows, and sort results in a single readable statement. But understanding SQL well means understanding the gap between how a query is *written* and how it is actually *processed*.

The written syntax is SELECT ... FROM ... WHERE ... ORDER BY ..., but the logical execution order nearly reverses this: FROM first identifies the source table, then WHERE filters rows according to boolean conditions, then SELECT projects (picks) only the specified columns, and finally ORDER BY sorts the result set. This matters practically: you cannot reference a column alias defined in SELECT inside a WHERE clause, because WHERE runs before SELECT resolves those aliases. Many beginners write `SELECT salary * 1.1 AS adjusted FROM employees WHERE adjusted > 50000` and are confused when it fails — at the time WHERE runs, "adjusted" doesn't exist yet.

The WHERE clause is where most filtering logic lives. It evaluates a boolean expression for each row, and only rows where the expression is TRUE pass forward. SQL includes useful predicates beyond simple comparison: BETWEEN a AND b tests an inclusive range; IN (val1, val2, ...) checks set membership; LIKE 'pattern%' enables wildcard string matching; and IS NULL correctly handles missing values. Crucially, NULL ≠ NULL in SQL — a comparison like `column = NULL` never returns TRUE, even when the column is null. You must use IS NULL. Boolean operators AND, OR, and NOT compose these predicates into complex filters.

One of the most important habits to build early is naming columns explicitly instead of using SELECT *. In exploration, * is convenient. In any production query or application code, * is risky: schema changes (adding or renaming columns) can silently break downstream logic, and fetching all columns wastes I/O when only a few are needed. Naming your columns also makes queries self-documenting — anyone reading the query can see exactly what fields it depends on.

ORDER BY sorts the final result. Without it, SQL makes no guarantee about row order — the engine returns rows in whatever order suits its execution plan, and that order can change between runs as data and statistics change. If your application depends on a particular ordering, always specify ORDER BY explicitly. LIMIT then restricts the output to the first n rows after sorting, which is the basis for pagination across nearly every web application. Together, ORDER BY and LIMIT are the tools that turn a raw result set into a predictable, manageable slice of data.
