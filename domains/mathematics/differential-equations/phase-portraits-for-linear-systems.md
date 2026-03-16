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
status: draft
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

## Explainer

A **phase portrait** is a map of all possible futures. For a 2D linear system y' = Ay, every initial condition (y₁(0), y₂(0)) determines a unique solution, and the phase portrait draws all solution trajectories together in the **(y₁, y₂)-plane** — called the **phase plane**. Rather than plotting each solution against time, you plot the path each solution traces through state space. The result is a picture of the system's global behavior: where trajectories go, how fast, and whether they converge or diverge.

From your work on the eigenvalue method, you know solutions are built from eigenvectors and eigenvalues of A. This directly determines the portrait's structure. When A has **two real eigenvalues of the same sign**, the straight-line trajectories along the two eigenvectors act as "spines" of the portrait. All other trajectories curve between these spines, flowing toward the origin if both eigenvalues are negative (**stable node**) or away if both are positive (**unstable node**). When eigenvalues have **opposite signs**, trajectories approach the origin along the stable eigenvector direction but flee along the unstable one — this is a **saddle point**, where every trajectory except the stable manifold eventually escapes.

When eigenvalues are **complex conjugates** α ± βi, the real part α controls radial behavior and β controls rotation. If α < 0, trajectories spiral inward toward the origin — a **stable spiral**. If α > 0, they spiral outward — an **unstable spiral**. If α = 0 (purely imaginary eigenvalues), there is no radial drift and trajectories form **closed ellipses** — a **center**, representing perpetual oscillation with neither growth nor decay. The imaginary part β sets the angular frequency of the rotation.

The equilibrium at the origin is the organizing center of the entire portrait. Every trajectory is either converging to it, diverging from it, spiraling around it, or orbiting it — determined entirely by the eigenvalues of A. This picture generalizes to nonlinear systems through **linearization**: near any equilibrium of a nonlinear system, the behavior is well-approximated by the linearized system (the Jacobian at the equilibrium point). The phase portrait of the linearization predicts local behavior of the nonlinear system whenever the equilibrium is not a center in the linearization — making this classification of linear phase portraits the essential toolkit for analyzing the far more prevalent nonlinear case.
