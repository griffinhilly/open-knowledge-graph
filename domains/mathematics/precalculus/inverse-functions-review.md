---
id: inverse-functions-review
title: Inverse Functions Review
domain: mathematics
course: precalculus
prerequisites:
- id: function-notation-review
  type: hard
- id: domain-and-range
  type: hard
- id: composition-of-functions-advanced
  type: soft
builds-toward:
- inverse-trigonometric-functions
- derivatives-of-logarithmic-functions
tags:
- functions
- inverses
- one-to-one
stage: formal-systems
status: validated
---
# Inverse Functions Review

## Core Idea
An inverse function f^(-1) reverses the action of f: if f(a) = b, then f^(-1)(b) = a. A function has an inverse if and only if it is one-to-one (passes the horizontal line test). The domain of f becomes the range of f^(-1) and vice versa. Graphically, f and f^(-1) are reflections across the line y = x. Inverse functions are the foundation for logarithms, inverse trig functions, and solving equations.

## How It's Best Learned
Start with simple examples (linear functions), find inverses algebraically by swapping x and y and solving, then verify by composing f(f^(-1)(x)) = x. Use the horizontal line test to determine invertibility, and discuss restricting domains to create invertible functions.

## Common Misconceptions
- Confusing f^(-1)(x) with 1/f(x): inverse function vs. reciprocal.
- Forgetting to swap domain and range when finding the inverse.
- Assuming all functions have inverses without checking one-to-one.

## Explainer

You know from your study of function notation that a function f takes an input x and produces an output f(x). An **inverse function** f⁻¹ does exactly the reverse: it takes the output of f and recovers the original input. Formally, if f(a) = b, then f⁻¹(b) = a. This is not about reciprocals — f⁻¹(x) is not 1/f(x) — it's about undoing. If f multiplies by 3, then f⁻¹ divides by 3. If f adds 5, then f⁻¹ subtracts 5. If f takes a square (with appropriate domain), f⁻¹ takes a square root.

The critical question is: when does an inverse exist? Here, your knowledge of domain and range becomes essential. A function can only be inverted if it is **one-to-one**: every output comes from exactly one input. If two different inputs produced the same output, which one would the inverse recover? It cannot do both. The geometric test is the **horizontal line test** — if any horizontal line crosses the graph more than once, the function is not one-to-one and has no inverse (over that full domain). The standard function f(x) = x² fails this test over all reals (since f(2) = f(−2) = 4), but succeeds if you restrict the domain to x ≥ 0 — which is exactly how the square root function is defined as the inverse of the "right half" of the parabola.

To find the inverse algebraically: write y = f(x), then swap x and y (since the inverse reverses the roles of input and output), and solve for y. That expression in y is f⁻¹(x). The domain of f⁻¹ is the range of f, and the range of f⁻¹ is the domain of f — they swap. You can always verify: the composition f(f⁻¹(x)) = x and f⁻¹(f(x)) = x should both hold (wherever defined). This composition identity is the *definition* of what it means for two functions to be inverses of each other.

Graphically, f and f⁻¹ are reflections of each other across the line y = x. This is because swapping x and y in the equation is precisely the algebraic description of reflecting across y = x. If the point (2, 5) is on the graph of f, then (5, 2) is on the graph of f⁻¹. This visual symmetry is a powerful check: if the graph of f doesn't look like a reflection of the graph of f⁻¹ across y = x, something has gone wrong.

This topic is the conceptual prerequisite for two major upcoming ideas. Logarithms are the inverse functions of exponentials — log_b(x) asks "what power of b gives x?" — and inverse trigonometric functions like arcsin, arccos, arctan are inverses of the trig functions restricted to appropriate domains. Every time you solve an equation by "undoing" an operation — taking a log of both sides, applying arcsin to isolate an angle — you are using inverse functions. Understanding the one-to-one requirement now prevents confusion later about why arcsin(sin(x)) ≠ x for all x.
