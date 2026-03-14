---
id: greedy-activity-selection
title: Activity Selection Problem Using Greedy Algorithms
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: greedy-algorithms
  type: hard
tags:
- greedy
- activity-selection
- interval-scheduling
- optimization
- correctness-proof
stage: formal-systems
status: draft
---

# Activity Selection Problem Using Greedy Algorithms

## Core Idea
The activity selection problem: given activities with start and end times, select the maximum number of non-overlapping activities. Greedy solution: sort by end time and greedily select activities that don't overlap with the last selected. This achieves optimality in O(n log n) time and demonstrates that greedy algorithms can be optimal when the problem has greedy-choice property and optimal substructure.

## How It's Best Learned
Trace the greedy algorithm by hand on a small activity set. Prove optimality via the greedy-choice property: the first activity to finish is always in some optimal solution. Contrast with other orderings (start time, duration) to see why they fail.

## Common Misconceptions
- Any greedy approach works for activity selection (only end-time ordering is optimal). - Greedy algorithms are always optimal (they're optimal only when the problem has greedy-choice property and optimal substructure).
