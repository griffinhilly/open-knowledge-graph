---
id: simple-pendulum
title: The Simple Pendulum
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: circular-motion-kinematics
  type: soft
- id: trigonometric-ratios-review
  type: soft
tags:
- pendulum
- SHM
- oscillation
- gravity
stage: formal-systems
status: validated
---

# The Simple Pendulum

## Core Idea
A simple pendulum (point mass on a massless string of length L) undergoes approximate SHM for small angles (θ < ~15°), with angular frequency ω = √(g/L) and period T = 2π√(L/g). The restoring force is the tangential component of gravity: F_t = −mg sinθ ≈ −mgθ (small angle). The period depends on L and g, but not on mass or amplitude (for small oscillations).

## How It's Best Learned
Measure pendulum period for various lengths and verify the T ∝ √L relationship. Also test the small-angle approximation by comparing measured periods at 5°, 20°, and 45° amplitude — the approximation degrades at large angles.

## Common Misconceptions
- Thinking heavier pendulums oscillate faster: period is mass-independent.
- Applying T = 2π√(L/g) for large swings: it overestimates period because sin θ < θ only for small θ.
- Confusing the pendulum length L (measured to the center of mass) with the string length when using a physical bob of nonnegligible size.

## Questions

```yaml
- question: "Pendulum A has a 100g bob; pendulum B has an identical string length but a 400g bob. How do their periods compare under small-angle oscillations?"
  type: multiple-choice
  options:
    - "Pendulum B has half the period of A, because a heavier bob oscillates faster"
    - "Pendulum B has twice the period of A, because more mass means more inertia"
    - "They have identical periods, because period is independent of mass"
    - "Pendulum B has a slightly longer period due to increased air resistance from the larger bob"
  answer: 2
  explanation: "Period is mass-independent: T = 2π√(L/g) contains no mass term. A heavier bob experiences a proportionally stronger gravitational restoring force, but it also has proportionally greater inertia — both increase by the same factor, leaving the period unchanged. This is the same reason all objects fall at the same rate in a gravitational field (Galileo's insight): mass cancels from the equation of motion. The period depends only on string length L and local gravitational acceleration g."

- question: "A pendulum is released from 45° amplitude. Which statement correctly describes how T = 2π√(L/g) applies to this situation?"
  type: multiple-choice
  options:
    - "The formula gives the exact period, because it was derived from Newton's second law without approximation"
    - "The formula underestimates the period, because the true restoring force sin θ > θ at large angles"
    - "The formula overestimates the period, because sin θ < θ for non-small angles, making the true restoring force weaker than the approximation assumes"
    - "The formula works for any amplitude up to 90°; it only fails beyond 90°"
  answer: 2
  explanation: "For θ > 0, sin θ < θ (in radians). The true restoring force −mg sin θ is therefore weaker than the approximated force −mgθ used to derive T = 2π√(L/g). A weaker restoring force means slower oscillation — longer period. So the small-angle formula underestimates the true period at large amplitudes. At 45°, the true period exceeds the formula's prediction by about 4.5%. This is why precision pendulum clocks keep amplitudes small — even a slight increase in swing amplitude causes the clock to run slow."

- question: "Doubling the length of a simple pendulum increases its period by a factor of √2, not by a factor of 2."
  type: true-false
  answer: true
  explanation: "T = 2π√(L/g), so T ∝ √L. If L doubles, the new period is T' = 2π√(2L/g) = √2 · 2π√(L/g) = √2 · T ≈ 1.414T. To double the period you would need to quadruple the length (since √4 = 2). This non-linear dependence — period scales as the square root of length — is a characteristic feature of the pendulum and an important counterexample to the naive expectation that 'doubling the length doubles the period.'"

- question: "The period formula T = 2π√(L/g) is exact for all oscillation amplitudes, as long as the pendulum is a true 'simple pendulum' (point mass on a massless string)."
  type: true-false
  answer: false
  explanation: "The formula is approximate — valid only for small angles (typically θ < 15° for better than ~1% accuracy). It follows from the small-angle approximation sin θ ≈ θ, which linearizes the equation of motion. The true equation of motion is α = −(g/L) sin θ, which is nonlinear. The true period for amplitude θ₀ involves an elliptic integral and depends on θ₀ — it grows with amplitude. At 30° the error is ~1.7%; at 45° ~4.5%; at 90° ~18%. A real pendulum clock run at large amplitude would lose time."

- question: "Why does the period of a simple pendulum become amplitude-dependent for large swings, even though it is amplitude-independent for small ones?"
  type: short-answer
  answer: "For small angles, sin θ ≈ θ, making the restoring force linear in displacement and the equation of motion identical to that of a harmonic oscillator. A linear restoring force produces amplitude-independent oscillation — this is the hallmark of simple harmonic motion. For large angles, sin θ < θ, so the restoring force is weaker than the linear approximation predicts. This nonlinearity means the effective 'spring constant' depends on amplitude: at larger swings, the restoring force is proportionally weaker, and the pendulum oscillates more slowly. The period grows with amplitude because the nonlinearity breaks the SHM approximation."
  explanation: "The key connection is to SHM: amplitude independence is a consequence of linearity. Any system with a strictly linear restoring force (F = −kx) oscillates at a fixed frequency regardless of amplitude. The pendulum achieves this only approximately, for small θ. Once the sinusoidal nonlinearity becomes significant, the frequency (and period) depends on how far the pendulum swings — larger swing, weaker effective restoring force per unit displacement, slower oscillation."
```

