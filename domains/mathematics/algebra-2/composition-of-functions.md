---
id: composition-of-functions
title: Composition of Functions
domain: mathematics
course: algebra-2
prerequisites:
  - id: function-notation-review
    type: hard
builds-toward:
  - inverse-functions
  - chain-rule
tags: [functions, composition, substitution]
stage: abstract-reasoning
status: validated
---

# Composition of Functions

## Core Idea
The composition of f and g, written (f o g)(x) = f(g(x)), means applying g first, then applying f to the result. Composition is not commutative: f(g(x)) is generally different from g(f(x)). The domain of f o g is all x in the domain of g such that g(x) is in the domain of f. Composition is the foundation for understanding inverse functions, the chain rule in calculus, and function decomposition.

## How It's Best Learned
Start by evaluating compositions at specific values: if f(x) = x^2 and g(x) = x+1, find f(g(3)) step by step. Then find the composition formula f(g(x)). Practice both f(g(x)) and g(f(x)) to demonstrate non-commutativity. Discuss domain restrictions. Decompose complex functions into compositions of simpler ones.

## Common Misconceptions
- Thinking f(g(x)) = f(x) * g(x) (composition is not multiplication).
- Assuming f(g(x)) = g(f(x)) (composition is not commutative).
- Applying the functions in the wrong order (in f(g(x)), g is applied first).
- Not considering domain restrictions on the composition.
