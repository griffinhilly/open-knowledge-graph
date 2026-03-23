---
id: sql-sorting-limiting-results
title: 'SQL: Sorting, Limiting, and Pagination'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-inner-join-combining-tables
tags:
- SQL
- ORDER BY
- LIMIT
- pagination
stage: formal-systems
status: validated
---

# SQL: Sorting, Limiting, and Pagination

## Core Idea
ORDER BY sorts result sets by one or more columns in ascending (ASC) or descending (DESC) order. LIMIT and OFFSET enable pagination for large result sets, essential for user interfaces and API responses. These clauses control the presentation of query results.

## How It's Best Learned
Practice sorting by multiple columns with different directions, and use LIMIT/OFFSET to implement pagination. Understand how databases optimize ordering when indexes exist.

## Questions

```yaml
- question: "A developer runs: SELECT department FROM employees ORDER BY salary DESC LIMIT 5. The column 'salary' is not in the SELECT list. What happens?"
  type: multiple-choice
  options:
    - "The query fails because you can only ORDER BY columns that appear in SELECT"
    - "The query succeeds and returns the 5 departments of the highest-paid employees"
    - "The query returns 5 rows but salary values are substituted with NULL"
    - "The query runs but ignores the ORDER BY clause since salary is not selected"
  answer: 1
  explanation: "In most databases, you can ORDER BY a column that does not appear in your SELECT list. ORDER BY operates on the row before projection (column selection), so the engine has access to all columns for sorting purposes. The query correctly returns the 5 departments corresponding to the highest-paid employees. This is a useful pattern for top-N queries where you want to sort by a criterion you don't need to display."

- question: "A web app shows products 10 per page. Page 1 uses OFFSET 0, page 2 uses OFFSET 10, and so on. What is the fundamental performance problem with this approach at page 500?"
  type: multiple-choice
  options:
    - "OFFSET 4990 is a syntax error in SQL"
    - "The database reads and discards 4990 rows internally before returning 10, making deep pages progressively slower"
    - "LIMIT 10 with a large OFFSET returns duplicate rows across pages"
    - "ORDER BY becomes unreliable when combined with large OFFSET values"
  answer: 1
  explanation: "OFFSET-based pagination has a hidden cost: the database must process all the skipped rows before it can return the requested ones. At page 500 with OFFSET 4990, the database reads 5000 rows and discards 4990 of them to give you 10. This cost scales linearly with page depth, making deep pages much slower than shallow ones. More efficient alternatives — keyset pagination, cursor-based pagination — avoid this by using a 'last seen' value as a filter rather than an offset count."

- question: "ORDER BY is applied after WHERE filtering, meaning rows are sorted from the already-filtered result set."
  type: true-false
  answer: true
  explanation: "SQL has a defined logical execution order: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT/OFFSET. ORDER BY operates on the nearly-final result after all filtering and aggregation. This means ORDER BY sees only the rows that passed WHERE conditions, and LIMIT then trims from the sorted output. Understanding this order is essential for reasoning about what ORDER BY can access and what TOP-N queries guarantee."

- question: "Using LIMIT without ORDER BY guarantees you receive the same set of rows each time you run the query."
  type: true-false
  answer: false
  explanation: "Without ORDER BY, SQL result sets are unordered — the database returns rows in whatever sequence is internally convenient, which may vary between runs depending on query planning, caching, concurrency, or physical storage changes. LIMIT without ORDER BY picks an arbitrary subset of that unordered output. If you need deterministic pagination, you must always pair LIMIT with an ORDER BY on a unique or stable column. This is a common source of subtle bugs in applications that assume LIMIT alone produces consistent results."

- question: "Why does OFFSET-based pagination become progressively slower on large datasets, and what does this imply about how it should be used?"
  type: short-answer
  answer: "OFFSET instructs the database to skip N rows before returning results, but the database must still read and process those N rows internally — it cannot jump directly to row N+1 in the general case. At OFFSET 10,000 for a 10-row page, the engine processes 10,010 rows to return 10. Performance degrades linearly with page depth. This means OFFSET pagination is practical for shallow pages but problematic for deep pagination on large tables. For high-page-count use cases, keyset pagination (filtering on a 'last seen' ID or timestamp) is more efficient because it lets the database use an index to jump directly to the right starting point."
  explanation: "The core issue is that OFFSET is a 'skip count' instruction, not a direct pointer. Without a specialized index, the database has no way to know where row N starts without reading rows 1 through N-1 first. Understanding this limitation early prevents building systems that work in development (small data) but break in production (large data)."
```

## Explainer

SQL result sets are, by default, unordered — the database returns rows in whatever sequence is most convenient internally (often insertion order or index traversal order, but never guaranteed). **ORDER BY** gives you explicit control over the output sequence. You specify one or more columns and a direction for each: `ORDER BY salary DESC` sorts from highest to lowest salary, while `ORDER BY last_name ASC, first_name ASC` sorts alphabetically by last name, breaking ties with first name. ASC (ascending) is the default if you omit the direction. Conceptually, ORDER BY is applied after all filtering and grouping — it shapes the final presentation of results, not what rows are included.

**LIMIT** restricts how many rows the query returns. `SELECT * FROM products ORDER BY price DESC LIMIT 10` gives you the 10 most expensive products. This is essential for performance and usability: if a table has millions of rows, returning all of them to an application or user interface is wasteful. LIMIT lets you take just the top N results you need. Combined with ORDER BY, it becomes a powerful pattern for "top-N" queries — the highest, lowest, most recent, or least common entries in a dataset.

**OFFSET** skips a specified number of rows before returning results, enabling **pagination**. `LIMIT 10 OFFSET 20` skips the first 20 rows and returns rows 21 through 30. A web application displaying 10 products per page uses OFFSET 0 for page 1, OFFSET 10 for page 2, and OFFSET 20 for page 3. However, OFFSET-based pagination has a hidden cost: the database still reads and discards all the skipped rows internally. For page 1,000 with 10 rows per page, the database processes 10,000 rows to return 10. On large datasets, this gets progressively slower with deeper pages — a limitation worth knowing about even at this stage, because you will encounter more efficient pagination strategies (like keyset pagination) later.

The logical order of SQL clause execution matters here: FROM and JOIN identify the source tables, WHERE filters rows, GROUP BY aggregates, HAVING filters groups, SELECT chooses columns, ORDER BY sorts, and finally LIMIT/OFFSET trims the output. ORDER BY operates on the nearly-final result, and LIMIT operates last. This means you can ORDER BY a column that is not in your SELECT list (in most databases), and LIMIT always applies after sorting, guaranteeing you get the correct top-N results rather than an arbitrary subset.
