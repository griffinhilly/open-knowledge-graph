---
id: pell-equation
title: Pell's Equation
domain: mathematics
course: number-theory
prerequisites:
- id: continued-fractions
  type: hard
tags:
- diophantine
- pell
- continued-fractions
stage: advanced
status: validated
---

# Pell's Equation

## Core Idea
Pell's equation x² − Dy² = 1, where D is a non-square positive integer, always has infinitely many positive integer solutions. Solutions arise via the periodic continued fraction expansion of √D, and the fundamental solution generates all others via multiplication in ℚ(√D).

## Questions

```yaml
- question: "The fundamental solution to x² − 3y² = 1 is (2, 1). What is the next-smallest positive integer solution?"
  type: multiple-choice
  options:
    - "(4, 2) — double the fundamental solution"
    - "(5, 3) — adding the fundamental solution to itself"
    - "(7, 4) — computed by squaring ε₁ = 2 + √3 in ℚ(√3)"
    - "(11, 6) — the next convergent of the continued fraction of √3"
  answer: 2
  explanation: "To generate new solutions from the fundamental solution (x₁, y₁) = (2, 1), form ε₁ = x₁ + y₁√3 = 2 + √3 and compute ε₁² = (2+√3)² = 4 + 4√3 + 3 = 7 + 4√3, giving (x₂, y₂) = (7, 4). Verify: 7² − 3·4² = 49 − 48 = 1 ✓. Simply doubling (option A) fails because solutions don't scale linearly — (4,2) gives 16 − 12 = 4 ≠ 1. The multiplication in ℚ(√D) is what generates solutions, not arithmetic on the integers."

- question: "Why does the continued fraction expansion of √D (for non-square positive integer D) always yield solutions to x² − Dy² = 1?"
  type: multiple-choice
  options:
    - "Every sufficiently close rational approximation to √D automatically satisfies the Pell equation exactly"
    - "The continued fraction is infinite, so by the pigeonhole principle some convergent must work"
    - "√D is irrational, so its continued fraction is eventually periodic, and convergents at the end of each complete period satisfy p² − Dq² = ±1, with full periods giving +1"
    - "The Pell equation is defined to have solutions wherever the continued fraction algorithm terminates"
  answer: 2
  explanation: "The periodicity of the continued fraction of √D is the key fact (proved by Lagrange). Because the expansion repeats, the convergents at the end of each period are not just good rational approximations to √D — they satisfy the Pell equation exactly. This is not a coincidence or a pigeonhole argument: the arithmetic of convergents and the structure of the equation are connected through the theory of quadratic irrationalities. Not every convergent works — only those at period-end — which is why knowing the period length is essential."

- question: "The fundamental solution to x² − Dy² = 1 always appears as a convergent of the continued fraction expansion of √D."
  type: true-false
  answer: true
  explanation: "This is the central result connecting continued fractions to Pell's equation. The fundamental solution (x₁, y₁) is the smallest positive-integer solution, and it always occurs at the convergent p_k/q_k corresponding to the end of the first complete period of the continued fraction of √D. Every subsequent solution is generated algebraically from this seed."

- question: "If (x₁, y₁) is the fundamental solution to x² − Dy² = 1, then (2x₁, 2y₁) is also a solution."
  type: true-false
  answer: false
  explanation: "Scaling a solution by a constant does not produce new solutions. Check: (2x₁)² − D(2y₁)² = 4x₁² − 4Dy₁² = 4(x₁² − Dy₁²) = 4·1 = 4 ≠ 1. Solutions grow through multiplication in ℚ(√D): the n-th solution comes from computing (x₁ + y₁√D)ⁿ = xₙ + yₙ√D, an operation that preserves the norm-1 property but is non-linear in the integers x and y."

- question: "Explain why knowing the fundamental solution (x₁, y₁) to x² − Dy² = 1 guarantees infinitely many solutions, and describe how they are generated."
  type: short-answer
  answer: "Form ε₁ = x₁ + y₁√D in the ring ℤ[√D] ⊂ ℚ(√D). The equation x² − Dy² = 1 is equivalent to saying ε = x + y√D has norm 1 (i.e., ε·ε̄ = (x + y√D)(x − y√D) = 1). Because norms multiply — N(αβ) = N(α)·N(β) — every power ε₁ⁿ also has norm 1. Since ε₁ > 1, the powers ε₁ⁿ for n = 1, 2, 3, … are all distinct elements xₙ + yₙ√D with xₙ, yₙ positive integers satisfying the Pell equation. The continued fraction finds the seed; the multiplicative structure of ℚ(√D) generates the infinite family."
  explanation: "The algebraic key is that x² − Dy² = 1 defines a group under multiplication in ℚ(√D): the set of norm-1 elements is closed under multiplication and inversion. The fundamental solution is a generator of this group (it has infinite order because ε₁ > 1). So all solutions are exactly the integer powers of ε₁ — positive and negative — making the solution set infinite and completely described by one seed value."
```

## Explainer

Pell's equation x² - Dy² = 1 asks for integer points on a hyperbola that are in an extraordinarily precise sense "close to √D." To see why, rewrite the equation as x/y ≈ √D: if (x, y) is a solution, then (x/y)² ≈ D, so x/y is a rational approximation to √D with error |x/y - √D| ≈ 1/(2y²√D). Your prerequisite — **continued fractions** — provides exactly the tool for finding such best-rational-approximations systematically.

The continued fraction expansion of √D is eventually **periodic** for any non-square positive integer D. For example, √2 = [1; 2, 2, 2, ...] and √3 = [1; 1, 2, 1, 2, ...]. The **convergents** p_n/q_n of this expansion are the best rational approximations to √D: no fraction with a smaller denominator gets closer. The connection to Pell's equation is that the convergents at the end of each complete period satisfy p_n² - Dq_n² = ±1 exactly — and among those, every other period gives +1. The **fundamental solution** (x₁, y₁) is the smallest positive solution, always found at the first period completion.

A concrete example: for D = 2, the continued fraction is [1; 2, 2, ...] with period 1, and the first convergent is p₁/q₁ = 3/2. Check: 3² - 2·2² = 9 - 8 = 1. ✓ For D = 3, the period is [1; 1, 2], so the first convergent at period-end is 2/1, but 4 - 3 = 1, giving (2, 1). Check: 4 - 3·1 = 1. ✓ The algorithm is completely mechanical once you can compute the periodic continued fraction.

Once you have the fundamental solution (x₁, y₁), all others are generated by a remarkable algebraic structure. Think of ε₁ = x₁ + y₁√D as an element of the algebraic number system ℚ(√D). The equation x² - Dy² = 1 is equivalent to (x + y√D)(x - y√D) = 1, meaning these elements have **norm** 1. Multiplying two norm-1 elements gives another norm-1 element: ε₁ⁿ = xₙ + yₙ√D yields the n-th solution (xₙ, yₙ). For D = 2: ε₁ = 3 + 2√2, so ε₁² = 17 + 12√2, giving (17, 12). Check: 17² - 2·12² = 289 - 288 = 1. ✓ The continued fraction finds the seed; the algebraic structure of ℚ(√D) generates the infinite family.
