---
id: amortized-analysis
title: Amortized Analysis
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: time-space-complexity
  type: hard
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
builds-toward:
- union-find
- hash-tables
tags:
- amortized
- complexity
- analysis
- aggregate
stage: formal-systems
status: draft
---

# Amortized Analysis

## Core Idea
Amortized analysis determines the average cost per operation over a sequence of operations, even when individual operations vary in cost. The key insight is that expensive operations (like resizing a dynamic array) happen infrequently enough that their cost is spread — amortized — over many cheap operations. Three common methods are aggregate analysis, the accounting method, and the potential method. Dynamic array append is O(1) amortized even though periodic resizing costs O(n).

## How It's Best Learned
Study the dynamic array append operation as the canonical example. Work through both the aggregate method (total cost / n operations) and the accounting method (assign credits to operations) to build intuition for each approach.

## Common Misconceptions
- Amortized cost is not the same as average-case cost; it applies to sequences of operations on a single data structure, not random inputs.
- An operation with O(1) amortized cost can still be O(n) in the worst case for a single call — real-time systems must account for this.
