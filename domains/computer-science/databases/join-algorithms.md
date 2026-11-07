---
id: join-algorithms
title: "Join Algorithms: Nested-Loop, Sort-Merge, and Hash Join"
domain: computer-science
course: databases
prerequisites:
- id: sql-joins
  type: hard
- id: relational-algebra
  type: hard
- id: physical-storage-pages-records
  type: hard
- id: hash-indexes
  type: soft
- id: merge-sort
  type: soft
builds-toward:
- query-optimization
tags:
- query-processing
- joins
- nested-loop-join
- hash-join
- sort-merge-join
- cost-model
stage: formal-systems
status: validated
---
# Join Algorithms: Nested-Loop, Sort-Merge, and Hash Join

## Core Idea
A database can compute the same join in several physical ways, and their costs differ by orders of magnitude. Nested-loop joins compare each tuple of one input with the tuples of the other and work for any join condition. Sort-merge join sorts both inputs on the join attribute and merges them in one pass. Hash join partitions both inputs with a hash function so that matching tuples land in the same partition, then joins each partition in memory. The query optimizer estimates disk I/O for each method and chooses the cheapest for the query at hand.

## How It's Best Learned
Use one running example with known sizes in blocks and tuples, and compute the block transfers for each algorithm by hand, following the cost formulas in Silberschatz, Korth and Sudarshan's chapter on query processing. Run `EXPLAIN` on a real database to see which join method the optimizer picks, then add or drop an index and watch the plan change. Emphasize which methods need an equality condition and which can handle any predicate.

## Common Misconceptions
- A join is always computed by comparing every pair of rows. (That is only the naive nested-loop method; indexes, sorting and hashing avoid most comparisons for equi-joins.)
- Hash join requires both tables to fit in memory. (Hash join first partitions both inputs to disk so that each partition of the smaller input fits in memory.)
- The choice of outer and inner relation does not matter. (In nested-loop joins, the cost depends on which input is outer; making the smaller relation outer usually lowers the I/O.)

## Questions

```yaml
- question: "A query joins r and s on the condition r.start_date < s.end_date. Which join algorithm can be applied directly to this condition?"
  type: multiple-choice
  options:
    - "Hash join"
    - "Block nested-loop join"
    - "Sort-merge join on start_date = end_date"
    - "None; databases cannot evaluate non-equality joins"
  answer: 1
  explanation: "Nested-loop joins test the join predicate on each pair of tuples, so they work for any condition. Hash join relies on equal keys hashing to the same partition, so it supports only equality (equi-) joins. The standard sort-merge join is also designed for equality conditions."

- question: "Relation r occupies 100 blocks and relation s occupies 1,000 blocks. Using block nested-loop join with r as the outer relation and, in the worst case, only one buffer block for each relation, how many block transfers are needed?"
  type: multiple-choice
  options:
    - "1,100"
    - "100,100"
    - "101,000"
    - "1,000,000"
  answer: 1
  explanation: "For each block of the outer relation r, the whole inner relation s is scanned: 100 x 1,000 = 100,000 transfers, plus 100 to read r once, for 100,100. With s as the outer relation it would be 1,000 x 100 + 1,000 = 101,000, which is why the smaller relation is usually chosen as outer."

- question: "Hash join can be used only when the smaller of the two relations fits entirely in main memory."
  type: true-false
  answer: false
  explanation: "When the build relation is too large, hash join first partitions both relations on disk using the same hash function on the join attribute. Matching tuples fall into matching partitions, and only one partition of the build relation must fit in memory at a time. If partitions are still too big, they can be partitioned again recursively."

- question: "Name one situation in which sort-merge join is an especially good choice compared with hash join."
  type: short-answer
  answer: "When one or both inputs are already sorted on the join attribute, for example because they are read through a clustered B+-tree index or come from an earlier sort, so the sorting step is free or cheap; or when the query's output must be sorted on the join attribute anyway, such as with an ORDER BY on that column."
  explanation: "Sort-merge join's main cost is sorting. If sorting is already done or is needed for later steps, the merge pass costs only one read of each input, and the sorted output can be reused."
```

## Explainer

SQL lets you say which rows you want joined. It does not say how to find them. That choice belongs to the database, and it matters, because tables are stored in disk blocks and reading blocks dominates the cost. Textbooks therefore count **block transfers**. Write b_r and b_s for the number of blocks in relations r and s, and n_r for the number of tuples in r.

The simplest method is the **nested-loop join**. For each tuple of the outer relation r, scan all of s and test the join condition on each pair. It works for any condition, even `r.a < s.b`, but in the worst case it reads s once per tuple of r: n_r x b_s + b_r transfers. The **block nested-loop join** improves this by reading s once per block of r instead: b_r x b_s + b_r in the worst case. With more memory, it holds several blocks of r at a time and scans s fewer times. If s has an index on the join attribute, an **indexed nested-loop join** replaces each scan of s with an index lookup, which is very effective when r is small.

For equality joins, two smarter methods avoid comparing most pairs. **Sort-merge join** sorts both relations on the join attribute, using external sorting if needed. It then walks through both sorted lists together, like merging in merge sort, and outputs matching groups. After sorting, the merge reads each relation once, b_r + b_s transfers. If the inputs are already sorted, for example through a clustered index, the method is very cheap.

**Hash join** uses a hash function h on the join attribute. In the partition phase, it reads both relations and writes each tuple into one of several partitions according to h. Tuples with equal keys always land in partitions with the same number. In the build-and-probe phase, it loads one partition of the smaller relation, the build input, into an in-memory hash table. It then reads the matching partition of the other relation and probes the table for each tuple. Ignoring partially filled blocks, this costs about 3(b_r + b_s) transfers: read both, write partitions, read partitions again.

No method wins every time. Nested loops handle any predicate and are good for small inputs. Index joins win when one side is small and the other is indexed. Hash join is often best for large unsorted equi-joins. Sort-merge shines when sorted order is already available. The query optimizer estimates sizes and picks the cheapest plan.
