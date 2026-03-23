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
stage: expert
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

## Questions

```yaml
- question: "A system has a complex-conjugate pole pair at s = −0.05 ± j20. What does the magnitude response look like near ω = 20 rad/s?"
  type: multiple-choice
  options:
    - "A deep notch at ω = 20, because poles suppress the response at frequencies near their imaginary parts"
    - "A sharp resonant peak near ω = 20, because the pole pair is very close to the imaginary axis and the distance from the poles to jω becomes very small there"
    - "No notable feature — poles not on the imaginary axis cannot create peaks or notches in the frequency response"
    - "A gradual roll-off beginning at ω = 20, unrelated to the specific pole location"
  answer: 1
  explanation: "The magnitude is the product of zero distances divided by the product of pole distances. As ω approaches 20, the evaluation point j·20 comes very close to the pole at −0.05 + j20 (the real part −0.05 is tiny). The distance from that pole to j·20 approaches 0.05 — nearly zero — making the denominator very small and the magnitude very large. The closer poles sit to the imaginary axis (the smaller σ in s = −σ ± jω_d), the sharper and higher the resonant peak. This is the geometric explanation for why lightly-damped systems exhibit sharp resonances."

- question: "A transfer function has a zero at s = j8 (exactly on the imaginary axis). What happens to the magnitude response at ω = 8 rad/s?"
  type: multiple-choice
  options:
    - "The magnitude reaches a local maximum because zeros reinforce signals at their frequency"
    - "The magnitude is undefined because evaluating H(jω) at a zero creates division by zero"
    - "The magnitude drops to exactly zero, because the distance from the zero at j8 to the evaluation point j8 is zero, making the numerator vanish"
    - "The magnitude decreases slightly but remains positive — zeros only affect the phase, not the magnitude"
  answer: 2
  explanation: "The numerator factor (jω − z_k) evaluated at ω = 8 with zero z_k = j8 is (j8 − j8) = 0. The magnitude is |K| × (product of zero distances) / (product of pole distances); when one zero distance is exactly zero, the entire numerator product is zero, so |H(j8)| = 0. This is a perfect null — the system completely rejects the frequency ω = 8 rad/s. This is exactly how notch filters are designed: place a pair of complex-conjugate zeros on the imaginary axis at the frequency to be blocked. The distinction from option D is critical: zeros on the imaginary axis affect both magnitude (creating nulls) and phase."

- question: "The magnitude response |H(jω)| equals |K| times the product of distances from all zeros to the point jω, divided by the product of distances from all poles to jω."
  type: true-false
  answer: true
  explanation: "This follows directly from the factored form H(s) = K·∏(s − z_k)/∏(s − p_i). Substituting s = jω, each factor (jω − z_k) is a complex number whose magnitude is the Euclidean distance from the zero z_k to the point jω on the imaginary axis. The magnitude of a product equals the product of magnitudes, so |H(jω)| = |K| × ∏|jω − z_k| / ∏|jω − p_i| — exactly the product of zero distances over the product of pole distances. This geometric interpretation converts frequency response computation into a distance measurement problem, enabling rapid sketching by inspection."

- question: "A zero located at s = j·ω₀ on the imaginary axis causes a peak in the magnitude response at frequency ω₀, because the zero contributes energy at that exact frequency."
  type: true-false
  answer: false
  explanation: "A zero on the imaginary axis at s = jω₀ causes the magnitude to drop to exactly zero at ω = ω₀ — a complete null, not a peak. The zero sits in the numerator; when jω reaches the zero's location, the numerator distance goes to zero, and so does the entire magnitude. Peaks are caused by poles close to the imaginary axis (the denominator becomes small). The confusion between poles and zeros causing peaks vs. nulls is the most common error in applying the geometric interpretation. Remember: zeros ↔ nulls (numerator → zero), poles ↔ peaks (denominator → zero)."

- question: "A system has a single real pole at s = −3 and a single real zero at s = −30 (no other poles or zeros, gain K = 1). Using the geometric distance interpretation, describe the qualitative shape of the magnitude response from ω = 0 to ω → ∞."
  type: short-answer
  answer: "At ω = 0: distance from pole (−3) to j0 is 3; distance from zero (−30) to j0 is 30; so |H(0)| = 30/3 = 10. As ω increases: both distances grow, but the pole at −3 is much closer to the imaginary axis than the zero at −30. Near ω ≈ 3, the pole distance is roughly at its minimum (distance ≈ √(3² + ω²) − 3 is small), causing a gradual roll-off in the ratio. The zero at −30 contributes a gradually increasing numerator distance that begins to counteract the pole's effect as ω approaches 30. For ω >> 30: both distances grow approximately as ω, and their ratio approaches 1. The overall shape is a low-pass response that starts at magnitude 10 at DC, rolls off as the pole's effect dominates at intermediate frequencies, then levels out toward 1 at very high frequencies as the zero's compensating effect kicks in."
  explanation: "This intuition — poles close to the imaginary axis dominate the response near their frequency, zeros far away contribute slowly — is the foundation for Bode plot approximations. Real poles at s = −σ 'turn on' their effect at ω ≈ σ; zeros do the same. The geometric interpretation makes visible why a pole at −3 causes an effect at much lower frequencies than a zero at −30."
```

