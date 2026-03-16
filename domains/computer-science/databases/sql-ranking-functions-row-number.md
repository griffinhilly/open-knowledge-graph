---
id: sql-ranking-functions-row-number
title: 'Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
builds-toward:
- sql-lag-lead-offset-functions
tags:
- sql
- ranking
- window-functions
stage: formal-systems
status: draft
---

# Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK

## Core Idea
ROW_NUMBER assigns unique sequential integers regardless of ties, RANK assigns the same number to tied rows and skips ranks, and DENSE_RANK also handles ties but does not skip ranks. Each serves different ranking semantics.

## How It's Best Learned
Create a query with tied values and apply each function to observe the differences, especially in the handling of gaps.

## Common Misconceptions
ROW_NUMBER always produces unique values even for ties; use RANK or DENSE_RANK to handle ties correctly. The ORDER BY in the OVER clause determines rank order.

## Explainer

From your introduction to window functions, you know that they compute values across a set of rows related to the current row without collapsing the result set like GROUP BY does. Ranking functions are the most commonly used window functions, and understanding the differences between the three — ROW_NUMBER, RANK, and DENSE_RANK — comes down to one question: how should ties be handled?

Imagine a table of exam scores: Alice scored 95, Bob scored 92, Carol scored 92, and Dave scored 88. **ROW_NUMBER** assigns a unique sequential integer to each row, ignoring ties entirely. With `ROW_NUMBER() OVER (ORDER BY score DESC)`, you get Alice=1, Bob=2, Carol=3, Dave=4 — or Alice=1, Carol=2, Bob=3, Dave=4. The order between Bob and Carol is arbitrary because they're tied, and the database makes no guarantee about which comes first. ROW_NUMBER is useful when you need exactly one number per row (pagination, deduplication) and don't care about tie semantics.

**RANK** respects ties by assigning the same rank to tied values, then skipping the next rank(s). Using `RANK() OVER (ORDER BY score DESC)`, Alice=1, Bob=2, Carol=2, Dave=4. Notice that rank 3 is skipped because two people share rank 2. This matches how sports rankings work — if two athletes tie for second place, the next finisher is fourth, not third. **DENSE_RANK** also assigns equal ranks to ties but does not skip: Alice=1, Bob=2, Carol=2, Dave=3. Dense ranking is useful when you want to know how many distinct rank levels exist (there are 3 distinct score tiers in this example, not 4).

All three functions require an `ORDER BY` clause inside the `OVER()` specification — this is what defines the ranking order. You can also add **PARTITION BY** to rank within groups independently. For example, `RANK() OVER (PARTITION BY department ORDER BY salary DESC)` ranks employees within each department separately, restarting the rank numbering for each group. A powerful pattern is using ROW_NUMBER for deduplication: if you have duplicate records and want to keep only the most recent, you can assign `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC)` and then filter to rows where the row number equals 1. This selects exactly one row per customer — the most recently updated one.
