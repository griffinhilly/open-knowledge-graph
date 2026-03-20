---
id: signal-detection-and-hypothesis-testing
title: Signal Detection and Statistical Hypothesis Testing
domain: engineering
course: signals-and-systems
prerequisites:
- id: matched-filter-signal-detection
  type: soft
builds-toward:
- quantization-error-and-noise-analysis
- parametric-signal-models-ar-ma-arma
tags:
- detection
- hypothesis-testing
- statistics
- SNR
stage: advanced
status: draft
---

# Signal Detection and Statistical Hypothesis Testing

## Core Idea
Signal detection frames the problem as binary hypothesis testing: is the observed signal noise alone (H0) or signal plus noise (H1)? The optimal detector is the likelihood ratio test, which compares the probability of observations under each hypothesis. Detection performance is measured by probability of detection and false-alarm rate, controlled by threshold. SNR determines detection performance; higher SNR enables lower false-alarm rates for fixed detection probability.

## How It's Best Learned
Design a detector for a known sinusoid in Gaussian white noise. Compute receiver operating characteristic (ROC) curves showing detection probability vs false-alarm rate at different SNR levels.

## Common Misconceptions
- Thinking higher threshold always improves detection (increases misses).
- Confusing matched filtering with optimal detection threshold.
- Not recognizing that SNR fundamentally limits detection performance.

## Explainer

Signal detection is the art of making decisions under uncertainty, and the statistical framework of hypothesis testing gives it mathematical precision. From your work with matched filters, you know that the matched filter maximizes SNR by correlating a received signal against a known template. But maximizing SNR is only half the problem: you still need a rule for converting that filter output into a binary decision. Signal detection theory provides this rule by framing the problem as a competition between two hypotheses: **H₀** (null hypothesis — noise alone) and **H₁** (alternative hypothesis — signal plus noise). Every observation is evaluated against both hypotheses, and a decision is made about which is more likely.

The optimal decision rule emerges from the **likelihood ratio test**. For each observation x, you compute the ratio of the probability of observing x under H₁ to the probability under H₀. If this ratio exceeds a threshold γ, you decide H₁; otherwise H₀. The threshold γ is the core design parameter that trades off two types of error: **probability of detection** (Pd) — the chance of correctly declaring a signal present — and **probability of false alarm** (Pfa) — the chance of mistakenly declaring a signal when there is none. Raising the threshold makes you more conservative: false alarms decrease, but so do correct detections. Lowering the threshold catches more real signals but at the cost of more false alarms.

The **receiver operating characteristic (ROC) curve** plots Pd versus Pfa as the threshold sweeps from zero to infinity, tracing the complete detection-false-alarm tradeoff for a fixed system. A perfect detector hugs the upper-left corner (Pd = 1, Pfa = 0); a random guesser lies on the diagonal. What pushes the ROC curve toward that ideal corner? **Signal-to-noise ratio (SNR)**. Higher SNR means the signal and noise distributions in the observation space are better separated, making it possible to find a threshold that simultaneously achieves high Pd and low Pfa. This is why increasing SNR — by boosting signal power, reducing noise, or integrating over longer time — fundamentally lifts detection performance in a way no threshold adjustment can achieve on its own.

A common misconception is that raising the threshold always "improves" the detector. It reduces false alarms, yes, but it simultaneously increases **missed detections** — cases where a real signal goes unrecognized. The right threshold depends on cost tradeoffs specific to the application: in radar, a false alarm wastes a countermeasure while a miss lets a threat through; in medical screening, a false alarm triggers unnecessary procedures while a miss allows disease to progress. By assigning explicit costs to each error type, the Bayesian-optimal threshold follows directly from the likelihood ratio. SNR sets the ceiling on achievable performance; the threshold allocates that performance between the two error types according to application priorities.
