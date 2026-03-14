---
id: solving-recurrence-relations-master-theorem
title: 'Solving Recurrence Relations: Master Theorem and Methods'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: asymptotic-notation-big-o-omega-theta
  type: hard
- id: recursion-tail-recursion-optimization
  type: hard
builds-toward:
- divide-and-conquer-strategy
- dynamic-programming-intro
tags:
- recurrence-relations
- master-theorem
- analysis
stage: formal-systems
status: draft
---

# Solving Recurrence Relations: Master Theorem and Methods

## Core Idea
Recurrence relations describe algorithmic time complexity recursively (e.g., T(n) = 2T(n/2) + n for merge sort). The Master Theorem solves recurrences of the form T(n) = aT(n/b) + f(n) in closed form by comparing f(n) against n^(log_b a).

## How It's Best Learned
Start with simple examples: T(n) = T(n-1) + 1 (linear time), T(n) = 2T(n/2) + n (merge sort). Draw recursion trees to visualize the work at each level. Apply the Master Theorem's three cases and verify with concrete values. Code up a few recursive algorithms and count operations.

## Common Misconceptions
- The Master Theorem doesn't apply to all recurrences—f(n) must be a polynomial or near-polynomial.
- Confusing which exponent to use: it's log_b(a), not log(a/b).
- Forgetting that T(n) = T(n/2) + n is NOT dominated by a geometric series if n grows too slowly.
