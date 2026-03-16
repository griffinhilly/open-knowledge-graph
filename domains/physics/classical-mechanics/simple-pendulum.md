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
stage: abstract-reasoning
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

## Explainer

From your study of **simple harmonic motion**, you know the defining feature: a restoring force proportional to displacement, F = −kx, produces oscillation with angular frequency ω = √(k/m) and period T = 2π/ω independent of amplitude. The simple pendulum is one of the most important physical systems to exhibit approximately this behavior — but only approximately, and understanding the approximation is as important as understanding the result.

The setup: a point mass m hangs from a massless string of length L, free to swing in a vertical plane. When displaced by angle θ from vertical, the forces on the mass are gravity mg downward and string tension along the string. The tangential component of gravity (perpendicular to the string, the component responsible for changing the angle) is −mg sin θ, directed back toward equilibrium. The equation of motion is mL α = −mg sin θ, or α = −(g/L) sin θ, where α = d²θ/dt². This is not SHM — it is a nonlinear differential equation because of the sin θ term.

The **small-angle approximation** resolves this. For angles under about 15°, sin θ ≈ θ (in radians) to within about 1% accuracy. Substituting, the equation becomes α = −(g/L) θ — which is exactly the SHM equation with ω² = g/L. The **period** follows immediately: T = 2π/ω = **2π√(L/g)**. Two features stand out. First, the mass cancelled: a heavier bob feels more gravitational force, but also has more inertia, and these effects cancel exactly. Second, the period scales as √L, not L — doubling the string length increases the period by a factor of √2 ≈ 1.41, not 2.

The period's dependence on g makes the pendulum a precision instrument for measuring gravitational acceleration. Rearranging, g = 4π²L/T²: measure the length carefully, time many oscillations (to average out timing errors), and you have g. Historically, this was one of the most precise methods available for measuring g at different latitudes, revealing that Earth is not a perfect sphere — g is slightly larger at the poles, where you are closer to Earth's center. Gravitational surveys using pendulums helped map Earth's interior density variations long before seismology or satellite measurements.

The approximation breaks down for large amplitudes. The true period for amplitude θ₀ involves an elliptic integral and exceeds the small-angle prediction by an amount that grows with θ₀². At 30° amplitude the error is about 1.7%; at 45° it is about 4.5%; at 90° it is about 18%. The pendulum still oscillates, but the period is amplitude-dependent — a key departure from ideal SHM. This amplitude dependence means that a large-amplitude clock pendulum would run slow, which is why precision clocks kept their pendulums at small amplitudes and why escapement mechanisms were designed to maintain constant amplitude rather than letting it decay.
