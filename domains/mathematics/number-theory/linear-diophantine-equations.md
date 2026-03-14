---
id: linear-diophantine-equations
title: Linear Diophantine Equations
domain: mathematics
course: number-theory
prerequisites:
- id: bezout-identity
  type: hard
- id: modular-arithmetic
  type: soft
builds-toward:
- pells-equation
tags:
- diophantine
- linear-equations
- integer-solutions
stage: advanced
status: draft
---

# Linear Diophantine Equations

## Core Idea
A linear Diophantine equation ax + by = c has integer solutions if and only if gcd(a,b) divides c. When solutions exist, there are infinitely many, parameterized by one particular solution and the homogeneous solution space.

## How It's Best Learned
Determine solvability using gcd. Find one solution via extended Euclidean algorithm, then parameterize all solutions. Verify by substitution.

## Common Misconceptions
Not all linear equations in two variables have integer solutions (solvability requires the gcd condition). Confusing the parameterization formula.
