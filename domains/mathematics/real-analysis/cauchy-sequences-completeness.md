---
id: cauchy-sequences-completeness
title: Cauchy Sequences and Completeness
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- metric-space-topology
tags:
- cauchy
- completeness
- convergence
stage: advanced
status: draft
---

# Cauchy Sequences and Completeness

## Core Idea
A sequence (aₙ) is Cauchy if for every ε > 0, there exists N such that n, m > N implies |aₙ - aₘ| < ε. In ℝ, a sequence converges if and only if it is Cauchy. This characterization requires no knowledge of the limit beforehand, making it powerful for existence proofs. ℝ is 'complete' because Cauchy sequences always converge.

## Explainer

From ε-N convergence you know what it means for a sequence to converge to a limit L: for every ε > 0, the terms eventually stay within ε of L. But that definition has a built-in limitation — you need to *know L in advance*. Many of the deepest existence proofs in analysis require showing a limit exists without being able to write it down explicitly. The **Cauchy criterion** solves this: instead of asking "are the terms close to some target?", ask "are the terms close to *each other*?" If n, m > N implies |aₙ - aₘ| < ε, the sequence is **Cauchy** — and in ℝ, that is enough to guarantee convergence.

The intuition is that a sequence which keeps "settling down" — where later terms cluster together more and more tightly — must be approaching something. Crucially, being Cauchy makes no reference to a limit; it is an intrinsic property of the sequence itself. In ℝ, the two conditions are equivalent: convergence implies Cauchy (easy to prove using the triangle inequality), and Cauchy implies convergence (the hard direction, which uses the completeness of ℝ). The proof of the hard direction constructs a candidate limit using the Bolzano-Weierstrass theorem and then verifies it works.

**Completeness** is the property that makes this equivalence hold. Not every number system is complete. Consider the rational numbers ℚ: the sequence 1, 1.4, 1.41, 1.414, 1.4142, … (decimal approximations of √2) is Cauchy in ℚ — terms get arbitrarily close to each other — but it does not converge in ℚ, because its limit √2 is irrational. ℚ has "holes." ℝ was constructed precisely to plug those holes: every Cauchy sequence of real numbers converges to a real number. This is not a theorem you prove from more basic facts about ℝ — it is one of the *defining* properties of the real number system.

The Cauchy criterion is the standard tool for proving convergence when the limit cannot be computed explicitly. It also generalizes beautifully: the concept of a **complete metric space** (a central topic in metric space topology) is defined by exactly this property — every Cauchy sequence converges. The real line ℝ, Euclidean spaces ℝⁿ, and the space of continuous functions on a closed interval are all complete; ℚ and the open interval (0,1) are not. Recognizing completeness as a structural property, rather than an accident of ℝ, is the key conceptual shift this topic prepares you for.
