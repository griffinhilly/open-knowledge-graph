---
id: convergence-fourier-series
title: Convergence of Fourier Series
domain: mathematics
course: differential-equations
prerequisites:
- id: fourier-series-definition
  type: hard
- id: sequences-convergence
  type: hard
builds-toward:
- even-odd-extensions-fourier
tags:
- convergence
- dirichlet-conditions
- pointwise
stage: advanced
status: draft
---

# Convergence of Fourier Series

## Core Idea
If f is piecewise smooth and periodic, its Fourier series converges pointwise to f at continuity points and to the average of left and right limits at jump discontinuities. The Dirichlet conditions (finitely many jumps and extrema per period) guarantee this convergence. The Gibbs phenomenon causes overshoot at discontinuities, a key practical consideration.

## How It's Best Learned
Start with a concrete piecewise smooth function (like a square wave) and examine partial sum plots for N = 1, 5, 20, 100. Watch where the convergence is clean (continuous regions) and where it stays ragged (near jumps). Verify the Dirichlet conditions explicitly. Compute what the series gives at a jump point and confirm it matches the average of the left and right limits.

## Common Misconceptions
- Thinking Fourier series always converge to f(x) everywhere — they only do so at points of continuity.
- Expecting the Gibbs overshoot to shrink as N → ∞ — the overshoot narrows but maintains approximately 9% of the jump height.
- Confusing pointwise convergence with uniform convergence — Fourier series of piecewise smooth functions converge pointwise but not uniformly at jump discontinuities.

## Explainer

You already know from Fourier series definition how to compute the coefficients aₙ and bₙ — the integrals of f against cosines and sines. But computing coefficients and having the resulting series actually converge to f are two different things. For a general function, the partial sums Sₙ(x) might not approach anything. The convergence theorem answers the question: under what conditions does the series converge, and to what?

The **Dirichlet conditions** give a practical sufficient guarantee: if f is **piecewise smooth** on a period — meaning finitely many jump discontinuities and finitely many local extrema — then the Fourier series converges **pointwise** at every point. Pointwise convergence (a concept from your prerequisite on sequence convergence) means that for each fixed x, the sequence of partial sums S₁(x), S₂(x), S₃(x), ... converges to a specific limit. At any point where f is continuous, that limit is f(x) itself — the series reconstructs the function exactly. This is the good case.

At **jump discontinuities**, the series does something principled rather than arbitrary: it converges to the **average of the left and right limits**, [f(x⁻) + f(x⁺)]/2. For a square wave that jumps between −1 and +1, the series converges to exactly 0 at each jump point, regardless of what f was defined to equal there. This is the only symmetric and consistent choice — the Fourier series effectively "splits the difference" at every jump.

The **Gibbs phenomenon** reveals a subtlety that doesn't improve with more terms. Near a jump discontinuity, the partial sums overshoot the function by approximately 9% of the jump height — and this overshoot persists as N → ∞. It narrows (concentrating in a shrinking neighborhood of the jump) but never vanishes. This is not a failure of convergence: the series does converge pointwise to the correct average at the jump. But the convergence is not **uniform** near the jump — the maximum error over a small interval near the discontinuity stays bounded away from zero no matter how many terms you take. In signal processing, this Gibbs ringing means that sharp transitions in audio or images cannot be perfectly reproduced by a finite Fourier representation, a fundamental practical constraint.
