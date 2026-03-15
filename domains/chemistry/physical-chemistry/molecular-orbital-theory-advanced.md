---
id: molecular-orbital-theory-advanced
title: 'Molecular Orbital Theory: LCAO-MO'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: born-oppenheimer-approximation
  type: hard
- id: hydrogen-atom-wavefunctions
  type: hard
- id: variational-principle-chemistry
  type: hard
- id: covalent-bonding
  type: soft
- id: quantum-mechanics-postulates-core
  type: hard
builds-toward:
- huckel-molecular-orbital-theory
- electronic-spectroscopy-theory
tags:
- LCAO
- bonding-antibonding
- MO-theory
- sigma
- pi-orbitals
- overlap-integral
stage: advanced
status: validated
---

# Molecular Orbital Theory: LCAO-MO

## Core Idea
Molecular orbital theory constructs MOs as linear combinations of atomic orbitals (LCAO): φ = c_A χ_A + c_B χ_B. Applying the variational principle leads to the secular determinant, whose solutions give bonding and antibonding orbital energies and coefficients. The key integrals are the overlap integral S, Coulomb integral α, and resonance integral β; their relative magnitudes determine the energy stabilization of bonding MOs and the destabilization of antibonding ones. Bond order is (bonding electrons − antibonding electrons)/2. MO theory correctly predicts O₂ paramagnetism and the non-existence of He₂, where valence bond theory struggles.

## How It's Best Learned
Work through H₂⁺ in detail before tackling H₂ and second-row homonuclear diatomics. Draw the MO energy-level diagrams, fill in electrons using the Aufbau principle, and compute bond orders.

## Common Misconceptions
- Confusing the LCAO coefficients c with probabilities; the coefficients can be negative, while |c|² gives orbital contribution.
- Thinking bonding MOs are always lower in energy than the constituent AOs — they are only if S is positive and β < 0.
