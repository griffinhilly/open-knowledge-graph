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
stage: expert
status: validated
---

# Radial Distribution Function and Liquid Structure

## Core Idea
The radial distribution function gives the density of particles at distance r from a reference particle, averaged over all orientations. It quantifies local packing around each particle and directly relates to thermodynamic properties through the pressure and energy.

## Questions

```yaml
- question: "For a simple liquid at equilibrium, g(r) = 2.8 at r ≈ 3.4 Å (the first peak) and g(r) → 1 as r → ∞. What do these two values tell you about the liquid structure?"
  type: multiple-choice
  options:
    - "There are 2.8 particles per cubic ångstrom at 3.4 Å, and the density drops to 1 particle per cubic ångstrom at large distances"
    - "The probability of finding a neighbor at 3.4 Å is 2.8 times higher than it would be in an ideal gas; at large r, correlations die out and local density matches the bulk average"
    - "The coordination number of the liquid is 2.8, meaning each atom has on average 2.8 nearest neighbors"
    - "The liquid has 2.8 times the density of a gas at the first coordination shell distance, and becomes a uniform gas at long range"
  answer: 1
  explanation: "g(r) is normalized by the ideal gas expectation. g(r) = 2.8 at the first peak means the probability of finding a neighbor at that distance is 2.8 times what you would expect in a uniform (ideal gas) distribution at the same bulk density. It does not give absolute particle count per volume — you need to multiply g(r) by the bulk density ρ and the shell volume 4πr²dr to get the actual number of neighbors. The large-r limit g(r) → 1 reflects that at large separations, correlations fade and the local density matches the bulk average — which is the definition of having no long-range order."

- question: "You measure g(r) for two materials: Material X shows sharp, non-decaying peaks at fixed distances that persist for large r. Material Y shows a first peak at r ≈ σ, then damped oscillations that relax to g(r) = 1 by r ≈ 4σ. What do these patterns indicate?"
  type: multiple-choice
  options:
    - "Material X is a liquid with short correlation length; Material Y is an ideal gas with correlated fluctuations"
    - "Material X is a crystal with long-range periodic order; Material Y is a liquid with finite structural correlation length"
    - "Both materials are liquids, but Material X is at lower temperature where order persists longer"
    - "Material X is a gas at high pressure; Material Y is a supercritical fluid above the critical point"
  answer: 1
  explanation: "The g(r) fingerprint distinguishes phases clearly. Non-decaying peaks at lattice spacings that persist for all r is the signature of a crystal: long-range periodic order means correlations persist at any distance. Damped oscillations that relax to 1 are the signature of a liquid: short-range order exists (coordination shells at 1σ, 2σ, etc.) but correlations decay exponentially over a finite structural correlation length. An ideal gas would show g(r) = 1 everywhere (no correlations at all). This is why g(r) measured by X-ray or neutron diffraction is a primary tool for phase characterization."

- question: "If g(r) = 1 for most values of r in a fluid, this means the fluid is at its maximum density — most shells are equally and fully occupied."
  type: true-false
  answer: false
  explanation: "g(r) = 1 everywhere is the signature of an ideal gas — a fluid with no interparticle correlations or interactions. It does not mean maximum density; it means that the local density at any distance from a reference particle is exactly equal to the bulk average density ρ. Real fluids at any density show deviations from g(r) = 1: a hard core at small r (g = 0 where atoms cannot overlap) and peaks at the coordination shells. A high-density fluid actually shows more pronounced structure (larger peaks and deeper troughs in g(r)) than a low-density one, as packing constraints create stronger local order."

- question: "The internal energy and pressure of a fluid can be computed directly from g(r) and the pair potential u(r), without simulating individual particle trajectories."
  type: true-false
  answer: true
  explanation: "This is the central power of the radial distribution function. The energy equation states U = N⟨KE⟩ + (N²/2V) ∫ u(r) g(r) 4πr² dr, and the pressure equation gives P = ρkT − (ρ²/6) ∫ r(du/dr) g(r) 4πr² dr. Both integrals require only g(r) (the structural information, measurable by scattering) and u(r) (the pair potential, known from theory or fitting). This means a single scattering experiment can yield thermodynamic data for the fluid without tracking individual particles — a remarkable bridge between structure and thermodynamics."

- question: "Explain why g(r) must equal zero for small r in any real liquid, and what physical property of matter enforces this constraint."
  type: short-answer
  answer: "g(r) = 0 at small r because real atoms have a repulsive core — a short-range repulsion (from Pauli exclusion of electron clouds) that prevents two atoms from occupying the same space. The pair potential u(r) rises steeply to very large positive values as r decreases below the atomic diameter σ. This makes it thermodynamically impossible for two atoms to overlap, so the probability of finding a neighbor at r < σ is essentially zero. In g(r) terms, the strong repulsion ensures that shells at short distances contribute zero to the running sum ρ g(r) 4πr² dr."
  explanation: "The hard-core exclusion at small r is the most fundamental structural feature of matter — it is why solids and liquids have finite volume and cannot be compressed indefinitely. The distance at which g(r) first rises from zero to its first peak is approximately the effective diameter of the atoms or molecules in the liquid. For liquid argon, this is about 3.4 Å (the Lennard-Jones σ parameter). For water, the first peak in the oxygen-oxygen g(r) is at about 2.8 Å, reflecting the shorter hydrogen-bonded contact distance. Reading the position of g(r)'s first rise from zero directly gives you the effective atomic size."
```

