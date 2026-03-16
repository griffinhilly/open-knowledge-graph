---
id: weak-star-convergence
title: Weak* Convergence
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: weak-convergence
  type: hard
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

# Weak* Convergence

## Core Idea
A sequence of functionals (fₙ) in X* converges weak* to f if fₙ(x) → f(x) for every x ∈ X. The weak* topology on X* enables compactness: the closed unit ball is weak* compact (Alaoglu's theorem).

## Explainer

You now know two modes of convergence for sequences in a normed space: norm convergence (strong convergence), and **weak convergence**, where xₙ → x weakly if f(xₙ) → f(x) for every bounded linear functional f. Weak* convergence lives one level higher: instead of testing vectors against functionals, it tests **functionals against vectors**. A sequence (fₙ) in the dual space X* converges **weak*** to f if fₙ(x) → f(x) for every fixed x ∈ X. The "star" marks that the dual space X* is now the space being tested, and the original space X provides the test functions.

The distinction between weak and weak* convergence matters when X is not reflexive. Recall from your dual spaces prerequisite that the dual of X is X*, and the double dual is X**. Weak convergence in X* means testing against elements of (X*)* = X** — every functional on X*. Weak* convergence tests only against the elements of X sitting inside X** via the canonical embedding. This is a strictly coarser topology when X is not reflexive: there are more weak* convergent sequences than weakly convergent ones in X*. In a reflexive space, X = X** and the two topologies coincide.

Why does this weaker topology matter? Because it enables compactness. The **Banach-Alaoglu theorem** states that the closed unit ball in X* is compact in the weak* topology — for any normed space X. This is a profound statement because the unit ball in an infinite-dimensional space is never compact in the norm topology (Riesz's theorem). Weak* compactness rescues compactness arguments that would otherwise fail in infinite dimensions, and is the engine behind many existence proofs in analysis, PDEs, and optimization: extract a bounded sequence of approximate solutions, use Alaoglu to find a weak* convergent subnet or subsequence, then show the limit is an exact solution.

A concrete instance: in L^∞([0,1]), the dual of L¹, a bounded sequence of functions (gₙ) in L^∞ with ‖gₙ‖∞ ≤ 1 always has a weak* convergent subnet. Weak* convergence here means ∫gₙh → ∫gh for every h ∈ L¹. This limit g need not be pointwise limit, it need not converge in norm, but it exists and is bounded — which is enough for many applications. This "weak* limit extraction" technique appears throughout harmonic analysis, probability theory (as tightness and vague convergence of measures), and the calculus of variations.
