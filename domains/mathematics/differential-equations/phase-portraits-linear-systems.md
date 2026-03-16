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
stage: formal-systems
status: draft
---

# Phase Portraits for Linear Systems

## Core Idea
A phase portrait plots trajectories of solutions to a 2D system in the (x₁, x₂) plane. Real positive eigenvalues give diverging nodes; real negative eigenvalues give converging nodes; opposite signs give saddles; complex eigenvalues give spirals. Phase portraits immediately reveal stability and long-term behavior, providing geometric intuition without explicit solutions.

## Explainer

From eigenvalues and eigenvectors, you know that the general solution to x′ = Ax is a linear combination of terms of the form e^{λt}v, where λ is an eigenvalue and v the corresponding eigenvector. The **phase portrait** is a picture of all these solutions at once. Instead of plotting x₁(t) or x₂(t) against time, you plot trajectories in the (x₁, x₂) plane — the **phase plane**. Each initial condition traces a curve, and the collection of curves reveals the system's global behavior without solving for t explicitly.

The shape of the phase portrait is dictated entirely by the eigenvalues of A. Consider the four main cases. If both eigenvalues are real and negative, every trajectory flows toward the origin — this is a **stable node**, and all solutions decay to equilibrium. If both are real and positive, trajectories flow away from the origin — an **unstable node**. Along each eigendirection, solutions grow or shrink purely exponentially; near those directions, trajectories are straightened out. If the eigenvalues have opposite signs, the phase portrait shows a **saddle**: trajectories along the stable eigendirection (negative eigenvalue) flow in, while those along the unstable eigendirection (positive eigenvalue) blow out. Almost every trajectory eventually escapes to infinity.

Complex eigenvalues λ = α ± βi produce a qualitatively different picture: **spirals**. The imaginary part β drives rotation in the phase plane; the real part α drives growth (α > 0, unstable spiral) or decay (α < 0, stable spiral). When α = 0 exactly, trajectories are closed ellipses — a **center** — and solutions are purely periodic. The orientation of the spiral (clockwise or counterclockwise) is determined by the off-diagonal entries of A. A repeated real eigenvalue gives a **degenerate node**: if A is diagonalizable, trajectories still flow straight in or out; if not (a Jordan block), trajectories spiral mildly before straightening.

The phase portrait answers stability questions immediately. Is the equilibrium at the origin attracting, repelling, or mixed? The sign of the real parts of the eigenvalues tells you at a glance. This geometric reading of eigenvalues will generalize to nonlinear systems: near any equilibrium point, the linearized system (its Jacobian) has a phase portrait, and that local picture governs the nonlinear behavior in a neighborhood — the content of stability classification, your next topic.


