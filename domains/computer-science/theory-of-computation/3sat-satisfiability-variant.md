---
id: 3sat-satisfiability-variant
title: 3-SAT and k-SAT Variants
domain: computer-science
course: theory-of-computation
prerequisites:
- id: sat-boolean-satisfiability
  type: hard
- id: np-completeness
  type: hard
tags:
- np-complete
- clause-restrictions
stage: advanced
status: draft
---

# 3-SAT and k-SAT Variants

## Core Idea
3-SAT restricts SAT to formulas where each clause has exactly three literals; k-SAT generalizes to k literals per clause. Remarkably, 3-SAT remains NP-complete despite the restriction—restricting clause size doesn't reduce hardness beyond 3 literals. 2-SAT is solvable in polynomial time via implication graphs; k-SAT for k ≥ 3 is NP-complete. The phase transition phenomenon—random k-SAT formulas become hardest near the satisfiability threshold—is a major topic in complexity physics.

## Questions

```yaml
- question: "A colleague claims: 'I have a SAT formula where every clause has exactly 2 literals. Since it's a restricted version of NP-complete SAT, it must also be NP-complete.' Is this correct?"
  type: multiple-choice
  options:
    - "Yes — any restriction of an NP-complete problem is still NP-complete"
    - "Yes — 2-SAT is NP-complete, just like 3-SAT, because the clauses still require exponential search to satisfy"
    - "No — 2-SAT is solvable in polynomial time via implication graphs, because each 2-literal clause encodes implications that can be checked with strongly connected components"
    - "No — 2-SAT is in P because with only 2 literals per clause there are too few combinations to be hard"
  answer: 2
  explanation: "Restricting clause size does not automatically preserve NP-completeness — the specific restriction matters enormously. 2-SAT is in P: each clause (a ∨ b) is equivalent to two implications (¬a → b and ¬b → a). Collecting all such implications yields a directed implication graph, and the formula is satisfiable iff no variable x and its negation ¬x appear in the same strongly connected component — checkable in linear time. The complexity cliff occurs between k=2 (polynomial) and k=3 (NP-complete)."

- question: "Why is 3-SAT more commonly used than general SAT as the source problem for NP-completeness reductions?"
  type: multiple-choice
  options:
    - "3-SAT is easier to solve than general SAT, so reductions from 3-SAT are less likely to introduce errors"
    - "3-SAT is strictly harder than general SAT, making reductions more powerful"
    - "The fixed clause size of exactly 3 literals provides a uniform, predictable structure that simplifies constructing reductions to new problems"
    - "Using 3-SAT avoids the need to first prove the source problem is NP-complete"
  answer: 2
  explanation: "General SAT has clauses of arbitrary size, which makes reduction constructions irregular — you must handle clauses of size 1, 2, 10, 100, etc. 3-SAT's fixed clause size of exactly 3 literals provides uniform structure: every source gadget looks the same, and reduction mappings are cleaner and easier to verify. 3-SAT is not harder than general SAT (both are NP-complete), but its regularity makes it the preferred intermediate step. Most of the hundreds of known NP-completeness proofs go through 3-SAT."

- question: "Restricting SAT to clauses of exactly 3 literals (3-SAT) makes the problem easier than general SAT, because fewer literals per clause means fewer possibilities to check."
  type: true-false
  answer: false
  explanation: "False. 3-SAT is NP-complete — just as hard as general SAT. Restricting clause size to 3 does not reduce the fundamental computational hardness. In fact, the restriction goes the other direction from making things easier: Cook's theorem proves general SAT is NP-complete, and then a separate reduction shows that even with the structural constraint of exactly 3 literals per clause, the problem remains NP-complete. The number of literals per clause does not determine hardness for k ≥ 3."

- question: "For random 3-SAT instances, the hardest instances to solve in practice occur near the satisfiability threshold (m/n ≈ 4.27), where the probability of satisfiability transitions sharply from near-1 to near-0."
  type: true-false
  answer: true
  explanation: "True. This phase transition is one of the most striking empirical findings in complexity theory. Below the threshold, almost all random instances are satisfiable and easy to find solutions for. Above it, almost all instances are unsatisfiable and easy to refute. Right at the threshold, instances are balanced between these regimes — the search space has many 'near-solutions' but no actual solutions, forcing solvers to explore deeply before concluding unsatisfiability. This mirrors physical phase transitions and reveals deep structure in the problem's solution landscape."

- question: "Why is 2-SAT solvable in polynomial time while 3-SAT is NP-complete? What structural property of 2-SAT enables an efficient algorithm?"
  type: short-answer
  answer: "Each 2-SAT clause (a ∨ b) is logically equivalent to two implications: ¬a → b and ¬b → a. Collecting all such implications creates a directed implication graph, and the formula is satisfiable iff no variable x and its negation ¬x belong to the same strongly connected component (SCC) — meaning the same truth value is forced for both x and ¬x, a contradiction. SCCs can be found in linear time with Tarjan's or Kosaraju's algorithm. 3-SAT clauses do not decompose into implications between individual literals in this way, so the implication graph approach breaks down and no polynomial algorithm is known."
  explanation: "The key is that 2-clause implications have a linear, chainable structure that the SCC algorithm can exploit globally in one pass. 3-literal clauses create more complex logical dependencies that cannot be captured by a simple directed graph of pairwise implications. The jump from 2 to 3 is the complexity-theoretic cliff: at k=2, the implication structure is exploitable; at k=3, the interaction between literals becomes rich enough to encode arbitrary computational problems, which is exactly what NP-completeness means."
```

