---
id: sql-ranking-functions-row-number
title: 'Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
- id: sql-lag-lead-offset-functions
  type: soft
- id: sql-coalesce-nullif-functions
  type: soft
builds-toward:
- sql-lag-lead-offset-functions
tags:
- sql
- ranking
- window-functions
stage: formal-systems
status: validated
---
# Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK

## Core Idea
ROW_NUMBER assigns unique sequential integers regardless of ties, RANK assigns the same number to tied rows and skips ranks, and DENSE_RANK also handles ties but does not skip ranks. Each serves different ranking semantics.

## How It's Best Learned
Create a query with tied values and apply each function to observe the differences, especially in the handling of gaps.

## Common Misconceptions
ROW_NUMBER always produces unique values even for ties; use RANK or DENSE_RANK to handle ties correctly. The ORDER BY in the OVER clause determines rank order.

## Questions

```yaml
- question: "Four students take an exam: Alice scores 95, Bob scores 92, Carol scores 92, Dave scores 88. Using DENSE_RANK() ORDER BY score DESC, what ranks are assigned?"
  type: multiple-choice
  options:
    - "Alice=1, Bob=2, Carol=3, Dave=4"
    - "Alice=1, Bob=2, Carol=2, Dave=4"
    - "Alice=1, Bob=2, Carol=2, Dave=3"
    - "Alice=1, Bob=3, Carol=3, Dave=4"
  answer: 2
  explanation: "DENSE_RANK assigns equal ranks to tied values and does NOT skip subsequent ranks. Bob and Carol both score 92, so they both receive rank 2. Dave receives rank 3 — the next consecutive rank — not rank 4. Option B (answer index 1) describes RANK behavior, which skips rank 3 because two people share rank 2. Option A describes ROW_NUMBER, which assigns unique integers ignoring ties. DENSE_RANK's defining feature is consecutive rank values regardless of ties."

- question: "You want to deduplicate a customer table by keeping exactly one row per customer — the most recently updated record. Which ranking function is most appropriate and why?"
  type: multiple-choice
  options:
    - "RANK(), because it handles ties by assigning the same rank to duplicates"
    - "DENSE_RANK(), because it produces consecutive integers that make filtering easy"
    - "ROW_NUMBER(), because it guarantees exactly one row receives rank 1 per partition"
    - "Any of the three work equally well for this use case"
  answer: 2
  explanation: "ROW_NUMBER is the right choice here because deduplication requires exactly one row to receive rank 1 per customer — even if two rows have identical updated_at timestamps. ROW_NUMBER always assigns unique sequential integers, so exactly one row per PARTITION BY group gets row number 1. RANK and DENSE_RANK would assign the same rank to tied updated_at values, meaning filtering WHERE rank = 1 could return multiple rows per customer. When you need 'pick exactly one,' ROW_NUMBER is the only safe choice."

- question: "When two rows have identical values in the ORDER BY clause, both RANK and DENSE_RANK will assign them the same rank number."
  type: true-false
  answer: true
  explanation: "Both RANK and DENSE_RANK respect ties by assigning equal rank values to rows that are equal in the ORDER BY expression. This is what distinguishes them from ROW_NUMBER, which always assigns unique integers even to tied rows. The difference between RANK and DENSE_RANK is not in how they handle the tied rows themselves, but in what rank number they assign to the row immediately after the tie: RANK skips ranks, DENSE_RANK does not."

- question: "Adding a PARTITION BY clause to a ranking window function causes all rows in the entire query result to share a single global rank sequence."
  type: true-false
  answer: false
  explanation: "PARTITION BY causes the ranking function to restart independently for each partition — the opposite of sharing a global sequence. For example, RANK() OVER (PARTITION BY department ORDER BY salary DESC) restarts at rank 1 for each department. Without PARTITION BY, the ranking operates across all rows as a single group. PARTITION BY is precisely the mechanism for computing rankings within groups rather than globally."

- question: "What is the practical difference between RANK and DENSE_RANK, and in what scenario would each be the more appropriate choice?"
  type: short-answer
  answer: "RANK skips rank numbers after ties (two people tie for 2nd, next is 4th); DENSE_RANK does not skip (two people tie for 2nd, next is 3rd). Use RANK when you want to match real-world ranking conventions where tied positions consume slots (sports standings, competition results). Use DENSE_RANK when you want to count distinct performance tiers — the DENSE_RANK value tells you how many distinct rank levels exist above the current row."
  explanation: "The key is what the rank number communicates. RANK's gaps convey 'n people ranked above you' — it answers 'what position are you in?' DENSE_RANK's consecutive values convey 'n distinct levels above you' — it answers 'how many tiers are you from the top?' Neither is universally better; the choice depends on the semantic meaning of 'rank' required by your use case."
```

## Explainer

From your introduction to window functions, you know that they compute values across a set of rows related to the current row without collapsing the result set like GROUP BY does. Ranking functions are the most commonly used window functions, and understanding the differences between the three — ROW_NUMBER, RANK, and DENSE_RANK — comes down to one question: how should ties be handled?

Imagine a table of exam scores: Alice scored 95, Bob scored 92, Carol scored 92, and Dave scored 88. **ROW_NUMBER** assigns a unique sequential integer to each row, ignoring ties entirely. With `ROW_NUMBER() OVER (ORDER BY score DESC)`, you get Alice=1, Bob=2, Carol=3, Dave=4 — or Alice=1, Carol=2, Bob=3, Dave=4. The order between Bob and Carol is arbitrary because they're tied, and the database makes no guarantee about which comes first. ROW_NUMBER is useful when you need exactly one number per row (pagination, deduplication) and don't care about tie semantics.

**RANK** respects ties by assigning the same rank to tied values, then skipping the next rank(s). Using `RANK() OVER (ORDER BY score DESC)`, Alice=1, Bob=2, Carol=2, Dave=4. Notice that rank 3 is skipped because two people share rank 2. This matches how sports rankings work — if two athletes tie for second place, the next finisher is fourth, not third. **DENSE_RANK** also assigns equal ranks to ties but does not skip: Alice=1, Bob=2, Carol=2, Dave=3. Dense ranking is useful when you want to know how many distinct rank levels exist (there are 3 distinct score tiers in this example, not 4).

All three functions require an `ORDER BY` clause inside the `OVER()` specification — this is what defines the ranking order. You can also add **PARTITION BY** to rank within groups independently. For example, `RANK() OVER (PARTITION BY department ORDER BY salary DESC)` ranks employees within each department separately, restarting the rank numbering for each group. A powerful pattern is using ROW_NUMBER for deduplication: if you have duplicate records and want to keep only the most recent, you can assign `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC)` and then filter to rows where the row number equals 1. This selects exactly one row per customer — the most recently updated one.
