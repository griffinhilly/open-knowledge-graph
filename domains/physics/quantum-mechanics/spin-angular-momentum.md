---
id: spin-angular-momentum
title: Spin Angular Momentum
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: spin-quantum-number
  type: soft
builds-toward:
- total-angular-momentum
tags:
- spin
- angular-momentum
stage: abstract-reasoning
status: draft
---

# Spin Angular Momentum

## Core Idea
Spin is intrinsic angular momentum with no classical analog. Electrons have s = ½, obeying [Ŝ_i, Ŝ_j] = iℏ ε_{ijk} Ŝ_k. The spin magnetic moment couples to magnetic fields.

## Explainer

You already know from commutation relations that the algebra [L̂_i, L̂_j] = iℏ ε_{ijk} L̂_k completely determines what values orbital angular momentum can take: the magnitude squared is L² = ℏ²l(l+1) with l = 0, 1, 2, … and the z-component is m_l ℏ with m_l ranging in integer steps from −l to +l. Spin obeys exactly the same algebra — [Ŝ_i, Ŝ_j] = iℏ ε_{ijk} Ŝ_k — but with a crucial difference: the quantum number s need not be an integer. The algebraic derivation allows s to be any non-negative half-integer: 0, 1/2, 1, 3/2, …

For electrons (and protons, neutrons, and quarks), s = 1/2. This is an intrinsic property like mass or charge — you cannot change it by any interaction, and it has no classical analog. A spinning charged ball would give orbital angular momentum, but spin is not rotation of any extended object; the electron is pointlike. The two spin states are m_s = +1/2 (**spin-up**, often written |↑⟩ or |+⟩) and m_s = −1/2 (**spin-down**, |↓⟩ or |−⟩). The full quantum state of an electron requires specifying both its spatial wavefunction ψ(r) and its spin state — the total Hilbert space is a tensor product of the spatial and spin spaces.

Spin has a physical observable consequence through the **spin magnetic moment**: **μ_s** = −g_s μ_B **S**/ℏ, where μ_B = eℏ/2m_e is the Bohr magneton and g_s ≈ 2 is the electron's g-factor (the factor of 2 is a relativistic effect, predicted exactly by the Dirac equation and corrected to ≈ 2.002319… by quantum electrodynamics). In a magnetic field B along z, the interaction energy is −μ_z B = g_s μ_B m_s B, which splits the two spin states by ΔE = g_s μ_B B. This is the basis of **electron spin resonance (ESR)** and, for nuclear spins, **MRI**.

The Stern-Gerlach experiment provided the first direct evidence for spin. A beam of silver atoms — each with one outer electron in an l = 0 orbital, so no orbital angular momentum — was deflected into exactly two spots when passed through an inhomogeneous magnetic field. Classical physics predicts a continuous spread; quantum mechanics with s = 1/2 predicts exactly two deflections, corresponding to m_s = ±1/2. This 2s+1 = 2 splitting, with no s = 0 explanation possible, was the experimental proof of half-integer angular momentum. Spin is not a metaphor or approximation — it is a discrete, measurable property of particles, and its algebra is the same commutator structure you already know.


