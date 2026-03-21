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
stage: advanced
status: draft
---

# Nyquist Criterion and Stability from Frequency Response

## Core Idea
The Nyquist criterion states that the number of clockwise encirclements of the (-1, 0) point in the G(jω)H(jω) polar plot equals the number of unstable closed-loop poles. A stable open-loop system with M unstable poles requires M counterclockwise encirclements for closed-loop stability. This provides both a graphical and analytical stability test.

## Questions

```yaml
- question: "A feedback system has an open-loop transfer function with 2 unstable poles (P = 2). The engineer plots the Nyquist diagram and counts 1 clockwise encirclement of the (-1, 0) point. What does this imply about the closed-loop system?"
  type: multiple-choice
  options:
    - "The closed-loop system is stable because only 1 encirclement is present"
    - "The closed-loop system is unstable: N = Z - P gives Z = N + P = 1 + 2 = 3 unstable closed-loop poles"
    - "The result is inconclusive — the Bode plot must also be checked before drawing conclusions"
    - "The closed-loop system is marginally stable since the Nyquist plot did not pass through (-1, 0)"
  answer: 1
  explanation: "The Nyquist stability criterion states N = Z - P, where N is the number of net clockwise encirclements of (-1, 0), Z is the number of unstable closed-loop poles, and P is the number of unstable open-loop poles. With N = 1 and P = 2: 1 = Z - 2, so Z = 3. Three unstable closed-loop poles means the system is unstable. For stability, Z = 0 is required, which needs N = -P = -2 — two counterclockwise encirclements."

- question: "Why is the point (-1, 0) specifically the critical point in the Nyquist criterion, rather than the origin or any other reference?"
  type: multiple-choice
  options:
    - "It is chosen by convention to make the gain margin equal to 1 at marginal stability"
    - "A closed-loop instability occurs when 1 + G(jω)H(jω) = 0, i.e., G(jω)H(jω) = -1, which is exactly the point (-1, 0) — the gain and phase condition for marginal closed-loop instability"
    - "The (-1, 0) point is where the phase of the open-loop transfer function crosses 0°, marking the natural frequency"
    - "(-1, 0) is the point where the open-loop gain equals the phase margin by definition"
  answer: 1
  explanation: "The closed-loop characteristic equation is 1 + G(s)H(s) = 0. A root on the imaginary axis at s = jω means G(jω)H(jω) = -1, which corresponds to (-1, 0) in the complex plane. The argument principle applied to 1 + GH maps encirclements of its origin to encirclements of (-1, 0) in the GH-plane (they differ by a shift of 1 on the real axis). The (-1, 0) point is not a convention — it is the exact condition under which the closed-loop system is on the verge of instability."

- question: "The Nyquist criterion can correctly determine closed-loop stability even when the open-loop transfer function has poles in the right half plane."
  type: true-false
  answer: true
  explanation: "This is one of Nyquist's key advantages over Bode analysis. The formula N = Z - P explicitly accounts for open-loop RHP poles (P ≠ 0). For stability, Z = 0 is required, so exactly P counterclockwise encirclements are needed to compensate. Bode gain and phase margins implicitly assume P = 0 (minimum-phase, stable open loop) and therefore cannot reliably analyze systems with open-loop instability."

- question: "Gain margin and phase margin derived from a Bode diagram provide an equivalent and equally reliable stability assessment to the Nyquist criterion, including for systems with open-loop unstable poles."
  type: true-false
  answer: false
  explanation: "Bode margins are valid only when the open-loop system is stable and minimum-phase (no RHP poles or zeros). For systems with open-loop RHP poles, the Bode margin interpretation fails: the crossover frequencies may suggest adequate margins while the closed loop is actually unstable, or a conditionally stable system may require a specific range of gains that Bode margins do not reveal. The Nyquist criterion handles non-minimum-phase plants and open-loop unstable systems correctly through explicit N = Z - P accounting."

- question: "Why does the Nyquist criterion analyze encirclements of (-1, 0) rather than simply checking whether the open-loop transfer function has any poles in the right half plane?"
  type: short-answer
  answer: "The stability question is about the closed-loop poles, not the open-loop poles. A system can be open-loop unstable but closed-loop stable — this is precisely how feedback is used to stabilize an inherently unstable plant. The Nyquist criterion applies the argument principle to count RHP zeros of 1 + G(s)H(s), which are the closed-loop poles, by counting encirclements of (-1, 0) in the GH-plane. This converts a closed-loop pole-counting problem (which would require computing the closed-loop transfer function explicitly) into an encirclement-counting problem on the open-loop frequency response (which is directly measurable). The formula N = Z - P relates encirclements to closed-loop RHP poles after accounting for known open-loop RHP poles."
  explanation: "This is also why Nyquist works on experimentally identified frequency responses: you do not need an analytic transfer function — you can measure G(jω) directly by sweeping a sinusoidal input and plot the Nyquist diagram from the measured data."
```

## Explainer

From your study of frequency response, you know how to compute and plot G(jω) as ω sweeps from 0 to ∞ — the magnitude and phase of the open-loop transfer function at each frequency. The **Nyquist criterion** asks you to extend this to a full polar plot and watch what happens around one special point: (−1, 0) in the complex plane. That point is special because it represents the exact gain-and-phase condition for marginal instability in the closed-loop system.

The deep reason is the **argument principle** from complex analysis. Consider the closed-loop characteristic equation 1 + G(s)H(s) = 0, whose roots are the closed-loop poles. If you map the Nyquist contour — a large clockwise D-shaped path encircling the entire right-half plane — through G(s)H(s), the number of clockwise encirclements of the origin of 1 + GH equals the number of zeros of 1 + GH inside the contour (unstable closed-loop poles, Z) minus the number of poles of GH inside the contour (unstable open-loop poles, P). The same encirclement count around the origin of 1 + GH equals the encirclement count around (−1, 0) of GH itself, because they differ by a shift of 1 on the real axis. So: **N = Z − P**, where N is clockwise encirclements of (−1, 0).

For closed-loop stability, you need Z = 0 (no unstable closed-loop poles). Therefore you need N = −P, meaning P counterclockwise encirclements. If the open-loop system is stable (P = 0), closed-loop stability requires N = 0: the Nyquist plot must not encircle (−1, 0) at all. If the open-loop system has P unstable poles — as happens with some integrating systems or marginally stable plants — you need exactly P counterclockwise encirclements to cancel them. Crucially, this analysis works even when the open-loop system is unstable, which is something root locus and Bode methods handle less cleanly.

The connection to **gain and phase margin** from your prerequisite is direct. On the Nyquist plot, the gain margin is how much you can scale G(jω) before it reaches (−1, 0) along the negative real axis; the phase margin is how far the plot is from (−1, 0) at the unit-gain circle crossing. Both are geometric distances from the critical point. Nyquist provides the rigorous foundation that Bode diagrams approximate: Bode works well for systems without right-half-plane poles or zeros, but Nyquist handles the general case and makes the stability mechanism — encirclement of the critical point — explicit and countable rather than approximate.
