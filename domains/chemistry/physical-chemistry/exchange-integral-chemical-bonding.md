---
id: exchange-integral-chemical-bonding
title: Exchange Integral and Chemical Bonding
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-diagrams
  type: hard
- id: huckel-molecular-orbital-theory
  type: soft
builds-toward:
- molecular-orbital-symmetry-classification
- aromaticity-huckel-rule-pi-system
tags:
- molecular-orbital-theory
- bonding
- quantum-mechanics
stage: advanced
status: draft
---

# Exchange Integral and Chemical Bonding

## Core Idea
The exchange integral (resonance integral β) quantifies orbital overlap between atomic orbitals and their ability to delocalize electron density. Bonding arises not from classical Coulomb attraction but from quantum mechanical exchange—allowing electrons to occupy overlapping orbitals lowers energy. This is purely quantum and cannot be explained by classical electrostatics.

## How It's Best Learned
Calculate exchange integrals for simple diatomic molecules (H₂, H₂⁺); plot how integral varies with internuclear distance. Observe the correlation between orbital overlap and bond strength.

## Explainer

From constructing molecular orbital diagrams, you know that atomic orbitals combine to form bonding and antibonding molecular orbitals, and that the energy splitting between them determines bond strength. The **exchange integral** (commonly denoted **β** or **K**) is the quantum mechanical quantity that controls this splitting — it answers the question: by how much does the energy drop when an electron is allowed to spread across two atomic orbitals simultaneously?

To understand what β represents physically, consider the simplest possible bond: H₂⁺, a single electron shared between two protons. In the LCAO (linear combination of atomic orbitals) approach, you write the molecular wavefunction as ψ = c₁φₐ + c₂φᵦ, where φₐ and φᵦ are hydrogen 1s orbitals on atoms A and B. When you calculate the energy of this state, three types of integrals appear. The **Coulomb integral** (α) is the energy of an electron in one atomic orbital, including its interaction with the other nucleus — it sets the baseline energy. The **overlap integral** (S) measures how much the two atomic orbitals physically overlap in space. The **exchange integral** (β) is the crucial one: it evaluates the energy associated with the electron being simultaneously in both orbitals, β = ∫φₐ Ĥ φᵦ dτ. This integral has no classical analogue — it arises purely from the quantum mechanical superposition of states.

The bonding orbital has energy (α + β)/(1 + S) and the antibonding orbital has energy (α − β)/(1 − S). Since β is negative for bonding interactions (the exchange lowers energy), the bonding orbital is stabilized and the antibonding orbital is destabilized. The magnitude of β directly determines the **bond strength**: a larger |β| means a greater energy gap and a stronger bond. And |β| depends critically on **orbital overlap** — when the two atomic orbitals overlap significantly in the bonding region between the nuclei, β is large. When the atoms are far apart, overlap vanishes and β goes to zero, meaning no bond forms. This is why bond strength correlates with overlap: the exchange integral is the mathematical bridge between geometric overlap and energetic stabilization.

The concept extends beyond H₂⁺ to all covalent bonds. In Hückel theory for π systems, β becomes a parameter representing the interaction energy between adjacent p orbitals, and the pattern of molecular orbital energies for benzene, butadiene, and other conjugated systems all flow from solving eigenvalue problems in terms of α and β. The deeper lesson is that **covalent bonding is fundamentally a quantum mechanical exchange phenomenon** — electrons are stabilized not by being "shared" in any classical sense, but by the quantum mechanical fact that a wavefunction delocalized across two centers has lower kinetic energy than one confined to a single atom.