## Explainer

Your prerequisite study of the **pair distribution function** established the general concept: g(r₁, r₂) measures the probability of finding a particle at r₂ given one at r₁, relative to what you would expect from a uniform gas. The **radial distribution function** g(r) specializes this to isotropic fluids — systems where the structure depends only on the distance r = |r₂ − r₁|, not on direction. This isotropy holds for liquids and dense gases in equilibrium. The definition is that the number of particles in a thin shell of radius r and thickness dr around a reference particle is dn = ρ g(r) 4πr² dr, where ρ = N/V is the mean number density. If g(r) = 1 everywhere, particles are distributed exactly as in an ideal gas — no correlations. Real g(r) encodes all the structure that interactions impose.

Reading a g(r) plot tells you the liquid's anatomy. Start from r = 0: g(r) = 0 at very short distances because the repulsive core of the interparticle potential prevents two atoms from overlapping. As r increases to roughly the diameter of an atom, g(r) jumps to a large peak — this is the **first coordination shell**, the layer of nearest neighbors packed tightly around the reference atom. In a simple liquid like liquid argon, this peak is typically at r ≈ σ (the atomic diameter) and reaches g(r) ≈ 3. Beyond the first shell, g(r) shows damped oscillations corresponding to second, third, and further coordination shells, before relaxing to g(r) → 1 at large r where correlations die out. The oscillations decay over a distance set by the **structural correlation length**, which is finite in a liquid but would diverge near a critical point. Contrast with a crystal, where g(r) shows sharp peaks at the lattice vectors that never decay, or an ideal gas, where g(r) = 1 everywhere.

The power of g(r) lies in connecting structure to thermodynamics. The internal energy of a fluid with pairwise interactions u(r) is U = N⟨KE⟩ + (N²/2V) ∫ u(r) g(r) 4πr² dr. This **energy equation** says you can compute the potential energy just by knowing how atoms are distributed (g(r)) and how they interact (u(r)). Similarly, the **pressure equation** P = ρkT − (ρ²/6) ∫ r (du/dr) g(r) 4πr² dr relates the equation of state to g(r). Both integrals have the same structure: sum u(r) or −r du/dr weighted by the local density ρ g(r) 4πr² dr. This is the central bridge: a structural measurement (g(r), accessible by X-ray or neutron scattering) gives you thermodynamic properties without having to track individual particle trajectories.

In practice, g(r) is measured by **X-ray or neutron diffraction**, because the scattered intensity is related to the Fourier transform of g(r), known as the **static structure factor** S(q). Measuring S(q) and inverting gives g(r). For liquid water, g(r) reveals the characteristic double-peak structure from hydrogen bonding; for liquid metals, a simple single-peak structure like noble-gas liquids. Molecular dynamics simulations compute g(r) by averaging histograms of interparticle distances over time, and the result can be directly compared to experiment. The fact that both routes give the same g(r) is one of the key validations that classical pairwise force fields correctly describe liquid structure, even for systems as complex as water.
