---
id: partition-subset-sum-problems
title: Partition and Subset Sum Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: dynamic-programming-intro
  type: soft
- id: hamiltonian-path-cycle
  type: soft
- id: 3sat-satisfiability-variant
  type: soft
builds-toward:
- approximation-algorithms-design
tags:
- np-complete
- numeric-problems
- pseudo-polynomial
stage: advanced
status: validated
---
# Partition and Subset Sum Problems

## Core Idea
Partition asks: can a set of integers be divided into two subsets with equal sum? Subset sum asks: given a set and target, does a subset sum to the target? Both are NP-complete but admit pseudo-polynomial algorithms via dynamic programming in O(n·S) time where S is the sum. This illustrates how NP-complete problems vary: partition has no PTAS (polynomial-time approximation scheme), but knapsack does. These problems show hardness is nuanced—NP-completeness is not the end of analysis.

## Questions

```yaml
- question: "Subset Sum has a dynamic programming solution that runs in O(n·S) time, where n is the number of items and S is the target sum. A student claims this proves Subset Sum is in P. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing is wrong — O(n·S) is polynomial in the input size, so it proves Subset Sum is in P"
    - "O(n·S) is polynomial in the numeric value of S but exponential in the number of bits needed to encode S, making it pseudo-polynomial rather than truly polynomial"
    - "The student is wrong because dynamic programming cannot solve NP-complete problems at all"
    - "The student is wrong because the correct complexity is O(n²·S), which is clearly not polynomial"
  answer: 1
  explanation: "The subtle point is what 'polynomial' means relative to input size. The input to Subset Sum is not the number S itself but the binary encoding of S, which has log₂(S) bits. So the runtime O(n·S) is actually O(n·2^(log S)) — exponential in the bit-length of S. A truly polynomial algorithm would run in time polynomial in n and log S. When S is small relative to n, the DP is fast in practice. When S is exponentially large (say, S ≈ 2^n), the DP is just as slow as brute force. This is precisely the pseudo-polynomial vs. polynomial distinction."

- question: "Under which condition would Subset Sum instances be efficiently solvable in practice, despite being NP-complete in the worst case?"
  type: multiple-choice
  options:
    - "When the integers are all small — bounded by a polynomial function of n — so the target sum S is also polynomially bounded"
    - "When the target is exactly half the total sum (the Partition variant), which is always easier than general Subset Sum"
    - "When the integers are all powers of 2, because binary representations are always easy to sum"
    - "When the items are sorted in decreasing order, enabling greedy pruning"
  answer: 0
  explanation: "The O(n·S) DP is efficient when S is small relative to n. If each integer is at most some polynomial p(n), then S ≤ n·p(n), which is also polynomial in n, and the DP runs in polynomial time. This is exactly what 'weakly NP-complete' means: the hardness is tied to the magnitude of the numbers, not their count. Real-world instances often have this property (e.g., prices measured in cents rarely exceed millions), which is why the DP approach is practical despite the worst-case intractability."

- question: "Partition is a special case of Subset Sum where the target is exactly half the total sum of all elements."
  type: true-false
  answer: true
  explanation: "Partition asks: can we split a set into two subsets with equal total? If the full set has total T, we need each half to sum to T/2. This is exactly Subset Sum with target T/2. Because Partition reduces to Subset Sum, and Subset Sum reduces to Partition (Partition can encode any Subset Sum instance with padding), the two problems are equivalent in complexity. Both are NP-complete, both admit O(n·S) pseudo-polynomial DP, and both are weakly NP-complete."

- question: "Since Partition and the 0-1 Knapsack problem are both NP-complete, they have the same approximability — any approximation scheme that works for one should work for the other."
  type: true-false
  answer: false
  explanation: "NP-completeness is a coarse classification that says nothing about approximability. Knapsack (with values and a capacity) admits a fully polynomial-time approximation scheme (FPTAS): you can get within any (1−ε) factor of optimal in polynomial time. Partition has no polynomial-time approximation scheme (PTAS) unless P = NP — even getting close to the optimal split is hard. Two NP-complete problems with nearly identical descriptions can inhabit completely different parts of the approximation hierarchy. This is one of the deepest lessons from the study of these problems."

- question: "What does it mean for a problem to be 'weakly NP-complete' rather than 'strongly NP-complete,' and why does this distinction matter practically?"
  type: short-answer
  answer: "A problem is weakly NP-complete if it is NP-complete in general but solvable in polynomial time when the numeric values in the input are bounded by a polynomial in the input length (i.e., it admits a pseudo-polynomial algorithm). Partition and Subset Sum are weakly NP-complete because their O(n·S) DP runs efficiently when numbers are small. A strongly NP-complete problem, like 3-SAT or graph coloring, remains NP-hard even when all numeric values are bounded by a polynomial — there is no pseudo-polynomial escape hatch. The distinction matters practically because weakly NP-complete problems are often tractable on real inputs where numbers happen to be small, while strongly NP-complete problems offer no such relief."
  explanation: "The weak/strong distinction is invisible from the NP-completeness certificate alone — it requires examining whether the hardness comes from large numbers or from combinatorial structure. Understanding this guides the choice of algorithm: pseudo-polynomial DP for weakly NP-complete problems, approximation algorithms or heuristics for strongly NP-complete ones."
```

