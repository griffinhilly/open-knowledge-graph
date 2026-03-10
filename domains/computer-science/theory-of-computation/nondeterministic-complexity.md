---
id: nondeterministic-complexity
title: Nondeterministic Time Complexity and NP
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: turing-machine-variants
  type: soft
- id: nondeterministic-finite-automata
  type: soft
builds-toward:
- p-vs-np-problem
- np-completeness
tags:
- NP
- nondeterministic
- verifier
- certificate
- complexity
stage: advanced
status: draft
---

# Nondeterministic Time Complexity and NP

## Core Idea
NP is the class of decision problems solvable by a nondeterministic TM in polynomial time, equivalently the problems whose solutions can be *verified* in polynomial time given a certificate (witness). The two definitions are equivalent: a nondeterministic TM 'guesses' a certificate and verifies it. NP contains P (any polynomial-time solution is also a polynomial-time certificate) and includes many natural combinatorial problems: satisfiability, Hamiltonian path, graph coloring, and subset sum. Whether NP equals P is the most famous open problem in mathematics.

## How It's Best Learned
For each NP problem, identify the certificate explicitly (e.g., for 3-SAT: a satisfying assignment; for Hamiltonian path: the path itself) and verify it checks in polynomial time. This grounds the abstract definition in concrete examples.

## Common Misconceptions
- Confusing NP with 'not polynomial' — NP does not stand for 'non-polynomial'; it stands for 'nondeterministic polynomial'.
- Thinking NP problems have no polynomial-time algorithms — it is unknown whether P = NP; some NP problems might be in P.
- Assuming verification being easy implies solving is hard — this is the P vs NP question, not an established fact.
