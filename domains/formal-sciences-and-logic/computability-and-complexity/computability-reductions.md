---
id: computability-reductions
title: Computability Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines
  type: hard
- id: halting-problem
  type: soft
- id: injective-surjective-bijective
  type: soft
builds-toward:
- rices-theorem
- re-and-co-re-languages
- polynomial-time-reductions
tags:
- reductions
- undecidability
- computability
- many-one-reducibility
stage: advanced
status: draft
---

# Computability Reductions

## Core Idea
A many-one reduction from problem A to problem B is a computable function f such that x ∈ A if and only if f(x) ∈ B. If such a reduction exists, B is 'at least as hard' as A: any algorithm for B can be used to solve A. Reductions are the primary tool for proving undecidability — to show a new problem is undecidable, reduce the halting problem to it. Turing reductions (oracle reductions) are more general and allow multiple adaptive queries, measuring relative computability rather than mere hardness.

## How It's Best Learned
Practice constructing explicit reduction functions on concrete problem pairs. A useful exercise: show that the acceptance problem (does TM M accept input w?) reduces to the halting problem and vice versa, establishing their Turing equivalence.

## Common Misconceptions
- Reduction direction is easy to confuse: to show B is hard, reduce a known-hard problem A *to* B, not B to A.
- Many-one reductions are stricter than Turing reductions; a Turing reduction allows multiple queries to an oracle while many-one allows exactly one.
