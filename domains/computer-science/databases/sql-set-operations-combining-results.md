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
status: validated
---

# SQL: Set Operations (UNION, INTERSECT, EXCEPT)

## Core Idea
Set operations combine results from multiple SELECT statements. UNION concatenates unique rows from both queries. INTERSECT returns only rows appearing in both queries. EXCEPT returns rows in the first query but not the second. These operations implement relational set algebra.

## How It's Best Learned
Practice combining results from different tables and queries with different set operations. Understand the difference between UNION (unique rows) and UNION ALL (all rows including duplicates).

## Questions

```yaml
- question: "A company has two tables: active_customers and archived_customers. Some customers appear in both (reactivated users). You want a complete list of every unique customer. Which query is correct?"
  type: multiple-choice
  options:
    - "SELECT * FROM active_customers UNION ALL SELECT * FROM archived_customers"
    - "SELECT * FROM active_customers INTERSECT SELECT * FROM archived_customers"
    - "SELECT * FROM active_customers UNION SELECT * FROM archived_customers"
    - "SELECT * FROM active_customers EXCEPT SELECT * FROM archived_customers"
  answer: 2
  explanation: "UNION removes duplicate rows, so reactivated customers who appear in both tables appear only once — giving the correct unique list. UNION ALL (option A) keeps duplicates, potentially showing the same customer twice. INTERSECT (option B) returns only customers who appear in both tables (just the reactivated ones), not the full list. EXCEPT (option D) returns active customers who never appeared in the archive, dropping the reactivated customers entirely."

- question: "Query A returns customer IDs who ordered in January. Query B returns customer IDs who ordered in February. What does 'A EXCEPT B' return?"
  type: multiple-choice
  options:
    - "Customers who ordered in both January and February"
    - "Customers who ordered in January but not in February"
    - "Customers who ordered in February but not in January"
    - "All customers who ordered in either month"
  answer: 1
  explanation: "EXCEPT returns rows from the first query (A) that do not appear in the second (B) — January customers minus those who also ordered in February. Note the asymmetry: B EXCEPT A gives the opposite (February-only customers). INTERSECT (option A) would return both-months customers; UNION (option D) would return all customers who ordered in either month."

- question: "UNION ALL always returns more rows than UNION when applied to the same two queries."
  type: true-false
  answer: false
  explanation: "If the two queries return completely disjoint rows (no overlapping values), UNION and UNION ALL return the same number of rows — there is nothing to deduplicate. UNION ALL returns more rows only when duplicates actually exist. When queries have mutually exclusive WHERE conditions that guarantee disjoint results, UNION ALL is both correct and faster because it skips the deduplication step entirely."

- question: "In a SQL set operation, ORDER BY can be placed inside each individual SELECT statement to control sort order before the rows are combined."
  type: true-false
  answer: false
  explanation: "ORDER BY applies to the final combined result, not to individual queries in a set operation. Placing ORDER BY inside individual SELECT statements within UNION/INTERSECT/EXCEPT is either a syntax error or silently ignored, depending on the database. The correct placement is at the very end of the entire statement, after all queries and set operation keywords. The logical order of operations is: combine result sets first, then sort the final combined output."

- question: "When is it correct to replace UNION with UNION ALL, and what is the benefit?"
  type: short-answer
  answer: "Use UNION ALL when you know the two queries return disjoint rows (no duplicates possible), or when duplicates in the result are acceptable. The benefit is performance: UNION must sort or hash the entire combined result to find and eliminate duplicates — expensive on large datasets. UNION ALL simply concatenates the two result sets without any deduplication work, making it significantly faster. If WHERE clauses are mutually exclusive, UNION ALL is both correct and the more efficient choice."
  explanation: "Deduplication in UNION typically requires an O(n log n) sort or hash over all combined rows. For large tables this can be costly. Developers often reflexively write UNION when UNION ALL would suffice — a common source of unnecessary query slowness. The key is confirming correctness: if duplicates are possible and undesirable (as in the unique-customer scenario), you must use UNION despite the cost. But when you can guarantee disjointness from the query structure, UNION ALL is both safe and faster."
```

## Explainer

You know how to write SELECT queries that pull data from tables. But sometimes the answer you need lives across multiple queries that cannot be combined with a JOIN — perhaps you want a unified list of all customers and all suppliers, or you want to find products that appear in one catalog but not another. **Set operations** let you combine the result sets of two or more SELECT statements using the same logic as mathematical set theory: union, intersection, and difference.

**UNION** stacks the results of two queries vertically and removes duplicate rows. If Query A returns {1, 2, 3} and Query B returns {2, 3, 4}, `A UNION B` returns {1, 2, 3, 4}. This is useful when you need a combined list from structurally similar but separate sources — for instance, merging active and archived orders into one timeline. **UNION ALL** does the same stacking but keeps all duplicates. It is faster because the database skips the deduplication step, and you should prefer it whenever you know there are no duplicates or when duplicates are acceptable.

**INTERSECT** returns only rows that appear in *both* result sets. Using the same example, `A INTERSECT B` returns {2, 3}. This is the overlap — useful for finding, say, customers who placed orders in both January and February. **EXCEPT** (called MINUS in some databases) returns rows from the first query that do *not* appear in the second. `A EXCEPT B` returns {1}. This is the set difference — useful for identifying customers who were active last year but have not placed an order this year.

All set operations require **union compatibility**: the two SELECT statements must produce the same number of columns, and corresponding columns must have compatible data types. The column names in the result come from the first query. If you need to combine queries with different column counts, you can add NULL placeholders or constant values to align them. Ordering applies to the combined result, so place any ORDER BY at the end of the entire statement, not within individual queries.

A practical consideration is performance. UNION, INTERSECT, and EXCEPT all require duplicate elimination, which typically means sorting or hashing the entire result set. For large datasets, this can be expensive. UNION ALL avoids this cost entirely. When writing queries, ask yourself: do I actually need deduplication? If the source queries are guaranteed to return disjoint rows (common when each query has a mutually exclusive WHERE condition), UNION ALL gives the same result as UNION but runs faster.
