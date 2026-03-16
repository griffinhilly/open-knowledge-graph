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
status: draft
---

# SQL: Sorting, Limiting, and Pagination

## Core Idea
ORDER BY sorts result sets by one or more columns in ascending (ASC) or descending (DESC) order. LIMIT and OFFSET enable pagination for large result sets, essential for user interfaces and API responses. These clauses control the presentation of query results.

## How It's Best Learned
Practice sorting by multiple columns with different directions, and use LIMIT/OFFSET to implement pagination. Understand how databases optimize ordering when indexes exist.

## Explainer

SQL result sets are, by default, unordered — the database returns rows in whatever sequence is most convenient internally (often insertion order or index traversal order, but never guaranteed). **ORDER BY** gives you explicit control over the output sequence. You specify one or more columns and a direction for each: `ORDER BY salary DESC` sorts from highest to lowest salary, while `ORDER BY last_name ASC, first_name ASC` sorts alphabetically by last name, breaking ties with first name. ASC (ascending) is the default if you omit the direction. Conceptually, ORDER BY is applied after all filtering and grouping — it shapes the final presentation of results, not what rows are included.

**LIMIT** restricts how many rows the query returns. `SELECT * FROM products ORDER BY price DESC LIMIT 10` gives you the 10 most expensive products. This is essential for performance and usability: if a table has millions of rows, returning all of them to an application or user interface is wasteful. LIMIT lets you take just the top N results you need. Combined with ORDER BY, it becomes a powerful pattern for "top-N" queries — the highest, lowest, most recent, or least common entries in a dataset.

**OFFSET** skips a specified number of rows before returning results, enabling **pagination**. `LIMIT 10 OFFSET 20` skips the first 20 rows and returns rows 21 through 30. A web application displaying 10 products per page uses OFFSET 0 for page 1, OFFSET 10 for page 2, and OFFSET 20 for page 3. However, OFFSET-based pagination has a hidden cost: the database still reads and discards all the skipped rows internally. For page 1,000 with 10 rows per page, the database processes 10,000 rows to return 10. On large datasets, this gets progressively slower with deeper pages — a limitation worth knowing about even at this stage, because you will encounter more efficient pagination strategies (like keyset pagination) later.

The logical order of SQL clause execution matters here: FROM and JOIN identify the source tables, WHERE filters rows, GROUP BY aggregates, HAVING filters groups, SELECT chooses columns, ORDER BY sorts, and finally LIMIT/OFFSET trims the output. ORDER BY operates on the nearly-final result, and LIMIT operates last. This means you can ORDER BY a column that is not in your SELECT list (in most databases), and LIMIT always applies after sorting, guaranteeing you get the correct top-N results rather than an arbitrary subset.
