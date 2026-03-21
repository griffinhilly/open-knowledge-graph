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

## Questions

```yaml
- question: "A control system has one open-loop right-half-plane pole (P = 1). Its Nyquist plot makes exactly one counter-clockwise encirclement of −1. How many closed-loop RHP poles does this system have?"
  type: multiple-choice
  options:
    - "Z = 2 — counter-clockwise encirclements add instability"
    - "Z = 0 — the closed-loop system is stable"
    - "Z = 1 — the encirclement count equals the closed-loop pole count"
    - "Cannot be determined without counting all encirclements"
  answer: 1
  explanation: "By N = Z − P: one counter-clockwise encirclement means N = −1 (counter-clockwise encirclements are negative by convention). So Z = N + P = −1 + 1 = 0. The closed-loop system has no RHP poles and is stable. This illustrates the non-intuitive result that when the open-loop system has unstable poles (P > 0), the Nyquist plot *must* encircle −1 counter-clockwise for stability — zero encirclements would give Z = P = 1, meaning one unstable closed-loop pole. Stability requires counter-clockwise encirclements to cancel the open-loop instability."

- question: "Why is the critical point −1+0j rather than the origin when applying Cauchy's argument principle to closed-loop stability?"
  type: multiple-choice
  options:
    - "By engineering convention, −1 is always the gain crossover point for stable systems"
    - "Mapping G(s)H(s) instead of 1+G(s)H(s) shifts the reference by −1, so encirclements of the origin in F(s) correspond to encirclements of −1 in the G(s)H(s) plot"
    - "The −1 point corresponds to the location of all open-loop poles for typical plants"
    - "Cauchy's theorem requires the critical point to be on the negative real axis"
  answer: 1
  explanation: "Cauchy's argument principle counts encirclements of the *origin* by F(s) = 1+G(s)H(s). The zeros of F(s) are the closed-loop poles (roots of 1+GH = 0). But instead of mapping F(s), we map G(s)H(s) directly — a plot that is already easy to construct from Bode data. Shifting by −1: F(s) = 0 ↔ G(s)H(s) = −1. So counting encirclements of the origin by F(s) is equivalent to counting encirclements of −1 by G(s)H(s). The critical point moves from the origin to −1 solely because we substituted G(s)H(s) for the original function F(s) = 1+G(s)H(s)."

- question: "For an open-loop stable system (P = 0), zero encirclements of −1 is sufficient for closed-loop stability, but any number of counter-clockwise encirclements is also acceptable."
  type: true-false
  answer: false
  explanation: "When P = 0, stability requires Z = 0 closed-loop RHP poles. From N = Z − P = Z − 0 = Z, we need N = 0: exactly zero net encirclements. Counter-clockwise encirclements correspond to N < 0, which would mean Z = N < 0 — a mathematical impossibility (you can't have negative poles). Any clockwise or counter-clockwise net encirclements when P = 0 indicate instability. The Nyquist curve must pass to the right of −1 at the −180° crossing (or equivalently, −1 must lie outside the curve) for an open-loop stable system to be closed-loop stable."

- question: "An open-loop unstable system with two RHP poles (P = 2) requires exactly two counter-clockwise encirclements of −1 for closed-loop stability."
  type: true-false
  answer: true
  explanation: "For stability, Z = 0 (no closed-loop RHP poles). From N = Z − P, we need N = 0 − 2 = −2. A negative N means 2 counter-clockwise encirclements. This is the counterintuitive result: for an open-loop unstable plant, the Nyquist plot of the closed-loop stabilizing controller must encircle −1 counter-clockwise exactly P times. Too many or too few counter-clockwise encirclements both result in closed-loop instability. This is why Bode analysis (which only checks whether the curve crosses −1) can give wrong stability conclusions for open-loop unstable plants."

- question: "Why does the Nyquist criterion require counter-clockwise encirclements of −1 for closed-loop stability when the open-loop system has right-half-plane poles?"
  type: short-answer
  answer: "The relation N = Z − P connects encirclements (N), closed-loop RHP poles (Z), and open-loop RHP poles (P). For a stable closed-loop system we need Z = 0, so N must equal −P. A negative N means P counter-clockwise encirclements. The physical intuition: the open-loop plant already has P unstable poles that 'want to' push the closed-loop system unstable. The feedback loop must 'compensate' for each of these by generating one counter-clockwise encirclement of the critical point — each CCW encirclement cancels one unit of open-loop instability in Cauchy's counting. If the Nyquist curve instead makes fewer than P CCW encirclements, the closed-loop system inherits some of the open-loop instability (Z > 0)."
  explanation: "This is why Nyquist extends beyond Bode analysis. Bode analysis only checks whether the phase is above −180° at gain crossover — a rule derived implicitly assuming P = 0. When P > 0, the Bode rules predict instability (the curve must cross −1), but a well-designed feedback controller can still be stable because those crossings are CCW rather than CW. The Nyquist criterion correctly counts signed encirclements and handles this case; Bode's approximate rules do not."
```

