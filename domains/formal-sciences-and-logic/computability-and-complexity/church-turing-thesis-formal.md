---
id: church-turing-thesis-formal
title: The Church-Turing Thesis
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: soft
- id: general-recursive-functions
  type: soft
- id: functions-and-function-properties
  type: soft
- id: recursion-on-finite-structures
  type: soft
- id: set-fundamentals
  type: soft
builds-toward:
- halting-problem-formal
- computability-reductions
tags:
- computability
- philosophy-of-computation
- models-of-computation
stage: advanced
status: validated
---

# The Church-Turing Thesis

## Core Idea
The Church-Turing thesis is the informal claim that every effectively computable function — any function a human could compute by following a definite mechanical procedure — is computable by a Turing machine. It is a thesis, not a theorem, because 'effectively computable' cannot be formally defined without circularity. The robustness of the thesis is supported by the fact that Turing machines, lambda calculus, recursive functions, register machines, and all other proposed models of computation have been proven to compute exactly the same class of functions.

## How It's Best Learned
Study the historical context: Church proposed lambda calculus, Turing proposed Turing machines, and Kleene proposed recursive functions, all independently in the 1930s, and they were shown equivalent. Then consider hypothetical counterexamples (hypercomputation, quantum computation) and why none have succeeded in surpassing the Church-Turing bound.

## Common Misconceptions
- The thesis does not claim every physically realizable process is Turing-computable — it specifically concerns idealized mechanical procedures.
- It is not provably false by definition; it is an empirical generalization subject to revision if a more powerful but still 'mechanical' model were discovered.
