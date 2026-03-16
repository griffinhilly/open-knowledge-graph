---
id: sensitivity-and-robustness-functions
title: Sensitivity and Complementary Sensitivity Functions
domain: engineering
course: control-systems
prerequisites:
- id: model-uncertainty-robust-stability
  type: hard
- id: feedback-control-fundamentals
  type: soft
builds-toward:
- state-feedback-control-design
tags:
- sensitivity
- robustness
- transfer-functions
- performance
stage: advanced
status: draft
---

# Sensitivity and Complementary Sensitivity Functions

## Core Idea
Sensitivity function S(s) = 1/(1+L(s)) quantifies output deviation per unit plant perturbation; complementary sensitivity T(s) = L(s)/(1+L(s)) quantifies closed-loop response relative to open-loop. Trade-off: S and T are complementary (S + T = 1), so reducing error sensitivity at some frequencies increases it elsewhere. Design balances sensitivity and robustness across frequency range.

## Explainer

Start with the loop transfer function L(s) = C(s)P(s) — the product of controller and plant gains around the feedback loop. You learned from feedback control fundamentals that high loop gain reduces steady-state error. The **sensitivity function** S(s) = 1/(1 + L(s)) quantifies exactly how much error persists: if the plant changes by a small fraction δ, the output changes by S(jω) × δ at frequency ω. Where |L(jω)| is large, S is small and the feedback loop is tight — disturbances are well rejected. Where |L(jω)| is small (high frequencies), S approaches 1 and the loop has little authority.

The **complementary sensitivity function** T(s) = L(s)/(1 + L(s)) is the closed-loop transfer function from reference to output. It measures tracking performance: T close to 1 means the output faithfully follows the reference. The identity S + T = 1 is not just algebra — it is the fundamental conservation law of feedback. You cannot simultaneously reduce S and T at the same frequency. Making the loop tight for tracking (T ≈ 1) forces S ≈ 0 at those frequencies, which is good. But trying to make S small at high frequencies necessarily makes T large there, which means high-frequency noise on the sensor gets amplified into the control output.

This constraint has a deeper form known as Bode's sensitivity integral: for a stable, minimum-phase loop, the integral of log|S(jω)| over all frequencies equals zero. Suppressing sensitivity in one frequency band creates a "waterbed" — sensitivity must rise elsewhere to compensate. This is why integral controllers that eliminate steady-state error (pushing S to zero at DC) inevitably create a sensitivity peak at some finite frequency. You chose the location and height of that peak when you designed the controller.

For robust stability, the model uncertainty analysis you already know connects directly to T. If the true plant is P(1 + Δ), where |Δ(jω)| ≤ l_m(ω) is the multiplicative uncertainty bound, the closed-loop remains stable for all such plants if and only if |T(jω)| < 1/l_m(ω) at all frequencies. Large T — good tracking — conflicts with small T required for robustness to high-frequency uncertainty. This trade-off is inescapable and defines the bandwidth of any feedback system: push the crossover frequency too high and uncertainty grows faster than T falls, causing instability; too low and the loop is sluggish. The sensitivity and complementary sensitivity functions are the quantitative language for navigating this design space.
