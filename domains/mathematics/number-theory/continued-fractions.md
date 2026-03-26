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
status: validated
---

# Continued Fractions

## Core Idea
Every real number has a unique continued fraction expansion [a_0; a_1, a_2, ...]. Rational expansions terminate; quadratic irrationals become periodic. The convergents give best rational approximations in a precise sense.

## Questions

```yaml
- question: "The fraction 355/113 is famously close to π. According to continued fraction theory, what makes it so special compared to other fractions with denominator ≤ 113?"
  type: multiple-choice
  options:
    - "It is a convergent of π's continued fraction expansion, so no fraction with a smaller denominator is closer to π"
    - "It was computed by truncating the decimal expansion of π to 3 digits in numerator and denominator"
    - "It is the unique fraction of that denominator that equals π when rounded to 6 decimal places"
    - "It minimizes the sum of numerator and denominator while staying within 0.001 of π"
  answer: 0
  explanation: "355/113 is a convergent of π's continued fraction expansion. A fundamental theorem states that convergents are the best rational approximations: no fraction with a smaller denominator lies closer to the real number. This is much stronger than just being accurate — it means 355/113 is optimal among all fractions p/q with q ≤ 113."

- question: "A student is told that √2 has a periodic continued fraction expansion. They conclude that π must also have a periodic expansion since both are irrational. What theorem directly refutes this reasoning?"
  type: multiple-choice
  options:
    - "Only quadratic irrationals — numbers of the form (p + √q)/r — have eventually periodic continued fraction expansions"
    - "Only algebraic numbers of any degree can have periodic continued fraction expansions"
    - "Periodic expansions are only possible for rational numbers, not irrationals"
    - "The periodicity of √2 is a special coincidence with no general theorem behind it"
    - "Any irrational with bounded partial quotients has a periodic expansion"
  answer: 0
  explanation: "Lagrange's theorem states that a real number has an eventually periodic continued fraction if and only if it is a quadratic irrational — a number of the form (p + √q)/r with p, q, r integers. π is transcendental (not even algebraic), so its continued fraction cannot be periodic. Irrationality alone is insufficient."

- question: "The continued fraction expansion of every rational number terminates in finitely many steps."
  type: true-false
  answer: true
  explanation: "True. Expanding a rational number p/q via the continued fraction algorithm is equivalent to running the Euclidean algorithm on p and q. Since the Euclidean algorithm always terminates (remainders strictly decrease and are non-negative integers), the continued fraction expansion of any rational number terminates in finitely many steps."

- question: "Any irrational number with a periodic continued fraction expansion is expected to be transcendental."
  type: true-false
  answer: false
  explanation: "False. It is exactly the opposite: any irrational with a periodic continued fraction is a quadratic irrational (a root of a degree-2 polynomial with integer coefficients), which is algebraic, not transcendental. Transcendental numbers like e and π cannot have periodic continued fraction expansions."

- question: "Why do the convergents of a continued fraction give the best rational approximations to a real number, rather than just good ones?"
  type: short-answer
  answer: "Convergents are optimal in the sense that no fraction with a smaller denominator lies closer to the target number. The algorithm that generates them — mimicking the Euclidean algorithm — discards only information about how much the approximation can improve, keeping only the partial quotients that give the largest improvement per unit of denominator size. This means a convergent beats every fraction p/q with q smaller than its own denominator."
  explanation: "The key is the combination of two facts: (1) the error of each convergent pₙ/qₙ satisfies |x − pₙ/qₙ| < 1/(qₙ·qₙ₊₁), and (2) any non-convergent fraction with denominator between qₙ and qₙ₊₁ has larger error than pₙ/qₙ. Together these prove optimality — being a convergent is both necessary and sufficient for best-approximation status among fractions with that denominator."
```

## Explainer

You already know the **Euclidean algorithm**: given two integers a and b, you repeatedly divide to find remainders until you hit zero, yielding gcd(a, b). A continued fraction is what happens when you keep track of those quotients as a structured expression. For example, computing gcd(355, 113) produces quotients 3, 7, 16 — and the continued fraction [3; 7, 16] = 3 + 1/(7 + 1/16) = 355/113, one of the famous approximations to π. The Euclidean algorithm and continued fractions are two faces of the same process.

To expand a real number x into a continued fraction, take the integer part a₀ = ⌊x⌋, then take the reciprocal of the remainder and repeat: a₁ = ⌊1/(x − a₀)⌋, and so on. This produces [a₀; a₁, a₂, ...] where every aᵢ is a positive integer (except possibly a₀, which can be any integer). For a rational number, the process terminates in finitely many steps — exactly as the Euclidean algorithm halts when the remainder reaches zero. For an irrational number, the expansion never terminates and gives an infinite sequence of partial quotients.

The special behavior of **quadratic irrationals** — numbers of the form (p + √q)/r — is one of the striking theorems: their continued fraction expansions are eventually periodic. The most famous example is √2 = [1; 2, 2, 2, ...], a purely repeating expansion. By contrast, the expansions for e and π are not periodic (they cannot be quadratic irrationals), though they have their own fascinating patterns. Periodicity links continued fractions to **Pell's equation**, which this topic builds toward.

The **convergents** pₙ/qₙ are the rational numbers you get by truncating the expansion at each step: p₀/q₀ = a₀, p₁/q₁ = a₀ + 1/a₁, and so on. These are not just random approximations — they are the *best* rational approximations to x in a precise sense: no fraction with a smaller denominator lies closer to x. This is why 355/113 (accurate to 6 decimal places) is so remarkable for approximating π; its convergent status means no fraction with denominator ≤ 113 does better. The theory of continued fractions thus transforms the problem of rational approximation into a systematic algorithm, connecting number theory to analysis through the machinery you have already built with the Euclidean algorithm.
