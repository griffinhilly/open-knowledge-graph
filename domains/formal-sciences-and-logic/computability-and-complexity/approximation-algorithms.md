---
id: approximation-algorithms
title: Approximation Algorithms
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: algorithm-analysis-big-o
  type: soft
- id: knapsack-problem-variations
  type: soft
tags:
- complexity
- approximation
- optimization
- intractability
stage: advanced
status: validated
---
# Approximation Algorithms

## Core Idea
Approximation algorithms provide provably near-optimal solutions to NP-hard optimization problems in polynomial time, measured by their approximation ratio — the worst-case ratio between the algorithm's solution and the true optimum. The class APX contains problems with constant-factor approximations, PTAS (Polynomial-Time Approximation Scheme) allows (1+epsilon)-approximation for any epsilon > 0, and FPTAS further requires time polynomial in both input size and 1/epsilon. Inapproximability results, often proved via the PCP theorem and gap-preserving reductions, show that for some problems (like MAX-3SAT or chromatic number), no polynomial-time algorithm can achieve better than a specific ratio unless P = NP.

## How It's Best Learned
Study the 2-approximation for vertex cover (take both endpoints of a maximal matching) and the greedy O(log n)-approximation for set cover as clean introductory examples. Then learn the PTAS for Euclidean TSP and the FPTAS for knapsack to see the full spectrum. Finally, encounter the PCP theorem's implication that MAX-3SAT has no PTAS, which reveals hard limits on approximability.

## Common Misconceptions
- An approximation ratio of 2 does not mean the answer is "twice as bad" in practice — it is a worst-case guarantee, and real performance is often much better.
- Not all NP-hard problems are equally hard to approximate — some admit FPTAS while others cannot be approximated within any constant factor unless P = NP.

## Questions

```yaml
- question: "An approximation algorithm for minimum vertex cover returns a solution of size 24. Given a 2-approximation guarantee, what can you conclude about the size of the optimal solution?"
  type: multiple-choice
  options:
    - "The optimal solution has size at most 12"
    - "The optimal solution has size exactly 12"
    - "The optimal solution has size at least 12"
    - "The optimal solution has size at most 24"
  answer: 2
  explanation: "A 2-approximation guarantees ALG ≤ 2 · OPT, so OPT ≥ ALG / 2 = 12. You can only say the optimal is *at least* 12 — not exactly 12, and not at most 12. The approximation ratio bounds how far above optimal the algorithm can go, which gives a lower bound on OPT from the algorithm's output, not an upper bound."

- question: "What is the key difference between a PTAS and an FPTAS for an optimization problem?"
  type: multiple-choice
  options:
    - "A PTAS gives a constant-factor approximation; an FPTAS gives a (1+ε)-approximation"
    - "In a PTAS, running time is polynomial in n for each fixed ε but may grow exponentially as ε→0; in an FPTAS, running time is also polynomial in 1/ε"
    - "A PTAS requires the problem to be in APX; an FPTAS works on any NP-hard problem"
    - "A PTAS approximates within 1% of optimal; an FPTAS approximates within 0.1% of optimal"
  answer: 1
  explanation: "Both PTAS and FPTAS give (1+ε)-approximations, but at different computational costs. A PTAS runs in polynomial time for any fixed ε, but the exponent may depend on ε (e.g., n^{1/ε}), making it impractical for very small ε. An FPTAS requires time polynomial in both n and 1/ε simultaneously (e.g., O(n²/ε)), so high precision is achievable without exponential blowup. The knapsack problem has an FPTAS; Euclidean TSP has a PTAS but not an FPTAS."

- question: "An approximation ratio of 2 is a worst-case guarantee, so the algorithm's actual output may be much closer to optimal on typical inputs."
  type: true-false
  answer: true
  explanation: "Approximation ratios are worst-case bounds — they guarantee the algorithm never exceeds a certain multiple of OPT, but say nothing about average-case performance. In practice, algorithms with a 2-approximation guarantee often return solutions within 10–20% of optimal on real instances. The ratio defines the theoretical worst case, not the expected output quality."

- question: "Since most NP-hard problems are computationally equivalent under polynomial reductions, they are most equally difficult to approximate."
  type: true-false
  answer: false
  explanation: "NP-hardness means all NP-hard problems are equivalent in terms of exact solvability, but their approximability varies enormously. Vertex cover has a 2-approximation; knapsack has an FPTAS (arbitrarily good polynomial approximation); graph coloring cannot be approximated within n^{1−ε} for any ε > 0 unless P = NP. The PCP theorem and gap-preserving reductions reveal a rich approximability hierarchy that does not follow from NP-hardness alone."

- question: "Explain why the greedy maximal-matching algorithm for vertex cover achieves a 2-approximation. What property of the optimal solution provides the key lower bound?"
  type: short-answer
  answer: "The algorithm finds a maximal matching (a set of edges with no shared endpoints, where no more edges can be added) and returns both endpoints of every matched edge. The key: the optimal vertex cover must include at least one endpoint of each matched edge — otherwise that edge would be uncovered. So OPT ≥ |matching|. The algorithm takes 2·|matching| vertices, giving a ratio of at most 2·|matching| / OPT ≤ 2·|matching| / |matching| = 2."
  explanation: "The analysis works by finding a structural lower bound on OPT (every cover must hit every matched edge) and then bounding the algorithm's output against that lower bound. The algorithm never computes OPT directly. This 'bound the algorithm against a lower bound on OPT' strategy — using problem structure rather than knowing the optimum — is the backbone of most approximation analyses."
```

