---
id: fixed-parameter-tractability
title: Fixed-Parameter Tractability (FPT)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: vertex-cover-problem
  type: soft
tags:
- parameterized-complexity
- tractable-hardness
- algorithms
stage: advanced
status: draft
---

# Fixed-Parameter Tractability (FPT)

## Core Idea
Fixed-parameter tractability asks: while a problem is NP-hard in general, can it be solved in time f(k)·n^O(1) where k is a problem parameter (like solution size) and f is an arbitrary computable function? A problem is FPT if such algorithms exist. For instance, vertex cover is FPT parameterized by cover size k, though NP-complete in general. FPT provides a refined complexity landscape beyond classical NP-hardness.

## Questions

```yaml
- question: "An algorithm solves a problem in time O(n^k), where k is the size of the solution being sought. Is this algorithm FPT with respect to parameter k?"
  type: multiple-choice
  options:
    - "Yes — the running time is polynomial in n for any fixed value of k, which is exactly what FPT means"
    - "No — FPT requires the exponent of n to be a constant independent of k; in O(n^k) the polynomial degree grows with k, so this is not FPT"
    - "Yes — n^k is always faster than exponential time 2^n, so it qualifies as tractable for large inputs"
    - "It depends on the specific problem — O(n^k) is FPT for some problems and not others"
  answer: 1
  explanation: "FPT requires time f(k) · n^c where c is a constant that does NOT depend on k. In O(n^k), the exponent of n is k itself — so the polynomial degree grows without bound as k increases. For k=20, this gives O(n^20), which is computationally infeasible for any realistic n. A genuine FPT algorithm isolates the dependency on k into a multiplicative factor — like O(2^k · n) — while keeping the n-dependence at a fixed polynomial degree. The confusion between 'polynomial in n for fixed k' and 'FPT' is one of the most common errors in parameterized complexity."

- question: "Why does the branching algorithm for vertex cover (branching on any uncovered edge (u,v) and recursing with k−1) achieve FPT complexity?"
  type: multiple-choice
  options:
    - "Because the graph has at most n vertices, limiting the total number of recursive calls to n regardless of k"
    - "Because at each step we branch into two subproblems each with k decremented by 1, producing a search tree of depth k with at most 2^k leaves, each checkable in O(n) time — giving total cost O(2^k · n)"
    - "Because vertex cover uses dynamic programming that avoids redundant subproblems, reducing the search space from exponential to polynomial"
    - "Because vertex cover is actually easier than NP-complete in practice, and the branching algorithm simply exploits this hidden structure"
  answer: 1
  explanation: "The key insight: any valid vertex cover must include u or v (or both) from every uncovered edge. Branching into two subproblems — include u, or include v — each with k decremented by 1 gives a binary search tree of depth at most k (you can make at most k inclusion decisions). With branching factor 2 and depth k, there are at most 2^k leaves. Each leaf requires O(n) work to verify. Total: O(2^k · n) = f(k) · n^1. This is FPT because the exponent of n is the constant 1, independent of k."

- question: "A problem that is NP-hard in general can still be FPT with respect to a carefully chosen parameter k, allowing efficient solutions when k is small."
  type: true-false
  answer: true
  explanation: "True. This is the fundamental insight of parameterized complexity theory. NP-hardness is a worst-case statement over all possible inputs — it does not mean every instance is hard. FPT identifies structural parameters that, when small, make the problem tractable. Vertex cover is NP-complete in general (no polynomial algorithm in n alone is known) but FPT parameterized by solution size k, with an algorithm running in O(2^k · n) that is practical for small k. The difficulty is isolated in the parameter; the dependence on n remains polynomial."

- question: "A problem is FPT with respect to parameter k if it can be solved in time O(n^k), because this running time is polynomial in n for any fixed value of k."
  type: true-false
  answer: false
  explanation: "False. This is the most important distinction in FPT theory. FPT requires f(k) · n^c where c is a constant independent of k. In O(n^k), the exponent of n grows with k, so for k=50, you need O(n^50) — infeasible even for modest n. True FPT puts the k-dependence in a multiplicative factor (e.g., 2^k, k!, anything computable) while keeping n's exponent fixed. O(2^k · n) is FPT; O(n^k) is not. The class XP contains problems solvable in O(n^k) for fixed k, and XP properly contains FPT — they are distinct complexity classes."

- question: "Explain the conceptual difference between an algorithm running in O(n^k) and one running in O(2^k · n), and why only the second is considered FPT."
  type: short-answer
  answer: "In O(n^k), the polynomial degree of n grows with k: for k=10 you need O(n^10), for k=20 you need O(n^20) — computationally infeasible for large n at any k beyond a handful. In O(2^k · n), the exponent of n is always 1 (a fixed constant), so the n-dependence is always linear; only the multiplicative factor 2^k grows with k. For k=20, this is about 10^6 · n — perfectly tractable for large n. FPT requires f(k) · n^c where c is a constant: O(2^k · n) satisfies this with c=1, f(k)=2^k, while O(n^k) fails because c=k grows with the parameter. The essential point is that FPT isolates the combinatorial hardness entirely into the parameter k, keeping the input-size dependence polynomial with a fixed, small degree."
  explanation: "This distinction matters practically: when inputs have k ≤ 20 or k ≤ 50, even a large constant 2^50 ≈ 10^15 is bounded and fixed, while n-polynomial with fixed exponent scales gracefully. O(n^k) provides no such benefit — as k grows, the algorithm becomes worse on large inputs in a way that cannot be bounded by fixing k 'once and for all'."
```

