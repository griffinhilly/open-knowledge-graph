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

## Questions

```yaml
- question: "You need to schedule the maximum number of non-overlapping activities. Which sorting criterion guarantees an optimal greedy solution?"
  type: multiple-choice
  options:
    - "Sort by start time — activities starting earliest should be prioritized"
    - "Sort by end time — finishing earliest leaves the most remaining capacity for future activities"
    - "Sort by duration — shortest activities maximize the number that fit"
    - "Sort by number of conflicts — activities with fewer conflicts should be selected first"
  answer: 1
  explanation: "Sorting by end time is the only criterion that provably guarantees optimality. Sorting by start time fails because an activity starting early might run very long and block many others. Sorting by duration fails because a short activity might sit in the middle of the timeline, blocking two longer ones that together could have fit. Earliest-finish-time is correct because it leaves maximum remaining time after each selection, which is exactly what the greedy-choice property formalizes."

- question: "The greedy-choice property for activity selection states that..."
  type: multiple-choice
  options:
    - "The activity with the fewest overlapping activities is always in some optimal solution"
    - "The earliest-starting activity is always in some optimal solution"
    - "The earliest-finishing activity is always in some optimal solution"
    - "Any activity can be the first selection without affecting the number selected"
  answer: 2
  explanation: "The greedy-choice property says the earliest-finishing activity a₁ is always in some optimal solution. The proof is an exchange argument: if an optimal solution uses some other activity a' instead of a₁, you can swap a' for a₁ without creating new conflicts (since a₁ finishes no later than a'), producing a valid solution of the same size. This swap argument is what makes the greedy approach provably correct — not just heuristically sensible. Option B (earliest start) is a common trap; it is not provably optimal."

- question: "Sorting activities by shortest duration always maximizes the number of non-overlapping activities selected."
  type: true-false
  answer: false
  explanation: "This is a common misconception. A short activity positioned in the middle of the timeline can block two longer activities that together would have increased the total count. For example, given activities A(1–8), B(3–4), C(5–9), sorting by duration selects B(duration 1) first, then nothing else fits around it. Sorting by end time selects B(ends 4), then C(ends 9), giving 2 activities. Only end-time ordering is provably optimal."

- question: "The activity selection problem can be solved optimally in O(n log n) time, with the sort dominating and the selection pass requiring only O(n)."
  type: true-false
  answer: true
  explanation: "After sorting by end time in O(n log n), the greedy selection is a single linear scan: iterate through activities, and select each one whose start time is at or after the finish time of the last selected activity. This O(n) pass requires no backtracking or reconsideration of earlier choices, which is what makes the greedy approach efficient. Dynamic programming for the weighted variant is O(n²) or O(n log n) with binary search — more expensive because it cannot rely on the greedy-choice property."

- question: "Explain why sorting activities by end time — rather than by start time or shortest duration — leads to an optimal greedy solution."
  type: short-answer
  answer: "Sorting by end time works because finishing earliest leaves the maximum amount of remaining timeline available for subsequent activities. Any other selection could block more future choices. The greedy-choice property formalizes this: the earliest-finishing activity is always in some optimal solution (provable by an exchange argument — swapping any other first choice for the earliest-finishing activity never reduces the total count). Start time fails because an early-starting activity may run too long; duration fails because a short activity in the middle can block two longer compatible activities."
  explanation: "The core insight is that the greedy algorithm's correctness is not intuitive — it requires the exchange argument to prove. Understanding this proof is what distinguishes genuine mastery from pattern-matching: it shows *why* end time is special (it minimizes the 'cost' of each selection in terms of future capacity consumed) and why no other simple criterion achieves the same guarantee."
```

## Explainer

From your study of greedy algorithms, you know the core idea: make the locally optimal choice at each step and hope it leads to a globally optimal solution. The **activity selection problem** is the textbook example where this strategy provably works. The setup is simple: you have a set of activities, each with a start time and an end time, and you want to attend as many non-overlapping activities as possible. Think of scheduling meetings in a conference room — once you commit to a meeting, you cannot attend any other meeting that overlaps with it.

The greedy strategy is to **sort activities by end time** and then iterate through them, selecting each activity whose start time is at or after the end time of the last activity you selected. The first activity you pick is the one that finishes earliest. This is counterintuitive — why not pick the shortest activity, or the one that starts earliest? The answer is that finishing earliest leaves the maximum remaining time for subsequent activities. Picking the shortest activity can fail because a short activity might sit right in the middle of the timeline, blocking two others. Picking the earliest start time can fail because an activity that starts early might run very long, blocking everything else. Only the earliest-finishing criterion guarantees you never waste future capacity.

The proof of optimality uses the **greedy-choice property**: the earliest-finishing activity is always part of some optimal solution. Here is the intuition. Suppose an optimal solution does not include the earliest-finishing activity a₁. It must include some other activity a' that overlaps with a₁. Since a₁ finishes no later than a', you can swap a' for a₁ without creating any new conflicts — the resulting solution has the same number of activities and is still valid. By induction, the greedy algorithm builds a solution that is as large as any optimal one. This property combined with **optimal substructure** (once you select an activity, the remaining subproblem is the same type of problem on the remaining compatible activities) is what makes the greedy approach work.

The algorithm runs in O(n log n) time, dominated by the sort. The selection pass itself is O(n) — a single scan through the sorted list. This is a dramatic improvement over a brute-force approach that would consider all 2ⁿ subsets of activities. The activity selection problem is also the foundation for more complex **interval scheduling** variants: weighted activity selection (where each activity has a value and you maximize total value — this requires DP, not greedy), interval partitioning (minimizing the number of rooms needed), and job scheduling with deadlines. Recognizing that a problem has the structure of activity selection is often the key insight that makes a seemingly complex scheduling task tractable.