## Explainer

You already know from NP-completeness that problems like vertex cover and traveling salesman are almost certainly intractable exactly — no polynomial-time algorithm is expected to find the optimal solution in general. But in practice, we still need answers. Approximation algorithms offer a principled escape: instead of insisting on the optimum, we accept a provably near-optimal solution and guarantee how far off we can be. The **approximation ratio** is this guarantee, expressed as the worst-case ratio between what the algorithm returns and the true optimum. A 2-approximation for vertex cover means the algorithm finds a cover at most twice the size of the smallest possible cover — not "about twice as large in practice," but "never more than twice, provably, on any input."

The approximability landscape is a hierarchy. At the top are problems with **constant-factor approximations** (the class APX): vertex cover has a 2-approximation, set cover has an O(log n)-approximation. Below that, some problems admit a **PTAS (Polynomial-Time Approximation Scheme)**: for any ε > 0, you can get a (1+ε)-approximation in polynomial time — say within 1% of optimal — though the running time may grow badly as ε shrinks (like n^{1/ε}). Even better, an **FPTAS (Fully Polynomial-Time Approximation Scheme)** requires time polynomial in both n and 1/ε simultaneously, meaning you can tune ε without paying an exponential penalty. Knapsack has an FPTAS; Euclidean TSP has a PTAS; general TSP does not have either (unless P = NP).

The other side of the picture is **inapproximability**: hardness results that show certain approximation ratios are themselves out of reach. The PCP theorem — one of the deepest results in complexity theory — implies that MAX-3SAT cannot be approximated beyond a ratio of roughly 7/8 in polynomial time unless P = NP. For graph coloring, no polynomial-time algorithm can achieve an n^{1-ε}-approximation for any ε > 0 unless P = NP. These results come from **gap-preserving reductions**: if you could approximate problem A too well, you could solve some NP-hard problem B exactly, contradicting P ≠ NP.

The cleanest way to develop intuition is through the 2-approximation for vertex cover. The algorithm is simple: find a maximal matching (a set of edges with no shared endpoints, where you cannot add another edge), then take both endpoints of every matched edge. Why does this work? The optimal vertex cover must include at least one endpoint of each matched edge (otherwise that edge is uncovered), so OPT ≥ |matching|. The algorithm takes 2·|matching| vertices, so the ratio is at most 2. Notice that the analysis is tight: the algorithm does not compute the optimum, but the gap is bounded by a counting argument rooted in the structure of the matching. This style of reasoning — bound the algorithm's output against a lower bound on OPT — is the backbone of most approximation analyses.
