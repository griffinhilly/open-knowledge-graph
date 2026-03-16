---
id: wiener-filter-optimal-estimation
title: Wiener Filter for Optimal Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
- id: lti-systems-and-impulse-response
  type: hard
builds-toward:
- kalman-filter-state-estimation
- adaptive-filtering-lms
tags:
- optimal-filtering
- estimation
- wiener
- frequency-domain
stage: advanced
status: draft
---

# Wiener Filter for Optimal Estimation

## Core Idea
The Wiener filter minimizes mean-square error for linear estimation, with optimal transfer function H(ω) = Sxy(ω)/Sxx(ω) in the frequency domain. It requires knowledge of signal and noise statistics. The non-causal solution is optimal but unrealizable; causal approximations reduce performance but enable real-time implementation.

## Explainer

You already know that an LTI system shapes a signal's power spectral density: if input has PSD Sxx(ω), the output PSD is |H(ω)|²·Sxx(ω). You also know that cross-correlation between signals reveals how much one predicts the other. The Wiener filter brings these two ideas together into a single engineering question: *given a noisy observation of a signal, what linear filter extracts the best estimate of the original?*

Start from first principles. You observe x(t) = s(t) + n(t) — signal plus noise — and you want to estimate s(t) by passing x(t) through a linear filter with impulse response h(t). The output ŝ(t) = (h * x)(t). "Best" means minimizing the **mean-square error** E[(s(t) − ŝ(t))²]. The famous result is that the optimal filter, in the frequency domain, is H_opt(ω) = S_sx(ω)/S_xx(ω). Here S_sx(ω) is the cross-power spectral density between desired signal and observation, and S_xx(ω) is the PSD of the observation. If signal and noise are uncorrelated, S_sx = S_ss and S_xx = S_ss + S_nn, giving the intuitive form H_opt(ω) = S_ss/(S_ss + S_nn) — a frequency-dependent weighting that passes frequencies where signal dominates and suppresses frequencies where noise dominates.

The formula reveals profound intuition: the Wiener filter is doing **frequency-by-frequency signal-to-noise weighting**. At frequencies where the signal PSD vastly exceeds the noise PSD, H ≈ 1 (pass everything). At frequencies where noise dominates, H ≈ 0 (block everything). This is smarter than a fixed low-pass filter because the optimal cutoff adapts to the spectral shape of both the signal and the noise. A speech signal buried in white noise at high frequencies needs a soft high-frequency rolloff; the Wiener filter computes exactly how soft, and at what frequencies.

There is one critical complication: the solution derived above is **non-causal** — the filter at time t can use future samples of x, which is impossible in real time. This forces a choice. In offline processing (seismic deconvolution, image restoration), the non-causal filter is ideal. In real-time systems, a causal approximation is needed. The **Wiener-Hopf equation** solves the constrained version, but obtaining the causal factor requires spectral factorization — a mathematically involved step. This is why the Kalman filter, which your next topic covers, emerged as an alternative: it naturally produces a causal, recursive estimator by tracking state sequentially, achieving Wiener-optimal performance without the spectral factorization challenge.

The practical limitation of the Wiener filter is its reliance on *known* statistics: S_xx and S_sx must be computed in advance from representative data. When the signal or noise statistics change over time, the fixed filter becomes suboptimal. This motivates **adaptive filters** (LMS and RLS algorithms), which update filter coefficients in real time to track nonstationary statistics. The Wiener solution provides the target that adaptive algorithms converge toward — the fixed-point of the adaptation process. Understanding the Wiener filter is therefore the conceptual foundation for all of modern optimal and adaptive signal processing.
