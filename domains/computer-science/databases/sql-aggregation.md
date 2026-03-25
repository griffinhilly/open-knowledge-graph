---
id: sql-aggregation
title: SQL Aggregation and GROUP BY
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-subqueries
- query-optimization
tags:
- SQL
- GROUP BY
- HAVING
- COUNT
- SUM
- AVG
- aggregate functions
stage: formal-systems
status: validated
---

# SQL Aggregation and GROUP BY

## Core Idea
Aggregate functions (COUNT, SUM, AVG, MIN, MAX) compute summary statistics over groups of rows rather than returning individual rows. GROUP BY partitions the result set into groups by one or more columns before applying aggregation, so SUM(amount) GROUP BY region yields a total per region rather than a grand total. HAVING filters groups after aggregation, analogous to how WHERE filters individual rows before aggregation; HAVING is necessary for conditions referencing aggregate results like HAVING COUNT(*) > 10.

## How It's Best Learned
Build up from COUNT(*) over all rows, then group by a categorical column, then add HAVING. Practice distinguishing whether a filter belongs in WHERE (before grouping) vs. HAVING (after grouping) by asking: 'does this condition apply to individual rows or to the group?'

## Common Misconceptions
- Every column in SELECT must either appear in GROUP BY or be wrapped in an aggregate function — omitting this causes an error or undefined behavior.
- COUNT(*) counts all rows including NULLs; COUNT(column) skips NULL values in that column.
- HAVING and WHERE are often confused: WHERE filters before grouping, HAVING filters the resulting groups.

## Questions

```yaml
- question: "A database has an 'orders' table with columns customer_id, order_date, and amount. You want to show only customers who have placed more than 5 orders total. Where does this filter belong?"
  type: multiple-choice
  options:
    - "In a WHERE clause: WHERE COUNT(order_id) > 5"
    - "In a HAVING clause: HAVING COUNT(*) > 5, after GROUP BY customer_id"
    - "In a WHERE clause: WHERE order_count > 5, since WHERE runs after aggregation"
    - "Either WHERE or HAVING work — they filter at different stages but produce identical results"
  answer: 1
  explanation: "The count of orders per customer is an aggregate value — it doesn't exist until after GROUP BY groups the rows. HAVING is specifically designed to filter on aggregate results after grouping. WHERE cannot reference COUNT(*) because WHERE runs before grouping, when the per-customer count hasn't been computed yet. Option A would cause an error. Option C is wrong about when WHERE runs (it runs before aggregation). This WHERE/HAVING distinction is the central skill in aggregation."

- question: "Consider: SELECT region, sales_rep, SUM(amount) FROM sales GROUP BY region. What is wrong with this query?"
  type: multiple-choice
  options:
    - "SUM(amount) is wrong — you should use AVG(amount) when grouping by region"
    - "Nothing — this is a valid query that groups by region and shows each sales rep's contribution"
    - "sales_rep appears in SELECT but not in GROUP BY and is not aggregated — this is a SQL error"
    - "You need a HAVING clause whenever you use GROUP BY"
  answer: 2
  explanation: "Every column in SELECT must either appear in GROUP BY or be wrapped in an aggregate function. When rows are grouped by region, multiple rows (with different sales_rep values) collapse into one output row per region. SQL cannot know which single sales_rep value to display alongside the regional SUM — so most SQL engines raise an error (or return an arbitrary/undefined value). The fix is to either add sales_rep to GROUP BY or remove it from SELECT."

- question: "The HAVING clause is evaluated after grouping is complete, which is why it can reference aggregate functions like SUM() and COUNT()."
  type: true-false
  answer: true
  explanation: "Execution order matters here: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. HAVING operates on the grouped result set, after each group has been formed and its aggregates computed. This is why HAVING SUM(amount) > 10000 works — by the time HAVING is evaluated, SUM(amount) exists as a value per group. WHERE, evaluated earlier, operates on individual rows before any grouping occurs."

- question: "COUNT(*) and COUNT(column_name) always return the same result when applied to the same table."
  type: true-false
  answer: false
  explanation: "COUNT(*) counts all rows in the group, including rows where any column has NULL values. COUNT(column_name) counts only rows where that specific column is NOT NULL. If any rows have a NULL in the counted column, COUNT(column_name) < COUNT(*). This distinction is important when dealing with optional fields — for example, COUNT(*) might count all customers while COUNT(phone_number) counts only those with a phone number on record."

- question: "Explain why the distinction between WHERE and HAVING depends on *when* each clause is evaluated in query execution, and give an example of a filter that belongs in each."
  type: short-answer
  answer: "WHERE is evaluated before GROUP BY — it filters individual rows that enter the grouping process. HAVING is evaluated after GROUP BY — it filters the resulting groups based on their aggregate values. A WHERE filter applies to raw row data (e.g., WHERE order_date >= '2024-01-01' to include only 2024 orders before grouping). A HAVING filter applies to computed group statistics (e.g., HAVING SUM(amount) > 10000 to show only high-revenue groups). The diagnostic test: if the condition references an aggregate function, it must be HAVING; if it references a raw column, it can be WHERE."
  explanation: "The timing distinction explains why you cannot write WHERE SUM(amount) > 10000 — the SUM doesn't exist yet when WHERE is evaluated. Understanding execution order (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY) resolves most aggregation query bugs. The practical consequence: using WHERE to pre-filter rows before grouping is also a performance optimization — it reduces the number of rows that need to be grouped."
```

## Explainer

You already know how SELECT retrieves individual rows from a table — filtering with WHERE, choosing columns, ordering results. Aggregation changes the question from "show me the rows" to "summarize the rows." **Aggregate functions** like COUNT, SUM, AVG, MIN, and MAX collapse many rows into a single summary value. Writing `SELECT COUNT(*) FROM orders` gives you one number: the total row count. Writing `SELECT AVG(price) FROM products` gives you one number: the average price across all products. The database reads every qualifying row but returns a single summary instead of the rows themselves.

The real power arrives with **GROUP BY**, which partitions rows into buckets before aggregating. Think of it like sorting a deck of cards by suit and then counting each pile separately. `SELECT region, SUM(amount) FROM sales GROUP BY region` first groups all rows sharing the same region value, then computes SUM(amount) independently within each group. The result has one row per group, not one row per original record. A critical rule follows from this: every column in your SELECT must either appear in the GROUP BY clause or be wrapped in an aggregate function. If you select `region` and `SUM(amount)`, you must group by `region` — otherwise the database cannot know which single region value to display alongside the sum.

The distinction between **WHERE** and **HAVING** is the most commonly confused aspect of aggregation, and it comes down to timing. WHERE filters individual rows *before* grouping happens — it decides which rows enter the groups in the first place. HAVING filters *after* grouping — it decides which completed groups appear in the final result. If you want only orders from 2024 to be included in your sums, that is a WHERE condition: `WHERE order_date >= '2024-01-01'`. If you want to see only regions whose total exceeds $10,000, that is a HAVING condition: `HAVING SUM(amount) > 10000`. The test is simple — ask whether the condition references an aggregate result. If yes, it belongs in HAVING; if it references raw column values, it belongs in WHERE.

One subtlety worth noting: `COUNT(*)` counts all rows in a group, including those with NULL values in any column. `COUNT(column_name)` counts only rows where that specific column is not NULL. This distinction matters when your data has missing values — counting customers versus counting customers who have a phone number on file can yield very different results. Understanding this behavior, combined with the WHERE/HAVING timing distinction, gives you precise control over how groups are formed and filtered.
