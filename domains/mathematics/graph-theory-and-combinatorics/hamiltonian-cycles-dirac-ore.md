---
id: hamiltonian-cycles-dirac-ore
title: 'Hamiltonian Cycles: Dirac and Ore Conditions'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: hamiltonian-circuits
  type: hard
- id: hamiltonian-cycle-conditions
  type: soft
tags:
- graph-theory
- hamiltonicity
stage: advanced
status: validated
---
# Hamiltonian Cycles: Dirac and Ore Conditions

## Core Idea
Dirac's Theorem states that a graph with n ≥ 3 vertices where every vertex has degree at least n/2 is Hamiltonian. Ore's Theorem generalizes: if for every non-adjacent pair u,v we have deg(u) + deg(v) ≥ n, the graph is Hamiltonian. These conditions elegantly show that high minimum degree guarantees Hamiltonian cycles, though deciding Hamiltonicity in general remains NP-hard.

## How It's Best Learned
Verify these conditions on small graphs (n ≤ 6) and check that they hold for known Hamiltonian graphs.

## Common Misconceptions
These conditions are sufficient but not necessary; graphs can be Hamiltonian without satisfying Dirac or Ore conditions.

## Questions

```yaml
- question: "A graph has 10 vertices and every vertex has degree 4. A student concludes: 'Dirac's threshold is n/2 = 5, and every vertex has degree only 4, so the graph is not Hamiltonian.' Is this reasoning correct?"
  type: multiple-choice
  options:
    - "Yes — the Dirac degree condition is not met, so the graph cannot have a Hamiltonian cycle"
    - "No — Dirac's condition is sufficient but not necessary; the graph might still be Hamiltonian even though the condition fails"
    - "No — Dirac's threshold for 10 vertices is actually 4, not 5, so the condition is satisfied"
    - "Yes — degree 4 in a 10-vertex graph is always too low for any Hamiltonian cycle to exist"
  answer: 1
  explanation: "This is the central misconception. Dirac's theorem is a one-way guarantee: if the degree condition is satisfied, a Hamiltonian cycle must exist. But failing the condition tells you nothing — the graph might still be Hamiltonian. A simple cycle (Cₙ) on 10 vertices has every vertex with degree 2 and is trivially Hamiltonian. The student incorrectly treats a sufficient condition as if it were necessary."

- question: "Ore's theorem is strictly more broadly applicable than Dirac's theorem because:"
  type: multiple-choice
  options:
    - "Ore requires every vertex to have degree ≥ n/2 individually, while Dirac only requires non-adjacent pairs to have high degree"
    - "Every graph satisfying Dirac also satisfies Ore, but not every graph satisfying Ore satisfies Dirac"
    - "Ore's condition applies only to bipartite graphs, which Dirac cannot handle"
    - "Ore uses algebraic conditions while Dirac uses purely combinatorial ones, making Ore more general"
  answer: 1
  explanation: "Ore's condition requires that for every non-adjacent pair u, v: deg(u) + deg(v) ≥ n. If every vertex individually has degree ≥ n/2 (Dirac), then any non-adjacent pair sums to at least n (satisfying Ore). So Dirac implies Ore — every Dirac graph is also an Ore graph. But Ore can hold when individual vertices have low degree, as long as every low-degree vertex is adjacent to every other low-degree vertex, so some Ore graphs are not Dirac graphs."

- question: "A cycle graph Cₙ on n ≥ 3 vertices is Hamiltonian despite having every vertex with degree 2, far below the Dirac threshold of n/2."
  type: true-false
  answer: true
  explanation: "The n-cycle is a Hamiltonian cycle by construction — it visits every vertex exactly once and returns to the start. Yet every vertex has degree 2, which is far below Dirac's n/2 threshold for n ≥ 5. This is one of the simplest examples showing that Dirac and Ore conditions are not necessary for Hamiltonicity."

- question: "If a graph fails Ore's condition for some non-adjacent pair (u, v) where deg(u) + deg(v) < n, then the graph can seldom have a Hamiltonian cycle."
  type: true-false
  answer: false
  explanation: "Ore's theorem is a sufficient condition, not necessary. Failing it means only that Ore's guarantee doesn't apply — not that no Hamiltonian cycle exists. A graph can fail Ore's condition for some pair and still be Hamiltonian by some other structural reason. The converse of a sufficient condition is not generally true."

- question: "Why is the fact that Dirac and Ore conditions are sufficient but not necessary important for understanding the computational difficulty of detecting Hamiltonian cycles?"
  type: short-answer
  answer: "If these conditions were necessary and sufficient, you could check Hamiltonicity in polynomial time: compute degrees, verify the condition, done. But because they are only sufficient, they identify a restricted class of graphs (dense enough ones) where the hard problem becomes easy — but leave the general case untouched. Deciding Hamiltonicity in an arbitrary graph is NP-hard: no polynomial-time algorithm is known. Dirac and Ore carve out well-structured regions where the guarantee holds, but failing those conditions leaves you with no general shortcut. The contrast with Eulerian circuits — which have a clean necessary-and-sufficient degree condition and are easy to detect — makes the hardness of the Hamiltonian case especially striking."
  explanation: "This distinction between sufficient-only and necessary-and-sufficient conditions directly maps to algorithmic difficulty. A sufficient condition is a fast path for a subset of cases; a necessary-and-sufficient condition is a complete decision procedure. The absence of a necessary-and-sufficient condition for Hamiltonicity is not an accident — it reflects the NP-hardness of the problem."
```

