---
id: sql-set-operations-combining-results
title: 'SQL: Set Operations (UNION, INTERSECT, EXCEPT)'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
tags:
- SQL
- UNION
- INTERSECT
- EXCEPT
- set operations
stage: formal-systems
status: draft
---

# SQL: Set Operations (UNION, INTERSECT, EXCEPT)

## Core Idea
Set operations combine results from multiple SELECT statements. UNION concatenates unique rows from both queries. INTERSECT returns only rows appearing in both queries. EXCEPT returns rows in the first query but not the second. These operations implement relational set algebra.

## How It's Best Learned
Practice combining results from different tables and queries with different set operations. Understand the difference between UNION (unique rows) and UNION ALL (all rows including duplicates).

## Explainer

You know how to write SELECT queries that pull data from tables. But sometimes the answer you need lives across multiple queries that cannot be combined with a JOIN — perhaps you want a unified list of all customers and all suppliers, or you want to find products that appear in one catalog but not another. **Set operations** let you combine the result sets of two or more SELECT statements using the same logic as mathematical set theory: union, intersection, and difference.

**UNION** stacks the results of two queries vertically and removes duplicate rows. If Query A returns {1, 2, 3} and Query B returns {2, 3, 4}, `A UNION B` returns {1, 2, 3, 4}. This is useful when you need a combined list from structurally similar but separate sources — for instance, merging active and archived orders into one timeline. **UNION ALL** does the same stacking but keeps all duplicates. It is faster because the database skips the deduplication step, and you should prefer it whenever you know there are no duplicates or when duplicates are acceptable.

**INTERSECT** returns only rows that appear in *both* result sets. Using the same example, `A INTERSECT B` returns {2, 3}. This is the overlap — useful for finding, say, customers who placed orders in both January and February. **EXCEPT** (called MINUS in some databases) returns rows from the first query that do *not* appear in the second. `A EXCEPT B` returns {1}. This is the set difference — useful for identifying customers who were active last year but have not placed an order this year.

All set operations require **union compatibility**: the two SELECT statements must produce the same number of columns, and corresponding columns must have compatible data types. The column names in the result come from the first query. If you need to combine queries with different column counts, you can add NULL placeholders or constant values to align them. Ordering applies to the combined result, so place any ORDER BY at the end of the entire statement, not within individual queries.

A practical consideration is performance. UNION, INTERSECT, and EXCEPT all require duplicate elimination, which typically means sorting or hashing the entire result set. For large datasets, this can be expensive. UNION ALL avoids this cost entirely. When writing queries, ask yourself: do I actually need deduplication? If the source queries are guaranteed to return disjoint rows (common when each query has a mutually exclusive WHERE condition), UNION ALL gives the same result as UNION but runs faster.
