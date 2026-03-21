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

## Questions

```yaml
- question: "Does the equation 6x + 10y = 9 have integer solutions?"
  type: multiple-choice
  options:
    - "Yes — all linear equations in two variables have solutions"
    - "No — gcd(6, 10) = 2, which does not divide 9, so no integer solutions exist"
    - "Yes — setting y = 0 gives x = 3/2, which can be rounded to the nearest integer"
    - "No — because both 6 and 10 are even, no combination can produce an odd number"
  answer: 1
  explanation: "The solvability criterion: ax + by = c has integer solutions if and only if gcd(a, b) divides c. Here gcd(6, 10) = 2, and 2 does not divide 9 (since 9 is odd). Therefore no integers x, y can satisfy this equation. Option A is the common misconception — integer solutions are far more restricted than real solutions. Option C correctly finds a real solution but forgets we need integers. Option D gets the right answer for the wrong reason — the issue is divisibility of c by the gcd, not parity of the coefficients per se."

- question: "The equation 4x + 6y = 10 has a particular solution x₀ = 1, y₀ = 1. Which expression gives ALL integer solutions?"
  type: multiple-choice
  options:
    - "x = 1 + 4n, y = 1 − 6n for any integer n"
    - "x = 1 + 3n, y = 1 − 2n for any integer n"
    - "x = 1 + 6n, y = 1 − 4n for any integer n"
    - "x = 1 + 2n, y = 1 − 3n for any integer n"
  answer: 1
  explanation: "With a = 4, b = 6, d = gcd(4, 6) = 2, the general solution is x = x₀ + (b/d)n = 1 + 3n and y = y₀ − (a/d)n = 1 − 2n. The step sizes are b/d = 3 and a/d = 2 (the reduced coefficients), not b and a themselves. Option A uses the original coefficients. Option C swaps them. Verify: 4(1+3n) + 6(1−2n) = 4 + 12n + 6 − 12n = 10. ✓"

- question: "If gcd(a, b) = 1, then the equation ax + by = c has integer solutions for every integer c."
  type: true-false
  answer: true
  explanation: "When gcd(a, b) = 1, the divisibility condition 'gcd(a,b) | c' becomes '1 | c,' which holds for every integer c. By Bézout's identity, 1 can be expressed as ax₀ + by₀ for some integers x₀, y₀; scaling by c gives a(cx₀) + b(cy₀) = c. Coprime coefficients guarantee solvability for any right-hand side — no divisibility restriction on c exists."

- question: "A linear Diophantine equation ax + by = c either has exactly one integer solution or no integer solution."
  type: true-false
  answer: false
  explanation: "This is the most common misconception. When a solution exists, there are always infinitely many, parameterized by all integers n: x = x₀ + (b/d)n, y = y₀ − (a/d)n. Each value of n gives a distinct integer solution. The equation either has zero solutions (when gcd(a,b) ∤ c) or infinitely many (when gcd(a,b) | c)."

- question: "Why does the gcd of a and b determine whether ax + by = c has integer solutions?"
  type: short-answer
  answer: "The set of all integers representable as ax + by, where x and y range over all integers, is exactly the set of multiples of gcd(a, b). By Bézout's identity, gcd(a, b) itself can be written as an integer linear combination of a and b, and every multiple of gcd(a, b) can be reached by scaling that combination. So if c is a multiple of d = gcd(a, b), scale the Bézout representation to get a solution. If c is not a multiple of d, no combination of integer multiples of a and b can sum to c, because every such sum is a multiple of d."
  explanation: "The structural fact is that {ax + by : x, y ∈ ℤ} = dℤ (the set of multiples of d). The solvability condition gcd(a,b) | c simply says c must belong to this set."
```

## Explainer

A **linear Diophantine equation** is simply a linear equation in two (or more) integer unknowns: ax + by = c, where a, b, c are given integers and you seek integer solutions x, y. The word "Diophantine" just signals that only integers count — rational or real solutions are not enough. Your prerequisite, **Bézout's identity**, hands you the key insight: gcd(a, b) can be expressed as an integer linear combination of a and b. This immediately tells you when solutions exist.

The solvability criterion is clean: ax + by = c has integer solutions if and only if gcd(a, b) divides c. Here is why. The set of all integers expressible as ax + by is exactly the set of multiples of gcd(a, b). So c must be a multiple of gcd(a, b) for the equation to work. If gcd(a, b) = d and d does not divide c, there are no solutions at all — not even close ones. If d | c, you can write c = d · (c/d), find a Bézout representation d = ax₀ + by₀ via the extended Euclidean algorithm, and scale: x = x₀·(c/d), y = y₀·(c/d) is one particular solution.

Once you have one solution (x₀, y₀), all solutions follow a pattern. Substituting x = x₀ + t and y = y₀ + s into the equation shows that at(x₀+t) + b(y₀+s) = c forces at + bs = 0, meaning a·t = -b·s. The general solution is x = x₀ + (b/d)·n, y = y₀ - (a/d)·n for any integer n. The step sizes b/d and a/d are the reduced coefficients after dividing out the common factor. Moving n by 1 shifts x by b/d and compensates y by -a/d, keeping ax + by constant at c. There are infinitely many solutions, equally spaced along a line in the (x, y) plane.

The connection to modular arithmetic (your soft prerequisite) is direct: ax + by = c, when solved for x, becomes ax ≡ c (mod b). Finding x mod b is a modular linear equation, solvable precisely when gcd(a, b) | c, giving d = gcd(a, b) solutions mod b. The two frameworks — parameterization and modular arithmetic — are two views of the same structure. Mastering this equation is the foundation for Pell's equation and Chinese Remainder Theorem problems, where integer constraints replace real-number freedom.
