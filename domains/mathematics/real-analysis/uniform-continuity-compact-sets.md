---
id: uniform-continuity-compact-sets
title: Uniform Continuity on Compact Sets
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-continuity
  type: hard
- id: compact-sets
  type: hard
- id: heine-borel-theorem
  type: soft
tags:
- uniform-continuity
- compact
- compactness
stage: advanced
status: draft
---

# Uniform Continuity on Compact Sets

## Core Idea
Every continuous function on a compact set is uniformly continuous. This is a theorem with profound implications: on [a,b], all continuous functions are uniformly continuous, justifying the integral's existence. The proof uses compactness via contradiction: a failure of uniform continuity produces a non-convergent sequence with no convergent subsequence, violating Bolzano-Weierstrass.

## Explainer

You've already wrestled with the difference between pointwise and **uniform continuity**. Recall the distinction: pointwise continuity says that for each point x and each ε > 0, you can find a δ that works *at x*; but δ can depend on x, so it might shrink to zero as x moves. Uniform continuity demands one δ that works simultaneously *everywhere* on the domain. The function f(x) = 1/x on (0, 1) is continuous at every point but not uniformly continuous — as x approaches 0, you need ever-tinier δ to keep the function within ε.

The key theorem connects uniform continuity to compactness: **if f is continuous on a compact set K, then f is uniformly continuous on K**. On a closed bounded interval [a, b] — compact by Heine-Borel — every continuous function automatically gets the stronger uniform continuity property for free. The intuition is that compactness prevents the "runaway" behavior that destroys uniform continuity. On (0, 1), the trouble is that the endpoint 0 is missing; sequences approaching 0 have no limit *inside* the domain. On [0, 1], that endpoint is included, so every sequence has its limit inside the set, and the function's behavior at the limit controls the behavior nearby.

The formal proof works by contradiction. Suppose f is continuous on compact K but not uniformly continuous. Then there exists ε > 0 such that for every δ > 0, there exist points xₙ, yₙ with |xₙ − yₙ| < 1/n yet |f(xₙ) − f(yₙ)| ≥ ε. This gives a sequence (xₙ) in K. Because K is compact (equivalently, because K is closed and bounded by Heine-Borel), **Bolzano-Weierstrass** guarantees a convergent subsequence x_{nₖ} → p ∈ K. The corresponding y_{nₖ} also converges to p (since |xₙ − yₙ| → 0). But then continuity of f at p forces f(x_{nₖ}) → f(p) and f(y_{nₖ}) → f(p), making |f(x_{nₖ}) − f(y_{nₖ})| → 0 — contradicting that it stays ≥ ε. Compactness is what gives you the convergent subsequence; without it, the argument collapses.

The theorem's payoff reaches across analysis. The Riemann integral's definition requires that continuous functions on [a, b] can be uniformly approximated by step functions — which is exactly what uniform continuity guarantees. Without this theorem, the integral's existence for continuous functions would require a much more painful argument. Whenever you see a theorem that works on closed bounded intervals but fails on open ones, compactness is usually the invisible reason.
