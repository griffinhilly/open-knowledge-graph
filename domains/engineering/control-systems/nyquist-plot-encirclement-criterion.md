---
id: nyquist-plot-encirclement-criterion
title: Nyquist Plot and Encirclement Criterion
domain: engineering
course: control-systems
prerequisites:
- id: nyquist-stability-criterion
  type: hard
- id: sinusoidal-response-magnitude-phase-angle
  type: hard
- id: complex-analysis
  type: soft
builds-toward:
- gain-margin-phase-margin-stability
tags:
- nyquist-diagram
- encirclement
- stability-test
- closed-loop-poles
- frequency-response
stage: advanced
status: draft
---

# Nyquist Plot and Encirclement Criterion

## Core Idea
The Nyquist criterion states: the closed-loop system is stable if and only if the plot of G(jω) encircles the point −1 a number of times equal to the number of RHP poles in the open-loop transfer function G(s). This elegant result connects open-loop frequency response to closed-loop stability.

## Questions

```yaml
- question: "A closed-loop system has no open-loop RHP poles (P = 0). Its Nyquist plot makes exactly one clockwise encirclement of the point −1. What can you conclude about closed-loop stability?"
  type: multiple-choice
  options:
    - "The closed-loop system is stable — the plant is open-loop stable, so the closed-loop must also be stable"
    - "The closed-loop system is unstable: Z = N + P = 1 + 0 = 1, meaning one RHP closed-loop pole exists"
    - "The closed-loop system is marginally stable — one clockwise encirclement indicates a pole on the imaginary axis"
    - "No conclusion can be drawn without also knowing the phase margin at the crossover frequency"
  answer: 1
  explanation: "The Nyquist criterion counts RHP closed-loop poles as Z = N + P, where N is the number of clockwise encirclements of −1 and P is the number of open-loop RHP poles. Here N = 1 (clockwise) and P = 0, so Z = 1 — one closed-loop pole in the right half-plane, meaning instability. The common misconception is that an open-loop stable plant (P = 0) guarantees a stable closed loop — it does not. Adding feedback can destabilize a stable plant, and the Nyquist criterion detects this via encirclement count."

- question: "Why does the Nyquist stability criterion examine encirclements of the specific point −1 + 0j rather than the origin?"
  type: multiple-choice
  options:
    - "The point −1 is where the open-loop transfer function G(jω) always reaches its maximum magnitude"
    - "Closed-loop instability occurs when 1 + G(s) = 0, i.e., when G(s) = −1; the critical point −1 is exactly where the closed-loop characteristic equation has a root"
    - "The origin is excluded because G(jω) always passes through the origin at ω = 0"
    - "The argument principle can only be applied to contours that avoid the imaginary axis"
  answer: 1
  explanation: "The closed-loop transfer function has poles where 1 + G(s) = 0, i.e., where G(s) = −1. In the Nyquist analysis, the argument principle is applied to F(s) = 1 + G(s) — counting its zeros in the RHP gives the number of unstable closed-loop poles. Zeros of F(s) = 1 + G(s) correspond to points where G(s) = −1, which is the point (−1, 0) in the complex plane. So encircling −1 in the Nyquist plot of G(jω) is equivalent to encircling the origin in the Nyquist plot of F(jω) = 1 + G(jω). The −1 point is the direct read-off of when the closed-loop characteristic equation is satisfied."

- question: "The Nyquist criterion can correctly determine the stability of a closed-loop system even when the open-loop plant has poles in the right half-plane (unstable open-loop poles), whereas Bode plot analysis cannot reliably handle this case."
  type: true-false
  answer: true
  explanation: "For open-loop stable systems (P = 0), Bode-based gain and phase margin analysis is sufficient and intuitive. But when P > 0, stability requires the Nyquist plot to encircle −1 exactly P times counterclockwise — a requirement that looks like instability to the Bode-only intuition. The argument principle underlying the Nyquist criterion handles any number of open-loop RHP poles through the Z = N + P formula. Bode analysis silently fails for non-minimum-phase systems and unstable plants because it cannot track the encirclement count correctly."

- question: "For a system with no open-loop RHP poles, the closed-loop system is stable as long as the Nyquist plot does not encircle or pass through the origin of the complex plane."
  type: true-false
  answer: false
  explanation: "The critical point is −1, not the origin. Stability requires the Nyquist plot of G(jω) to not encircle the point (−1, 0j). The origin has no special significance in the Nyquist stability criterion — G(jω) can pass through or encircle the origin without affecting stability. This is a common confusion: the argument principle in its raw form counts encirclements of the origin, but the Nyquist criterion shifts this to −1 because we analyze F(s) = 1 + G(s) and translate back to G."

- question: "Explain why the Nyquist criterion evaluates encirclements of the point −1 rather than the origin, and what physical condition the −1 point represents."
  type: short-answer
  answer: "The Nyquist criterion applies the argument principle to F(s) = 1 + G(s), whose zeros are the closed-loop poles. Zeros of F(s) in the RHP mean unstable closed-loop poles. The argument principle counts zeros minus poles of F inside the RHP contour by counting clockwise encirclements of the origin by F(jω). Since F(jω) = 1 + G(jω), an encirclement of the origin by F corresponds to an encirclement of −1 by G. Physically, the point −1 is where G(s) = −1, which satisfies 1 + G(s) = 0 — exactly the closed-loop characteristic equation. It represents the condition for closed-loop resonance or instability: the loop gain equals −1 (magnitude 1, phase −180°), meaning feedback reinforces rather than corrects disturbances."
  explanation: "The phase condition −180° is also where the Bode phase margin is defined: how many additional degrees of phase lag would bring the system to G(jω) = −1. Gain margin answers how much gain increase would bring the magnitude to 1 when the phase is already −180°. Both margins measure distance from the critical −1 point in different directions — confirming that −1 is the center of stability analysis in both the Nyquist and Bode frameworks."
```

