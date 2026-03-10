---
id: algorithm-design-basics
title: Algorithm Design Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: recursion-basics
  type: soft
- id: list-operations
  type: soft
- id: loop-control-statements
  type: soft
- id: big-o-notation
  type: soft
tags:
- algorithms
- pseudocode
- problem decomposition
- search
- sort
- complexity
stage: abstract-reasoning
status: draft
---

# Algorithm Design Basics

## Core Idea
Algorithm design is the process of specifying a step-by-step procedure to solve a problem correctly and efficiently. Foundational techniques include linear search (scan until found), binary search (halve the search space each step), selection sort, and insertion sort. Before coding, writing pseudocode makes the logic explicit without syntactic noise. Algorithm correctness is verified by tracing examples; efficiency is characterized by how runtime and memory scale with input size, expressed informally with Big-O notation.

## How It's Best Learned
Implement search and sort algorithms from scratch without looking up the code. Trace them on small arrays by hand. Measure runtime experimentally on different-sized inputs and compare to Big-O predictions.

## Common Misconceptions
- Assuming the first working solution is good enough without considering efficiency.
- Skipping pseudocode and jumping to code, which embeds language-specific confusion into the logic.
- Thinking sorting is always O(n²) — comparison-based sorts can achieve O(n log n).
