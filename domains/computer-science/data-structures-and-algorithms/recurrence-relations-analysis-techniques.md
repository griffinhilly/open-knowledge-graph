---
id: recurrence-relations-analysis-techniques
title: Analyzing Recursive Algorithms via Recurrence Relations
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: asymptotic-notation-big-o-omega-theta
  type: hard
builds-toward:
- divide-and-conquer-strategy
- dynamic-programming-intro
- solving-recurrence-relations-master-theorem
tags:
- recursion
- recurrence
- analysis
stage: formal-systems
status: draft
---

# Analyzing Recursive Algorithms via Recurrence Relations

## Core Idea
Recursive algorithms can be analyzed by setting up recurrence relations—equations describing the running time T(n) in terms of T(n/2), T(n-1), or other smaller inputs. Solving these relations (via substitution, recurrence trees, or the master theorem) yields closed-form complexity bounds.

## How It's Best Learned
Trace recursive calls for small inputs, build a recurrence tree to visualize, then apply master theorem or substitution method. Compare on examples like T(n) = T(n/2) + O(n) for binary search.

## Common Misconceptions
- Forgetting the base case in recurrences.
- Misidentifying the non-recursive work term.
- Assuming all recursive algorithms have the same complexity structure.
