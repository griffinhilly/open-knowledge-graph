---
id: sat-and-np-complete-problems
title: Boolean Satisfiability and Standard NP-Complete Problems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: cook-levin-theorem-formal
  type: hard
builds-toward:
- np-completeness-reduction-proof-techniques
tags:
- SAT
- NP-completeness
- hard-problems
stage: advanced
status: draft
---

# Boolean Satisfiability and Standard NP-Complete Problems

## Core Idea
SAT (Boolean satisfiability) is NP-complete by the Cook-Levin theorem: any NP problem reduces to SAT in polynomial time. Other canonical NP-complete problems—3-SAT, independent set, vertex cover, Hamiltonian path—form a landscape of computationally hard problems. Solving SAT efficiently would imply P = NP and break modern cryptography.

## Explainer

From the Cook-Levin theorem you already know that SAT is NP-complete: any nondeterministic polynomial-time computation can be encoded as a Boolean formula, so SAT captures the hardest problems in NP. But the Cook-Levin proof produces complicated formulas — exponentially large circuits of gates. In practice, nearly everything in complexity theory reduces not directly from SAT but from a simplified variant: **3-SAT**, where every clause has *exactly three literals*. The reduction from SAT to 3-SAT is a key exercise: replace a clause with k > 3 literals by introducing fresh auxiliary variables and a chain of 3-literal clauses that is satisfiable iff the original was. 3-SAT is easier to reduce *from* than SAT because its structure is rigid and uniform, making it the primary workhorse for NP-completeness proofs.

The landscape of NP-complete problems is built by a web of polynomial-time reductions. **Independent set** asks: does a graph contain k vertices with no edge between any pair? **Vertex cover** asks: do k vertices touch every edge? These two are complementary — S is an independent set iff the complement V \ S is a vertex cover — so they reduce to each other trivially. **Clique** — does the graph contain a complete subgraph on k vertices? — reduces to independent set by complementing the graph. **Hamiltonian path** and **Hamiltonian cycle** ask whether a graph has a path or cycle visiting every vertex exactly once, and these reduce from 3-SAT by gadget constructions that force the Hamiltonian path to "choose" truth assignments. **Subset sum** — can a subset of integers sum to a target T? — is NP-complete too, showing that number-theoretic problems are not inherently easier than graph problems.

The unifying principle behind all these reductions is that **hardness transfers**: if problem A reduces to problem B, then B is at least as hard as A. Once you know 3-SAT is NP-complete, proving that a new problem X is NP-complete requires only (1) showing X is in NP (exhibit a polynomial-time verifier) and (2) showing 3-SAT (or any NP-complete problem) reduces to X in polynomial time. You pick whichever NP-complete problem is most convenient to reduce from. The skill in NP-completeness proofs is designing reduction gadgets that faithfully translate the source problem's structure into the target problem's language.

The practical consequence is stark. If any NP-complete problem were solvable in polynomial time, every NP problem would be — including factoring large integers and breaking RSA. Modern cryptography, blockchain systems, and secure communication rely on the assumed hardness of NP problems (or problems believed to be at least as hard). Solving SAT efficiently would unravel cryptographic security across the internet. This is why NP-completeness is not an abstract curiosity but a load-bearing pillar of both theoretical computer science and practical security.
