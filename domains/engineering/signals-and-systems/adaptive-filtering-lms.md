---
id: adaptive-filtering-lms
title: Adaptive Filtering with LMS Algorithm
domain: engineering
course: signals-and-systems
prerequisites:
- id: wiener-filter-optimal-estimation
  type: hard
- id: random-signals-autocorrelation-psd
  type: soft
builds-toward:
- rls-adaptive-filtering
tags:
- adaptive-filters
- lms
- gradient-descent
- convergence
stage: advanced
status: draft
---

# Adaptive Filtering with LMS Algorithm

## Core Idea
The Least Mean Squares (LMS) algorithm adapts filter coefficients using stochastic gradient descent: w[n+1] = w[n] – μ·e[n]·x[n]. For sufficiently small step size μ, coefficients converge in expectation to the Wiener solution. LMS has O(N) computational complexity per update, making it practical for real-time applications, with a tradeoff between convergence speed and final error.

## Explainer

The **Wiener filter** — your prerequisite — gives the optimal linear filter for a stationary signal in closed form: w_opt = R_xx⁻¹ r_xd, where R_xx is the input autocorrelation matrix and r_xd is the cross-correlation between input and desired signal. The solution is optimal in the minimum mean-square error sense. The problem is practical: to compute R_xx⁻¹, you need to know the statistics of your signal, and those statistics must remain constant (stationarity). In real applications — speech enhancement, echo cancellation, channel equalization — the signal statistics change over time and are not known in advance. The LMS algorithm solves this by estimating the gradient from a single sample at a time, never requiring explicit knowledge of R_xx.

The update rule w[n+1] = w[n] + 2μ·e[n]·x[n] (where e[n] is the error between desired output d[n] and filter output ŷ[n] = wᵀ[n]x[n]) is a **stochastic gradient descent** step. The true gradient of the mean-square error is -2·E[e[n]x[n]], but LMS replaces the expectation with a single instantaneous product e[n]·x[n]. This is a noisy estimate of the gradient, so the update takes a small step in an approximately correct direction rather than an exact step. Over many iterations, the random errors average out and the weight vector drifts toward the Wiener solution. The **step size** μ controls the learning rate: large μ means fast adaptation but large residual fluctuation around the optimum (**misadjustment**); small μ means slow adaptation but accurate final solution. Convergence requires μ < 1/(N·λ_max), where N is the filter length and λ_max is the largest eigenvalue of R_xx.

The genius of LMS is its O(N) complexity per sample update — only N multiplications and additions per time step, regardless of filter length. This is vastly cheaper than inverting R_xx (O(N³)) and makes real-time implementation practical on embedded hardware. Active noise-canceling headphones, for example, use LMS to adapt coefficients continuously as the noise environment changes: the microphone signal is x[n], the desired signal d[n] is silence (or near-silence detected by a reference microphone), and the filter updates in microseconds to track changing noise patterns. Echo cancelers in telephone networks use LMS with filter lengths of hundreds of taps to model the impulse response of the acoustic or electrical echo path, subtracting the estimated echo from the received signal.

The limitation of LMS is sensitivity to eigenvalue spread: if R_xx has some very large and some very small eigenvalues (a condition called high **eigenvalue spread**), a single step size μ must simultaneously be small enough not to diverge along the large-eigenvalue directions and large enough to converge usefully along the small-eigenvalue directions. The result is slow adaptation along the ill-conditioned directions. This motivates the Recursive Least Squares (RLS) algorithm — your next topic — which effectively preconditions the gradient by an estimate of R_xx⁻¹ at each step, achieving faster convergence at the cost of O(N²) complexity per update.
