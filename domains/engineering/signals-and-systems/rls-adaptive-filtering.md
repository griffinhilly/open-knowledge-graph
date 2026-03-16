---
id: rls-adaptive-filtering
title: Recursive Least-Squares Adaptive Filtering
domain: engineering
course: signals-and-systems
prerequisites:
- id: adaptive-filtering-lms
  type: hard
tags:
- adaptive-filters
- rls
- least-squares
- convergence
stage: advanced
status: draft
---

# Recursive Least-Squares Adaptive Filtering

## Core Idea
Recursive Least-Squares (RLS) adapts filter coefficients to minimize weighted sum of squared errors using matrix inversion lemma for efficient recursive updates. Convergence is typically faster than LMS and can track time-varying systems with exponential weighting. The O(N²) complexity per update is higher than LMS but suitable for ill-conditioned channels.

## Explainer

You already know the LMS algorithm: it takes a small step in the direction of the negative gradient of the instantaneous squared error, nudging filter weights toward a better solution one sample at a time. LMS is appealingly simple, but its convergence speed is limited by the step size and — crucially — by how spread out the eigenvalues of the input autocorrelation matrix are. When eigenvalues are very unequal (a mismatched channel, for instance), LMS slows down dramatically because the single step size cannot be optimal in all directions simultaneously. RLS fixes this by directly minimizing the **weighted sum of all past squared errors**, not just the current one.

The key idea is that instead of a scalar step size, RLS maintains a matrix called the **inverse correlation matrix** P (often written as the gain matrix). This matrix tracks the curvature of the error surface in every direction, and the RLS update uses it to take a Newton-like step that adjusts the coefficients optimally across all dimensions at once. Computing P from scratch at every time step would require inverting an N×N matrix — expensive. The **matrix inversion lemma** (also called the Woodbury identity) allows you to update P recursively from its previous value using rank-1 operations, reducing the per-sample cost from O(N³) to O(N²). Even so, O(N²) is substantially costlier than LMS's O(N), which is the fundamental trade-off.

The **forgetting factor** λ (typically 0.95–0.999) gives RLS the ability to track time-varying systems. Past errors are weighted by λ^k where k is the number of samples ago they occurred — recent errors count more, older ones are exponentially down-weighted. A small λ makes the filter more responsive to changes but noisier; a large λ gives smoother estimates but slower tracking. Setting λ = 1 (no forgetting) means RLS minimizes the entire history of errors equally, which is correct for stationary problems but cannot follow a drifting channel.

In practice, RLS converges in roughly N iterations (where N is the filter order), whereas LMS may need thousands of iterations for the same result. This makes RLS the preferred choice in any application where initial convergence speed matters, where the channel is highly ill-conditioned, or where you need accurate estimates after only a short burst of training data. The cost is memory (storing P and intermediate vectors), arithmetic (O(N²) multiplications per sample), and some numerical sensitivity — the matrix P can become indefinite due to floating-point errors if not periodically reset or stabilized. For very large filters (N in the thousands), this quadratic cost becomes prohibitive, which motivates order-recursive variants like the **fast RLS** and **lattice-ladder** algorithms that exploit the structure of the autocorrelation matrix to reduce computation back toward O(N).


