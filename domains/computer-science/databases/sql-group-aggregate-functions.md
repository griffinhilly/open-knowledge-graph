---
id: sql-group-aggregate-functions
title: 'SQL: Aggregation Functions (COUNT, SUM, AVG, MIN, MAX)'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-sorting-limiting-results
tags:
- SQL
- aggregate
- COUNT
- SUM
- AVG
- MIN
- MAX
stage: formal-systems
status: draft
---

# SQL: Aggregation Functions (COUNT, SUM, AVG, MIN, MAX)

## Core Idea
Aggregate functions compute single values from multiple rows: COUNT (number of rows), SUM (total), AVG (average), MIN (minimum), MAX (maximum). Aggregates with GROUP BY enable summarization and statistical analysis of data.

## Explainer

You know how to retrieve rows from a table with SELECT. But often you do not want individual rows — you want a summary. How many orders did we receive last month? What is the average salary by department? What was the highest temperature recorded this year? **Aggregate functions** collapse many rows into a single computed value. The five standard aggregates — COUNT, SUM, AVG, MIN, and MAX — cover the most common summarization needs.

Without GROUP BY, an aggregate operates on the entire result set and returns exactly one row. `SELECT COUNT(*) FROM orders` returns the total number of orders. `SELECT AVG(salary) FROM employees` returns the average salary across all employees. The key mental shift is that you are no longer thinking row-by-row — you are thinking about the *collection* as a whole. Each aggregate function takes a column (or expression) as input, processes every qualifying row, and produces a single output value.

**GROUP BY** is what makes aggregation truly powerful. It partitions rows into groups based on one or more columns, and then the aggregate function runs independently within each group. `SELECT department_id, AVG(salary) FROM employees GROUP BY department_id` produces one row per department, each showing that department's average salary. The rule is strict: every column in your SELECT must either appear in the GROUP BY clause or be inside an aggregate function. If you ask for `department_id` and `AVG(salary)`, the database needs to know that `department_id` identifies the group — otherwise it would not know which department to associate with which average.

When you need to filter on aggregated results, you use **HAVING** instead of WHERE. WHERE filters rows *before* grouping; HAVING filters groups *after* aggregation. For example, `SELECT department_id, COUNT(*) AS headcount FROM employees GROUP BY department_id HAVING COUNT(*) > 10` returns only departments with more than 10 employees. A common mistake is putting aggregate conditions in the WHERE clause — this fails because WHERE operates on individual rows before any grouping has occurred, so aggregate functions are not yet available.

One subtlety worth noting is how NULLs interact with aggregates. COUNT(*) counts all rows including those with NULLs, but COUNT(column_name) skips rows where that column is NULL. SUM, AVG, MIN, and MAX all ignore NULLs. This means AVG(salary) computes the average over non-NULL salaries only — it does not treat NULLs as zero. Understanding this behavior prevents subtle bugs in reports where missing data could silently skew your summaries.