## Explainer

You already know that the Boolean satisfiability problem (SAT) asks whether a propositional formula in conjunctive normal form (CNF) has a satisfying assignment, and that SAT is NP-complete — the first problem proven to be so via Cook's theorem. **3-SAT** takes this general problem and adds a structural constraint: every clause must contain exactly three literals. A typical 3-SAT instance looks like `(x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ x₄ ∨ x₂) ∧ ...` where each parenthesized group has exactly three terms. The surprising result is that this restricted version is *still* NP-complete — limiting clauses to three literals does not make the problem meaningfully easier.

Why does 3-SAT matter so much in complexity theory? Because it is the workhorse of NP-completeness reductions. When you want to prove a new problem is NP-complete, you typically reduce *from* 3-SAT rather than from general SAT. The fixed clause size of three makes the reduction machinery simpler and more uniform — you always know exactly what the source structure looks like. Most of the hundreds of known NP-completeness proofs go through 3-SAT as an intermediate step, making it arguably the most useful single problem in the NP-completeness toolkit.

The picture changes dramatically when you shrink the clause size to two. **2-SAT** — where every clause has exactly two literals — is solvable in polynomial time. The key insight is that each 2-SAT clause `(a ∨ b)` is logically equivalent to the implications `¬a → b` and `¬b → a`. Collecting all such implications creates a directed **implication graph**, and the formula is satisfiable if and only if no variable and its negation belong to the same strongly connected component. This can be checked in linear time. So the jump from k = 2 to k = 3 is where the complexity-theoretic cliff occurs: 2-SAT is in P, while k-SAT for any k ≥ 3 is NP-complete.

There is also a fascinating empirical phenomenon. For random 3-SAT instances with `n` variables and `m` clauses, the ratio `m/n` controls difficulty. Below a critical threshold (approximately 4.27 for 3-SAT), almost all random instances are satisfiable and easy to solve. Above it, almost all are unsatisfiable and easy to refute. Right at the threshold — the **phase transition** — instances are hardest, often requiring exponential search time in practice. This mirrors phase transitions in physics (like water freezing at 0°C) and reveals deep structural properties of the problem landscape that inform both algorithm design and our understanding of computational hardness.
