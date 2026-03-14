---
id: computability-models-equivalence
title: Equivalence of Computational Models
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: church-turing-thesis-formal
  type: hard
- id: turing-machines-formal
  type: hard
- id: lambda-calculus
  type: hard
builds-toward:
- turing-computable-vs-church-computable
- general-recursive-functions
tags:
- computability
- models-of-computation
- church-turing
stage: advanced
status: draft
---

# Equivalence of Computational Models

## Core Idea
Turing machines, lambda calculus, and mu-recursive functions all define the same class of computable functions. This foundational result—the Church-Turing thesis—establishes that no reasonable model of computation can compute anything beyond what Turing machines compute, making computability a robust, model-independent notion.

## How It's Best Learned
Compare the definitions of computation across at least two models (e.g., Turing machines and lambda calculus), then study a concrete encoding of one model into another.

## Common Misconceptions
- Thinking Church-Turing thesis is a proven theorem (it is a thesis about the limits of formal computation).
- Confusing the thesis with the claim that all algorithms can be fast (computability is about existence, not efficiency).
