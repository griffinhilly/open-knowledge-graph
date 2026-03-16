---
id: sat-canonical-problem
title: 'Satisfiability Problem: The Canonical NP-Complete Problem'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
builds-toward:
- three-sat-reductions
tags:
- satisfiability
- boolean-satisfiability
- sat-solvers
- completeness
stage: advanced
status: draft
---

# Satisfiability Problem: The Canonical NP-Complete Problem

## Core Idea
The Boolean satisfiability problem (SAT) asks whether a Boolean formula has an assignment making it true. SAT is the prototypical NP-complete problem and appears across logic, AI, hardware verification, and combinatorics. The complexity of SAT directly connects to fundamental questions about problem-solving and the limits of efficient computation.

## How It's Best Learned
Experiment with SAT solvers (e.g., MiniSat) on small instances. Convert a graph coloring instance to SAT to see the encoding.

## Explainer

You know NP-completeness: a problem is NP-complete if it is in NP *and* every NP problem reduces to it in polynomial time. SAT — the Boolean satisfiability problem — is the canonical example, historically the first proved NP-complete (Cook, 1971; Levin, 1973), and the starting point for the vast web of NP-completeness reductions that followed.

**SAT** asks: given a Boolean formula φ over variables x₁, ..., xₙ with connectives ∧, ∨, ¬, does any truth-value assignment to the variables make φ evaluate to true? For example, (x₁ ∨ ¬x₂) ∧ (¬x₁ ∨ x₂) is satisfiable (set x₁ = x₂ = T), while (x₁) ∧ (¬x₁) is not. The certificate for membership in SAT is just the satisfying assignment — easy to verify in linear time by evaluating the formula. So SAT is in NP.

That SAT is NP-*hard* — that every NP problem reduces to SAT — is the deep claim, proved by the Cook-Levin theorem. The proof encodes any nondeterministic Turing machine computation as a Boolean formula: variables represent the machine's configuration (tape content, head position, state) at each of polynomially many time steps, and the formula asserts that the transitions are valid and the computation accepts. This encoding is polynomial in the input size. Because every NP problem has such an NTM computation, every NP problem has a polynomial-time reduction to SAT. SAT is thus a universal language for NP: it can express any NP problem.

In practice, modern **SAT solvers** (MiniSat, CryptoMiniSat, Z3) are remarkably powerful despite the theoretical hardness. They use the DPLL algorithm enhanced with **conflict-driven clause learning (CDCL)** — when a partial assignment leads to a contradiction, the solver learns a new clause that prunes future search. Industrial instances with millions of variables in hardware verification, automated planning, cryptanalysis, and program synthesis are routinely solved. Understanding SAT in both its theoretical (NP-completeness, reductions from other problems) and practical (solver algorithms, phase transitions near the satisfiability threshold) aspects gives you the central problem around which complexity theory and automated reasoning both revolve.
