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

## Questions

```yaml
- question: "An adaptive equalizer is applied to a highly frequency-selective channel where the input autocorrelation matrix has eigenvalues spanning several orders of magnitude. LMS converges very slowly; RLS converges in about N iterations. What is the fundamental reason for RLS's advantage?"
  type: multiple-choice
  options:
    - "RLS uses a larger step size than LMS, allowing faster gradient descent along every direction"
    - "RLS maintains an inverse correlation matrix P that captures the curvature of the error surface in every direction, enabling Newton-like updates that are optimal across all dimensions simultaneously"
    - "RLS operates in the frequency domain, bypassing the time-domain eigenvalue spread problem entirely"
    - "RLS averages over more past data points, reducing variance and allowing larger effective step sizes"
  answer: 1
  explanation: "LMS uses a single scalar step size μ — one scalar for all directions in weight space. When the error surface has very different curvatures in different directions (high eigenvalue spread), a single step size cannot be simultaneously optimal everywhere: it must be small enough to avoid divergence in steep directions, which makes it unnecessarily slow in shallow directions. RLS tracks the full inverse correlation matrix P, which encodes the curvature in every direction. The RLS update is a Newton step — it adjusts weights optimally across all dimensions at once, eliminating the eigenvalue-spread sensitivity."

- question: "A RLS filter is tracking a slowly time-varying channel. The forgetting factor is set to λ = 0.97. What is the practical effect of decreasing λ to 0.90?"
  type: multiple-choice
  options:
    - "The filter converges more slowly because smaller λ gives less weight to recent data"
    - "The filter tracks faster but with more noise variance, because older data is down-weighted more aggressively, making estimates more responsive but less stable"
    - "The filter becomes equivalent to batch least squares, ignoring the time-varying nature of the channel"
    - "The filter converges faster and more stably because smaller λ improves the conditioning of the inverse correlation matrix"
  answer: 1
  explanation: "The forgetting factor λ determines how quickly old data is discounted: past errors are weighted by λ^k where k is how many samples ago they occurred. Smaller λ means older data is forgotten more quickly — the filter effectively uses a shorter window of past observations. This makes the filter more responsive to changes in channel statistics (faster tracking) but also more sensitive to noise (higher variance in steady-state estimates). Setting λ = 1 means all past data is equally weighted — no forgetting, no tracking capability for time-varying channels."

- question: "RLS converges in approximately N iterations regardless of the eigenvalue spread of the input autocorrelation matrix, because the inverse correlation matrix P allows the algorithm to make optimal updates in every direction simultaneously."
  type: true-false
  answer: true
  explanation: "This is the key advantage of RLS over LMS. Because P encodes the error surface curvature in all directions, RLS effectively normalizes the step in each direction by the local curvature — taking a large step in shallow directions and a small step in steep directions. This is the Newton's method principle applied to adaptive filtering. The convergence time is approximately N iterations (the filter order), independent of eigenvalue spread — a stark contrast to LMS, which can require thousands of iterations for ill-conditioned channels."

- question: "Setting the forgetting factor λ = 1 in RLS makes the filter maximally responsive to sudden changes in channel statistics."
  type: true-false
  answer: false
  explanation: "This is the opposite of the truth. λ = 1 means no forgetting — all past errors are weighted equally regardless of how old they are. This gives the filter the longest possible memory: it minimizes the total sum of all past squared errors, which is correct for stationary problems but means it cannot adapt to sudden changes. The filter is 'stuck' tracking the average channel over its entire history. To maximize responsiveness to sudden changes, you would use a small λ (e.g., 0.90–0.95), which aggressively downweights older data."

- question: "Explain why RLS converges much faster than LMS for adaptive equalization of a highly frequency-selective channel, and what cost is paid for this improved convergence."
  type: short-answer
  answer: "LMS uses a single scalar step size for all directions in weight space. When the input autocorrelation matrix has very unequal eigenvalues — as it does for frequency-selective channels — the error surface has different curvatures in different directions. A single step size must be small enough to avoid divergence in the steepest direction, making it far too small in shallow directions and causing slow overall convergence. RLS maintains the inverse correlation matrix P, which tracks the curvature in every direction. The RLS update scales each direction by its curvature, taking a Newton-like step that is simultaneously optimal in all dimensions — this eliminates the eigenvalue-spread problem, achieving convergence in ~N iterations. The cost is computational: RLS requires O(N²) multiplications per sample (versus LMS's O(N)), plus O(N²) memory for storing P, plus numerical sensitivity that requires periodic reinitialization."
  explanation: "The core trade-off is convergence speed versus computational complexity. RLS buys fast convergence by maintaining a full matrix description of the error surface, but this matrix requires O(N²) work per update and becomes prohibitively expensive for large filter orders."
```

## Explainer

You already know the LMS algorithm: it takes a small step in the direction of the negative gradient of the instantaneous squared error, nudging filter weights toward a better solution one sample at a time. LMS is appealingly simple, but its convergence speed is limited by the step size and — crucially — by how spread out the eigenvalues of the input autocorrelation matrix are. When eigenvalues are very unequal (a mismatched channel, for instance), LMS slows down dramatically because the single step size cannot be optimal in all directions simultaneously. RLS fixes this by directly minimizing the **weighted sum of all past squared errors**, not just the current one.

The key idea is that instead of a scalar step size, RLS maintains a matrix called the **inverse correlation matrix** P (often written as the gain matrix). This matrix tracks the curvature of the error surface in every direction, and the RLS update uses it to take a Newton-like step that adjusts the coefficients optimally across all dimensions at once. Computing P from scratch at every time step would require inverting an N×N matrix — expensive. The **matrix inversion lemma** (also called the Woodbury identity) allows you to update P recursively from its previous value using rank-1 operations, reducing the per-sample cost from O(N³) to O(N²). Even so, O(N²) is substantially costlier than LMS's O(N), which is the fundamental trade-off.

The **forgetting factor** λ (typically 0.95–0.999) gives RLS the ability to track time-varying systems. Past errors are weighted by λ^k where k is the number of samples ago they occurred — recent errors count more, older ones are exponentially down-weighted. A small λ makes the filter more responsive to changes but noisier; a large λ gives smoother estimates but slower tracking. Setting λ = 1 (no forgetting) means RLS minimizes the entire history of errors equally, which is correct for stationary problems but cannot follow a drifting channel.

In practice, RLS converges in roughly N iterations (where N is the filter order), whereas LMS may need thousands of iterations for the same result. This makes RLS the preferred choice in any application where initial convergence speed matters, where the channel is highly ill-conditioned, or where you need accurate estimates after only a short burst of training data. The cost is memory (storing P and intermediate vectors), arithmetic (O(N²) multiplications per sample), and some numerical sensitivity — the matrix P can become indefinite due to floating-point errors if not periodically reset or stabilized. For very large filters (N in the thousands), this quadratic cost becomes prohibitive, which motivates order-recursive variants like the **fast RLS** and **lattice-ladder** algorithms that exploit the structure of the autocorrelation matrix to reduce computation back toward O(N).


