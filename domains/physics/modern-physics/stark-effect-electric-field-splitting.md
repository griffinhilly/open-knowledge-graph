---
id: stark-effect-electric-field-splitting
title: 'Stark Effect: Energy Level Splitting in Electric Fields'
domain: physics
course: modern-physics
prerequisites:
- id: zeeman-effect-magnetic-splitting
  type: soft
- id: hydrogen-atom-schrodinger-solution
  type: soft
tags:
- electric-field
- energy-levels
- atomic-physics
stage: advanced
status: draft
---

# Stark Effect: Energy Level Splitting in Electric Fields

## Core Idea
An external electric field E induces an electric dipole moment in atoms and shifts energy levels by ΔE ∝ E (linear Stark effect, rare) or ΔE ∝ E² (quadratic Stark effect, more common). The effect arises from mixing of nearby levels by the field. In hydrogen's 2s and 2p levels, the degeneracy is lifted—the 2s and 2p are split by the field.

## How It's Best Learned
Compare Stark and Zeeman effects: both are perturbations of atomic energy levels. For hydrogen, calculate the perturbation matrix and find the shifted energy levels. Observe Stark shifts spectroscopically.

## Common Misconceptions
Not all atoms show a linear Stark effect (hydrogen is special due to accidental degeneracy). The shift is not always proportional to the applied field (higher-order terms can dominate).

## Explainer

The Stark effect is the electric analogue of the Zeeman effect you've already encountered. Where a magnetic field couples to the magnetic dipole moment of an electron, an electric field couples to the electric dipole moment. The key difference is that most atoms in their ground state don't have a permanent electric dipole moment — the electron cloud is spherically symmetric. So the field first has to *create* a dipole by distorting the cloud, and the energy shift is proportional to E² (the **quadratic Stark effect**). This is the normal case for most atoms and for most levels of hydrogen.

Hydrogen in its first excited state is special because the 2s and 2p levels are **accidentally degenerate** — they share the same energy at the level of the Schrödinger equation for bare hydrogen. When two levels are degenerate, even a tiny perturbation can mix them strongly. The electric field perturbation operator is H′ = eEz, which connects states that differ by Δℓ = ±1. This couples the 2s (ℓ = 0) state directly to the 2p (ℓ = 1) states; the perturbation matrix has off-diagonal elements proportional to E. Diagonalizing it yields energy eigenvalues that are *linear* in the field: ΔE = ±3eEa₀, where a₀ is the Bohr radius. This is the **linear Stark effect** — the exception enabled by accidental degeneracy.

The physical picture is intuitive: the field polarizes the atom, creating a dipole oriented along the field direction. The two mixed eigenstates correspond to electron distributions shifted toward or away from the positive electrode — one state is stabilized and the other destabilized. The spectral lines that were degenerate split into distinct components, and the splitting grows linearly with field strength rather than quadratically.

More generally, the Stark effect is one of the most direct experimental probes of atomic structure. The magnitude of the quadratic shift measures the **polarizability** of the atom — how easily its charge distribution deforms in a field — which is directly tied to the matrix elements of the dipole operator between the ground and excited states. Measuring Stark shifts spectroscopically therefore yields detailed quantitative information about the geometry and scale of the electron cloud that complements what you can extract from the zero-field spectrum alone.
