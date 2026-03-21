---
id: sql-window-functions-over-partition
title: 'Window Functions: OVER Clause, PARTITION BY, and Frames'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: sql-group-aggregate-functions
  type: hard
builds-toward:
- sql-subqueries
- query-execution-plan-analysis-explain
tags:
- window-functions
- OVER
- PARTITION-BY
- ranking
- frame
stage: formal-systems
status: draft
---

# Window Functions: OVER Clause, PARTITION BY, and Frames

## Core Idea
Window functions compute aggregates or rankings over subsets (windows) of result rows without collapsing rows like GROUP BY does. The OVER clause defines the window using PARTITION BY to divide rows into groups and ORDER BY to specify row order. Frame specifications (ROWS/RANGE BETWEEN) limit which rows contribute. Common functions include ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, and aggregate functions with OVER.

## Questions

```yaml
- question: "You need a query that returns each employee's name, salary, and their department's total salary — all on the same row. Which approach works?"
  type: multiple-choice
  options:
    - "SELECT name, salary, SUM(salary) FROM employees GROUP BY department — the total appears alongside each row"
    - "SELECT name, salary, SUM(salary) OVER (PARTITION BY department) FROM employees — the total is computed per department without collapsing rows"
    - "Use a HAVING clause to attach totals to individual rows after grouping"
    - "This is impossible in a single query — you need a separate query for totals"
  answer: 1
  explanation: "GROUP BY with SUM collapses all rows in each department into one — you cannot simultaneously show individual employee rows and the group total. Window functions solve this: OVER (PARTITION BY department) computes the sum within each department partition but attaches the result as a column on every row without collapsing anything. This is the fundamental distinction between window functions and GROUP BY aggregates: both compute over groups, but only window functions preserve the original rows."

- question: "In a query using RANK() and DENSE_RANK() on the scores 90, 85, 85, 80, what ranks do the two 85s receive under each function?"
  type: multiple-choice
  options:
    - "RANK: both get rank 2, next gets rank 3. DENSE_RANK: both get rank 2, next gets rank 3."
    - "RANK: both get rank 2, next gets rank 4. DENSE_RANK: both get rank 2, next gets rank 3."
    - "RANK: both get rank 2, next gets rank 3. DENSE_RANK: both get rank 2, next gets rank 4."
    - "Both functions assign the same ranks — they differ only in how they handle NULL values."
  answer: 1
  explanation: "RANK() assigns tied rows the same rank but then skips ranks: two rows tied at rank 2 mean the next rank is 4 (ranks 1, 2, 2, 4). DENSE_RANK() also assigns the same rank to ties but does not skip: the sequence is 1, 2, 2, 3. The difference matters when using these for top-N queries — RANK can produce surprising gaps, while DENSE_RANK gives a contiguous ranking. Neither is 'wrong'; the choice depends on what the query semantics require."

- question: "PARTITION BY inside an OVER clause works exactly like GROUP BY — it reduces the number of output rows to one per partition."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about window functions. GROUP BY genuinely collapses rows — one output row per group. PARTITION BY inside OVER divides rows into groups for computation purposes only; every original row remains in the output. A query with SUM(salary) OVER (PARTITION BY dept) on a 1000-row table still returns 1000 rows — each with the department total attached. This non-collapsing behavior is what makes window functions useful: they let you compare individual rows against group-level aggregates without losing the individual-row detail."

- question: "Adding ORDER BY inside an OVER clause (without a frame specification) changes the behavior of aggregate functions like SUM from a full-partition total to a running total."
  type: true-false
  answer: true
  explanation: "When you add ORDER BY to an OVER clause without an explicit frame, most databases default to a frame of RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW — which includes all rows from the start of the partition up to the current row. SUM(amount) OVER (PARTITION BY dept) computes the total for the whole department, attaching the same value to every row. SUM(amount) OVER (PARTITION BY dept ORDER BY date) computes a cumulative sum that grows with each row in date order. This default-frame behavior is subtle and is a common source of bugs when developers forget that ORDER BY inside OVER has semantic effects beyond just sorting."

- question: "Explain why SUM(amount) OVER (PARTITION BY dept ORDER BY date) produces different results from SUM(amount) OVER (PARTITION BY dept), even though both partition by department."
  type: short-answer
  answer: "Adding ORDER BY inside the OVER clause changes the default frame from the entire partition to a running frame (UNBOUNDED PRECEDING to CURRENT ROW). Without ORDER BY, the frame covers all rows in the department partition — every row gets the same total. With ORDER BY, the frame grows row by row in date order — each row gets the sum of all rows up to and including itself within the partition. The result is a cumulative running total that increases as dates advance, rather than a static department-wide total."
  explanation: "The frame specification — whether explicit or implicit — is the subtlest part of window functions. The same SUM function with the same PARTITION BY can produce a full total, a running total, or a sliding average depending solely on the frame. Understanding that ORDER BY inside OVER triggers a default running frame (not just sorting) is essential for writing correct window function queries and for debugging unexpected results."
```

## Explainer

You already know how GROUP BY with aggregate functions like SUM and COUNT collapses rows into summary groups — one output row per group. This is powerful, but it forces a choice: either you see the detail rows or the aggregates, never both. **Window functions** eliminate this tradeoff. They compute aggregates, rankings, or positional lookups across a set of rows related to the current row, but they do not collapse anything. Every detail row stays in the result, and the window function's output appears as an additional column alongside it.

The syntax centers on the **OVER clause**, which defines the "window" — the set of rows the function looks at for each row in the result. `SUM(amount) OVER (PARTITION BY department)` computes the total amount for each department, but instead of collapsing to one row per department, it attaches that total to every row within the department. **PARTITION BY** is like GROUP BY's cousin: it divides rows into groups, but only for the purpose of the window calculation. If you omit PARTITION BY, the window is the entire result set. Adding **ORDER BY** inside the OVER clause sorts rows within each partition, which is essential for ranking functions and running totals: `SUM(amount) OVER (PARTITION BY department ORDER BY hire_date)` gives a cumulative sum that grows as you move through rows in hire-date order.

**Ranking functions** are among the most common window functions. `ROW_NUMBER()` assigns a unique sequential integer to each row within its partition. `RANK()` does the same but assigns the same number to ties, leaving gaps (1, 2, 2, 4). `DENSE_RANK()` assigns the same number to ties without gaps (1, 2, 2, 3). These are invaluable for queries like "find the top 3 salespeople per region" — something that is extremely awkward with GROUP BY alone. **LAG** and **LEAD** let you access values from previous or subsequent rows: `LAG(revenue, 1) OVER (ORDER BY month)` gives you last month's revenue on each row, making period-over-period comparisons trivial.

The **frame specification** gives you even finer control. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` limits the window to a sliding three-row range, enabling moving averages. `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes all rows from the start of the partition up to the current row's value, which is the default for ordered windows and produces running totals. The frame is the most subtle part of window functions, but understanding it unlocks the difference between a running sum, a sliding average, and a full-partition total — all using the same SUM function with different frame boundaries.
