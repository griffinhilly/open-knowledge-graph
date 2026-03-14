---
id: np-and-polynomial-time
title: NP and Polynomial-Time Verification
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: nondeterministic-turing-machines
  type: hard
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
builds-toward:
- np-completeness-formal
- polynomial-time-reductions
- cook-levin-theorem-formal
- probabilistic-computation
tags:
- complexity
- NP
- verification
- certificates
stage: advanced
status: validated
---

# NP and Polynomial-Time Verification

## Core Idea
NP (nondeterministic polynomial time) is the class of decision problems for which 'yes' instances have polynomial-length certificates verifiable in polynomial time. Equivalently, NP consists of problems solvable by a nondeterministic TM in polynomial time. Every problem in P is in NP (a certificate is the solution itself), but whether P = NP is the most famous open problem in computer science. NP captures many natural combinatorial search problems including satisfiability, graph coloring, and the traveling salesman problem.

## How It's Best Learned
For each NP problem, identify what the certificate is and write a polynomial-time verifier. For 3-SAT, the certificate is a satisfying assignment; for Hamiltonian Cycle, it is the cycle itself. This verifier-based definition is often more intuitive than the NTM-based definition.

## Common Misconceptions
- NP does not stand for 'non-polynomial' — it stands for 'nondeterministic polynomial.' Problems in NP might or might not have polynomial-time solutions.
- The complement of an NP problem defines co-NP, which is not known to equal NP, and is itself a major open question.
