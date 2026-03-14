---
id: formal-computational-models
title: 'Formal Models of Computation: Turing Machines and Lambda Calculus'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: church-turing-thesis-formal
  type: hard
builds-toward:
- recursive-languages
- recursively-enumerable-languages
- turing-degrees-equivalence
tags:
- computation
- turing-machines
- lambda-calculus
- church-turing
stage: advanced
status: draft
---

# Formal Models of Computation: Turing Machines and Lambda Calculus

## Core Idea
Turing machines and the lambda calculus are formal models that formalize the intuitive notion of 'algorithm' and 'computable function'. The Church-Turing thesis asserts that these models, despite superficial differences, capture exactly the same class of computable functions—those computable by any reasonable mechanical process.

## How It's Best Learned
Study Turing machines and lambda calculus in parallel; show explicit translations between them. Implement a simple Turing machine simulator to build intuition.

## Common Misconceptions
- Assuming Turing completeness means all Turing-complete systems solve the same problems equally fast. They compute the same functions, not with the same complexity.
- Overlooking that Church-Turing thesis is not a theorem; it's a conjecture about what 'computable' means.
