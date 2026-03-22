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

## Questions

```yaml
- question: "A radar designer raises the detection threshold to reduce false alarms. What is the unavoidable consequence?"
  type: multiple-choice
  options:
    - "The probability of detection also increases — fewer false alarms means the system is more reliable overall"
    - "The probability of missed detections increases — real targets are more likely to go unrecognized"
    - "SNR improves because the threshold filters out more noise"
    - "The ROC curve shifts toward the upper-left corner, improving overall performance"
  answer: 1
  explanation: "Raising the threshold makes the detector more conservative: it requires stronger evidence before declaring a signal present. This reduces false alarms (Pfa), but it simultaneously increases missed detections — cases where a real signal falls below the threshold and goes undetected. The ROC curve itself does not shift; the designer is simply moving to a different operating point on the same curve. Threshold adjustment is a tradeoff within a fixed performance ceiling set by SNR, not a way to escape that ceiling."

- question: "What does increasing SNR do to the receiver operating characteristic (ROC) curve?"
  type: multiple-choice
  options:
    - "It shifts the operating point along the existing ROC curve toward lower false-alarm rates"
    - "It shifts the entire ROC curve toward the upper-left, enabling simultaneously higher detection and lower false-alarm rates"
    - "It has no effect on the ROC curve — SNR only matters for the matched filter, not the detector"
    - "It makes the ROC curve steeper near Pfa = 0 but flatter elsewhere"
  answer: 1
  explanation: "SNR determines how well separated the signal-plus-noise and noise-only distributions are in observation space. Higher SNR means greater separation, so there exists a threshold that simultaneously achieves high probability of detection and low probability of false alarm — the ROC curve bows further toward the ideal upper-left corner. Threshold adjustment moves you along the ROC curve; SNR improvement lifts the curve itself. This is why reducing noise or increasing signal power fundamentally improves detection in a way no threshold tuning can achieve."

- question: "In the likelihood ratio test, raising the detection threshold γ reduces the probability of false alarm."
  type: true-false
  answer: true
  explanation: "A higher threshold γ requires the likelihood ratio to be larger before declaring H₁, meaning you demand stronger evidence that a signal is present. This makes it less likely that pure noise — which generates smaller likelihood ratios on average — exceeds the threshold. So Pfa decreases. The cost is that weaker real signals also fail to exceed the higher threshold, increasing the probability of missed detections. The threshold γ directly controls the tradeoff point on the ROC curve."

- question: "Raising the detection threshold improves detection performance because it reduces errors."
  type: true-false
  answer: false
  explanation: "This is the core misconception in detection theory. Raising the threshold reduces one type of error (false alarms) while increasing another (missed detections). There is no threshold setting that eliminates both simultaneously — the ROC curve defines the fundamental tradeoff. What 'improves' detection in the sense of lifting overall performance is increasing SNR, not adjusting the threshold. The threshold allocates the available performance between error types according to application priorities; it cannot create performance that SNR does not permit."

- question: "Why can't adjusting the detection threshold substitute for improving SNR when the goal is to simultaneously reduce both false alarms and missed detections?"
  type: short-answer
  answer: "The ROC curve traces all achievable (Pfa, Pd) pairs for a fixed SNR. Every point on the curve corresponds to a different threshold. Moving along the curve by adjusting the threshold reduces one error type only by increasing the other — you cannot simultaneously improve both. Only increasing SNR separates the signal and noise distributions further, lifting the ROC curve toward the ideal corner and making it possible to achieve lower Pfa and higher Pd at the same time."
  explanation: "The key insight is that SNR sets the ceiling on performance — it determines the shape of the ROC curve — while the threshold determines where on that curve the system operates. A system with poor SNR is stuck on a ROC curve close to the diagonal, no matter how carefully the threshold is set. Improving SNR (by boosting signal power, reducing noise bandwidth, or integrating over longer intervals) stretches the curve toward the upper-left, expanding the region of achievable performance. Threshold tuning is local; SNR improvement is global."
```

## Explainer

Signal detection is the art of making decisions under uncertainty, and the statistical framework of hypothesis testing gives it mathematical precision. From your work with matched filters, you know that the matched filter maximizes SNR by correlating a received signal against a known template. But maximizing SNR is only half the problem: you still need a rule for converting that filter output into a binary decision. Signal detection theory provides this rule by framing the problem as a competition between two hypotheses: **H₀** (null hypothesis — noise alone) and **H₁** (alternative hypothesis — signal plus noise). Every observation is evaluated against both hypotheses, and a decision is made about which is more likely.

The optimal decision rule emerges from the **likelihood ratio test**. For each observation x, you compute the ratio of the probability of observing x under H₁ to the probability under H₀. If this ratio exceeds a threshold γ, you decide H₁; otherwise H₀. The threshold γ is the core design parameter that trades off two types of error: **probability of detection** (Pd) — the chance of correctly declaring a signal present — and **probability of false alarm** (Pfa) — the chance of mistakenly declaring a signal when there is none. Raising the threshold makes you more conservative: false alarms decrease, but so do correct detections. Lowering the threshold catches more real signals but at the cost of more false alarms.

The **receiver operating characteristic (ROC) curve** plots Pd versus Pfa as the threshold sweeps from zero to infinity, tracing the complete detection-false-alarm tradeoff for a fixed system. A perfect detector hugs the upper-left corner (Pd = 1, Pfa = 0); a random guesser lies on the diagonal. What pushes the ROC curve toward that ideal corner? **Signal-to-noise ratio (SNR)**. Higher SNR means the signal and noise distributions in the observation space are better separated, making it possible to find a threshold that simultaneously achieves high Pd and low Pfa. This is why increasing SNR — by boosting signal power, reducing noise, or integrating over longer time — fundamentally lifts detection performance in a way no threshold adjustment can achieve on its own.

A common misconception is that raising the threshold always "improves" the detector. It reduces false alarms, yes, but it simultaneously increases **missed detections** — cases where a real signal goes unrecognized. The right threshold depends on cost tradeoffs specific to the application: in radar, a false alarm wastes a countermeasure while a miss lets a threat through; in medical screening, a false alarm triggers unnecessary procedures while a miss allows disease to progress. By assigning explicit costs to each error type, the Bayesian-optimal threshold follows directly from the likelihood ratio. SNR sets the ceiling on achievable performance; the threshold allocates that performance between the two error types according to application priorities.
