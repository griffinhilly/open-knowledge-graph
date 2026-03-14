---
id: quantum-tunneling-rectangular-barrier
title: Quantum Tunneling Through Rectangular Barriers
domain: physics
course: modern-physics
prerequisites:
- id: quantum-tunneling
  type: hard
- id: schrodinger-equation-intro
  type: hard
builds-toward:
- barrier-tunneling-transmission-probability
tags:
- quantum-mechanics
- tunneling
- barriers
stage: advanced
status: draft
---

# Quantum Tunneling Through Rectangular Barriers

## Core Idea
When a quantum particle encounters a potential barrier higher than its energy, the wavefunction does not abruptly vanish—it decays exponentially inside the barrier. If the barrier has finite width, the wavefunction is non-zero on the far side, giving a non-zero probability of finding the particle there. The tunneling probability is exponentially sensitive to barrier width and height.

## How It's Best Learned
Solve the time-independent Schrödinger equation in three regions (before, inside, and after the barrier) and match boundary conditions to find transmission coefficients. Calculate tunneling probability for specific barriers and particle energies.

## Common Misconceptions
Tunneling requires the particle energy to be below the barrier top (it happens when E < V, not E > V). The particle does not gain energy inside the barrier; it is temporary and violates energy conservation only by ΔE ~ ℏ/Δt consistent with uncertainty principle.
