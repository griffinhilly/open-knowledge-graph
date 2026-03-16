---
id: weak-convergence
title: Weak Convergence
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: dual-spaces-bounded-functionals
  type: hard
builds-toward:
- reflexive-spaces
tags:
- convergence
- weak-topology
stage: advanced
status: draft
---

# Weak Convergence

## Core Idea
A sequence (xₙ) converges weakly to x if f(xₙ) → f(x) for every bounded linear functional f ∈ X*. Weak convergence is weaker than norm convergence but sufficient for many applications.

## Explainer

In a finite-dimensional vector space, every kind of convergence is equivalent — a sequence converges if and only if each coordinate converges. In infinite-dimensional spaces, the situation is richer and more subtle. Norm convergence (also called strong convergence) requires ||xₙ - x|| → 0: the vectors get geometrically close. **Weak convergence** asks for something less: every bounded linear functional "sees" the sequence converging. If you probe the sequence with any continuous linear measurement, the measurements converge — but the vectors themselves need not be geometrically approaching x.

The definition makes precise use of the dual space X* you've studied. The dual space is the space of all bounded linear functionals f: X → ℝ (or ℂ). The sequence (xₙ) converges **weakly** to x, written xₙ ⇀ x, if for every f ∈ X*, the scalar sequence f(xₙ) → f(x) in ℝ. Every strongly convergent sequence converges weakly (by linearity and boundedness of f), but the converse fails in infinite dimensions. The canonical example in L²([0,1]): the sequence sin(nπt) converges weakly to 0 — every L² function's inner product with sin(nπt) tends to zero by the Riemann-Lebesgue lemma — yet ||sin(nπt)||₂ = 1/√2 for all n, so strong convergence fails completely.

The practical importance of weak convergence is that it often restores compactness. In finite dimensions, every bounded sequence has a convergent subsequence (Bolzano-Weierstrass). In infinite dimensions, this is spectacularly false for norm convergence — the unit sphere is not compact. But in a **reflexive** Banach space (the topic this builds toward), every bounded sequence has a weakly convergent subsequence. This is the infinite-dimensional substitute for Bolzano-Weierstrass, and it's indispensable in variational calculus and PDE theory: to find a minimum of a functional, you take a minimizing sequence, extract a weakly convergent subsequence, and show the limit is actually a minimizer.

The key intuition is that weak convergence is convergence "on average" or "as seen by every observer," where observers are bounded linear functionals. In L² this means integral convergence: ∫fₙg → ∫fg for every g ∈ L². The sequence can oscillate wildly (like sin(nπt)) while still converging weakly to zero, because the oscillations cancel out in every integral. Strong convergence demands the function approaches its limit pointwise in the L² sense; weak convergence only demands its correlations with every test function converge. The distinction separates what is geometrically close from what is merely "indistinguishable by measurement."
