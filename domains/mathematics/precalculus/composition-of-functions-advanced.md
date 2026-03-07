---
id: composition-of-functions-advanced
title: Composition of Functions — Advanced
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
  - id: domain-and-range
    type: soft
builds-toward:
  - chain-rule
  - inverse-functions-review
tags: [functions, composition]
stage: formal-systems
status: draft
---

# Composition of Functions

## Core Idea
The composition (f composed with g)(x) = f(g(x)) feeds the output of g into f. It creates a new function by chaining two functions together. The domain of f(g(x)) is restricted to inputs x where g(x) is defined and g(x) is in the domain of f. Composition is the conceptual foundation for the chain rule in calculus, which is arguably the most important derivative rule.

## How It's Best Learned
Start by evaluating compositions at specific numbers: find f(g(2)) step by step. Then form the algebraic expression f(g(x)). Practice decomposing composite functions (given h(x), find f and g such that h = f composed with g), as this skill is essential for the chain rule.

## Common Misconceptions
- Confusing f(g(x)) with f(x) * g(x) (composition is not multiplication).
- Assuming f(g(x)) = g(f(x)): composition is generally not commutative.
- Forgetting domain restrictions inherited from the inner function.