## Explainer

From your study of Bode plots, you can read off gain margin and phase margin — practical stability measures that work well for most minimum-phase, open-loop stable systems. The Nyquist criterion is the rigorous foundation behind those intuitions, and it extends to cases where Bode analysis breaks down: plants with right-half-plane poles or zeros, non-minimum-phase systems, and systems with transportation delays whose phase response wraps around indefinitely.

The starting point is **Cauchy's argument principle** from complex analysis. If you evaluate a complex function F(s) around a closed contour in the s-plane, the number of clockwise encirclements of the origin in the F(s)-plane equals Z − P, where Z is the number of zeros of F inside the contour and P is the number of poles inside the contour. For stability analysis, define F(s) = 1 + G(s)H(s), where G(s)H(s) is the open-loop transfer function. The zeros of F(s) are the closed-loop poles — the roots of the characteristic equation 1 + G(s)H(s) = 0. For the closed-loop system to be stable, we need all closed-loop poles in the left half plane (LHP), meaning Z = 0 RHP zeros of F. The **Nyquist contour** is a closed path in the s-plane that encircles the entire RHP: it runs up the imaginary axis from −j∞ to +j∞ and closes with a large semicircle to the right.

The key substitution: instead of mapping F(s) = 1 + G(s)H(s) and counting encirclements of the origin, map G(s)H(s) directly and count encirclements of the **critical point −1+0j**. These are equivalent because shifting F(s) left by 1 shifts encirclements from the origin to −1. So the Nyquist criterion becomes: N = Z − P, where N is the number of clockwise encirclements of −1 by the Nyquist plot of G(s)H(s), Z is the number of closed-loop RHP poles, and P is the number of open-loop RHP poles (which you know from factoring the plant). For a stable closed loop you need Z = 0, so you need N = −P — that is, P counter-clockwise encirclements of −1. For open-loop stable systems (P = 0), stability requires exactly zero encirclements in either direction.

The connection to Bode plots is geometric. As frequency ω sweeps from 0 to ∞, G(jω)H(jω) traces a curve in the complex plane. The Bode magnitude plot gives |G(jω)H(jω)| (distance from origin) and the phase plot gives ∠G(jω)H(jω) (angle from positive real axis) — together they uniquely specify each point on the Nyquist curve. **Gain margin** is the factor by which gain could be increased before the Nyquist curve passes through −1, measured at the frequency where phase is −180°. **Phase margin** is the additional phase lag that would bring the curve to −1 at the gain crossover frequency. Both margins are visible on the Nyquist plot as distances from the critical point. The Nyquist criterion tells you not just whether these margins are positive but exactly how many times the curve encircles −1 — crucial for open-loop unstable plants where the Bode margin rules give the wrong answer.
