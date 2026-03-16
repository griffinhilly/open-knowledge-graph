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

## Explainer

A **linear Diophantine equation** is simply a linear equation in two (or more) integer unknowns: ax + by = c, where a, b, c are given integers and you seek integer solutions x, y. The word "Diophantine" just signals that only integers count — rational or real solutions are not enough. Your prerequisite, **Bézout's identity**, hands you the key insight: gcd(a, b) can be expressed as an integer linear combination of a and b. This immediately tells you when solutions exist.

The solvability criterion is clean: ax + by = c has integer solutions if and only if gcd(a, b) divides c. Here is why. The set of all integers expressible as ax + by is exactly the set of multiples of gcd(a, b). So c must be a multiple of gcd(a, b) for the equation to work. If gcd(a, b) = d and d does not divide c, there are no solutions at all — not even close ones. If d | c, you can write c = d · (c/d), find a Bézout representation d = ax₀ + by₀ via the extended Euclidean algorithm, and scale: x = x₀·(c/d), y = y₀·(c/d) is one particular solution.

Once you have one solution (x₀, y₀), all solutions follow a pattern. Substituting x = x₀ + t and y = y₀ + s into the equation shows that at(x₀+t) + b(y₀+s) = c forces at + bs = 0, meaning a·t = -b·s. The general solution is x = x₀ + (b/d)·n, y = y₀ - (a/d)·n for any integer n. The step sizes b/d and a/d are the reduced coefficients after dividing out the common factor. Moving n by 1 shifts x by b/d and compensates y by -a/d, keeping ax + by constant at c. There are infinitely many solutions, equally spaced along a line in the (x, y) plane.

The connection to modular arithmetic (your soft prerequisite) is direct: ax + by = c, when solved for x, becomes ax ≡ c (mod b). Finding x mod b is a modular linear equation, solvable precisely when gcd(a, b) | c, giving d = gcd(a, b) solutions mod b. The two frameworks — parameterization and modular arithmetic — are two views of the same structure. Mastering this equation is the foundation for Pell's equation and Chinese Remainder Theorem problems, where integer constraints replace real-number freedom.