## Explainer

From your study of Hamiltonian circuits, you know that a Hamiltonian cycle visits every vertex in a graph exactly once before returning to the start — the graph-theoretic version of a round trip through every city. The hard question is whether such a cycle exists at all. Unlike Eulerian circuits, which have a clean necessary-and-sufficient condition (every vertex has even degree), Hamiltonicity has no simple characterization. But there are powerful *sufficient* conditions that guarantee a Hamiltonian cycle whenever certain degree requirements are met.

**Dirac's theorem** gives the clearest guarantee: if a graph has n ≥ 3 vertices and every vertex has **degree at least n/2**, then the graph is Hamiltonian. The intuition is density. If every vertex is connected to at least half the graph, you are never boxed in — no matter which path you're building, the current endpoint always has enough neighbors that you can continue visiting new vertices, and the high connectivity ensures you can eventually close the cycle back to the start. For a graph with 10 vertices, Dirac requires every vertex to have degree ≥ 5: each vertex must reach more than half the other vertices.

**Ore's theorem** relaxes the requirement from individual vertices to pairs. Instead of requiring each vertex to have high degree, it requires that for every pair of *non-adjacent* vertices u and v, deg(u) + deg(v) ≥ n. The idea: if u and v are not directly connected, they must together "cover" enough of the graph to ensure a Hamiltonian path exists between them. Every graph satisfying Dirac also satisfies Ore (if both vertices individually have degree ≥ n/2, their sum is ≥ n), but not vice versa — Ore can apply when individual vertices have low degree, as long as every low-degree vertex is adjacent to every other low-degree vertex.

The critical caveat is that both conditions are **sufficient but not necessary**. A graph can be Hamiltonian without satisfying either. A simple cycle on 10 vertices — each vertex with degree 2 — is trivially Hamiltonian (it is one big cycle), yet degree 2 is far below the Dirac threshold of 5. The theorems are one-way doors: satisfying the condition guarantees a Hamiltonian cycle, but failing the condition tells you nothing. This asymmetry reflects a deep fact: determining whether an arbitrary graph is Hamiltonian is NP-hard, meaning no polynomial-time algorithm is known. Eulerian circuits were easy; Hamiltonian cycles are genuinely hard. Dirac and Ore identify a large, well-structured region where the hard problem becomes easy.
