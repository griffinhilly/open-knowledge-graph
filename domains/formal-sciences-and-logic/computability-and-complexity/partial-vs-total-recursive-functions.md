---
id: partial-vs-total-recursive-functions
title: Partial vs. Total Recursive Functions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: general-recursive-functions
  type: hard
- id: mu-recursive-functions
  type: hard
builds-toward:
- decidability-and-semi-decidability
- halting-problem-formal
tags:
- recursion
- partial-functions
- computability
stage: advanced
status: draft
---

# Partial vs. Total Recursive Functions

## Core Idea
Partial recursive functions (computable by Turing machines) may not halt on all inputs, while total recursive functions halt on every input. Not all computable functions are total: the halting problem shows no total recursive function can predict if an arbitrary program halts. This gap between partial and total computability is foundational to undecidability.

## How It's Best Learned
Write examples of partial functions (e.g., integer division when denominator is computed) and total functions, then study the proof that some total functions are not computable.

## Common Misconceptions
- Assuming a computable partial function can always be extended to a total function.
- Confusing 'total recursive function' with 'algorithm that works' (many algorithms naturally admit partial functions).
