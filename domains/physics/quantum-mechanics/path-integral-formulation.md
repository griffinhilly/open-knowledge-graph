---
id: path-integral-formulation
title: Path Integral Formulation of Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
tags:
- path-integrals
- feynman
stage: advanced
status: draft
---

# Path Integral Formulation of Quantum Mechanics

## Core Idea
The amplitude for propagation from (x₀,t₀) to (xf,tf) sums over all paths: K = ∫ D[x(t)] e^{iS[x]/ℏ}, where S[x] = ∫ L dt is the action. Classical paths dominate (stationary phase); quantum fluctuations come from all paths. Equivalent to Schrödinger equation and elegant for transitions and semiclassics.

## Explainer

The Schrödinger equation gives you one complete picture of quantum mechanics: the wavefunction evolves in time deterministically, and you extract probabilities from it. Feynman's **path integral formulation** gives you a completely different but equivalent picture — one that makes the connection to classical mechanics vivid and almost tactile. The central idea is this: to find the quantum amplitude for a particle to travel from point x₀ at time t₀ to point xf at time tf, you sum a phase contribution from every conceivable path connecting those endpoints. Not just the classical path. Every path.

Each path x(t) contributes an amplitude with magnitude 1 and phase equal to the classical **action** S[x] = ∫ L dt divided by ℏ: the contribution is e^{iS[x]/ℏ}. The **action** is the time integral of the Lagrangian L = T − V — the quantity you studied in classical mechanics via Hamilton's principle. For familiar classical systems, S has units of energy × time, same as ℏ. The ratio S/ℏ is therefore dimensionless, and e^{iS/ℏ} is a pure phase on the unit circle in the complex plane.

The deep insight is what happens when you add up all these phases. For most paths, neighboring paths have wildly different phases that cancel when summed — **destructive interference** washes out their contributions. But near the **classical path** — the one that satisfies Hamilton's principle and makes S stationary (δS = 0) — neighboring paths have nearly identical phases. They add constructively. In the limit ℏ → 0, only the classical path survives. Quantum mechanics thus contains classical mechanics as a limit: classical trajectories are the paths of stationary phase, exactly as light rays are the paths of stationary phase in geometric optics. The particle doesn't "choose" the classical path — the classical path is what remains after all quantum interference has occurred.

For paths far from the classical trajectory, the action varies rapidly and the phases cancel. But nearby quantum fluctuations do survive, and their magnitude is governed by ℏ. This is what makes the path integral naturally suited to **semiclassical approximations**: expand around the classical path, treat fluctuations perturbatively, and you get systematic quantum corrections to classical results. The same framework that makes WKB transparent also makes the path integral the natural language for quantum field theory, where the "paths" become field configurations over all spacetime, and the action integral becomes the foundation for Feynman diagrams and perturbation theory.
