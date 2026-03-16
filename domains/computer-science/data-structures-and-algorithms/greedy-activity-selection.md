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

## Explainer

From your study of greedy algorithms, you know the core idea: make the locally optimal choice at each step and hope it leads to a globally optimal solution. The **activity selection problem** is the textbook example where this strategy provably works. The setup is simple: you have a set of activities, each with a start time and an end time, and you want to attend as many non-overlapping activities as possible. Think of scheduling meetings in a conference room — once you commit to a meeting, you cannot attend any other meeting that overlaps with it.

The greedy strategy is to **sort activities by end time** and then iterate through them, selecting each activity whose start time is at or after the end time of the last activity you selected. The first activity you pick is the one that finishes earliest. This is counterintuitive — why not pick the shortest activity, or the one that starts earliest? The answer is that finishing earliest leaves the maximum remaining time for subsequent activities. Picking the shortest activity can fail because a short activity might sit right in the middle of the timeline, blocking two others. Picking the earliest start time can fail because an activity that starts early might run very long, blocking everything else. Only the earliest-finishing criterion guarantees you never waste future capacity.

The proof of optimality uses the **greedy-choice property**: the earliest-finishing activity is always part of some optimal solution. Here is the intuition. Suppose an optimal solution does not include the earliest-finishing activity a₁. It must include some other activity a' that overlaps with a₁. Since a₁ finishes no later than a', you can swap a' for a₁ without creating any new conflicts — the resulting solution has the same number of activities and is still valid. By induction, the greedy algorithm builds a solution that is as large as any optimal one. This property combined with **optimal substructure** (once you select an activity, the remaining subproblem is the same type of problem on the remaining compatible activities) is what makes the greedy approach work.

The algorithm runs in O(n log n) time, dominated by the sort. The selection pass itself is O(n) — a single scan through the sorted list. This is a dramatic improvement over a brute-force approach that would consider all 2ⁿ subsets of activities. The activity selection problem is also the foundation for more complex **interval scheduling** variants: weighted activity selection (where each activity has a value and you maximize total value — this requires DP, not greedy), interval partitioning (minimizing the number of rooms needed), and job scheduling with deadlines. Recognizing that a problem has the structure of activity selection is often the key insight that makes a seemingly complex scheduling task tractable.
