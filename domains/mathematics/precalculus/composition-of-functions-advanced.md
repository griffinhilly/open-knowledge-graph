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
status: validated
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

## Explainer

**Function composition** is how you build complex processes out of simpler ones by chaining them together. You already know from function notation that a function f takes an input x and produces an output f(x). Composition simply says: take the output of one function and feed it as the input to another. Written (f ∘ g)(x) = f(g(x)), you first apply g, then apply f to whatever g produced. Think of it as a two-stage pipeline: input → g → g(x) → f → f(g(x)).

The order matters critically. f(g(x)) and g(f(x)) are different functions — composition is generally **not commutative**. A concrete example: let f(x) = x² and g(x) = x + 3. Then f(g(x)) = f(x + 3) = (x + 3)² = x² + 6x + 9, but g(f(x)) = g(x²) = x² + 3. These are different functions entirely. The inner function executes first; the outer function sees only the output of the inner one. Getting the order straight is the single most important skill in composition.

**Domain restrictions** are where composition gets subtle, and where your prerequisite knowledge of domain and range becomes essential. The composition f(g(x)) is only defined at x values where (a) g(x) is defined, and (b) g(x) falls within the domain of f. If g(x) = √x (defined only for x ≥ 0) and f(x) = 1/(x − 2) (undefined at x = 2), then f(g(x)) = 1/(√x − 2) has two restrictions: x ≥ 0 from g's domain, and √x ≠ 2, i.e., x ≠ 4, from f's restriction. Always check both sources of domain trouble.

The most important reason to master composition is the **chain rule** in calculus — arguably the most frequently used rule in all of differentiation. The chain rule says that if h(x) = f(g(x)), then h′(x) = f′(g(x)) · g′(x). But to apply it, you must first recognize that a given function is a composition, and identify which piece is the outer function f and which is the inner function g. For example, h(x) = sin(x²) decomposes as f(u) = sin(u) and g(x) = x². Being able to decompose "inside-out" — to look at a complicated expression and name its layers — is exactly the skill to practice now, before calculus demands it.
