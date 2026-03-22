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

## Questions

```yaml
- question: "An LMS adaptive filter has been running stably. An engineer doubles the step size μ hoping to track faster environmental changes. What is the most likely trade-off?"
  type: multiple-choice
  options:
    - "The filter converges faster and achieves lower steady-state error simultaneously"
    - "The filter tracks changes faster but exhibits larger residual fluctuations (higher misadjustment) around the Wiener solution"
    - "The filter converges to a completely different optimal solution determined by μ"
    - "The filter's O(N) computational complexity per sample increases"
  answer: 1
  explanation: "Larger μ means bigger steps toward the Wiener solution, so adaptation is faster. But the instantaneous gradient estimate e[n]·x[n] is noisy, so large steps also produce larger random excursions around the optimal point — this is misadjustment. The Wiener solution being targeted doesn't change; only the precision of the final estimate does. There is always a speed-accuracy trade-off in LMS."

- question: "Why does LMS not require explicit computation of the input autocorrelation matrix R_xx, unlike the Wiener filter?"
  type: multiple-choice
  options:
    - "LMS only works on deterministic signals where R_xx is trivially the identity matrix"
    - "LMS converges to a solution that is intentionally different from the Wiener optimal"
    - "LMS uses the instantaneous product e[n]·x[n] as a noisy single-sample estimate of the gradient, avoiding any explicit statistical computation"
    - "Modern processors can invert R_xx fast enough that LMS skips the step for efficiency"
  answer: 2
  explanation: "The Wiener filter requires R_xx⁻¹ r_xd, which demands knowledge of the signal's second-order statistics — impractical when statistics are unknown or nonstationary. LMS replaces the true gradient −2·E[e[n]x[n]] with the instantaneous estimate −2·e[n]·x[n], a noisy but unbiased approximation. Because each update needs only the current error and input sample, R_xx is never computed."

- question: "The LMS algorithm achieves O(N) computational complexity per update because it approximates the gradient using a single data sample rather than computing a full statistical expectation."
  type: true-false
  answer: true
  explanation: "Each LMS update requires only one inner product (to compute the filter output ŷ[n] = wᵀx[n]) and one outer product (to update weights: w[n+1] = w[n] + 2μe[n]x[n]). Both are O(N) operations. The Wiener solution requires inverting R_xx — an O(N³) operation — which LMS avoids entirely by working sample-by-sample."

- question: "Once an LMS adaptive filter has converged, its weight vector is fixed permanently at the Wiener solution and ceases to update."
  type: true-false
  answer: false
  explanation: "LMS never stops updating — it applies a new gradient step at every sample. Because the gradient estimate is noisy, the weights continue to fluctuate randomly around the Wiener solution even after convergence. This residual fluctuation is called misadjustment and is the price paid for O(N) complexity. It is controlled by choosing a sufficiently small μ."

- question: "The LMS algorithm uses a noisy, single-sample gradient estimate rather than the true gradient. Why does this still cause the weight vector to converge toward the Wiener solution over time?"
  type: short-answer
  answer: "The instantaneous gradient estimate e[n]·x[n] is an unbiased estimate of the true gradient E[e[n]x[n]] — the noise averages to zero over many samples. Each individual step may point in a slightly wrong direction, but on average the steps point toward the Wiener solution. Over many iterations, the random errors cancel and the weight vector drifts in the correct direction in expectation, converging to the Wiener solution (with residual misadjustment proportional to μ)."
  explanation: "This is the stochastic gradient descent principle: noisy gradient estimates work because their expectation equals the true gradient. The key condition is that the noise is zero-mean, so it neither biases the direction of convergence nor pushes the filter away from the Wiener solution on average."
```

## Explainer

The **Wiener filter** — your prerequisite — gives the optimal linear filter for a stationary signal in closed form: w_opt = R_xx⁻¹ r_xd, where R_xx is the input autocorrelation matrix and r_xd is the cross-correlation between input and desired signal. The solution is optimal in the minimum mean-square error sense. The problem is practical: to compute R_xx⁻¹, you need to know the statistics of your signal, and those statistics must remain constant (stationarity). In real applications — speech enhancement, echo cancellation, channel equalization — the signal statistics change over time and are not known in advance. The LMS algorithm solves this by estimating the gradient from a single sample at a time, never requiring explicit knowledge of R_xx.

The update rule w[n+1] = w[n] + 2μ·e[n]·x[n] (where e[n] is the error between desired output d[n] and filter output ŷ[n] = wᵀ[n]x[n]) is a **stochastic gradient descent** step. The true gradient of the mean-square error is -2·E[e[n]x[n]], but LMS replaces the expectation with a single instantaneous product e[n]·x[n]. This is a noisy estimate of the gradient, so the update takes a small step in an approximately correct direction rather than an exact step. Over many iterations, the random errors average out and the weight vector drifts toward the Wiener solution. The **step size** μ controls the learning rate: large μ means fast adaptation but large residual fluctuation around the optimum (**misadjustment**); small μ means slow adaptation but accurate final solution. Convergence requires μ < 1/(N·λ_max), where N is the filter length and λ_max is the largest eigenvalue of R_xx.

The genius of LMS is its O(N) complexity per sample update — only N multiplications and additions per time step, regardless of filter length. This is vastly cheaper than inverting R_xx (O(N³)) and makes real-time implementation practical on embedded hardware. Active noise-canceling headphones, for example, use LMS to adapt coefficients continuously as the noise environment changes: the microphone signal is x[n], the desired signal d[n] is silence (or near-silence detected by a reference microphone), and the filter updates in microseconds to track changing noise patterns. Echo cancelers in telephone networks use LMS with filter lengths of hundreds of taps to model the impulse response of the acoustic or electrical echo path, subtracting the estimated echo from the received signal.

The limitation of LMS is sensitivity to eigenvalue spread: if R_xx has some very large and some very small eigenvalues (a condition called high **eigenvalue spread**), a single step size μ must simultaneously be small enough not to diverge along the large-eigenvalue directions and large enough to converge usefully along the small-eigenvalue directions. The result is slow adaptation along the ill-conditioned directions. This motivates the Recursive Least Squares (RLS) algorithm — your next topic — which effectively preconditions the gradient by an estimate of R_xx⁻¹ at each step, achieving faster convergence at the cost of O(N²) complexity per update.