## Explainer

From your study of NP-completeness, you know that NP-complete problems are the hardest problems in NP — if any one of them has a polynomial-time algorithm, they all do. But that classification alone does not tell you how to cope with a specific NP-complete problem in practice. Partition and Subset Sum are the canonical examples of why the story does not end at "it's NP-complete." These two closely related problems reveal that the structure of the input — not just its size — determines how hard instances actually are to solve.

**Subset Sum** asks: given a set of integers and a target value *T*, is there a subset whose elements add up to exactly *T*? **Partition** is the special case where *T* equals half the total sum — can you split the set into two groups with equal totals? Both problems are NP-complete, which you can prove by reduction from known NP-complete problems. But here is the surprising twist: both admit **pseudo-polynomial time** algorithms using dynamic programming. The classic DP approach builds a boolean table where entry DP[i][s] records whether the first *i* elements can form a subset summing to *s*. The table has *n* × *S* entries (where *S* is the target sum), and filling each entry takes constant time. The total runtime is O(n·S) — polynomial in the numeric value of the input but exponential in the number of bits needed to represent *S*. This is exactly the distinction between polynomial and pseudo-polynomial time.

Why does this matter? Because it means the hardness of these problems depends on how large the numbers are, not just how many items you have. If your integers are bounded by some polynomial in *n* (say, each number fits in a few digits), the DP algorithm runs in genuinely polynomial time. It is only when the numbers are exponentially large relative to *n* that the problem becomes truly intractable. This is why Subset Sum and Partition are called **weakly NP-complete** — their hardness vanishes when numbers are small. Contrast this with **strongly NP-complete** problems like 3-SAT or graph coloring, which remain hard regardless of the magnitudes involved.

The approximation landscape adds another layer of nuance. The closely related Knapsack problem (which generalizes Subset Sum by adding values and a capacity constraint) admits a **fully polynomial-time approximation scheme** (FPTAS): for any desired accuracy ε, you can find a solution within a (1−ε) factor of optimal in time polynomial in both *n* and 1/ε. Partition, on the other hand, has no PTAS unless P = NP. This means two problems that look almost identical — both involve choosing subsets to hit numeric targets — have fundamentally different approximability. The lesson is that NP-completeness is a coarse classification. To understand what you can actually do with a hard problem, you must look deeper: at pseudo-polynomial algorithms, at weak versus strong NP-completeness, and at the approximation hierarchy. These distinctions are what separate theoretical impossibility from practical solvability.
