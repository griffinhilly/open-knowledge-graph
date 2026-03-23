---
id: phase-portraits-for-linear-systems
title: Phase Portraits for Linear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: eigenvalue-method-for-systems
  type: hard
- id: phase-line-analysis
  type: soft
builds-toward:
- stability-classification
- linearization-of-nonlinear-systems
tags:
- systems
- visualization
- qualitative
stage: formal-systems
status: validated
---

# Phase Portraits for Linear Systems

## Core Idea
A phase portrait in the (y₁, y₂)-plane shows solution trajectories of a 2D linear system y' = Ay. Trajectories are straight lines (when A has real eigenvalues) or spirals (complex eigenvalues), flowing away from or toward equilibrium based on eigenvalue signs.

## How It's Best Learned
Sketch phase portraits by hand for all eigenvalue cases: two negative reals (stable node), two positive reals (unstable node), opposite signs (saddle), complex with negative real part (stable spiral), complex with positive real part (unstable spiral), purely imaginary (center). Use eigenvectors to draw the straight-line trajectories first, then fill in the rest as curves flowing between them.

## Common Misconceptions
- Thinking the phase portrait shows solutions as functions of time — trajectories show paths in the (y₁,y₂) plane, not time series plots.
- Forgetting that the direction of flow (arrows) must be determined separately from the shape of the trajectories.
- Confusing a center (purely imaginary eigenvalues) with a spiral — centers give closed ellipses, not spirals.

## Questions

```yaml
- question: "A student sketches the phase portrait for y' = Ay where A has eigenvalues λ = ±2i. She draws inward spirals converging toward the origin. What error has she made?"
  type: multiple-choice
  options:
    - "She should have drawn outward spirals since both eigenvalues are imaginary"
    - "Purely imaginary eigenvalues produce closed elliptical orbits (a center), not spirals — spirals arise only when the real part of the eigenvalue is nonzero"
    - "She confused the phase portrait with a time-series plot"
    - "She should have drawn straight-line trajectories along the eigenvectors"
  answer: 1
  explanation: "A center (purely imaginary eigenvalues, α = 0) produces closed ellipses — the system oscillates indefinitely without growing or decaying. Spirals require a nonzero real part: negative real part gives a stable spiral (inward), positive gives an unstable spiral (outward). The student has confused the borderline center case with the nearby stable spiral. This distinction matters enormously because centers are structurally fragile — any perturbation to the real part tips them to spirals."

- question: "For a linear system y' = Ay where A has eigenvalues λ₁ = −3, λ₂ = +1, what describes the global behavior of trajectories in the phase portrait?"
  type: multiple-choice
  options:
    - "All trajectories spiral inward toward the origin"
    - "All trajectories diverge away from the origin"
    - "Trajectories approach the origin along the stable eigenvector direction but eventually flee along the unstable eigenvector — this is a saddle point"
    - "Trajectories form closed loops around the origin because the eigenvalues have opposite signs"
  answer: 2
  explanation: "Opposite-sign eigenvalues produce a saddle point. The eigenvector for λ₁ = −3 defines the stable manifold (trajectories along it converge to the origin); the eigenvector for λ₂ = +1 defines the unstable manifold (trajectories along it diverge). Every trajectory except those starting exactly on the stable manifold eventually dominates via the positive eigenvalue and escapes. Closed loops require purely imaginary eigenvalues — a completely different case."

- question: "Reading the time elapsed along a trajectory in a phase portrait tells you how quickly the system evolves."
  type: true-false
  answer: false
  explanation: "Phase portraits show paths in state space, not time. Arrows indicate the direction of flow, but the portrait does not encode how much time elapses between any two points on a trajectory. Two systems with very different eigenvalue magnitudes (fast vs. slow) can have visually identical phase portraits. Time-scale information requires looking at the eigenvalue magnitudes separately — a phase portrait is a purely geometric object."

- question: "The straight-line trajectories along eigenvectors serve as structural 'spines' of a phase portrait when eigenvalues are real — all other trajectories curve between them and approach or flee the origin tangent to them."
  type: true-false
  answer: true
  explanation: "When A has two real eigenvalues, the eigenvectors define invariant directions: a trajectory that starts exactly on an eigenvector direction stays on it. These straight-line trajectories organize the entire portrait — other trajectories curve between them. Near the origin, trajectories approach (or leave) tangent to the slow eigenvector direction (the one with smaller |λ|). The eigenvectors are the skeleton from which you reconstruct the full portrait."

- question: "Why does a system with purely imaginary eigenvalues (a center) behave qualitatively differently from one with eigenvalues having a tiny negative real part, and what does this imply for using linearization to classify equilibria?"
  type: short-answer
  answer: "With purely imaginary eigenvalues (α = 0), trajectories form closed ellipses — the system oscillates perpetually with no growth or decay. Adding even an infinitesimally small negative real part (α < 0) causes every trajectory to spiral inward, so the behavior changes from neutral oscillation to asymptotic stability. This is structural instability: the center is a borderline case that qualitatively changes with any perturbation to the real part. For linearization, this means that if the linearized system at an equilibrium is a center, you cannot conclude anything about the nonlinear system's behavior near that point — you must use higher-order analysis."
  explanation: "This is the key caveat for applying phase portrait classification to nonlinear systems via linearization. All other equilibrium types (stable/unstable nodes, spirals, saddles) are robust to small perturbations and transfer faithfully from linearization to the nonlinear system. Centers are the single exception — their behavior is non-generic and cannot be trusted from the linearization alone."
```

## Explainer

A **phase portrait** is a map of all possible futures. For a 2D linear system y' = Ay, every initial condition (y₁(0), y₂(0)) determines a unique solution, and the phase portrait draws all solution trajectories together in the **(y₁, y₂)-plane** — called the **phase plane**. Rather than plotting each solution against time, you plot the path each solution traces through state space. The result is a picture of the system's global behavior: where trajectories go, how fast, and whether they converge or diverge.

From your work on the eigenvalue method, you know solutions are built from eigenvectors and eigenvalues of A. This directly determines the portrait's structure. When A has **two real eigenvalues of the same sign**, the straight-line trajectories along the two eigenvectors act as "spines" of the portrait. All other trajectories curve between these spines, flowing toward the origin if both eigenvalues are negative (**stable node**) or away if both are positive (**unstable node**). When eigenvalues have **opposite signs**, trajectories approach the origin along the stable eigenvector direction but flee along the unstable one — this is a **saddle point**, where every trajectory except the stable manifold eventually escapes.

When eigenvalues are **complex conjugates** α ± βi, the real part α controls radial behavior and β controls rotation. If α < 0, trajectories spiral inward toward the origin — a **stable spiral**. If α > 0, they spiral outward — an **unstable spiral**. If α = 0 (purely imaginary eigenvalues), there is no radial drift and trajectories form **closed ellipses** — a **center**, representing perpetual oscillation with neither growth nor decay. The imaginary part β sets the angular frequency of the rotation.

The equilibrium at the origin is the organizing center of the entire portrait. Every trajectory is either converging to it, diverging from it, spiraling around it, or orbiting it — determined entirely by the eigenvalues of A. This picture generalizes to nonlinear systems through **linearization**: near any equilibrium of a nonlinear system, the behavior is well-approximated by the linearized system (the Jacobian at the equilibrium point). The phase portrait of the linearization predicts local behavior of the nonlinear system whenever the equilibrium is not a center in the linearization — making this classification of linear phase portraits the essential toolkit for analyzing the far more prevalent nonlinear case.
