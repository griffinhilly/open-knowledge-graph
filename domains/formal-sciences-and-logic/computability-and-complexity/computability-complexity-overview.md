---
id: computability-complexity-overview
title: 'Computability and Complexity: Overview and Connections'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: mu-recursive-functions
  type: soft
builds-toward:
- formal-computational-models
- undecidable-problems-examples
- complexity-class-definitions-hierarchy
tags:
- overview
- foundations
- computability
- complexity-theory
stage: advanced
status: draft
---
# Computability and Complexity: Overview and Connections

## Core Idea
Computability theory asks which problems can be solved algorithmically at all (decidability), while complexity theory asks which solvable problems can be solved efficiently. Together, they form the foundations of theoretical computer science, connecting mathematical logic to questions about practical computation limits.

## How It's Best Learned
Start with a high-level chronology: early undecidable problems, then complexity results starting from P vs NP. Connecting Gödel's incompleteness theorems to uncomputability helps build intuition.

## Common Misconceptions
- Confusing undecidable with hard-to-compute. Undecidable problems don't have algorithms at all, not even slow ones.
- Thinking P vs NP solves computability: P and NP are about efficient computation, not all computation.

## Explainer

The field of theoretical computer science begins with a question that preceded computers themselves: what can be computed at all? Alan Turing answered this in 1936 by defining a model of computation — the Turing machine — and showing that some problems cannot be solved by any algorithm whatsoever. This is the domain of **computability theory**: it identifies the outer boundary of algorithmic possibility, independent of time, space, or hardware. The classic example is the **halting problem**: no algorithm can correctly decide, for all program-input pairs, whether the program halts or runs forever. This is not a practical limitation — it is a mathematical impossibility, proved by a diagonal argument that constructs a program that contradicts any hypothetical decider.

Once we know a problem is computable, a second question arises: how *efficiently* can it be computed? This is the domain of **complexity theory**, which developed in the 1960s and 1970s. Complexity theory partitions decidable problems by the resources — primarily time and memory space — they require as input size grows. The complexity class **P** contains problems solvable in polynomial time; **NP** contains problems whose solutions can be *verified* in polynomial time. The central open question — whether P = NP — asks whether efficient verification always implies efficient solution. Most researchers believe P ≠ NP, but no proof exists either way.

The two fields share deep structural connections. Both use **diagonalization** — the technique Turing used to show the halting problem is undecidable — as a key proof method; the same idea yields the time and space hierarchy theorems in complexity. Both fields rely on **reductions**: transformations that convert one problem to another, preserving difficulty. In computability, many-one reductions define relative undecidability (if A reduces to B and A is undecidable, so is B). In complexity, polynomial-time reductions define NP-completeness. The Turing machine model is the foundation of both: computability asks whether a TM halts on a given input; complexity asks how quickly.

A useful mental map: imagine problems arranged by solvability. The outermost region is **undecidable** problems — no algorithm exists. Inside is the decidable region. Within that, the efficiently solvable ones form **P**. Complexity theory maps the interior of the decidable region in fine detail — PSPACE, the exponential classes, the NP-complete problems clustered on the boundary of P. Computability draws the outer boundary; complexity theory surveys the interior. Together they answer both halves of the fundamental question: what can be computed, and at what cost?
