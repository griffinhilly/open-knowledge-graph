---
id: lorenz-system
title: The Lorenz System
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: chaos-definition-and-properties
  type: hard
- id: hopf-bifurcation
  type: soft
builds-toward:
- strange-attractors
- lyapunov-exponents
tags:
- lorenz
- butterfly-effect
- atmospheric-convection
- strange-attractor
stage: expert
status: validated
---

# The Lorenz System

## Core Idea
The Lorenz system ẋ = σ(y - x), ẏ = rx - y - xz, ż = xy - bz is a three-dimensional ODE derived from a simplified model of atmospheric convection. For certain parameter values (classically σ = 10, b = 8/3, r = 28), it produces chaotic behavior: trajectories loop around two unstable fixed points in a butterfly-shaped pattern, never repeating and sensitive to initial conditions. It was the first widely-studied example of deterministic chaos and the origin of the "butterfly effect" metaphor.

## Questions

```yaml
- question: "The Lorenz system has three fixed points for r > 1: the origin and two symmetric points C± = (±√(b(r-1)), ±√(b(r-1)), r-1). At r = 28 with σ = 10 and b = 8/3, all three are unstable. Where do trajectories go if all fixed points are unstable?"
  type: multiple-choice
  options:
    - "Trajectories escape to infinity — with no stable fixed point, nothing can confine them"
    - "Trajectories settle onto a strange attractor — a bounded set with fractal structure that is neither a fixed point nor a periodic orbit"
    - "Trajectories settle into a stable limit cycle that doesn't encircle any of the fixed points"
    - "The system enters a quasiperiodic state on a torus"
  answer: 1
  explanation: "Despite all fixed points being unstable, the Lorenz system is dissipative — volumes in phase space contract (the divergence of the flow is -(σ + 1 + b) < 0). This means trajectories are confined to a bounded region even though no individual fixed point attracts them. The trajectories settle onto the Lorenz attractor: a fractal set of measure zero where they loop around C+ and C- in an unpredictable pattern. This is the defining feature of a strange attractor — it attracts trajectories while having zero volume and infinite complexity."

- question: "Lorenz discovered chaos while studying weather. He found that rounding his initial conditions from six decimal places to three produced a completely different trajectory after a short time. This illustrates:"
  type: multiple-choice
  options:
    - "A bug in his computer code"
    - "The system being non-deterministic — different runs give different results"
    - "Sensitive dependence on initial conditions — the hallmark of chaos, where exponential divergence means even tiny differences in initial conditions lead to completely different outcomes after sufficient time"
    - "Numerical instability in his integration scheme, not a property of the underlying equations"
  answer: 2
  explanation: "Lorenz's 1963 discovery is the founding moment of chaos theory. His system was deterministic — the same initial conditions always produce the same trajectory. But his rounding (a change of about 0.01%) grew exponentially until the two trajectories were completely unrelated. This is not numerical error (it persists as the integration step shrinks to zero) but a genuine property of the equations: the largest Lyapunov exponent is positive (≈ 0.9), meaning perturbations grow by a factor of e ≈ 2.7 per unit time. After about 30 time units, a difference of 10⁻³ has grown to order 1."

- question: "The Lorenz system is symmetric under (x, y, z) → (-x, -y, z). This means that if (x(t), y(t), z(t)) is a solution, then (-x(t), -y(t), z(t)) is also a solution."
  type: true-false
  answer: true
  explanation: "Substituting -x for x and -y for y in the equations: d(-x)/dt = σ(-y - (-x)) = -σ(y - x) = -ẋ ✓; d(-y)/dt = r(-x) - (-y) - (-x)z = -(rx - y - xz) = -ẏ ✓; dz/dt = (-x)(-y) - bz = xy - bz = ż ✓. The equations are invariant. This symmetry explains why the two lobes C+ and C- of the attractor are mirror images. The attractor itself respects this symmetry even though individual trajectories break it — a trajectory might spend more time near C+ than C- at any given moment."

- question: "Describe the bifurcation sequence of the Lorenz system as r increases from 0, with σ = 10 and b = 8/3."
  type: short-answer
  answer: "At r = 0, the origin is the only fixed point (globally stable). At r = 1, a pitchfork bifurcation creates C+ and C- while the origin becomes unstable. For 1 < r < r_H ≈ 24.74, C± are stable spirals. At r_H, a subcritical Hopf bifurcation makes C± unstable — but the unstable limit cycles created exist for r < r_H, not r > r_H. For r slightly above r_H, the system exhibits transient chaos before settling to C±. At r ≈ 24.06, a homoclinic bifurcation creates the strange attractor, which coexists with stable C± until r_H. For r > r_H ≈ 24.74, the strange attractor is the only attractor. The classic chaotic regime at r = 28 is well beyond this transition."
  explanation: "The Lorenz system's route to chaos is complex and involves several bifurcation types interacting. The subcritical Hopf bifurcation at C± is crucial — it means the transition to chaos is sudden (subcritical), not gradual. The coexistence of the strange attractor with stable fixed points between r ≈ 24.06 and r_H ≈ 24.74 creates a hysteretic region where the system's long-term behavior depends on initial conditions."
```

## Explainer

The Lorenz system holds a unique place in the history of science. In 1963, meteorologist Edward Lorenz published a set of three ordinary differential equations derived from a heavily truncated model of atmospheric convection — fluid heated from below, like the atmosphere warmed by the Earth's surface. The equations were simple enough to simulate on a 1960s computer, and what Lorenz discovered changed science: these three deterministic equations, with no randomness whatsoever, produced behavior that never repeated and was exquisitely sensitive to initial conditions. Weather prediction had a fundamental limit, and it wasn't about building better instruments.

The equations describe the evolution of three variables: x measures the rate of convective overturning, y measures the horizontal temperature variation, and z measures the vertical temperature stratification. The parameter r is the Rayleigh number (a dimensionless measure of how strongly the fluid is heated), σ is the Prandtl number (ratio of viscous to thermal diffusion), and b relates to the geometry of the convection cell. For r < 1, the only fixed point (the origin, representing no convection) is globally stable — heating is too weak to drive convection. At r = 1, a pitchfork bifurcation creates two new fixed points C+ and C-, representing steady convective rolls turning in opposite directions.

As r increases further, C+ and C- undergo a subcritical Hopf bifurcation and become unstable. Now all three fixed points are unstable, yet the system is dissipative (volumes in phase space contract at rate -(σ + 1 + b)). Where do trajectories go? They settle onto the **Lorenz attractor** — the famous butterfly-shaped set in three-dimensional space. Trajectories loop around C+, then switch to C-, then back, in a pattern that appears random but is completely determined by the initial conditions. The number of loops around one wing before switching to the other is exquisitely sensitive to the starting point — this is the butterfly effect.

The Lorenz attractor is a **strange attractor**: it has zero volume (the system is dissipative, so volumes collapse), yet it has a complicated, fractal internal structure. Its fractal dimension is approximately 2.06 — slightly more than a surface but far less than a volume. It attracts all nearby trajectories (it's an attractor) but nearby trajectories on the attractor diverge exponentially (it's strange). The largest Lyapunov exponent is about 0.9, meaning perturbations multiply by a factor of roughly e per unit time. This is the quantitative backbone of the butterfly effect: an initial uncertainty of 10⁻⁶ becomes order 1 in about 14 time units, setting a finite prediction horizon no matter how precisely you measure the initial state.
