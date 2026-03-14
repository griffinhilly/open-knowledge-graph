---
id: selection-algorithm-quickselect
title: 'Selection Algorithms: Finding the kth Smallest Element'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: quicksort
  type: hard
- id: algorithm-analysis-best-worst-average-case
  type: soft
tags:
- selection
- algorithms
- linear-time
stage: formal-systems
status: draft
---

# Selection Algorithms: Finding the kth Smallest Element

## Core Idea
Quickselect finds the kth smallest element in O(n) average time by partitioning (like quicksort) but recursing on only the relevant partition. The Median-of-Medians algorithm guarantees O(n) worst-case time but with a large constant factor, making quickselect preferable in practice.

## How It's Best Learned
Implement quickselect and compare to sorting then indexing. Observe average-case performance and analyze how the algorithm avoids sorting unused partitions. Study Median-of-Medians to understand worst-case linear-time selection.

## Common Misconceptions
- Thinking finding the kth smallest requires sorting; quickselect avoids most comparisons.
- Assuming Median-of-Medians is faster in practice; quickselect's constants are better.
- Not recognizing selection's applications beyond median finding (e.g., load balancing, percentile queries).
