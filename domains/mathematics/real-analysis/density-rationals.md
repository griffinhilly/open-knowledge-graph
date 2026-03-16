---
id: density-rationals
title: Density of the Rationals
domain: mathematics
course: real-analysis
prerequisites:
- id: archimedean-property
  type: hard
- id: supremum-infimum
  type: soft
builds-toward:
- weierstrass-approximation-theorem
- uniform-convergence-power-series
tags:
- rationals
- density
- approximation
stage: advanced
status: draft
---

# Density of the Rationals

## Core Idea
Between any two distinct real numbers, there exists at least one rational number. Equivalently, rational numbers are dense in the reals: every real number is the limit of a sequence of rationals. This consequence of the Archimedean Property shows that rationals are 'nearly everywhere' even though they are countable.

## Explainer

You already have the Archimedean property in hand: for any positive real number ε, there exists a natural number n large enough that 1/n < ε. This seemingly simple fact has a powerful consequence: the rational numbers, despite being countably infinite and therefore "small" in a set-theoretic sense, are **dense** in the real line. Between any two real numbers, no matter how close together, you can always find a rational.

The proof is short and elegant. Let a < b be real numbers. We want integers p and q with a < p/q < b, or equivalently qa < p < qb. By the Archimedean property applied to b − a > 0, there exists a natural number q with 1/q < b − a, meaning qb − qa > 1. Any interval of length greater than 1 must contain an integer — take p = ⌊qa⌋ + 1. Then qa < p ≤ qa + 1 < qb, so a < p/q < b. The rational p/q sits strictly between a and b. Applying the argument repeatedly shows infinitely many rationals lie between any two reals.

What does density really mean? It means rationals are **everywhere locally** — there is no gap between reals that a rational cannot fill. Every real number is the limit of a sequence of rationals: just take successive decimal truncations, like 3, 3.1, 3.14, 3.141, 3.1415, ... converging to π. This is why rational arithmetic suffices for computation even when true values are irrational — any irrational can be approximated to arbitrary precision by rationals, and your previously studied supremum-infimum framework gives this approximation its precise meaning.

Paradoxically, despite being dense, the rationals have **measure zero** in the sense of Lebesgue measure: they take up none of the real line's "length." The irrationals, by contrast, are uncountable and fill the line completely from a measure perspective. Density and measure capture different aspects of "how much" a set occupies. This tension — rationals everywhere locally, irrationals everywhere globally — will reappear when you study uniform convergence and the Weierstrass approximation theorem, where polynomials with rational coefficients approximate arbitrary continuous functions. The density of rationals is the engine behind every such approximation argument.
