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
