---
id: nyquist-stability-analysis-systems
title: Nyquist Criterion for Stability Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: bode-plot-construction-interpretation
  type: hard
- id: pole-zero-plot-stability-analysis
  type: hard
tags:
- nyquist-criterion
- stability
- feedback-systems
stage: advanced
status: draft
---

# Nyquist Criterion for Stability Analysis

## Core Idea
The Nyquist criterion uses the frequency response H(jω) plotted in the complex plane to determine closed-loop stability without explicitly computing poles. Encirclements of the (-1, 0) point indicate instability; gain and phase margins measure robustness to perturbations.

## Explainer

From Bode plot analysis, you know how to read gain and phase margins from frequency response graphs — those margins tell you how far the open-loop response is from the instability boundary at −1. From pole-zero analysis, you know that a closed-loop system is stable if and only if all its poles lie in the left half of the s-plane. The **Nyquist criterion** unifies these ideas, giving a rigorous test for closed-loop stability based only on the open-loop frequency response, without ever computing the closed-loop poles explicitly.

The mathematical foundation is the **argument principle** from complex analysis: if a function F(s) is analytic inside a closed contour in the s-plane, the number of times F(s) encircles the origin as s traverses the contour equals Z − P, where Z and P are the numbers of zeros and poles of F(s) inside the contour. For stability analysis, define F(s) = 1 + G(s)H(s) — the characteristic polynomial of the closed loop. The **Nyquist contour** encloses the entire right half plane (the region of instability). A closed-loop pole in the RHP is a zero of F(s) = 1 + G(s)H(s), which is equivalent to a zero of G(s)H(s) = −1. So counting encirclements of the point (−1, 0) in the G(s)H(s)-plane as s traverses the Nyquist contour gives N = Z − P, where Z is the number of unstable closed-loop poles and P is the number of unstable open-loop poles. For a stable closed loop, Z must equal zero: **N = −P** (counterclockwise encirclements equal the number of open-loop RHP poles, if any).

The practical recipe: plot G(jω)H(jω) as ω sweeps from 0 to +∞, then mirror (conjugate) to get −∞ to 0, and close the contour at infinity. Count net clockwise encirclements of (−1, 0). For a system with no open-loop RHP poles (P = 0), any clockwise encirclement means instability. For a system with P open-loop RHP poles (an unstable plant, for example), you need exactly P counterclockwise encirclements for stability. This is more powerful than Bode analysis alone: Bode margins implicitly assume a minimum-phase, stable open-loop system, while Nyquist handles non-minimum-phase plants and conditionally stable systems (where increasing gain actually stabilizes the loop) correctly.

**Gain margin** and **phase margin** have precise geometric meaning on the Nyquist plot. The gain margin is the factor by which gain can increase before the Nyquist plot crosses through (−1, 0) — equivalently, 1/|G(jω_pc)| where ω_pc is the phase crossover frequency (where phase = −180°). The phase margin is how many additional degrees of phase lag would move the unit-circle crossing of the Nyquist plot to exactly (−1, 0). Both margins measure the distance from the plot to the critical point, giving robustness to gain uncertainty and phase delay respectively. A well-designed feedback system typically targets gain margin > 6 dB and phase margin > 45°, ensuring the system can tolerate significant plant uncertainty or additional actuator lag before going unstable.
