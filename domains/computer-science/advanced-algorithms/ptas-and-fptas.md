---
id: ptas-and-fptas
title: PTAS and FPTAS
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: approximation-algorithms-advanced
  type: hard
- id: np-completeness
  type: hard
- id: dynamic-programming-intro
  type: soft
tags:
- ptas
- fptas
- approximation-schemes
- knapsack
stage: expert
status: validated
---

# PTAS and FPTAS

## Core Idea
A Polynomial-Time Approximation Scheme (PTAS) is a family of algorithms parameterized by epsilon > 0, where each algorithm runs in polynomial time in n (for fixed epsilon) and returns a (1+epsilon)-approximate solution. An FPTAS (Fully Polynomial-Time Approximation Scheme) is stronger: the running time is polynomial in both n and 1/epsilon. The knapsack problem admits an FPTAS via scaling and rounding item profits, then applying dynamic programming — running in O(n^2/epsilon) time. PTAS existence versus FPTAS existence is a meaningful distinction: not all problems with a PTAS have an FPTAS, and the FPTAS exclusion is connected to strong NP-hardness. Problems like Euclidean TSP admit a PTAS (Arora, Mitchell) but are unlikely to have an FPTAS.

## Questions

```yaml
- question: "The FPTAS for knapsack works by scaling down item profits by a factor that depends on epsilon and n, then running exact dynamic programming on the scaled instance. What determines the scaling factor and why does it produce polynomial running time?"
  type: multiple-choice
  options:
    - "Scale all profits to lie in [0, 1]; running time becomes O(n)"
    - "Scale profits by dividing by K = (epsilon * p_max) / n, round down to integers, then run DP on scaled profits. The maximum scaled profit is n/epsilon, so the DP table has O(n^2/epsilon) entries, making total time O(n^2/epsilon) — polynomial in both n and 1/epsilon"
    - "Scale profits to powers of 2; running time becomes O(n log P)"
    - "No scaling is needed — standard DP is already polynomial in 1/epsilon"
  answer: 1
  explanation: "The standard DP for knapsack runs in O(nP) time where P is the sum of all profits — pseudopolynomial because P can be exponential in the input size. The FPTAS scales profits by K = epsilon * p_max / n, rounding each profit down to floor(p_i / K). The maximum scaled profit is p_max / K = n/epsilon, so the DP table has dimensions n × (n/epsilon), giving O(n^2/epsilon) time. The rounding introduces at most K additive error per item, and at most nK = epsilon * p_max total error, which is at most epsilon * OPT (since OPT >= p_max). This yields a (1-epsilon)-approximation in polynomial time."

- question: "Every problem that admits a PTAS also admits an FPTAS."
  type: true-false
  answer: false
  explanation: "This is a common misconception. A PTAS allows running time like O(n^(1/epsilon)) — polynomial in n for fixed epsilon, but exponential in 1/epsilon. An FPTAS requires time polynomial in BOTH n and 1/epsilon. Strongly NP-hard problems (where the problem remains NP-hard even when all numbers are bounded by a polynomial in n) cannot have an FPTAS unless P = NP, because the FPTAS would solve the bounded-number version exactly by choosing epsilon < 1/n^c. Bin packing and Euclidean TSP have PTAS but no FPTAS (unless P = NP). The knapsack problem is only weakly NP-hard, which is why it admits an FPTAS."

- question: "Arora's PTAS for Euclidean TSP achieves (1+epsilon)-approximation in n^O(1/epsilon) time. Explain why this is a PTAS but not an FPTAS, and what structural property of Euclidean space makes a PTAS possible when general TSP cannot be approximated within any constant factor."
  type: short-answer
  answer: "The running time n^O(1/epsilon) is polynomial in n for any fixed epsilon (e.g., epsilon = 0.01 gives n^O(100)), but it is exponential in 1/epsilon, so it is not an FPTAS. The structural property that enables a PTAS is the geometry of Euclidean space: the triangle inequality ensures that 'detours' are bounded, and Arora's algorithm exploits this by partitioning the plane into a randomly shifted quadtree, finding the optimal tour within each cell, and patching cells together. The random shift ensures that the patching cost is small in expectation. General (metric) TSP has a constant-factor approximation (Christofides' 3/2) but general (non-metric) TSP cannot be approximated within any polynomial factor unless P = NP, because approximating it would solve Hamiltonian Cycle."
  explanation: "The distinction between PTAS and FPTAS is not just theoretical — the practical difference between n^100 and n^2 * 100 is enormous. Arora's result is remarkable precisely because it shows Euclidean structure can be exploited for arbitrarily good approximation, despite TSP being NP-hard."

- question: "A problem that is strongly NP-hard cannot have a pseudopolynomial-time algorithm unless P = NP."
  type: true-false
  answer: true
  explanation: "A pseudopolynomial algorithm runs in time polynomial in the numeric value of the input (not its bit length). If a problem is strongly NP-hard, it remains NP-hard even when all numbers are bounded by a polynomial in n — so a pseudopolynomial algorithm would be truly polynomial on these bounded instances, implying P = NP. Since an FPTAS for a number problem implies a pseudopolynomial algorithm (set epsilon = 1/(max_value + 1) to get exact solutions), strongly NP-hard problems cannot have FPTAS either. This is the key connection: weak NP-hardness (like knapsack) allows FPTAS; strong NP-hardness (like bin packing) blocks it."
```

## Explainer

Approximation algorithms give worst-case guarantees — a 2-approximation always returns a solution within a factor of 2 of optimal. But for many applications, you want to tune the accuracy: a 1.01-approximation for a shipping route, a 1.001-approximation for a portfolio allocation. Approximation schemes provide this tunability by parameterizing the accuracy with epsilon.

A PTAS is a family of algorithms indexed by epsilon > 0. For each epsilon, the algorithm runs in time polynomial in n (the input size) and returns a solution within factor (1+epsilon) of optimal. The catch is that the polynomial's degree or leading constant can depend on epsilon — a running time of O(n^(1/epsilon)) qualifies as a PTAS because for epsilon = 0.1 it is O(n^10), which is polynomial. But for epsilon = 0.001 it is O(n^1000), which is technically polynomial but practically useless. An FPTAS removes this catch: the running time must be polynomial in both n and 1/epsilon, like O(n^2/epsilon) or O(n^3/epsilon^2).

The knapsack FPTAS is the canonical example. The standard DP for knapsack runs in O(nP) time where P is the total profit — pseudopolynomial because P can be exponential in the input encoding. The FPTAS rescales profits by dividing by K = epsilon * p_max / n, effectively reducing the profit resolution. Rounding down to integers loses at most K profit per item, and with at most n items, the total loss is at most nK = epsilon * p_max <= epsilon * OPT. The scaled DP table has dimensions n by n/epsilon, giving O(n^2/epsilon) time. You trade a controlled amount of precision for a massive reduction in running time — from pseudopolynomial to fully polynomial.

The existence of an FPTAS is tied to the number-theoretic structure of the problem. Strongly NP-hard problems — those that remain NP-hard even when all numbers are polynomially bounded — cannot have FPTAS unless P = NP, because an FPTAS would solve the bounded case exactly. This is why knapsack (weakly NP-hard) has an FPTAS but bin packing (strongly NP-hard) does not. Problems like Euclidean TSP occupy an intermediate position: they admit a PTAS (using geometric structure) but the running time's dependence on 1/epsilon is exponential, and this is believed to be inherent. The PTAS / FPTAS / no-PTAS hierarchy provides a refined classification of NP-hard optimization problems by their approximability.
