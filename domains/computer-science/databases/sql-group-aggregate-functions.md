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

## Questions

```yaml
- question: "You want to find all departments that have more than 5 employees. Which query is correct?"
  type: multiple-choice
  options:
    - "SELECT department_id FROM employees WHERE COUNT(*) > 5 GROUP BY department_id"
    - "SELECT department_id FROM employees GROUP BY department_id WHERE COUNT(*) > 5"
    - "SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(*) > 5"
    - "SELECT department_id, COUNT(*) FROM employees WHERE department_id > 5"
  answer: 2
  explanation: "HAVING is the correct clause for filtering on aggregated results. WHERE filters individual rows *before* grouping occurs, so aggregate functions like COUNT(*) are not yet available in the WHERE clause — option A produces an error. Option B has invalid SQL syntax (WHERE cannot follow GROUP BY). Option D filters on department_id values rather than employee counts. HAVING runs after GROUP BY and aggregation, making it the correct place for conditions on COUNT, SUM, AVG, etc."

- question: "A salary table has 100 rows, but 10 rows have NULL in the salary column. What does SELECT AVG(salary) return?"
  type: multiple-choice
  options:
    - "The sum of all salaries divided by 100, treating NULLs as 0"
    - "The sum of non-NULL salaries divided by 90, ignoring the NULL rows"
    - "NULL — because any NULL in the data makes the aggregate undefined"
    - "An error — AVG cannot be computed when NULLs are present"
  answer: 1
  explanation: "All aggregate functions (SUM, AVG, MIN, MAX) ignore NULL values. AVG(salary) sums the 90 non-NULL salaries and divides by 90 — not 100. This is a common source of reporting bugs: if the NULL salaries were actually 0, AVG would give the wrong result because NULLs aren't treated as 0. Note that COUNT(*) counts all rows including NULLs, while COUNT(salary) would return 90 — the distinction between COUNT(*) and COUNT(column) is precisely this NULL handling behavior."

- question: "The HAVING clause filters rows before they are grouped, while WHERE filters groups after aggregation."
  type: true-false
  answer: false
  explanation: "This reverses the actual behavior. WHERE filters individual rows *before* grouping; HAVING filters groups *after* aggregation. The logical execution order is: WHERE → GROUP BY → aggregation → HAVING. This is why aggregate functions (COUNT, SUM, etc.) cannot appear in a WHERE clause — the aggregation hasn't happened yet at that stage. HAVING exists specifically to filter on aggregated results."

- question: "In a query using GROUP BY, every column in the SELECT clause that is not inside an aggregate function must appear in the GROUP BY clause."
  type: true-false
  answer: true
  explanation: "When GROUP BY collapses many rows into one group row, the database needs a single value to display for each non-aggregated column. The only columns guaranteed to have a single value per group are those that define the group (i.e., those in GROUP BY). Aggregate functions produce a single value per group by design. Any other column could have multiple different values within a group, making it ambiguous which to display — so SQL forbids it."

- question: "A query uses WHERE COUNT(*) > 5 and returns an error. Explain why this fails and write the correct approach."
  type: short-answer
  answer: "WHERE cannot use aggregate functions because WHERE executes before grouping — at the WHERE stage, rows haven't been grouped yet, so COUNT(*) has no groups to count. The fix is to move the condition to HAVING, which executes after GROUP BY and aggregation: SELECT department_id, COUNT(*) FROM employees GROUP BY department_id HAVING COUNT(*) > 5. WHERE filters individual rows; HAVING filters aggregated groups."
  explanation: "Understanding SQL's logical order of operations is essential for aggregate queries. The conceptual execution order is: FROM → WHERE → GROUP BY → aggregate functions → HAVING → SELECT → ORDER BY. Aggregate functions are only available from the GROUP BY step onward. WHERE cannot reference COUNT(*) because it runs before any counting has occurred. HAVING was introduced specifically to allow post-aggregation filtering, making the distinction between WHERE and HAVING not just syntactic but logically meaningful."
```

## Explainer

You know how to retrieve rows from a table with SELECT. But often you do not want individual rows — you want a summary. How many orders did we receive last month? What is the average salary by department? What was the highest temperature recorded this year? **Aggregate functions** collapse many rows into a single computed value. The five standard aggregates — COUNT, SUM, AVG, MIN, and MAX — cover the most common summarization needs.

Without GROUP BY, an aggregate operates on the entire result set and returns exactly one row. `SELECT COUNT(*) FROM orders` returns the total number of orders. `SELECT AVG(salary) FROM employees` returns the average salary across all employees. The key mental shift is that you are no longer thinking row-by-row — you are thinking about the *collection* as a whole. Each aggregate function takes a column (or expression) as input, processes every qualifying row, and produces a single output value.

**GROUP BY** is what makes aggregation truly powerful. It partitions rows into groups based on one or more columns, and then the aggregate function runs independently within each group. `SELECT department_id, AVG(salary) FROM employees GROUP BY department_id` produces one row per department, each showing that department's average salary. The rule is strict: every column in your SELECT must either appear in the GROUP BY clause or be inside an aggregate function. If you ask for `department_id` and `AVG(salary)`, the database needs to know that `department_id` identifies the group — otherwise it would not know which department to associate with which average.

When you need to filter on aggregated results, you use **HAVING** instead of WHERE. WHERE filters rows *before* grouping; HAVING filters groups *after* aggregation. For example, `SELECT department_id, COUNT(*) AS headcount FROM employees GROUP BY department_id HAVING COUNT(*) > 10` returns only departments with more than 10 employees. A common mistake is putting aggregate conditions in the WHERE clause — this fails because WHERE operates on individual rows before any grouping has occurred, so aggregate functions are not yet available.

One subtlety worth noting is how NULLs interact with aggregates. COUNT(*) counts all rows including those with NULLs, but COUNT(column_name) skips rows where that column is NULL. SUM, AVG, MIN, and MAX all ignore NULLs. This means AVG(salary) computes the average over non-NULL salaries only — it does not treat NULLs as zero. Understanding this behavior prevents subtle bugs in reports where missing data could silently skew your summaries.
