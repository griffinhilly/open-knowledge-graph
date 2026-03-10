---
id: hydrogen-atom-wavefunctions
title: Hydrogen Atom Wavefunctions and Atomic Orbitals
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: quantum-numbers
  type: hard
- id: atomic-orbitals
  type: soft
builds-toward:
- molecular-orbital-theory-advanced
- variational-principle-chemistry
- electronic-spectroscopy-theory
tags:
- hydrogen
- orbitals
- wavefunctions
- radial
- angular
- spherical-harmonics
stage: advanced
status: draft
---

# Hydrogen Atom Wavefunctions and Atomic Orbitals

## Core Idea
The hydrogen atom is the only multi-particle system with an exact analytical solution to the Schrödinger equation. The wavefunctions ψ_{nlm} are products of radial functions R_{nl}(r) and spherical harmonics Y_l^m(θ,φ), each labeled by three quantum numbers: principal (n), angular momentum (l), and magnetic (m). Energy levels depend only on n and go as E_n = −13.6/n² eV. The radial probability distribution P(r) = r²|R_{nl}|² reveals where electrons are most likely to be found, directly explaining orbital shapes and the concept of shells.

## How It's Best Learned
Plot radial probability distributions for s, p, and d orbitals and count nodes — n−l−1 radial nodes and l angular nodes. Connect each quantum number to a physical property: n → energy and size, l → shape, m → orientation.

## Common Misconceptions
- Conflating the orbital wavefunction (which can be negative) with the orbital shape (which is a surface of |ψ|²).
- Assuming the Bohr model radii match the most probable radius for all orbitals — they match only for s states.
