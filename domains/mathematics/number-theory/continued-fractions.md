---
id: continued-fractions
title: Continued Fractions
domain: mathematics
course: number-theory
prerequisites:
- id: euclidean-algorithm
  type: hard
builds-toward:
- best-rational-approximations
- pells-equation
tags:
- continued-fractions
- approximation
- irrationals
stage: advanced
status: draft
---

# Continued Fractions

## Core Idea
Every real number has a unique continued fraction expansion [a_0; a_1, a_2, ...]. Rational expansions terminate; quadratic irrationals become periodic. The convergents give best rational approximations in a precise sense.

## Explainer

You already know the **Euclidean algorithm**: given two integers a and b, you repeatedly divide to find remainders until you hit zero, yielding gcd(a, b). A continued fraction is what happens when you keep track of those quotients as a structured expression. For example, computing gcd(355, 113) produces quotients 3, 7, 16 — and the continued fraction [3; 7, 16] = 3 + 1/(7 + 1/16) = 355/113, one of the famous approximations to π. The Euclidean algorithm and continued fractions are two faces of the same process.

To expand a real number x into a continued fraction, take the integer part a₀ = ⌊x⌋, then take the reciprocal of the remainder and repeat: a₁ = ⌊1/(x − a₀)⌋, and so on. This produces [a₀; a₁, a₂, ...] where every aᵢ is a positive integer (except possibly a₀, which can be any integer). For a rational number, the process terminates in finitely many steps — exactly as the Euclidean algorithm halts when the remainder reaches zero. For an irrational number, the expansion never terminates and gives an infinite sequence of partial quotients.

The special behavior of **quadratic irrationals** — numbers of the form (p + √q)/r — is one of the striking theorems: their continued fraction expansions are eventually periodic. The most famous example is √2 = [1; 2, 2, 2, ...], a purely repeating expansion. By contrast, the expansions for e and π are not periodic (they cannot be quadratic irrationals), though they have their own fascinating patterns. Periodicity links continued fractions to **Pell's equation**, which this topic builds toward.

The **convergents** pₙ/qₙ are the rational numbers you get by truncating the expansion at each step: p₀/q₀ = a₀, p₁/q₁ = a₀ + 1/a₁, and so on. These are not just random approximations — they are the *best* rational approximations to x in a precise sense: no fraction with a smaller denominator lies closer to x. This is why 355/113 (accurate to 6 decimal places) is so remarkable for approximating π; its convergent status means no fraction with denominator ≤ 113 does better. The theory of continued fractions thus transforms the problem of rational approximation into a systematic algorithm, connecting number theory to analysis through the machinery you have already built with the Euclidean algorithm.