## Explainer

From NP-completeness theory, you know that many important problems are NP-hard: no polynomial-time algorithm is known, and finding one would imply P = NP. But NP-hardness is a worst-case statement that treats all inputs as equally difficult. In practice, inputs to hard problems often have **structure** — a small solution size, sparse graphs, bounded tree-width — and exploiting that structure can make the problem tractable. Fixed-parameter tractability formalizes this observation.

The key idea is to identify a **parameter** k that captures the "hard part" of the input, then analyze complexity in terms of both n (input size) and k. A problem is **FPT** (fixed-parameter tractable) with respect to k if it can be solved in time f(k) · n^c, where f is any computable function (possibly exponential or worse in k) and c is a constant. The crucial point: for any *fixed* value of k, the running time is polynomial in n. When k is small, f(k) is just a constant multiplier, and the algorithm runs efficiently even on large inputs.

The **vertex cover** problem illustrates this perfectly. The problem asks: given a graph G and an integer k, does G have a vertex cover of size at most k? (A vertex cover is a set S of vertices such that every edge has at least one endpoint in S.) The brute-force approach checks all k-subsets of vertices, costing O(n^k) — polynomial for fixed k, but the degree grows with k, which isn't FPT. The FPT algorithm uses a different insight: pick any uncovered edge (u,v); a valid cover must include u or v (or both). Branch into two subproblems — include u, or include v — and recurse with k decremented. The search tree has depth k and branching factor 2, so at most 2^k leaf nodes, each checkable in polynomial time. Total cost: O(2^k · n). This is f(k) · n^1, which is FPT.

The function f(k) can be wild — 2^(2^k), k!, anything computable — and the problem is still FPT. The point is that when your actual inputs have k ≤ 20 or k ≤ 50, even an exponential-in-k factor is manageable. This makes FPT algorithms genuinely useful for real instances of NP-hard problems, provided the right parameter is small. Not every parameterization works: **W[1]-hard** problems (the parameterized analog of NP-hard) are unlikely to be FPT under the standard parameterization, forming a separate hardness class. The existence of a rich hierarchy (W[1], W[2], ...) shows that parameterized complexity theory, like classical complexity, has deep structure beyond a simple FPT/non-FPT divide.

The conceptual shift from classical to parameterized complexity is a shift from binary classification (tractable vs. intractable) to a **refined landscape**: the same problem can be FPT under one parameterization and W[1]-hard under another. Vertex cover parameterized by solution size is FPT; parameterized by the number of vertices in the complement, it's W[1]-hard. Choosing the right parameter to expose tractability is both the art and the science of the field.

