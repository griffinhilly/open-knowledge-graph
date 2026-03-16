---
id: np-completeness-theorem
title: NP-Completeness and the Cook-Levin Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: cook-levin-theorem-formal
  type: hard
- id: np-hardness
  type: hard
builds-toward:
- sat-canonical-problem
- three-sat-reductions
tags:
- np-completeness
- cook-levin
- sat
- completeness
stage: advanced
status: draft
---

# NP-Completeness and the Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem proves that Boolean satisfiability (SAT) is NP-complete: every NP problem reduces to SAT, and SAT is in NP. This provides the first NP-complete problem; all other NP-complete problems are discovered by reducing from previously known NP-complete problems, creating a network of reductions.

## How It's Best Learned
Carefully study the Cook-Levin proof structure: how an NP Turing machine is encoded in a Boolean formula. Work through simplified reductions (e.g., CLIQUE → 3-SAT).

## Common Misconceptions
- Missing why Cook-Levin is a breakthrough: it provides the first NP-complete problem, enabling all subsequent reductions.
- Assuming Cook-Levin applies uniformly to other problems. It specifically handles SAT; other completeness proofs reduce from known NP-complete problems.

## Explainer

You already understand what NP-hardness means and what the Cook-Levin theorem says. Now it is time to see why those two things together produce an extraordinary structural result about computation. A problem is **NP-complete** if it is both in NP (it can be verified in polynomial time) and NP-hard (every NP problem reduces to it in polynomial time). The Cook-Levin theorem shows that SAT — Boolean satisfiability — is NP-complete. This is not a routine observation; it is the theorem that turned NP-hardness from a definition into a usable tool.

The proof of Cook-Levin works by encoding computation as Boolean formulas. Given any NP problem with verifier V running in polynomial time p(n), Cook-Levin constructs a formula φ such that: the input x is a yes-instance if and only if φ is satisfiable. The formula encodes the entire tableau of V's computation — the state of the machine at each time step — as Boolean variables, with clauses enforcing valid transitions, input consistency, and acceptance. The formula is polynomial in size because V runs in polynomial time. What makes this remarkable is that it works for *every* NP problem simultaneously: each such problem's verifier produces a different formula, but the construction is uniform. SAT is therefore the "receptacle" that absorbs all of NP.

The consequence is a chain reaction. Once SAT is known to be NP-complete, proving any other problem X is NP-complete requires only: (1) showing X is in NP, and (2) giving a polynomial-time reduction from SAT (or from any already-known NP-complete problem) to X. This is far easier than repeating the full Cook-Levin tableau construction. The direction matters: to show X is NP-hard, reduce a known hard problem *to* X, not the other way around. If SAT → X in polynomial time and SAT is hard, then X must be at least as hard. Over fifty years of research has produced hundreds of NP-complete problems this way — graph problems, scheduling problems, packing problems — all linked by this reduction network.

The deepest implication is what NP-completeness says about the entire complexity class. If any single NP-complete problem is in P — if any one of them can be solved in polynomial time — then every problem in NP is also in P, because the reduction chain collapses: solve any NP problem by reducing it to your one easy NP-complete problem. Conversely, if any NP-complete problem is provably not in P, then P ≠ NP. The P vs NP question is therefore equivalent to asking whether any one NP-complete problem is tractable. Cook-Levin turned an open question about the structure of computation into a question you can attack by studying any single combinatorial problem.