## Explainer

The Bode plot displays magnitude and phase as separate graphs against frequency. The **Nyquist plot** displays the same information as a single curve in the complex plane: as ω sweeps from −∞ to +∞, the complex number G(jω) traces a closed curve. Each point's distance from the origin is the gain |G(jω)| and its angle is the phase ∠G(jω). Your prerequisite on sinusoidal magnitude and phase gave you the raw material; the Nyquist plot is a different coordinate system for the same data — one that makes stability analysis geometric.

The criterion emerges from the **argument principle** of complex analysis. For a closed contour in the s-plane encircling certain poles and zeros of a function F(s), the image contour under F encircles the origin a number of times equal to (Z − P), where Z is the enclosed zeros and P is the enclosed poles. For stability analysis, take F(s) = 1 + G(s) — the closed-loop characteristic polynomial. Its zeros are the closed-loop poles; its poles are the open-loop poles (which you know). Stability requires all closed-loop poles in the left half-plane, meaning zero zeros of 1 + G(s) inside the right half-plane (RHP) contour.

The Nyquist D-contour encloses the entire RHP. By the argument principle, the number of RHP closed-loop poles Z = N + P, where N is the number of clockwise encirclements of the origin by the image of 1 + G(jω), and P is the known count of open-loop RHP poles. Since 1 + G encircling the origin is equivalent to G encircling −1 + 0j, the criterion states: for a stable closed-loop system, the Nyquist plot of G must encircle the **critical point −1** exactly P times counterclockwise.

For systems with no open-loop RHP poles (the common stable-plant case), this simplifies dramatically: stability holds if and only if the Nyquist plot does *not* encircle −1. The gain margin and phase margin from your Bode analysis are now geometric: gain margin is how much you could scale the Nyquist curve before it passes through −1; phase margin is how many degrees of rotation would bring the curve to −1. The Nyquist criterion is strictly more general than Bode-based reasoning — it handles unstable plants (P > 0) and non-minimum-phase systems rigorously, situations where Bode plot intuition can fail silently.
