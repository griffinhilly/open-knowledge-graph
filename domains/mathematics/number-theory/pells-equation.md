---
id: pells-equation
title: Pell's Equation
domain: mathematics
course: number-theory
prerequisites:
- id: continued-fractions
  type: hard
tags:
- pells-equation
- diophantine
- continued-fractions
stage: advanced
status: draft
---

# Pell's Equation

## Core Idea
Pell's equation x^2 - Dy^2 = 1 (D not a perfect square) has infinitely many integer solutions generated from a fundamental solution via the continued fraction expansion of √D. Solutions correspond to units in ℤ[√D].

## Explainer

Pell's equation x² − Dy² = 1 is deceptively simple to write down, yet finding its integer solutions requires one of the most beautiful tools in number theory: continued fractions, your main prerequisite. You've studied how irrational numbers like √2 = [1; 2, 2, 2, ...] can be represented as infinite continued fractions, and how their **convergents** — the rational approximations you get by truncating the continued fraction — give extraordinarily good approximations to the irrational number. The connection to Pell's equation is that these same convergents produce the solutions.

To find the smallest positive solution (x₁, y₁), called the **fundamental solution**, expand √D as a continued fraction [a₀; a₁, a₂, ...] and compute its convergents pₖ/qₖ. The fundamental solution appears as (p_{s−1}, q_{s−1}), where s is the period of the continued fraction expansion. For D = 2: √2 = [1; 2, 2, 2, ...] with period 1, and the first convergent beyond a₀ is 3/2, giving x = 3, y = 2. Check: 3² − 2·2² = 9 − 8 = 1. ✓ For D = 3: √3 = [1; 1, 2, 1, 2, ...] with period 2, and the convergent at period end is 2/1, giving x = 2, y = 1. Check: 4 − 3 = 1. ✓

What makes Pell's equation remarkable is that from just one fundamental solution, you generate infinitely many. All solutions are given by xₙ + yₙ√D = (x₁ + y₁√D)ⁿ. This algebraic structure — multiplying together expressions in the ring ℤ[√D] — reflects the fact that solutions are **units** (invertible elements) in that ring: if α = x₁ + y₁√D satisfies αᾱ = 1 (where ᾱ = x₁ − y₁√D), then αⁿ also satisfies this, generating a new solution. The multiplication rule corresponds to a matrix recurrence, and the solutions grow exponentially.

The reason continued fractions find the fundamental solution goes deeper than it might appear. The convergents pₖ/qₖ of √D are the best rational approximations to √D, meaning pₖ/qₖ ≈ √D, or equivalently pₖ ≈ qₖ√D, or pₖ² ≈ Dqₖ². The error in this approximation is so small — governed by the theory of continued fractions — that pₖ² − Dqₖ² lands exactly on 1 at the right index. The entire theory of Pell's equation is in some sense a story about how well rational numbers can approximate square roots of integers, and continued fractions are the perfect language for that story.
