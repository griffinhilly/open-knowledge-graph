---
id: tonelli-theorem
title: Tonelli's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: product-measures-fubini-theorem
  type: hard
tags:
- product-measures
stage: advanced
status: draft
---

# Tonelli's Theorem

## Core Idea
Tonelli's theorem extends Fubini's iteration to non-negative measurable functions that may not be integrable, using iterated integrals with values in [0,∞]. It complements Fubini by handling the non-integrable case.

## Explainer

From Fubini's theorem, you know that double integrals over product spaces can be computed as iterated integrals — integrate one variable at a time, in either order — provided the function is integrable (i.e., ∫∫|f| d(μ×ν) < ∞). But Fubini's theorem requires you to *already know* the function is integrable before you can swap the order of integration. This creates a chicken-and-egg problem: how do you verify integrability without computing the integral, and how do you compute the integral without knowing you can iterate?

**Tonelli's theorem** resolves this by handling **non-negative measurable functions** separately, with no integrability assumption. For f ≥ 0, all integrals are well-defined in [0, ∞] — they either converge to a finite value or diverge to +∞, but they never produce undefined expressions involving ∞ − ∞. Tonelli states: if f: X×Y → [0, ∞] is measurable with respect to the product σ-algebra, then the iterated integrals are equal to the double integral, even if all three equal +∞. Crucially, the iterated integrals equal each other and equal the double integral *without* any finiteness precondition.

The practical power of Tonelli is that it gives you a **strategy for verifying integrability**: to check whether f (not necessarily non-negative) is in L¹(X×Y), apply Tonelli to |f| first. If the iterated integral ∫(∫|f(x,y)| dν(y)) dμ(x) is finite, then |f| is integrable over the product space, and you can then apply Fubini to f itself to compute the integral by iteration. This two-step procedure — Tonelli to establish integrability, then Fubini to compute — is one of the most common patterns in measure theory.

Together, Fubini and Tonelli form a complete toolkit for handling double integrals. Fubini tells you that integration order doesn't matter *when* a function is integrable; Tonelli tells you *how to check* integrability and handles the non-negative case outright. The distinction matters because for functions of indefinite sign that fail to be absolutely integrable, iterated integrals in different orders can yield different finite values — a phenomenon that neither theorem allows for functions in their respective domains. The pairing of the two results is so natural that many texts present them together as "Fubini-Tonelli."
