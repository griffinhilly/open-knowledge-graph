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

## Explainer

From your study of quantum tunneling, you know that a particle can pass through a classically forbidden region. The rectangular barrier makes this quantitative. Imagine a particle moving in the +x direction toward a wall of height V₀ and width d, where the particle's total energy E is less than V₀. In classical mechanics, the particle simply bounces back — it can never enter the region where kinetic energy would be negative. In quantum mechanics, the particle is described by a wavefunction, and wavefunctions don't hard-stop at boundaries.

The tool for calculating what happens is the time-independent Schrödinger equation, which you solved for infinite and finite wells. For the rectangular barrier, divide space into three regions: Region I (before the barrier, x < 0), Region II (inside the barrier, 0 < x < d), and Region III (after the barrier, x > d). In Regions I and III, E > 0 and the kinetic energy is positive, so the Schrödinger equation gives oscillatory solutions — plane waves of the form Ae^{ikx} + Be^{-ikx}, where ℏk = √(2mE). These represent incoming, reflected, and transmitted waves.

Inside the barrier, E < V₀, so the kinetic energy is negative. The Schrödinger equation becomes d²ψ/dx² = κ²ψ where κ = √(2m(V₀−E))/ℏ. The solutions are real exponentials: Ce^{κx} + De^{-κx}. This exponential decay is the key to tunneling — the wavefunction doesn't vanish abruptly but fades. If the barrier is thin enough, a non-zero amplitude survives to Region III, meaning there is a non-zero probability of finding the particle on the far side.

The **transmission coefficient** T is found by matching ψ and dψ/dx at both boundaries x=0 and x=d. Matching at both interfaces gives four equations relating the amplitudes. After solving, the result for E < V₀ is approximately T ≈ e^{−2κd}, where κ = √(2m(V₀−E))/ℏ. This single formula captures why tunneling is exponentially sensitive to barrier width d and height (V₀−E): doubling the width roughly squares the transmission probability, and a taller barrier increases κ, suppressing T even faster.

This exponential sensitivity has profound physical applications. In alpha decay, a nucleus emits an alpha particle that tunnels through the Coulomb barrier — tiny changes in barrier height explain why some isotopes have half-lives of microseconds while others have half-lives of billions of years. The **scanning tunneling microscope** (STM) exploits the same sensitivity: a metallic tip brought nanometers from a surface passes a tunneling current that falls by a factor of ~10 for each additional ångström of distance, allowing atomic-resolution imaging. Tunnel diodes use controlled barrier engineering for fast electronic switching. In all these cases, the physics is the same rectangular-barrier calculation you've now learned to solve.


