---
id: sensitivity-and-disturbance-rejection
title: Sensitivity and Disturbance Rejection
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- robust-control-basics
tags:
- sensitivity-function
- complementary-sensitivity
- disturbance-rejection
- noise-sensitivity
- bandwidth
- waterbed-effect
stage: advanced
status: draft
---

# Sensitivity and Disturbance Rejection

## Core Idea
The sensitivity function S(s) = 1/(1 + G(s)C(s)) and complementary sensitivity function T(s) = G(s)C(s)/(1 + G(s)C(s)) together characterize how a feedback system responds to disturbances, references, and model uncertainty, satisfying the fundamental constraint S(s) + T(s) = 1 at every frequency. S(jω) quantifies how disturbances at the plant output are attenuated by feedback: |S(jω)| < 1 means disturbance rejection, while |S(jω)| > 1 means disturbance amplification. T(jω) describes how sensor noise propagates to the output and also measures the system's sensitivity to multiplicative plant uncertainty. Good disturbance rejection requires |S(jω)| to be small at low frequencies (high loop gain), while noise rejection and robustness to uncertainty require |T(jω)| to be small at high frequencies (low loop gain). Since S + T = 1, these goals are complementary: one cannot make both small at the same frequency, establishing a fundamental design tradeoff. Bode's integral theorem (the waterbed effect) further constrains design: for systems with RHP poles or zeros, reducing |S| in one frequency band necessarily increases it in another, making the tradeoff inescapable.

## How It's Best Learned
Plot S(jω) and T(jω) for a simple feedback system as the controller gain varies, observing how increasing gain pushes |S| down at low frequencies but increases the peak of |S| near the crossover frequency. Then introduce a disturbance signal and a noise signal simultaneously and observe how the closed-loop output is affected at different frequencies, directly connecting the S and T magnitudes to physical behavior. Study the S + T = 1 constraint graphically to internalize why perfect disturbance rejection and perfect noise rejection are mutually exclusive.

## Common Misconceptions
- Making the loop gain as large as possible does not minimize sensitivity at all frequencies — it reduces |S| at low frequencies but causes |S| to peak above unity near the crossover frequency, potentially amplifying disturbances in that band.
- The sensitivity function S(s) is not the same as the closed-loop transfer function T(s) — S relates disturbances to output while T relates reference inputs to output, and they play complementary roles in the design.
- The waterbed effect is not just a theoretical curiosity — it means that control design is fundamentally about distributing sensitivity across frequency, not eliminating it, and aggressive disturbance rejection in one band always comes at the cost of amplification elsewhere.
