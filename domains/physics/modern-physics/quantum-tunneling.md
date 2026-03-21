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

## Questions

```yaml
- question: "A particle with total energy E = 3 eV encounters a potential energy barrier of height V₀ = 5 eV and finite width. What does quantum mechanics predict?"
  type: multiple-choice
  options:
    - "The particle is reflected with 100% probability — it lacks sufficient energy to cross"
    - "The particle temporarily borrows 2 eV from the uncertainty principle to climb over the barrier"
    - "There is a nonzero probability that the particle is transmitted through the barrier, with its energy unchanged at 3 eV throughout"
    - "The particle's energy increases to 5 eV inside the barrier, then drops back to 3 eV on the far side"
  answer: 2
  explanation: "Tunneling does not involve energy change. The particle's energy is conserved at 3 eV throughout — inside the barrier, outside it, and in the transmitted wave. What changes inside the barrier is the character of the wavefunction: instead of oscillating, it decays exponentially. If the barrier is thin enough, this decaying tail has nonzero amplitude at the far wall, where it reconnects to a propagating wave. The 'borrowed energy' picture (options B and D) is a common but incorrect classical analogy. Quantum mechanically, the particle never 'climbs over' — it tunnels through."

- question: "A scanning tunneling microscope can image individual atoms because tunneling current is exquisitely sensitive to gap distance. If the tip-to-surface gap doubles from 0.1 nm to 0.2 nm, what happens to the tunneling current?"
  type: multiple-choice
  options:
    - "It decreases by a factor of 2 — current is proportional to 1/distance"
    - "It decreases by a factor of 4 — current decreases as the square of distance"
    - "It decreases by roughly an order of magnitude or more — transmission probability decays exponentially with barrier width"
    - "It stays approximately the same — atomic-scale gap changes are too small to matter"
  answer: 2
  explanation: "Tunneling probability decays exponentially with barrier width: T ≈ e^{−2κL}. Doubling L from 0.1 to 0.2 nm roughly squares the transmission probability (e^{−2κ(0.2)} = (e^{−2κ(0.1)})²), resulting in a massive drop in tunneling current — roughly an order of magnitude per 0.1 nm of gap change in typical STM conditions. This extreme sensitivity (not a gentle linear or quadratic falloff) is precisely what gives the STM its sub-angstrom height resolution. Linear or inverse-square laws would give far too gradual a response to detect individual atomic steps."

- question: "When a particle quantum-tunnels through a barrier, its total energy is momentarily higher than usual inside the barrier, allowing it to pass through the classically forbidden region."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about tunneling. The particle's total energy is constant throughout the process — it equals E before, during, and after tunneling. There is no energy borrowing or violation of energy conservation. Inside the barrier (where E < V₀), the wavefunction decays exponentially rather than oscillating, but this is a property of the mathematical solution to the Schrödinger equation in that region, not a sign that energy has changed. The Heisenberg uncertainty principle provides intuition for why tunneling is possible but does not license an energy-violation picture."

- question: "A heavier particle tunnels through a given barrier more easily than a lighter particle with the same energy and the same barrier."
  type: true-false
  answer: false
  explanation: "Mass appears in the exponent of the tunneling probability: κ = √(2m(V₀ − E))/ℏ. A larger mass means a larger κ, which means a more steeply decaying wavefunction inside the barrier, which means much less transmission. Electrons tunnel readily; protons (about 1800× heavier) tunnel far less; alpha particles (7000× heavier than electrons) tunnel least readily of all. The exponential sensitivity to mass is why alpha decay rates vary so dramatically across isotopes, and why nuclear fusion requires enormous temperatures or pressures to bring heavy nuclei close enough for their wavefunctions to overlap."

- question: "Why does tunneling probability decrease exponentially (rather than linearly or gradually) as the barrier width increases?"
  type: short-answer
  answer: "Inside the barrier, the wavefunction decays exponentially as ψ(x) ∝ e^{−κx}, because the Schrödinger equation in a classically forbidden region (E < V₀) has real exponential solutions rather than oscillating ones. The tunneling probability is proportional to |ψ|² at the far wall, so T ≈ e^{−2κL}. Each additional increment of barrier width multiplies the already-reduced amplitude by another exponential factor, compounding the suppression. This is inherent to the mathematics of exponential decay: unlike linear decay, each doubling of width squares the transmission probability rather than halving it."
  explanation: "This exponential sensitivity is not a nuisance — it is the feature that makes tunneling devices useful. The STM exploits it for atomic-resolution imaging; tunnel diodes exploit it for ultra-fast switching. It also explains why alpha decay rates span twenty orders of magnitude across different isotopes despite similar energies: small differences in the Coulomb barrier height and width translate to enormous differences in the exponential factor, producing half-lives that range from microseconds to billions of years."
```

## Explainer

You already know from the particle-in-a-box that a quantum wavefunction must solve the Schrödinger equation inside every region of space, including regions the particle "shouldn't" be able to enter. In the infinite square well, the walls are infinitely high, so the wavefunction is forced to zero there. But what happens when the barrier has a finite height V₀ and the particle's energy E is less than V₀? Classically, the answer is simple: the particle bounces back every time. Quantum mechanically, the story is richer.

Inside the barrier, the Schrödinger equation still has solutions — they just aren't oscillating sinusoids. Instead, the wavefunction decays exponentially as ψ(x) ∝ e^{−κx}, where **κ = √(2m(V₀ − E))/ℏ**. This decaying tail isn't zero, which means if the barrier is thin enough, the wavefunction still has nonzero amplitude when it reaches the far side. There, it reconnects to a freely oscillating wave — a transmitted particle. The particle hasn't "borrowed" energy to climb over the barrier; its energy is constant throughout. It has simply leaked through a region where its wavefunction is non-zero, even though it is forbidden classically.

The **transmission coefficient** T quantifies this: T ≈ e^{−2κL}, where L is the barrier width. This exponential dependence is the key signature of tunneling. Doubling the barrier width squares the transmission probability. Heavier particles have larger κ (m appears in the numerator), so they tunnel far less readily — this is why protons tunnel much less than electrons, and alpha particles tunnel much less still (though still enough to drive nuclear alpha decay). The Heisenberg uncertainty principle provides an intuition for why tunneling is possible: position uncertainty means we can't say with certainty that the particle is on the "wrong" side of the barrier.

The exponential sensitivity to barrier width has revolutionary practical consequences. In a **scanning tunneling microscope (STM)**, a metal tip is brought within ~1 nm of a conducting surface. The tunneling current between tip and surface varies by roughly an order of magnitude for every 0.1 nm change in gap — sub-angstrom height sensitivity that lets the STM image individual atoms. In semiconductor **tunnel diodes**, tunneling current allows devices to operate at speeds impossible with classical transport. In nuclear physics, alpha decay rates are entirely set by tunneling probability through the Coulomb barrier — the exponential factor explains why some nuclei decay in microseconds and others in billions of years despite having similar energies.
