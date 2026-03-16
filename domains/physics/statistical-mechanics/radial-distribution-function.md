---
id: radial-distribution-function
title: Radial Distribution Function and Liquid Structure
domain: physics
course: statistical-mechanics
prerequisites:
- id: pair-distribution-function
  type: hard
builds-toward:
- static-structure-factor
tags:
- structure
- correlations
- liquids
stage: advanced
status: draft
---

# Radial Distribution Function and Liquid Structure

## Core Idea
The radial distribution function gives the density of particles at distance r from a reference particle, averaged over all orientations. It quantifies local packing around each particle and directly relates to thermodynamic properties through the pressure and energy.

## Explainer

Your prerequisite study of the **pair distribution function** established the general concept: g(r₁, r₂) measures the probability of finding a particle at r₂ given one at r₁, relative to what you would expect from a uniform gas. The **radial distribution function** g(r) specializes this to isotropic fluids — systems where the structure depends only on the distance r = |r₂ − r₁|, not on direction. This isotropy holds for liquids and dense gases in equilibrium. The definition is that the number of particles in a thin shell of radius r and thickness dr around a reference particle is dn = ρ g(r) 4πr² dr, where ρ = N/V is the mean number density. If g(r) = 1 everywhere, particles are distributed exactly as in an ideal gas — no correlations. Real g(r) encodes all the structure that interactions impose.

Reading a g(r) plot tells you the liquid's anatomy. Start from r = 0: g(r) = 0 at very short distances because the repulsive core of the interparticle potential prevents two atoms from overlapping. As r increases to roughly the diameter of an atom, g(r) jumps to a large peak — this is the **first coordination shell**, the layer of nearest neighbors packed tightly around the reference atom. In a simple liquid like liquid argon, this peak is typically at r ≈ σ (the atomic diameter) and reaches g(r) ≈ 3. Beyond the first shell, g(r) shows damped oscillations corresponding to second, third, and further coordination shells, before relaxing to g(r) → 1 at large r where correlations die out. The oscillations decay over a distance set by the **structural correlation length**, which is finite in a liquid but would diverge near a critical point. Contrast with a crystal, where g(r) shows sharp peaks at the lattice vectors that never decay, or an ideal gas, where g(r) = 1 everywhere.

The power of g(r) lies in connecting structure to thermodynamics. The internal energy of a fluid with pairwise interactions u(r) is U = N⟨KE⟩ + (N²/2V) ∫ u(r) g(r) 4πr² dr. This **energy equation** says you can compute the potential energy just by knowing how atoms are distributed (g(r)) and how they interact (u(r)). Similarly, the **pressure equation** P = ρkT − (ρ²/6) ∫ r (du/dr) g(r) 4πr² dr relates the equation of state to g(r). Both integrals have the same structure: sum u(r) or −r du/dr weighted by the local density ρ g(r) 4πr² dr. This is the central bridge: a structural measurement (g(r), accessible by X-ray or neutron scattering) gives you thermodynamic properties without having to track individual particle trajectories.

In practice, g(r) is measured by **X-ray or neutron diffraction**, because the scattered intensity is related to the Fourier transform of g(r), known as the **static structure factor** S(q). Measuring S(q) and inverting gives g(r). For liquid water, g(r) reveals the characteristic double-peak structure from hydrogen bonding; for liquid metals, a simple single-peak structure like noble-gas liquids. Molecular dynamics simulations compute g(r) by averaging histograms of interparticle distances over time, and the result can be directly compared to experiment. The fact that both routes give the same g(r) is one of the key validations that classical pairwise force fields correctly describe liquid structure, even for systems as complex as water.
