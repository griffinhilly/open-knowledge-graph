---
id: atomic-orbitals
title: Atomic Orbitals
domain: physics
course: modern-physics
prerequisites:
- id: quantum-numbers
  type: hard
- id: wavefunction-and-probability
  type: hard
- id: atomic-structure-basics
  type: soft
- id: electron-configuration
  type: soft
builds-toward:
- pauli-exclusion-principle
- band-theory-intro
tags:
- quantum
- orbitals
- hydrogen
- electron-density
- s-p-d-f
stage: advanced
status: validated
---

# Atomic Orbitals

## Core Idea
Atomic orbitals are the wavefunctions ψ_{n,ℓ,m_ℓ} of the hydrogen electron, labeled by the quantum numbers n, ℓ, m_ℓ. Each orbital has a characteristic shape representing the probability density |ψ|² for finding the electron in space: s-orbitals are spherically symmetric, p-orbitals have two lobes, d-orbitals have four lobes or a torus. The radial part contains n−ℓ−1 nodes and the angular part has ℓ angular nodes. These orbital shapes form the basis for molecular bonding and the periodic table's structure.

## How It's Best Learned
Visualize orbital shapes using 3D probability density plots. Note how the number of nodes relates to the energy. For multi-electron atoms, use the same orbital shapes as an approximation (independent-electron model) and order them by increasing energy.

## Common Misconceptions
- Electrons orbit in circular paths like planets — orbitals are probability clouds with no definite trajectory.
- Higher ℓ always means higher energy — in hydrogen, all orbitals with the same n are degenerate; in multi-electron atoms this degeneracy is broken.

## Questions

```yaml
- question: "A hydrogen orbital has quantum numbers n=3, ℓ=1. How many angular nodes does this orbital have?"
  type: multiple-choice
  options: ["0", "1", "2", "3"]
  answer: 1
  explanation: "The angular quantum number ℓ directly gives the number of angular nodes. Since ℓ=1, there is 1 angular node, producing the two-lobe p-orbital shape. The total node count is n−1=2, so there is also 1 radial node — but that is a different kind of node."

- question: "In a hydrogen atom, the 3s orbital has lower energy than the 3p orbital because it is closer to the nucleus."
  type: true-false
  answer: false
  explanation: "In hydrogen (one electron), all orbitals with the same principal quantum number n have exactly the same energy — they are degenerate. The 3s, 3p, and 3d orbitals all sit at E = −13.6/9 eV. Energy degeneracy within a shell is broken only in multi-electron atoms, where electron shielding makes s orbitals lower in energy than p orbitals of the same n."

- question: "An atomic orbital is sometimes described as 'the electron's path around the nucleus.' Why is this description wrong, and what does an orbital actually represent?"
  type: short-answer
  answer: "An orbital is not a path but a wavefunction ψ (or probability density |ψ|²) that describes the probability of finding the electron at each point in space. Electrons have no definite trajectory — the orbital shape shows where the electron is most likely to be found if measured."
  explanation: "This targets the classical-orbit misconception. Unlike a planetary orbit, the electron exists in a quantum superposition without a definite position. The orbital's shape (sphere for s, lobes for p) represents regions of high probability density |ψ|², not a physical track. This distinction is foundational to all quantum chemistry."
```

## Explainer

You have already learned that quantum numbers (n, ℓ, m_ℓ) label the allowed states of a hydrogen electron, and that the wavefunction ψ gives the probability amplitude for finding the electron at a given location in space. Atomic orbitals are simply those wavefunctions: each combination of (n, ℓ, m_ℓ) defines a distinct orbital with a characteristic spatial shape.

The shape of an orbital is determined by the angular part of the wavefunction, which depends entirely on ℓ. When ℓ=0 (s-orbitals), there is no angular variation — the probability density |ψ|² is the same in every direction from the nucleus, so the orbital is a sphere. When ℓ=1 (p-orbitals), a single nodal plane cuts through the nucleus and splits the electron density into two lobes pointing along x, y, or z — the three 2p orbitals differ only in orientation. When ℓ=2 (d-orbitals), two angular nodes produce four-lobe or torus shapes. The rule is simple: ℓ angular nodes → ℓ angular node planes → the characteristic s/p/d/f shapes.

The radial part of the wavefunction adds further structure along the distance from the nucleus. A 2s orbital, for example, has one radial node — a spherical shell where the electron probability is exactly zero — enclosing an inner density region, then an outer one. The total node count is always n−1: the angular quantum number accounts for ℓ of them, and the radial part accounts for n−ℓ−1 more. Higher nodes correspond to higher spatial oscillation of the wavefunction, which corresponds to higher kinetic energy.

Energy in hydrogen depends only on n, not on ℓ or m_ℓ. All orbitals with the same n — say, 2s and all three 2p — are degenerate (equal energy). This is a special property of the 1/r Coulomb potential; other potential shapes do not produce this exact degeneracy. In multi-electron atoms, electron-electron repulsion breaks the degeneracy: s electrons penetrate closer to the nucleus than p electrons of the same n, experiencing stronger nuclear attraction and sitting at lower energy. This is why the periodic table fills 2s before 2p.

These orbital shapes are not an abstract curiosity — they are the foundation of molecular bonding. When two atoms approach, their wavefunctions overlap to form bonding and antibonding molecular orbitals. The directional lobes of p-orbitals determine bond angles (water's ~104.5° angle, for example); the spatial profiles of d-orbitals shape the colors and magnetism of transition metal complexes. Mastering orbital shapes means you have already internalized the language needed for nearly all of chemistry and materials science.
