---
id: time-complexity-classes
title: 'Time Complexity Classes: P and EXPTIME'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: time-space-complexity
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
builds-toward:
- nondeterministic-complexity
- space-complexity-classes
tags:
- P
- EXPTIME
- complexity
- polynomial-time
- time-complexity
stage: advanced
status: validated
---

# Time Complexity Classes: P and EXPTIME

## Core Idea
The class P consists of all decision problems solvable by a deterministic TM in polynomial time O(nᵏ) for some constant k. P captures problems that are 'efficiently solvable' and includes sorting, shortest paths, primality testing, and linear programming. EXPTIME contains problems solvable in exponential time 2^poly(n); it strictly contains P. Basing complexity on TM running time formalizes the intuitive notion of tractability. The polynomial-time model is robust across reasonable machine models — polynomial in one is polynomial in another.

## How It's Best Learned
Classify known algorithms into P: sorting is O(n log n) ⊆ P, BFS/DFS is O(V+E) ⊆ P. Then encounter problems (chess, exponential-search problems) known to require exponential time. This calibrates the P boundary.

## Common Misconceptions
- Thinking P means 'fast' in practice — O(n¹⁰⁰) is in P but completely impractical.
- Confusing EXPTIME with 'undecidable' — EXPTIME problems are decidable, just slow.

## Explainer

From your study of Turing machines and algorithm analysis, you know that some problems are computable and some are not. **Time complexity classes** refine the computable problems by asking: how much time does the fastest algorithm need? The class **P** (polynomial time) contains every decision problem — every yes-or-no question — that a deterministic Turing machine can solve in time O(nᵏ) for some fixed constant k, where n is the input size. Sorting an array, finding shortest paths in a graph, testing whether a number is prime, and solving linear programs are all in P.

The significance of P is not that polynomial algorithms are always fast in practice — O(n¹⁰⁰) is technically polynomial but useless. Rather, P captures a robust notion of **tractability** that is independent of the specific computational model. A problem solvable in polynomial time on a single-tape Turing machine is also polynomial on a multi-tape machine, a RAM machine, or any other reasonable deterministic model. The exponent and constants may change, but the polynomial boundary holds. This **robustness** is what makes P a meaningful theoretical class rather than an artifact of one particular machine definition.

**EXPTIME** contains problems solvable in time 2^p(n) for some polynomial p(n). Unlike the relationship between many complexity classes, we can prove that P ⊊ EXPTIME — P is strictly contained in EXPTIME. This is established by diagonalization and the time hierarchy theorem, which shows that giving a Turing machine substantially more time allows it to solve strictly more problems. Concrete EXPTIME-complete problems include determining the winner of generalized chess, checkers, or Go on an n×n board — games where the enormous branching factor and game length provably require exponential exploration.

Between P and EXPTIME lies the landscape where the most famous open questions in computer science reside. The class NP (which you will study next as nondeterministic polynomial time) sits between P and EXPTIME, and the P vs. NP question asks whether efficient verification of solutions implies efficient discovery of solutions. For now, the key conceptual takeaway is the hierarchy: some decidable problems are efficiently solvable (P), some require exponential time (EXPTIME-complete), and the time hierarchy theorem guarantees that more time genuinely means more computational power. Undecidable problems like the halting problem sit entirely outside this framework — they cannot be solved in any amount of time, no matter how generous.
