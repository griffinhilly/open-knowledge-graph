---
id: simple-harmonic-motion
title: Simple Harmonic Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: circular-motion-kinematics
  type: soft
- id: derivatives-of-trigonometric-functions
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: amplitude-period-phase-shift
  type: soft
- id: trigonometric-ratios-review
  type: soft
- id: second-order-linear-homogeneous-odes
  type: hard
- id: graphing-sine-and-cosine
  type: soft
builds-toward:
- spring-mass-system
- simple-pendulum
tags:
- SHM
- oscillation
- restoring-force
- sinusoidal
stage: formal-systems
status: validated
---

# Simple Harmonic Motion

## Core Idea
Simple harmonic motion (SHM) occurs when a restoring force is proportional to displacement from equilibrium: F = −kx. The resulting motion is sinusoidal: x(t) = A cos(ωt + φ), where A is amplitude, ω = √(k/m) is angular frequency, and φ is phase. Period T = 2π/ω depends only on system parameters (mass, spring constant), not amplitude. SHM is the mathematical archetype for all oscillatory behavior.

## How It's Best Learned
Derive the equations by applying F = ma to F = −kx: m(d²x/dt²) = −kx, then verify that x = A cos(ωt) is a solution. Connect SHM to circular motion: projecting uniform circular motion onto one axis produces SHM.

## Common Misconceptions
- Thinking larger amplitude means faster oscillation: period T is independent of amplitude in ideal SHM.
- Confusing angular frequency ω (rad/s) with ordinary frequency f (Hz): ω = 2πf.
- Assuming SHM equations apply when the restoring force is not proportional to displacement.

## Questions

```yaml
- question: "A spring-mass system oscillates in SHM with period T. The amplitude is then tripled, with mass and spring constant unchanged. What is the new period?"
  type: multiple-choice
  options: ["T/3", "T/√3", "T", "3T"]
  answer: 2
  explanation: "Period in SHM is T = 2π√(m/k), which depends only on mass and spring constant — not on amplitude. Tripling the amplitude means the system travels farther, but the restoring force also grows proportionally (F = −kx), so the system moves faster over the larger distance in exactly the same time. This amplitude-independence is a defining and non-obvious feature of SHM."

- question: "A system oscillates with angular frequency ω = 2π rad/s. This means the system completes 2π full oscillations per second."
  type: true-false
  answer: false
  explanation: "Angular frequency ω and ordinary frequency f are related by ω = 2πf. If ω = 2π rad/s, then f = ω/(2π) = 1 Hz — the system completes exactly one full oscillation per second. Angular frequency measures radians per second, and one full cycle is 2π radians. Confusing ω with f introduces an off-by-2π error that propagates into period and energy calculations."

- question: "Starting from Newton's second law applied to a restoring force F = −kx, explain how you conclude that the motion must be sinusoidal."
  type: short-answer
  answer: "Applying F = ma gives m(d²x/dt²) = −kx, or d²x/dt² = −(k/m)x = −ω²x. The solutions to this ODE are functions whose second derivative equals −ω² times themselves — sines and cosines. The general solution x(t) = A cos(ωt + φ) with ω = √(k/m) satisfies the equation exactly."
  explanation: "This is a second-order linear ODE with constant coefficients. The characteristic equation r² = −ω² has purely imaginary roots ±iω, giving complex exponential solutions e^(±iωt), which in real form are cos(ωt) and sin(ωt). The linearity of the ODE guarantees that any linear combination A cos(ωt + φ) is also a solution, with constants A and φ set by initial conditions."
```

## Explainer

Simple harmonic motion begins with a single law about forces: the restoring force on an object is proportional to its displacement from equilibrium and directed back toward it, F = −kx. The negative sign is essential — it means the force always pushes opposite to the displacement, so an object displaced to the right is pushed left, and one displaced to the left is pushed right. Any system satisfying this force law will oscillate.

To find *how* it oscillates, apply Newton's second law: F = ma becomes m(d²x/dt²) = −kx. Rearranging gives d²x/dt² = −(k/m)x. This is a second-order ODE saying: the acceleration is proportional to the position, with a negative constant. From your work on differential equations, you know that functions whose second derivative is a negative constant multiple of themselves are sines and cosines. Substituting x(t) = A cos(ωt + φ) and differentiating twice yields d²x/dt² = −ω²A cos(ωt + φ) = −ω²x, which matches if ω = √(k/m). The general solution is x(t) = A cos(ωt + φ), where A is the amplitude, ω is the angular frequency, and φ is the phase (set by initial conditions).

The period T = 2π/ω = 2π√(m/k) is one of the most counterintuitive results in introductory physics: **it does not depend on amplitude**. A pendulum swung through a small arc takes the same time to complete a cycle as one swung through a larger arc (for small angles). A spring-mass system with a 1 cm amplitude oscillates at the same frequency as one with a 10 cm amplitude, as long as mass and spring constant are the same. This is only true because the restoring force grows in exact proportion to displacement — if you go twice as far, you are pulled back twice as hard, so the system compensates perfectly.

Be careful with the two measures of frequency. **Angular frequency** ω is in radians per second and appears naturally in the equations of motion. **Ordinary frequency** f = ω/(2π) is in Hz (cycles per second) and is what you would measure with a stopwatch. The period T = 1/f = 2π/ω connects all three. A common error is plugging ω directly into a formula expecting f, or reading "2π rad/s" as "2π oscillations per second" — remember that one full oscillation is 2π radians, so ω = 2π means f = 1 Hz.

SHM is the archetype for oscillatory behavior across all of physics: electromagnetic oscillations in circuits (LC circuits obey q'' = −q/LC), quantum mechanical ground states, molecular vibrations, and acoustic resonance all reduce to the same equation under the right conditions. Whenever you see a restoring force that is linear in displacement, you are looking at SHM, and you immediately know the solution is sinusoidal with ω determined by the ratio of the restoring strength to the inertia of the system.