## Explainer

From pole-zero plots and stability analysis you know that the poles and zeros of a transfer function H(s) encode all of its behavior — poles at s = p_k where the system resonates or decays, zeros at s = z_k where the output is suppressed. To evaluate the **frequency response**, you substitute s = jω (moving along the imaginary axis) for each frequency ω and compute H(jω). The geometric interpretation turns this algebraic substitution into a visual exercise: the magnitude and phase at any frequency ω are fully determined by the distances and angles from each pole and zero to the evaluation point jω on the imaginary axis.

For a transfer function written in factored form H(s) = K·∏(s − z_k) / ∏(s − p_i), each factor (jω − z_k) is a complex number whose **magnitude** is the Euclidean distance from the zero z_k to the point jω, and whose **angle** is the angle that the vector from z_k to jω makes with the positive real axis. The magnitude response is therefore |H(jω)| = |K|·(product of distances from all zeros to jω) / (product of distances from all poles to jω). To compute phase: ∠H(jω) = ∠K + (sum of angles from all zeros) − (sum of angles from all poles).

The intuition becomes powerful when you think about what happens as jω approaches a pole or a zero. As ω approaches the imaginary part of a pole (e.g., a pole at s = −σ + jω_0), the distance from the pole to jω shrinks, so the denominator becomes small and |H(jω)| peaks — this is a resonant peak in the frequency response. As ω passes through the imaginary part of a zero, the distance from that zero to jω approaches zero, the numerator vanishes, and |H(jω)| dips to zero — a notch in the frequency response. A zero exactly on the imaginary axis at s = jω_0 means the system completely rejects the frequency ω_0. This is how notch filters are designed: place a pair of complex-conjugate zeros on the imaginary axis at the frequency you want to block.

Tracing the frequency response from ω = 0 to ω → ∞ geometrically: start at the origin on the imaginary axis and sweep upward. Draw arrows from each pole and zero to your current position; update the distances (magnitude) and angles (phase) as you move. A pole close to the imaginary axis contributes a large spike in magnitude and a rapid phase shift from 0° to −180° as you pass its level. A zero near the imaginary axis contributes a magnitude dip and a phase shift from 0° to +180°. Poles and zeros far from the imaginary axis contribute slowly varying, gentle effects. This lets you sketch the approximate shape of a frequency response by inspection from the pole-zero plot — before any computation.

The **Bode plot** (your next topic) is essentially a log-frequency version of this geometric reasoning, with approximations that straighten the smooth curves into piecewise-linear asymptotes. Each real pole at s = −ω_0 contributes a −20 dB/decade slope change at ω = ω_0 and a −45°/decade phase slope centered there; each zero contributes the equal and opposite effects. Complex-conjugate poles at s = −σ ± jω_d produce a resonant peak whose height depends on how close they sit to the imaginary axis (the **Q factor**: Q = ω_n / 2σ). Building comfort with the pole-zero geometric interpretation before studying Bode plots will make the Bode approximation rules feel like natural consequences rather than arbitrary recipes.
