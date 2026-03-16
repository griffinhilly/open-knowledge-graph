---
id: lebesgue-integral-non-negative
title: Lebesgue Integral for Non-Negative Functions
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-simple-functions
  type: hard
builds-toward:
- lebesgue-integral-general-definition
- monotone-convergence-theorem-analysis
- fatou-lemma-measure-theory
tags:
- integration
- lebesgue-integral
stage: abstract-reasoning
status: draft
---

# Lebesgue Integral for Non-Negative Functions

## Core Idea
For non-negative measurable f, define ∫f dμ = sup{∫φ dμ : φ simple, φ ≤ f}. This definition is monotone: f ≤ g implies ∫f ≤ ∫g. The integral may be infinite but is always defined.

## Explainer

You already know how to integrate **simple functions** — those that take only finitely many values on measurable sets. A simple function looks like a staircase: constant on each of finitely many pieces. Integrating it is easy: multiply each constant value by the measure of the set where it achieves that value, then sum. The Lebesgue integral for non-negative functions extends this to every non-negative measurable function by a single elegant move: approximate from below.

The key idea is the **supremum definition**: ∫f dμ = sup{∫φ dμ : φ simple, 0 ≤ φ ≤ f}. You take all the simple functions that underestimate f everywhere, integrate each one, and then take the least upper bound of all those numbers. If f is itself simple, this recovers the simple function integral. If f is a smooth curve, it approximates f from below with ever-finer staircases. The supremum captures the "total area" even when no single simple function achieves it.

This definition handles two important edge cases cleanly. First, it is always defined — the supremum of a set of non-negative numbers is either a finite non-negative number or +∞, never undefined. A function like 1/√x near 0 may have infinite integral; that's allowed and just equals +∞. Second, it is **monotone**: if f ≤ g everywhere, then every simple function below f is also below g, so the supremum for f is ≤ the supremum for g. This monotonicity is the engine behind the Monotone Convergence Theorem you'll see next.

Why restrict to non-negative functions first? Because non-negative functions have a clean order structure: if φ ≤ f, then more of φ means more of f. Negative values break this — you could have a function that is sometimes large-positive and sometimes large-negative, and the cancellations make "approximating from below" ambiguous. The general Lebesgue integral (for functions that can be negative) is built on top of this: split f into its positive part f⁺ = max(f, 0) and negative part f⁻ = max(−f, 0), integrate both as non-negative functions, and subtract — but only when at least one is finite to avoid ∞ − ∞.
