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

## Explainer

When you analyze a recursive algorithm, the running time naturally expresses itself as a **recurrence relation** — a formula that defines T(n) in terms of T on smaller inputs. For example, merge sort splits the array in half (two subproblems of size n/2), recurses on each half, and merges the results in O(n) time. This gives T(n) = 2T(n/2) + n. Binary search cuts the problem in half and does O(1) work per level: T(n) = T(n/2) + 1. The question is: what closed-form function does T(n) grow as? That is what recurrence-solving techniques answer.

The most intuitive approach is the **recursion tree method**. Draw the recurrence as a tree: the root does f(n) work and spawns a subproblems, each of size n/b. Each of those spawns a more subproblems, and so on until the base case. The total work is the sum across all levels. For merge sort, level 0 does n work, level 1 has two nodes each doing n/2 work (total n), level 2 has four nodes each doing n/4 work (total n), and so on. Every level contributes exactly n work, and there are log₂ n levels, giving T(n) = O(n log n). For binary search, each level does O(1) work across a single node, and there are log₂ n levels, so T(n) = O(log n). The recursion tree makes the pattern visible before you apply any formula.

The **Master Theorem** formalizes what the recursion tree reveals. For recurrences of the form T(n) = aT(n/b) + f(n), the theorem compares f(n) — the work done at each level outside the recursive calls — against n^(log_b a), which captures how fast the number of subproblems grows. There are three cases. **Case 1**: if f(n) grows polynomially slower than n^(log_b a), the leaves dominate and T(n) = Θ(n^(log_b a)). **Case 2**: if f(n) grows at the same rate as n^(log_b a), the work is evenly spread across levels and T(n) = Θ(n^(log_b a) × log n). **Case 3**: if f(n) grows polynomially faster than n^(log_b a), the root dominates and T(n) = Θ(f(n)), provided a regularity condition holds.

Applying this to merge sort: a = 2, b = 2, f(n) = n, and n^(log₂ 2) = n¹ = n. Since f(n) = Θ(n) matches n^(log_b a), we are in Case 2, giving T(n) = Θ(n log n). For binary search: a = 1, b = 2, f(n) = 1, and n^(log₂ 1) = n⁰ = 1. Again Case 2, giving T(n) = Θ(log n). For an algorithm like Strassen's matrix multiplication with T(n) = 7T(n/2) + Θ(n²): n^(log₂ 7) ≈ n^2.81, which grows faster than f(n) = n², so Case 1 applies and T(n) = Θ(n^2.81). The Master Theorem does not cover every recurrence — it requires the subproblems to be equal-sized and f(n) to be polynomially comparable to n^(log_b a) — but it handles the vast majority of divide-and-conquer algorithms you will encounter.
