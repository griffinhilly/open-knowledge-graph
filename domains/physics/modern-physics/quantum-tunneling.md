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

## Explainer

You already know from the particle-in-a-box that a quantum wavefunction must solve the Schrödinger equation inside every region of space, including regions the particle "shouldn't" be able to enter. In the infinite square well, the walls are infinitely high, so the wavefunction is forced to zero there. But what happens when the barrier has a finite height V₀ and the particle's energy E is less than V₀? Classically, the answer is simple: the particle bounces back every time. Quantum mechanically, the story is richer.

Inside the barrier, the Schrödinger equation still has solutions — they just aren't oscillating sinusoids. Instead, the wavefunction decays exponentially as ψ(x) ∝ e^{−κx}, where **κ = √(2m(V₀ − E))/ℏ**. This decaying tail isn't zero, which means if the barrier is thin enough, the wavefunction still has nonzero amplitude when it reaches the far side. There, it reconnects to a freely oscillating wave — a transmitted particle. The particle hasn't "borrowed" energy to climb over the barrier; its energy is constant throughout. It has simply leaked through a region where its wavefunction is non-zero, even though it is forbidden classically.

The **transmission coefficient** T quantifies this: T ≈ e^{−2κL}, where L is the barrier width. This exponential dependence is the key signature of tunneling. Doubling the barrier width squares the transmission probability. Heavier particles have larger κ (m appears in the numerator), so they tunnel far less readily — this is why protons tunnel much less than electrons, and alpha particles tunnel much less still (though still enough to drive nuclear alpha decay). The Heisenberg uncertainty principle provides an intuition for why tunneling is possible: position uncertainty means we can't say with certainty that the particle is on the "wrong" side of the barrier.

The exponential sensitivity to barrier width has revolutionary practical consequences. In a **scanning tunneling microscope (STM)**, a metal tip is brought within ~1 nm of a conducting surface. The tunneling current between tip and surface varies by roughly an order of magnitude for every 0.1 nm change in gap — sub-angstrom height sensitivity that lets the STM image individual atoms. In semiconductor **tunnel diodes**, tunneling current allows devices to operate at speeds impossible with classical transport. In nuclear physics, alpha decay rates are entirely set by tunneling probability through the Coulomb barrier — the exponential factor explains why some nuclei decay in microseconds and others in billions of years despite having similar energies.
