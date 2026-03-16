---
id: nyquist-stability-criterion
title: Nyquist Stability Criterion
domain: engineering
course: control-systems
prerequisites:
- id: bode-plot-stability-analysis
  type: hard
- id: complex-numbers-intro
  type: hard
- id: contour-integration
  type: hard
- id: complex-plane
  type: hard
- id: complex-functions-mappings
  type: soft
builds-toward:
- gain-and-phase-margins
tags:
- nyquist
- encirclement
- nyquist-contour
- winding-number
- argument-principle
stage: advanced
status: validated
---

# Nyquist Stability Criterion

## Core Idea
The Nyquist stability criterion provides a rigorous frequency-domain test for closed-loop stability based on the number of clockwise encirclements N of the critical point −1+0j by the Nyquist plot of the open-loop transfer function G(s)H(s). By Cauchy's argument principle, N = Z − P, where Z is the number of closed-loop right-half-plane poles and P is the number of open-loop RHP poles. For open-loop stable systems (P = 0), stability requires zero encirclements (N = 0). Unlike Bode's rules, the Nyquist criterion correctly handles non-minimum-phase plants, open-loop unstable plants, and systems with time delays that Bode's approximations cannot directly address.

## How It's Best Learned
Trace the Nyquist contour carefully and practice counting signed encirclements on hand-drawn Nyquist plots before using software. Relate the Nyquist plot to Bode plots by recognizing that the Bode magnitude and phase are simply the polar form of the Nyquist diagram at each frequency.

## Common Misconceptions
- Encircling the −1 point requires the contour to wind around it — direction and count both matter, not just proximity.
- For systems with open-loop imaginary-axis poles, the Nyquist contour must be indented around them; forgetting this changes the encirclement count.
- Zero encirclements guarantees stability only for open-loop stable systems (P = 0); when P > 0, exactly P counter-clockwise encirclements are needed.

## Explainer

From your study of Bode plots, you can read off gain margin and phase margin — practical stability measures that work well for most minimum-phase, open-loop stable systems. The Nyquist criterion is the rigorous foundation behind those intuitions, and it extends to cases where Bode analysis breaks down: plants with right-half-plane poles or zeros, non-minimum-phase systems, and systems with transportation delays whose phase response wraps around indefinitely.

The starting point is **Cauchy's argument principle** from complex analysis. If you evaluate a complex function F(s) around a closed contour in the s-plane, the number of clockwise encirclements of the origin in the F(s)-plane equals Z − P, where Z is the number of zeros of F inside the contour and P is the number of poles inside the contour. For stability analysis, define F(s) = 1 + G(s)H(s), where G(s)H(s) is the open-loop transfer function. The zeros of F(s) are the closed-loop poles — the roots of the characteristic equation 1 + G(s)H(s) = 0. For the closed-loop system to be stable, we need all closed-loop poles in the left half plane (LHP), meaning Z = 0 RHP zeros of F. The **Nyquist contour** is a closed path in the s-plane that encircles the entire RHP: it runs up the imaginary axis from −j∞ to +j∞ and closes with a large semicircle to the right.

The key substitution: instead of mapping F(s) = 1 + G(s)H(s) and counting encirclements of the origin, map G(s)H(s) directly and count encirclements of the **critical point −1+0j**. These are equivalent because shifting F(s) left by 1 shifts encirclements from the origin to −1. So the Nyquist criterion becomes: N = Z − P, where N is the number of clockwise encirclements of −1 by the Nyquist plot of G(s)H(s), Z is the number of closed-loop RHP poles, and P is the number of open-loop RHP poles (which you know from factoring the plant). For a stable closed loop you need Z = 0, so you need N = −P — that is, P counter-clockwise encirclements of −1. For open-loop stable systems (P = 0), stability requires exactly zero encirclements in either direction.

The connection to Bode plots is geometric. As frequency ω sweeps from 0 to ∞, G(jω)H(jω) traces a curve in the complex plane. The Bode magnitude plot gives |G(jω)H(jω)| (distance from origin) and the phase plot gives ∠G(jω)H(jω) (angle from positive real axis) — together they uniquely specify each point on the Nyquist curve. **Gain margin** is the factor by which gain could be increased before the Nyquist curve passes through −1, measured at the frequency where phase is −180°. **Phase margin** is the additional phase lag that would bring the curve to −1 at the gain crossover frequency. Both margins are visible on the Nyquist plot as distances from the critical point. The Nyquist criterion tells you not just whether these margins are positive but exactly how many times the curve encircles −1 — crucial for open-loop unstable plants where the Bode margin rules give the wrong answer.
