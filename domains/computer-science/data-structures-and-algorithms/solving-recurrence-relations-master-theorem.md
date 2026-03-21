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

## Questions

```yaml
- question: "Consider T(n) = 4T(n/2) + n. Applying the Master Theorem, what is the tight bound for T(n)?"
  type: multiple-choice
  options:
    - "Θ(n log n) — because f(n)=n and the log factor applies"
    - "Θ(n²) — because n^(log₂ 4) = n² dominates f(n)=n"
    - "Θ(n) — because f(n)=n and it matches the subproblem cost"
    - "Θ(n² log n) — because we are in Case 2 with n^(log₂ 4)"
  answer: 1
  explanation: "Here a=4, b=2, so n^(log_b a) = n^(log₂ 4) = n². Since f(n)=n grows polynomially slower than n² (specifically f(n) = O(n^(2−ε)) for ε=1), we are in Case 1: the leaves dominate and T(n) = Θ(n²). Option A is the classic mistake — applying Case 2 logic even though f(n) and n^(log_b a) are not equal. Case 2 only applies when f(n) = Θ(n^(log_b a))."

- question: "Why does merge sort run in Θ(n log n) rather than Θ(n²), even though it makes two recursive calls on roughly half the data?"
  type: multiple-choice
  options:
    - "Because the two recursive calls operate on non-overlapping halves, avoiding redundant work"
    - "Because f(n)=n matches n^(log₂ 2)=n, placing it in Case 2 where the log factor appears"
    - "Because merge sort is not a divide-and-conquer algorithm, so the Master Theorem gives a tighter bound"
    - "Because the recursion terminates after log n levels, and each level does O(1) work"
  answer: 1
  explanation: "For merge sort, a=2, b=2, f(n)=n (the merge step), and n^(log₂ 2) = n¹ = n. Since f(n) = Θ(n^(log_b a)), we are in Case 2: work is evenly distributed across levels, giving T(n) = Θ(n log n). The log factor emerges because there are log n levels AND each level does Θ(n) total work. Option D is close but backwards — each level does O(n) total work across all nodes, not O(1) per node."

- question: "The Master Theorem can be applied to the recurrence T(n) = T(n−1) + n."
  type: true-false
  answer: false
  explanation: "The Master Theorem requires the form T(n) = aT(n/b) + f(n), where each recursive call operates on a problem of size n/b — a fixed fraction of n. T(n) = T(n−1) + n subtracts a constant rather than dividing by a constant, so it does not fit the required form. To solve it, use substitution or telescoping: T(n) = n + (n−1) + ... + 1 = Θ(n²)."

- question: "In Case 2 of the Master Theorem (when f(n) = Θ(n^(log_b a))), the work done at each level of the recursion tree is the same."
  type: true-false
  answer: true
  explanation: "This is exactly why Case 2 produces a Θ(n^(log_b a) × log n) bound. Level k of the recursion has aᵏ subproblems each of size n/bᵏ, contributing aᵏ × f(n/bᵏ) total work. When f(n) = Θ(n^(log_b a)), this equals aᵏ × (n/bᵏ)^(log_b a) = n^(log_b a) — constant across all log n levels. Multiplying by the number of levels gives the result."

- question: "For T(n) = 2T(n/2) + n (merge sort), use a recursion tree argument to explain why the total work is Θ(n log n)."
  type: short-answer
  answer: "At level k of the recursion tree there are 2ᵏ subproblems, each of size n/2ᵏ, each doing O(n/2ᵏ) merge work. Total work at level k: 2ᵏ × (n/2ᵏ) = n. Every level contributes exactly n work, and the tree has log₂ n levels (from size n down to size 1). Total: n × log₂ n = Θ(n log n)."
  explanation: "The recursion tree makes the Θ(n log n) result visible without formula manipulation: observe that each level's total work is constant (n), count the levels (log n), and multiply. This is the intuition Case 2 of the Master Theorem formalizes."
```

## Explainer

When you analyze a recursive algorithm, the running time naturally expresses itself as a **recurrence relation** — a formula that defines T(n) in terms of T on smaller inputs. For example, merge sort splits the array in half (two subproblems of size n/2), recurses on each half, and merges the results in O(n) time. This gives T(n) = 2T(n/2) + n. Binary search cuts the problem in half and does O(1) work per level: T(n) = T(n/2) + 1. The question is: what closed-form function does T(n) grow as? That is what recurrence-solving techniques answer.

The most intuitive approach is the **recursion tree method**. Draw the recurrence as a tree: the root does f(n) work and spawns a subproblems, each of size n/b. Each of those spawns a more subproblems, and so on until the base case. The total work is the sum across all levels. For merge sort, level 0 does n work, level 1 has two nodes each doing n/2 work (total n), level 2 has four nodes each doing n/4 work (total n), and so on. Every level contributes exactly n work, and there are log₂ n levels, giving T(n) = O(n log n). For binary search, each level does O(1) work across a single node, and there are log₂ n levels, so T(n) = O(log n). The recursion tree makes the pattern visible before you apply any formula.

The **Master Theorem** formalizes what the recursion tree reveals. For recurrences of the form T(n) = aT(n/b) + f(n), the theorem compares f(n) — the work done at each level outside the recursive calls — against n^(log_b a), which captures how fast the number of subproblems grows. There are three cases. **Case 1**: if f(n) grows polynomially slower than n^(log_b a), the leaves dominate and T(n) = Θ(n^(log_b a)). **Case 2**: if f(n) grows at the same rate as n^(log_b a), the work is evenly spread across levels and T(n) = Θ(n^(log_b a) × log n). **Case 3**: if f(n) grows polynomially faster than n^(log_b a), the root dominates and T(n) = Θ(f(n)), provided a regularity condition holds.

Applying this to merge sort: a = 2, b = 2, f(n) = n, and n^(log₂ 2) = n¹ = n. Since f(n) = Θ(n) matches n^(log_b a), we are in Case 2, giving T(n) = Θ(n log n). For binary search: a = 1, b = 2, f(n) = 1, and n^(log₂ 1) = n⁰ = 1. Again Case 2, giving T(n) = Θ(log n). For an algorithm like Strassen's matrix multiplication with T(n) = 7T(n/2) + Θ(n²): n^(log₂ 7) ≈ n^2.81, which grows faster than f(n) = n², so Case 1 applies and T(n) = Θ(n^2.81). The Master Theorem does not cover every recurrence — it requires the subproblems to be equal-sized and f(n) to be polynomially comparable to n^(log_b a) — but it handles the vast majority of divide-and-conquer algorithms you will encounter.
