---
id: query-execution-plans
title: Query Execution Plans
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: relational-algebra
  type: soft
- id: indexing-concepts
  type: soft
- id: sql-aggregation
  type: soft
- id: sql-joins
  type: soft
- id: sql-subqueries
  type: soft
builds-toward:
- query-optimization
tags:
- query plan
- EXPLAIN
- execution plan
- operator tree
- join algorithms
- seq scan
stage: formal-systems
status: validated
---
# Query Execution Plans

## Core Idea
A query execution plan is the step-by-step strategy a database engine uses to retrieve data, represented as a tree of physical operators such as sequential scan, index scan, hash join, nested loop join, merge join, and sort. The query planner generates this plan using statistics about table sizes, column cardinalities, and available indexes, choosing the estimated lowest-cost option. Reading execution plans via EXPLAIN (estimated) and EXPLAIN ANALYZE (actual) reveals bottlenecks such as missing indexes, bad cardinality estimates, or expensive sorts.

## How It's Best Learned
Run EXPLAIN ANALYZE on real queries and learn to read the operator tree top-down. Identify the most expensive node and hypothesize whether an index, a rewrite, or updated statistics could eliminate it.

## Common Misconceptions
- EXPLAIN without ANALYZE shows only the estimated plan; actual row counts and times may differ substantially.
- A sequential scan is not always bad — for small tables or queries returning most rows, it outperforms an index scan.
- The database cannot always use an index even if one exists; function wrappers on indexed columns (e.g., LOWER(name) = 'foo') disable index use.

## Questions

```yaml
- question: "EXPLAIN ANALYZE on a query shows that a particular join node estimated 10 rows but actually processed 100,000. What does this large divergence most likely indicate?"
  type: multiple-choice
  options:
    - "The query contains a syntax error that caused incorrect results"
    - "The index on the joined column is missing and needs to be created"
    - "The planner used stale or inaccurate table statistics, causing it to choose a poor strategy based on bad cardinality estimates"
    - "The server ran out of memory and had to fall back to a slower execution method"
  answer: 2
  explanation: "When estimated and actual row counts diverge dramatically, the planner made its strategy decision based on inaccurate information — typically stale table statistics. The planner thought the join would produce 10 rows (perhaps because statistics haven't been updated after a large data load), so it chose a join method optimized for small output. In reality, 100,000 rows were produced, making that strategy expensive. The fix is usually ANALYZE (to refresh statistics) or query restructuring to help the planner understand selectivity. A missing index is a separate problem that wouldn't typically cause this specific symptom."

- question: "When is a sequential scan preferred over an index scan by the query planner?"
  type: multiple-choice
  options:
    - "Never — index scans are always faster than sequential scans because they skip irrelevant rows"
    - "Only when the table has no index defined on the queried column"
    - "When the query retrieves a large proportion of the table's rows, making the index traversal overhead exceed the cost of reading all pages sequentially"
    - "Only for tables smaller than 100 rows, regardless of query selectivity"
  answer: 2
  explanation: "A sequential scan reads pages in order from disk, with no overhead per row. An index scan must traverse the index tree, follow pointers to data pages, and potentially jump around disk non-sequentially — each pointer follow has a cost. When a query returns 80% of a table's rows, the index overhead on every single returned row outweighs the benefit of skipping the 20% that don't match. The planner computes an estimated cost for each approach and chooses the lower one. A sequential scan on a small or widely-scanned table is correct behavior — not a bug to be fixed."

- question: "Using a function wrapper on an indexed column — such as LOWER(email) = 'user@example.com' instead of email = 'USER@EXAMPLE.COM' — can prevent the database from using an index on that column."
  type: true-false
  answer: true
  explanation: "True. Most indexes store the raw column values. When you wrap the column in a function like LOWER(), the database cannot use the index on the raw values to answer LOWER(email) = 'user@example.com' — it would have to apply LOWER() to every row and compare. The solution is either to rewrite the query (store emails lowercase, compare lowercase) or to create a functional index specifically on LOWER(email). This is a common pitfall: an index exists, a query seems to match, but the planner correctly ignores the index because the function wrapper makes it unusable."

- question: "EXPLAIN (without ANALYZE) shows the actual execution time and row counts for a query by running it in a read-only mode."
  type: true-false
  answer: false
  explanation: "False. EXPLAIN alone shows only the estimated execution plan — the planner's prediction of what it will do and how much it will cost, without actually executing the query. EXPLAIN ANALYZE is required to see actual execution times and actual row counts, because it runs the query for real. The distinction matters enormously in practice: estimated rows can differ from actual rows by orders of magnitude, and you cannot diagnose cardinality misestimates from EXPLAIN alone. Always use EXPLAIN ANALYZE when debugging performance (but be aware it runs the query, so avoid on destructive statements without wrapping in a transaction)."

- question: "What is the query execution plan tree, and what does the flow of data from leaves to root mean in terms of how the database retrieves your results?"
  type: short-answer
  answer: "The execution plan is a tree of physical operators. At the leaves are data-access methods — sequential scans and index scans that read rows from tables. Each node processes the rows passed up from its children: a join node receives rows from two children (one per table) and combines them; a sort node receives rows and reorders them; a filter node discards rows that don't match a condition. Data flows upward through the tree, with each node transforming the stream it receives, until the root node produces the final result set returned to the client."
  explanation: "Reading plans top-down (or bottom-up) teaches you where the work actually happens. The most expensive node — identified by its cost estimate or actual time in EXPLAIN ANALYZE — is where optimization should focus. If a sequential scan deep in the tree processes millions of rows that are immediately filtered out higher up, that's where an index could help: move the filtering earlier (lower in the tree) so fewer rows travel up. Understanding the tree structure turns query optimization from guesswork into systematic diagnosis."
```

