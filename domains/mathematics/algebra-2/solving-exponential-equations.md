---
id: solving-exponential-equations
title: Solving Exponential Equations
domain: mathematics
course: algebra-2
prerequisites:
  - id: logarithm-properties
    type: hard
  - id: exponential-functions-and-graphs
    type: hard
builds-toward:
  - natural-logarithm-and-e
  - calculus-applications
tags: [exponential, equations, logarithms, solving]
stage: abstract-reasoning
status: draft
---

# Solving Exponential Equations

## Core Idea
Exponential equations have the variable in the exponent. Two main strategies: (1) If both sides can be written with the same base, set exponents equal (e.g., 2^x = 8 becomes 2^x = 2^3, so x = 3). (2) If not, take the logarithm of both sides and use log properties to isolate the variable (e.g., 3^x = 20 becomes x = log(20)/log(3)). Strategy 2 is the general method and works for all cases.

## How It's Best Learned
Start with equations solvable by rewriting with a common base. Then introduce the "take log of both sides" technique for equations that cannot be simplified to a common base. Practice with various bases including e. Apply to real-world problems (population doubling time, radioactive decay half-life).

## Common Misconceptions
- Trying to "bring down" the exponent without taking a logarithm first.
- Distributing log across addition: log(2^x + 5) != x*log(2) + log(5).
- Forgetting that log(both sides) requires both sides to be positive.
- Confusing e^x = 5 (take ln of both sides) with ln(x) = 5 (exponentiate both sides).
