---
id: phase-portraits-linear-systems
title: Phase Portraits for Linear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: matrix-exponential-method
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- stability-classification
tags:
- phase-portrait
- trajectories
- visualization
stage: advanced
status: validated
---

# Phase Portraits for Linear Systems

## Core Idea
A phase portrait plots trajectories of solutions to a 2D system in the (x₁, x₂) plane. Real positive eigenvalues give diverging nodes; real negative eigenvalues give converging nodes; opposite signs give saddles; complex eigenvalues give spirals. Phase portraits immediately reveal stability and long-term behavior, providing geometric intuition without explicit solutions.

## Questions

```yaml
- question: "A 2D linear system x′ = Ax has eigenvalues λ₁ = −2 and λ₂ = 3. Without solving the system explicitly, what can you conclude about trajectories near the origin?"
  type: multiple-choice
  options:
    - "All trajectories spiral toward the origin because one eigenvalue is negative"
    - "All trajectories converge to the origin because the negative eigenvalue eventually dominates"
    - "The origin is a saddle point: trajectories along one eigendirection flow in, but almost every other trajectory eventually escapes to infinity"
    - "The origin is a center because the two eigenvalues have equal magnitude"
  answer: 2
  explanation: "Opposite-sign eigenvalues produce a saddle point. The eigenvector for λ₁ = −2 is a stable direction: trajectories starting along it decay toward the origin. The eigenvector for λ₂ = 3 is an unstable direction: trajectories starting along it blow up. For almost every other initial condition, the unstable component eventually dominates and the trajectory escapes to infinity. A saddle is not a spiral (no complex eigenvalues), and neither eigenvalue 'wins'—they control behavior along their respective eigendirections. Option B is the key misconception: in a saddle, the negative eigenvalue does not dominate globally."

- question: "A linear system has eigenvalues λ = −0.1 ± 3i. What does the phase portrait look like near the origin?"
  type: multiple-choice
  options:
    - "Closed ellipses (center), because the imaginary part is much larger than the real part"
    - "An unstable spiral outward, because the imaginary part is positive"
    - "A stable spiral inward, because the real part is negative—trajectories rotate and gradually decay toward the origin"
    - "A node, because the real part is nonzero"
  answer: 2
  explanation: "Complex eigenvalues λ = α ± βi produce spirals. The imaginary part β drives rotation in the phase plane; the real part α drives growth or decay. Here α = −0.1 < 0, so trajectories decay toward the origin while rotating—a stable spiral. The magnitude of β relative to α determines how 'tight' the spiral is (many rotations before reaching the origin), but not whether it is stable. Option A is the most tempting wrong answer: a center requires α = 0 exactly; even a tiny negative real part creates a spiral that eventually converges."

- question: "For a 2D linear system x′ = Ax, whether the equilibrium at the origin is stable depends entirely on the signs of the real parts of the eigenvalues of A, not on the specific initial conditions chosen."
  type: true-false
  answer: true
  explanation: "Correct. Stability is a property of the equilibrium itself, not of particular trajectories. If both eigenvalues have negative real parts, every trajectory converges to the origin regardless of initial conditions. If any eigenvalue has a positive real part, almost every trajectory diverges (saddles have one of each). The phase portrait makes this global structure visible: you can classify the equilibrium as stable, unstable, or mixed by reading the eigenvalue signs, without computing any individual solution."

- question: "A phase portrait is a plot of the state variables x₁(t) and x₂(t) as separate functions of time t."
  type: true-false
  answer: false
  explanation: "False—this confuses a phase portrait with time-domain plots. A phase portrait plots trajectories in the phase plane: the (x₁, x₂) plane, where each axis is one state variable, not time. Time is implicit—a point on a trajectory tells you the state of the system at some moment, and the arrow shows the direction of evolution. This representation reveals the global geometric structure of all solutions simultaneously: you can see whether trajectories converge, diverge, or rotate without ever computing x₁(t) or x₂(t) explicitly."

- question: "Explain why a phase portrait conveys qualitative information about a dynamical system that a single solution curve x(t) does not."
  type: short-answer
  answer: "A single solution curve x(t) shows how one specific initial condition evolves over time, in coordinates where time is an axis. A phase portrait plots all trajectories in the state space simultaneously, without explicit time. This reveals the global structure: which directions are stable (attracting), which are unstable (repelling), whether the equilibrium is a node, saddle, or spiral, and how nearby trajectories relate to each other. From the phase portrait you can answer stability questions for all initial conditions at once—something impossible from any single solution."
  explanation: "The deeper point is that eigenvalues give you the phase portrait structure without solving anything. Reading λ signs tells you the qualitative behavior—stable/unstable, spiral/node/saddle—immediately. This geometric intuition built from linear systems then generalizes to nonlinear systems via linearization: the Jacobian at an equilibrium gives a local phase portrait that governs nearby behavior."
```

## Explainer

From eigenvalues and eigenvectors, you know that the general solution to x′ = Ax is a linear combination of terms of the form e^{λt}v, where λ is an eigenvalue and v the corresponding eigenvector. The **phase portrait** is a picture of all these solutions at once. Instead of plotting x₁(t) or x₂(t) against time, you plot trajectories in the (x₁, x₂) plane — the **phase plane**. Each initial condition traces a curve, and the collection of curves reveals the system's global behavior without solving for t explicitly.

The shape of the phase portrait is dictated entirely by the eigenvalues of A. Consider the four main cases. If both eigenvalues are real and negative, every trajectory flows toward the origin — this is a **stable node**, and all solutions decay to equilibrium. If both are real and positive, trajectories flow away from the origin — an **unstable node**. Along each eigendirection, solutions grow or shrink purely exponentially; near those directions, trajectories are straightened out. If the eigenvalues have opposite signs, the phase portrait shows a **saddle**: trajectories along the stable eigendirection (negative eigenvalue) flow in, while those along the unstable eigendirection (positive eigenvalue) blow out. Almost every trajectory eventually escapes to infinity.

Complex eigenvalues λ = α ± βi produce a qualitatively different picture: **spirals**. The imaginary part β drives rotation in the phase plane; the real part α drives growth (α > 0, unstable spiral) or decay (α < 0, stable spiral). When α = 0 exactly, trajectories are closed ellipses — a **center** — and solutions are purely periodic. The orientation of the spiral (clockwise or counterclockwise) is determined by the off-diagonal entries of A. A repeated real eigenvalue gives a **degenerate node**: if A is diagonalizable, trajectories still flow straight in or out; if not (a Jordan block), trajectories spiral mildly before straightening.

The phase portrait answers stability questions immediately. Is the equilibrium at the origin attracting, repelling, or mixed? The sign of the real parts of the eigenvalues tells you at a glance. This geometric reading of eigenvalues will generalize to nonlinear systems: near any equilibrium point, the linearized system (its Jacobian) has a phase portrait, and that local picture governs the nonlinear behavior in a neighborhood — the content of stability classification, your next topic.


