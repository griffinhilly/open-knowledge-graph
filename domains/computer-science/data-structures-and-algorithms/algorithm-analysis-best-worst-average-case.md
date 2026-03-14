---
id: algorithm-analysis-best-worst-average-case
title: Best, Worst, and Average Case Complexity Analysis
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: asymptotic-notation-big-o-omega-theta
  type: hard
- id: algorithm-design-basics
  type: hard
builds-toward:
- algorithm-complexity-in-practice
- selection-algorithm-quickselect
tags:
- complexity
- analysis
- asymptotics
stage: formal-systems
status: draft
---

# Best, Worst, and Average Case Complexity Analysis

## Core Idea
Every algorithm exhibits different performance under different input conditions. The best case (optimal input) is rarely the focus; worst case provides guarantees, while average case models typical behavior. Understanding which applies to a given context is essential for algorithm selection.

## How It's Best Learned
Analyze concrete algorithms like quicksort (O(n²) worst case, O(n log n) average) versus merge sort (O(n log n) in all cases). Compare on real datasets to see where average case analysis becomes relevant.

## Common Misconceptions
- Assuming average case equals worst case.
- Thinking best case is a useful metric for practical algorithm selection.
- Averaging time complexities across cases rather than understanding the distribution of inputs.
