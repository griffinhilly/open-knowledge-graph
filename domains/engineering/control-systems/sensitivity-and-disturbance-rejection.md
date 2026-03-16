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

## Explainer

The sensitivity function emerges naturally from what you already know about feedback. Recall that in a closed-loop system the output depends on both the reference signal and any disturbances or noise that enter the plant. From your study of transfer functions and feedback fundamentals, you know that the closed-loop transfer function from reference to output is T(s) = GC/(1+GC). The **sensitivity function** S(s) = 1/(1+GC) describes something different: how disturbances injected at the plant output survive to appear at the output. If you notice that the denominator 1+GC is identical in both functions, you can immediately see why S + T = 1 — it is an algebraic identity, not an approximation, holding at every value of s.

Think of |S(jω)| as a frequency-resolved disturbance survival rate. If |S(jω)| = 0.1 at 1 Hz, a 1 Hz disturbance entering the plant is reduced to 10% of its original amplitude — feedback rejects 90% of it. If |S(jω)| = 2 at 100 Hz, feedback actually amplifies that disturbance twofold. Large loop gain GC makes |S| small: the denominator 1+GC is much larger than 1, so S ≈ 1/GC → 0. But large loop gain at all frequencies is impossible — the loop must roll off at high frequencies to prevent instability and to avoid amplifying sensor noise. The **complementary sensitivity function** T describes how measurement noise propagates to the output: large |T| means noise gets through; small |T| means noise is rejected. Since S + T = 1, whenever you push |S| down at a frequency you push |T| up there. You are never eliminating sensitivity — you are choosing where to place it.

Bode's integral theorem formalizes this into the **waterbed effect**: for a plant with sufficient high-frequency roll-off, the integral of log|S(jω)| over all frequencies is zero (or positive if the plant has right-half-plane poles). Pushing down on one part of the sensitivity curve forces another part to bulge upward. Physically, this means aggressive disturbance rejection in one frequency band creates a band where disturbances are amplified. The peak of |S| above unity — the **sensitivity peak M_s** — is also a robustness measure: a larger M_s means the closed loop is closer to instability as the plant model changes, since it corresponds geometrically to how close the Nyquist curve passes to the −1 point.

The practical design insight is to treat S and T as frequency response targets. You want |S| small in the low-frequency band where process disturbances concentrate (requiring high loop gain there) and |T| small at high frequencies where sensor noise dominates (requiring low loop gain there). The **crossover frequency** — where loop gain transitions from large to small — sets the system bandwidth. A well-designed compensator achieves a smooth crossover without an excessive M_s peak. Bode's integral theorem tells you the total "area" under log|S| is fixed by the plant's unstable poles — clever control design allocates that unavoidable sensitivity to the least harmful frequency range, rather than pretending it can be eliminated.