## Explainer

When you write a SQL query, you describe *what* data you want — but not *how* the database should retrieve it. The **query execution plan** is the database's answer to that "how" question. Think of it like a GPS route: you specify the destination, and the planner picks a route based on current conditions. The planner considers table sizes, available indexes, column statistics, and join methods to produce a tree of physical operations that it estimates will be cheapest to execute. You already know from your work with SELECT, joins, and aggregation what these queries ask for; execution plans reveal the machinery underneath.

The plan is structured as a **tree of operators**. At the leaves are data-access methods: a **sequential scan** reads every row in a table (like flipping through an entire phone book), while an **index scan** uses an index to jump directly to matching rows (like using the alphabetical tabs). Above the leaves sit join operators — **nested loop join** iterates through one table and probes the other for each row, **hash join** builds a hash table from one side and probes it with the other, and **merge join** walks two pre-sorted inputs in tandem. Sort, aggregate, and filter operators appear higher in the tree. Each node passes rows upward to its parent until the root produces the final result.

The key tool for reading plans is **EXPLAIN**, which shows the estimated plan without running the query, and **EXPLAIN ANALYZE**, which actually executes the query and reports real row counts and timings alongside the estimates. The most important numbers to compare are the estimated versus actual row counts at each node. When these diverge dramatically — say the planner expected 10 rows but got 100,000 — it means the planner chose its strategy based on bad information, and you have found your bottleneck. This commonly happens when table statistics are stale (fix with ANALYZE) or when the planner cannot estimate selectivity for complex expressions.

Reading plans is a diagnostic skill, not a memorization exercise. Start at the most expensive node — the one consuming the most time or processing the most rows — and ask: could an index eliminate this sequential scan? Could rewriting the query avoid this sort? Could updated statistics fix this cardinality misestimate? Remember that a sequential scan on a small table is perfectly fine; the goal is not to eliminate all sequential scans but to ensure the planner is making informed choices. Over time, reading execution plans becomes the primary way you bridge the gap between writing correct SQL and writing *fast* SQL.
