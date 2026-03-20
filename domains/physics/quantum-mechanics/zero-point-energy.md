---
id: zero-point-energy
title: Zero-Point Energy
domain: physics
course: quantum-mechanics
prerequisites:
- id: harmonic-oscillator-quantum
  type: hard
tags:
- oscillator
- energy
- ground-state
stage: advanced
status: draft
---

# Zero-Point Energy

## Core Idea
The quantum harmonic oscillator cannot have zero energy; the ground state has E₀ = ½ℏω. This consequence of the uncertainty principle appears throughout quantum mechanics from molecular vibrations to quantum field theory.

## Explainer

From the quantum harmonic oscillator, you know that the allowed energies are E_n = (n + ½)ℏω for n = 0, 1, 2, … The ladder operators raise and lower n, but you cannot go below n = 0 — the lowering operator annihilates the ground state. So the minimum energy is not zero but **E₀ = ½ℏω**. Why can't the oscillator simply sit still at the bottom of the potential well with zero energy?

The answer comes from the **uncertainty principle**, Δx Δp ≥ ℏ/2. A classical particle at rest in a harmonic well has a perfectly defined position (the equilibrium point x = 0) and a perfectly defined momentum (zero). That would mean Δx = 0 and Δp = 0, violating the uncertainty principle. To be confined near x = 0 requires some spread Δx, which forces some spread Δp, which forces some nonzero kinetic energy. The ground state wavefunction is a Gaussian — the unique shape that minimizes the total energy subject to the uncertainty constraint — and the ½ℏω is precisely the minimum uncertainty energy. You can verify this by computing ⟨T⟩ = ⟨p²⟩/2m = ½ℏω/2 and ⟨V⟩ = ½mω²⟨x²⟩ = ½ℏω/2, so total ⟨E⟩ = ½ℏω. The kinetic and potential contributions are equal, just as in a classical oscillator — but neither can be zero.

Zero-point energy has concrete, measurable consequences everywhere in physics. **Liquid helium** remains liquid under atmospheric pressure all the way to absolute zero — unlike every other element — because its light atoms have such large zero-point motion that they cannot freeze into a lattice (you need to apply ~25 atm of pressure to solidify He-4). **Molecular vibrations** in the ground electronic state still have zero-point energy, shifting bond lengths and affecting reaction rates (the **kinetic isotope effect**: deuterium substitution slows reactions because its larger mass lowers ω, reducing zero-point energy and raising the effective activation barrier). In **quantum field theory**, every mode of every quantum field is a harmonic oscillator with a zero-point energy ½ℏω — summing over all modes gives the quantum vacuum a nonzero energy density, which contributes to the observed **Casimir effect** (attractive force between two uncharged parallel conducting plates) and is connected to the cosmological constant problem.
