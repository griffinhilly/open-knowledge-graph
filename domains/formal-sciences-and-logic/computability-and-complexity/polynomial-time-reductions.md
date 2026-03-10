---
id: polynomial-time-reductions
title: Polynomial-Time Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: time-complexity-classes
  type: hard
- id: computability-reductions
  type: soft
builds-toward:
- np-completeness
- cook-levin-theorem
tags:
- reductions
- polynomial-time
- complexity
- NP-hardness
stage: advanced
status: draft
---

# Polynomial-Time Reductions

## Core Idea
A polynomial-time many-one reduction (Karp reduction) from problem A to problem B is a polynomial-time computable function f such that x ∈ A iff f(x) ∈ B. If B has a polynomial-time algorithm, so does A. Polynomial-time reductions are the standard tool for proving NP-hardness: to show a new problem B is NP-hard, reduce a known NP-hard problem to B in polynomial time. This preserves computational hardness upward and solutions downward, enabling systematic comparison of complexity.

## How It's Best Learned
Master the 3-SAT to 3-Colorability reduction as a template: understand both the formal gadget construction and why it is correct. Practice building reductions from 3-SAT to other NP-complete problems, always verifying correctness and polynomial-time running time.

## Common Misconceptions
- The direction of reduction is crucial and often backwards from intuition: to show B is hard, reduce a known-hard problem *to* B, which shows B must be at least as hard.
- Polynomial-time reductions are more restrictive than Turing reductions used in computability theory; they do not allow multiple adaptive queries.
