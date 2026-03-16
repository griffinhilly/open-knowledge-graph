---
id: introduction-to-p-adic-numbers
title: Introduction to p-adic Numbers
domain: mathematics
course: number-theory
prerequisites:
- id: p-adic-valuation
  type: hard
builds-toward:
- arithmetic-in-p-adic-numbers
tags:
- p-adic
- completion
- metric-spaces
stage: advanced
status: draft
---

# Introduction to p-adic Numbers

## Core Idea
The p-adic numbers ℚ_p are the completion of ℚ with respect to the p-adic metric. They provide an alternative geometric intuition where 'closeness' is measured by divisibility: two numbers are close if their difference is highly divisible by p. This enables new perspectives on solving Diophantine equations.

## Explainer

From your study of the p-adic valuation, you know that vₚ(n) counts how many times p divides n, and that this valuation satisfies the ultrametric inequality. The p-adic numbers ℚ_p are what you get when you take this valuation seriously as a notion of *distance*. Define |x|ₚ = p^{−vₚ(x)}. Under this metric, two integers are close if their difference is highly divisible by p. For example, in ℚ₅, the numbers 1 and 126 = 1 + 5³ are only 1/125 apart, because 5³ divides their difference. Numbers we think of as "large" — like 5^{100} — are tiny in the p-adic world; numbers we think of as "close to 1" in the usual sense — like 2/3 — may be perfectly well-behaved p-adically.

The **completion** of ℚ with respect to the p-adic metric works exactly as you would construct the real numbers: take all Cauchy sequences of rationals (sequences where terms eventually get arbitrarily close under | · |ₚ) and identify sequences that converge to the same limit. The resulting space ℚ_p is complete — every Cauchy sequence converges — and contains ℚ as a dense subfield. This mirrors how ℝ is the completion of ℚ under the usual absolute value. The key difference is that while there is only one completion under the standard metric (up to equivalence), Ostrowski's theorem tells us that for every prime p, the p-adic metric gives a genuinely different, inequivalent completion.

One of the most striking features of p-adic numbers is their expansion: every element of ℤ_p (the p-adic integers, the "unit ball" of ℚ_p) can be written uniquely as a₀ + a₁p + a₂p² + ··· where each aᵢ ∈ {0, 1, ..., p−1}. This looks like a power series in p, and it converges p-adically because higher powers of p are smaller in | · |ₚ. This is the reverse of ordinary positional notation, where high powers of 10 are large. In ℚ_p, you can even make sense of "infinite series going left" — for instance, −1 = (p−1) + (p−1)p + (p−1)p² + ··· (the p-adic expansion of −1), a fact that is deeply counterintuitive from a real-number perspective.

The payoff for Diophantine equations comes through the **Hasse-Minkowski theorem** and the general principle of local-global reasoning: to understand integer solutions to a polynomial equation, one studies solutions in ℝ and in ℚ_p for every prime p (these are the "local" fields). A solution over all these completions is a necessary condition for a rational solution. Working p-adically is often much easier — p-adic numbers satisfy a strong form of Hensel's lemma, which lifts solutions mod p to full p-adic solutions under mild conditions — while the global (rational) problem is hard. The p-adics thus serve as tractable local test cases for the global arithmetic question.
