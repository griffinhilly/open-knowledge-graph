---
id: nyquist-stability-from-frequency-response
title: Nyquist Criterion and Stability from Frequency Response
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-phase-basics
  type: hard
- id: gain-phase-margin-stability-measures
  type: soft
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- nyquist
- stability-criterion
- encirclement
- polar-plot
stage: abstract-reasoning
status: draft
---

# Nyquist Criterion and Stability from Frequency Response

## Core Idea
The Nyquist criterion states that the number of clockwise encirclements of the (-1, 0) point in the G(jω)H(jω) polar plot equals the number of unstable closed-loop poles. A stable open-loop system with M unstable poles requires M counterclockwise encirclements for closed-loop stability. This provides both a graphical and analytical stability test.

## Explainer

From your study of frequency response, you know how to compute and plot G(jω) as ω sweeps from 0 to ∞ — the magnitude and phase of the open-loop transfer function at each frequency. The **Nyquist criterion** asks you to extend this to a full polar plot and watch what happens around one special point: (−1, 0) in the complex plane. That point is special because it represents the exact gain-and-phase condition for marginal instability in the closed-loop system.

The deep reason is the **argument principle** from complex analysis. Consider the closed-loop characteristic equation 1 + G(s)H(s) = 0, whose roots are the closed-loop poles. If you map the Nyquist contour — a large clockwise D-shaped path encircling the entire right-half plane — through G(s)H(s), the number of clockwise encirclements of the origin of 1 + GH equals the number of zeros of 1 + GH inside the contour (unstable closed-loop poles, Z) minus the number of poles of GH inside the contour (unstable open-loop poles, P). The same encirclement count around the origin of 1 + GH equals the encirclement count around (−1, 0) of GH itself, because they differ by a shift of 1 on the real axis. So: **N = Z − P**, where N is clockwise encirclements of (−1, 0).

For closed-loop stability, you need Z = 0 (no unstable closed-loop poles). Therefore you need N = −P, meaning P counterclockwise encirclements. If the open-loop system is stable (P = 0), closed-loop stability requires N = 0: the Nyquist plot must not encircle (−1, 0) at all. If the open-loop system has P unstable poles — as happens with some integrating systems or marginally stable plants — you need exactly P counterclockwise encirclements to cancel them. Crucially, this analysis works even when the open-loop system is unstable, which is something root locus and Bode methods handle less cleanly.

The connection to **gain and phase margin** from your prerequisite is direct. On the Nyquist plot, the gain margin is how much you can scale G(jω) before it reaches (−1, 0) along the negative real axis; the phase margin is how far the plot is from (−1, 0) at the unit-gain circle crossing. Both are geometric distances from the critical point. Nyquist provides the rigorous foundation that Bode diagrams approximate: Bode works well for systems without right-half-plane poles or zeros, but Nyquist handles the general case and makes the stability mechanism — encirclement of the critical point — explicit and countable rather than approximate.
