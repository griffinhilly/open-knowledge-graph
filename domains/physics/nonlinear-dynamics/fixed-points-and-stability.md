---
id: fixed-points-and-stability
title: Fixed Points and Stability
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: phase-space-and-flows
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- linearization-and-jacobian
- bifurcation-theory-saddle-node
tags:
- fixed-points
- stability
- equilibrium
- attractors
stage: advanced
status: validated
---

# Fixed Points and Stability

## Core Idea
A fixed point (or equilibrium) of ẋ = f(x) is a point x* where f(x*) = 0 — the system sits still. Stability classifies whether nearby trajectories are attracted to x* (stable), repelled from it (unstable), or exhibit mixed behavior (saddle). For linear systems, the eigenvalues of the coefficient matrix completely determine stability. For nonlinear systems, the eigenvalues of the Jacobian at x* determine local stability, provided no eigenvalue has zero real part.

## Questions

```yaml
- question: "A two-dimensional system has a fixed point where the Jacobian has eigenvalues λ₁ = -3 and λ₂ = -1. What type of fixed point is this?"
  type: multiple-choice
  options:
    - "Unstable node — both eigenvalues push trajectories away"
    - "Stable node — both eigenvalues are real and negative, so all trajectories approach the fixed point"
    - "Saddle point — the eigenvalues have opposite signs"
    - "Stable spiral — the eigenvalues are complex with negative real part"
  answer: 1
  explanation: "Both eigenvalues are real and negative, so perturbations decay exponentially along both eigendirections. Trajectories approach the fixed point tangent to the slow eigendirection (λ₂ = -1, which decays more slowly). This is a stable node. If the eigenvalues were complex conjugates with negative real part, you'd get a stable spiral instead."

- question: "A fixed point with eigenvalues λ = ±i (purely imaginary) is classified as a center in linear analysis. For a nonlinear system, can you conclude the fixed point is a center?"
  type: multiple-choice
  options:
    - "Yes — purely imaginary eigenvalues always guarantee a center, even in nonlinear systems"
    - "No — purely imaginary eigenvalues are a borderline case where nonlinear terms determine whether the fixed point is a true center, a stable spiral, or an unstable spiral"
    - "No — purely imaginary eigenvalues mean the fixed point is always unstable in the nonlinear case"
    - "Yes — but only if the system is Hamiltonian"
  answer: 1
  explanation: "Purely imaginary eigenvalues put us on the boundary between stable and unstable spirals. The linearization predicts closed orbits, but higher-order nonlinear terms can break the perfect periodicity, causing trajectories to slowly spiral in (stable) or out (unstable). This is precisely why Lyapunov's indirect method fails when eigenvalues have zero real part — the linearization is structurally unstable. Hamiltonian systems are special: their symplectic structure does guarantee centers persist, but this requires additional structural information beyond just eigenvalues."

- question: "Lyapunov stability requires that trajectories starting near a fixed point stay near it forever, while asymptotic stability additionally requires that they converge to the fixed point."
  type: true-false
  answer: true
  explanation: "Lyapunov stability (also called stability in the sense of Lyapunov) means: for any ε > 0, there exists δ > 0 such that trajectories starting within δ of x* remain within ε for all future time. Asymptotic stability adds convergence: trajectories not only stay close but actually approach x* as t → ∞. A center is Lyapunov stable but not asymptotically stable — orbits stay close (on closed loops) but never converge to the center. A stable node or spiral is asymptotically stable."

- question: "Explain why a saddle point, despite being unstable, plays a crucial role in organizing the phase portrait of a dynamical system."
  type: short-answer
  answer: "The stable and unstable manifolds of a saddle point act as separatrices that divide phase space into regions with qualitatively different long-term behavior. Trajectories on the stable manifold approach the saddle; those on the unstable manifold depart from it. These manifolds form the boundaries of basins of attraction for other attractors, so the saddle determines which initial conditions flow to which attractor. The saddle itself is never the final destination (except for the measure-zero set on its stable manifold), but it shapes the global flow topology."
  explanation: "Consider a ball on a saddle-shaped surface: it rolls away in two directions but approaches along two others. In phase space, the stable manifold of a saddle often forms the boundary between the basin of attraction of two stable fixed points. A system that starts on one side of this separatrix ends up at one attractor; starting on the other side leads to the other. This makes saddle points the 'traffic directors' of dynamical systems."
```

## Explainer

Every dynamical system ẋ = f(x) has a natural starting point for analysis: find the fixed points where f(x*) = 0, then determine their stability. Fixed points are the simplest possible behavior — nothing moves — and yet they organize the entire phase portrait. The stable fixed points are attractors that capture nearby trajectories. The unstable ones repel. The saddle points, with their stable and unstable manifolds, carve phase space into basins of attraction. Understanding fixed points and their stability tells you the skeleton of the dynamics.

Stability comes in degrees. **Lyapunov stability** means trajectories that start close to x* stay close forever — they don't wander off, but they don't necessarily converge either. Think of a ball rolling in a perfectly frictionless bowl: it oscillates around the bottom but never settles. **Asymptotic stability** means trajectories not only stay close but actually converge to x* as time progresses — now there's friction, and the ball settles to rest. **Exponential stability** is stronger still: the convergence rate is bounded by an exponential decay e^{-αt}. For most purposes in nonlinear dynamics, asymptotic stability is the key notion.

For linear systems ẋ = Ax, the eigenvalues of A tell the complete story. All eigenvalues with negative real parts: asymptotically stable. Any eigenvalue with positive real part: unstable. The classification gives nodes (real eigenvalues, same sign), saddles (real eigenvalues, opposite sign), spirals (complex eigenvalues), and centers (purely imaginary eigenvalues). Your linear algebra background in eigenvalues and eigenvectors directly provides the tools: eigenvectors give the directions of fastest growth or decay, eigenvalues give the rates. What's new in the nonlinear context is that this classification applies only locally, at each fixed point, via the Jacobian — and it can fail at borderline cases.

The borderline cases are where the real part of an eigenvalue is exactly zero. Here the linear approximation is **structurally unstable**: an arbitrarily small perturbation can change the qualitative behavior. A center (purely imaginary eigenvalues) could become a stable spiral, an unstable spiral, or remain a center depending on the nonlinear terms. A zero eigenvalue signals a potential bifurcation — a qualitative change in the system's behavior as parameters vary. These borderline cases are not pathological exceptions; they are the doorways to the richest phenomena in nonlinear dynamics, including bifurcations, limit cycles, and chaos.
