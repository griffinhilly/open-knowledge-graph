---
id: magnitude-phase-computation-pole-zero
title: Magnitude and Phase from Pole-Zero Geometry
domain: engineering
course: signals-and-systems
prerequisites:
- id: pole-zero-plot-stability-analysis
  type: hard
builds-toward:
- bode-plot-construction
- frequency-response-and-bode-plots
tags:
- frequency-response
- pole-zero
- magnitude
- phase
stage: abstract-reasoning
status: draft
---

# Magnitude and Phase from Pole-Zero Geometry

## Core Idea
The magnitude response is the product of distances from zeros divided by distances from poles to a point on the s-plane or z-plane. Phase is the sum of angles from poles minus sum of angles from zeros. This geometric interpretation allows rapid sketching of frequency response and understanding how pole-zero placement affects system behavior.

## How It's Best Learned
Plot a simple pole-zero diagram and measure distances and angles to points along the imaginary axis at increasing frequencies. Verify results with analytical transfer function evaluation.

## Common Misconceptions
- Forgetting to include contributions from all poles and zeros.
- Confusing which direction (pole or zero) multiplies vs divides magnitude.
- Using distances rather than complex magnitudes.

## Explainer

From pole-zero plots and stability analysis you know that the poles and zeros of a transfer function H(s) encode all of its behavior — poles at s = p_k where the system resonates or decays, zeros at s = z_k where the output is suppressed. To evaluate the **frequency response**, you substitute s = jω (moving along the imaginary axis) for each frequency ω and compute H(jω). The geometric interpretation turns this algebraic substitution into a visual exercise: the magnitude and phase at any frequency ω are fully determined by the distances and angles from each pole and zero to the evaluation point jω on the imaginary axis.

For a transfer function written in factored form H(s) = K·∏(s − z_k) / ∏(s − p_i), each factor (jω − z_k) is a complex number whose **magnitude** is the Euclidean distance from the zero z_k to the point jω, and whose **angle** is the angle that the vector from z_k to jω makes with the positive real axis. The magnitude response is therefore |H(jω)| = |K|·(product of distances from all zeros to jω) / (product of distances from all poles to jω). To compute phase: ∠H(jω) = ∠K + (sum of angles from all zeros) − (sum of angles from all poles).

The intuition becomes powerful when you think about what happens as jω approaches a pole or a zero. As ω approaches the imaginary part of a pole (e.g., a pole at s = −σ + jω_0), the distance from the pole to jω shrinks, so the denominator becomes small and |H(jω)| peaks — this is a resonant peak in the frequency response. As ω passes through the imaginary part of a zero, the distance from that zero to jω approaches zero, the numerator vanishes, and |H(jω)| dips to zero — a notch in the frequency response. A zero exactly on the imaginary axis at s = jω_0 means the system completely rejects the frequency ω_0. This is how notch filters are designed: place a pair of complex-conjugate zeros on the imaginary axis at the frequency you want to block.

Tracing the frequency response from ω = 0 to ω → ∞ geometrically: start at the origin on the imaginary axis and sweep upward. Draw arrows from each pole and zero to your current position; update the distances (magnitude) and angles (phase) as you move. A pole close to the imaginary axis contributes a large spike in magnitude and a rapid phase shift from 0° to −180° as you pass its level. A zero near the imaginary axis contributes a magnitude dip and a phase shift from 0° to +180°. Poles and zeros far from the imaginary axis contribute slowly varying, gentle effects. This lets you sketch the approximate shape of a frequency response by inspection from the pole-zero plot — before any computation.

The **Bode plot** (your next topic) is essentially a log-frequency version of this geometric reasoning, with approximations that straighten the smooth curves into piecewise-linear asymptotes. Each real pole at s = −ω_0 contributes a −20 dB/decade slope change at ω = ω_0 and a −45°/decade phase slope centered there; each zero contributes the equal and opposite effects. Complex-conjugate poles at s = −σ ± jω_d produce a resonant peak whose height depends on how close they sit to the imaginary axis (the **Q factor**: Q = ω_n / 2σ). Building comfort with the pole-zero geometric interpretation before studying Bode plots will make the Bode approximation rules feel like natural consequences rather than arbitrary recipes.