## Explainer

From your study of **simple harmonic motion**, you know the defining feature: a restoring force proportional to displacement, F = −kx, produces oscillation with angular frequency ω = √(k/m) and period T = 2π/ω independent of amplitude. The simple pendulum is one of the most important physical systems to exhibit approximately this behavior — but only approximately, and understanding the approximation is as important as understanding the result.

The setup: a point mass m hangs from a massless string of length L, free to swing in a vertical plane. When displaced by angle θ from vertical, the forces on the mass are gravity mg downward and string tension along the string. The tangential component of gravity (perpendicular to the string, the component responsible for changing the angle) is −mg sin θ, directed back toward equilibrium. The equation of motion is mL α = −mg sin θ, or α = −(g/L) sin θ, where α = d²θ/dt². This is not SHM — it is a nonlinear differential equation because of the sin θ term.

The **small-angle approximation** resolves this. For angles under about 15°, sin θ ≈ θ (in radians) to within about 1% accuracy. Substituting, the equation becomes α = −(g/L) θ — which is exactly the SHM equation with ω² = g/L. The **period** follows immediately: T = 2π/ω = **2π√(L/g)**. Two features stand out. First, the mass cancelled: a heavier bob feels more gravitational force, but also has more inertia, and these effects cancel exactly. Second, the period scales as √L, not L — doubling the string length increases the period by a factor of √2 ≈ 1.41, not 2.

The period's dependence on g makes the pendulum a precision instrument for measuring gravitational acceleration. Rearranging, g = 4π²L/T²: measure the length carefully, time many oscillations (to average out timing errors), and you have g. Historically, this was one of the most precise methods available for measuring g at different latitudes, revealing that Earth is not a perfect sphere — g is slightly larger at the poles, where you are closer to Earth's center. Gravitational surveys using pendulums helped map Earth's interior density variations long before seismology or satellite measurements.

The approximation breaks down for large amplitudes. The true period for amplitude θ₀ involves an elliptic integral and exceeds the small-angle prediction by an amount that grows with θ₀². At 30° amplitude the error is about 1.7%; at 45° it is about 4.5%; at 90° it is about 18%. The pendulum still oscillates, but the period is amplitude-dependent — a key departure from ideal SHM. This amplitude dependence means that a large-amplitude clock pendulum would run slow, which is why precision clocks kept their pendulums at small amplitudes and why escapement mechanisms were designed to maintain constant amplitude rather than letting it decay.
