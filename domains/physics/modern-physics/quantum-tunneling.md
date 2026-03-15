---
id: quantum-tunneling
title: Quantum Tunneling
domain: physics
course: modern-physics
prerequisites:
- id: particle-in-a-box
  type: hard
- id: heisenberg-uncertainty-principle
  type: soft
- id: differential-equations-intro
  type: hard
builds-toward:
- nuclear-fission-fusion
- radioactive-decay
tags:
- quantum
- tunneling
- barrier
- finite-well
- scanning-tunneling-microscope
stage: advanced
status: validated
---

# Quantum Tunneling

## Core Idea
A quantum particle can pass through a potential energy barrier even when its total energy is less than the barrier height — a phenomenon impossible classically. Inside the barrier the wavefunction decays exponentially rather than oscillating, and a transmitted wave emerges on the other side with reduced amplitude. The tunneling probability depends exponentially on barrier width and height, and on particle mass. Tunneling underpins nuclear alpha decay, the scanning tunneling microscope, semiconductor tunnel diodes, and nuclear fusion in stars.

## How It's Best Learned
Solve the Schrödinger equation for a rectangular barrier: match wavefunction and its derivative at both walls. Compute the transmission coefficient T and note its exponential sensitivity to barrier parameters. The calculation reinforces wavefunction matching technique.

## Common Misconceptions
- Tunneling requires the particle to 'borrow' energy temporarily — the particle's energy is constant throughout; only the wavefunction penetrates the forbidden region.
- Tunneling only occurs at the atomic scale — it is relevant at the nanoscale (STM) and also explains macroscopic effects like alpha decay rates.
