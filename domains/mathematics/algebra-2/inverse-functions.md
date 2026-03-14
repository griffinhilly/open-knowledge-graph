---
id: inverse-functions
title: Inverse Functions
domain: mathematics
course: algebra-2
prerequisites:
- id: function-notation-review
  type: hard
- id: equations-variables-both-sides
  type: hard
- id: composition-of-functions
  type: soft
builds-toward:
- logarithms-intro
- radical-functions-and-graphs
tags:
- functions
- inverse
- one-to-one
- horizontal-line-test
stage: abstract-reasoning
status: validated
---
# Inverse Functions

## Core Idea
The inverse function f^(-1) "undoes" f: if f(a) = b, then f^(-1)(b) = a. Graphically, f and f^(-1) are reflections over the line y = x. A function has an inverse if and only if it is one-to-one (passes the horizontal line test). To find f^(-1) algebraically: swap x and y in y = f(x), then solve for y. The composition f(f^(-1)(x)) = x and f^(-1)(f(x)) = x verifies the inverse relationship.

## How It's Best Learned
Start with simple examples: if f(x) = 2x + 3, find f^(-1)(x) by swapping and solving. Verify by composition. Use the horizontal line test to determine invertibility. Graph functions and their inverses to see the y = x reflection. Discuss restricting domains to create invertible functions (e.g., restricting x^2 to x >= 0).

## Common Misconceptions
- Confusing f^(-1)(x) with 1/f(x) (inverse function vs. reciprocal).
- Thinking every function has an inverse (only one-to-one functions do).
- Forgetting to swap x and y before solving.
- Not restricting the domain when needed (e.g., finding the inverse of x^2 without specifying x >= 0).
