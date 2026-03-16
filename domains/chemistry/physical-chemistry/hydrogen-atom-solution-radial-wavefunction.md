---
id: hydrogen-atom-solution-radial-wavefunction
title: 'Hydrogen Atom Solution: Radial Wavefunction'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hydrogen-atom-wavefunctions
  type: hard
- id: wave-function-normalization-orthogonality
  type: hard
- id: hydrogen-atom-quantum
  type: hard
builds-toward:
- electron-correlation-multi-electron-atoms
tags:
- hydrogen-atom
- quantum-mechanics
- wave-functions
- atomic-orbitals
stage: advanced
status: draft
---

# Hydrogen Atom Solution: Radial Wavefunction

## Core Idea
The hydrogen atom Schrödinger equation separates into radial and angular parts; the radial wave function R(r) describes how probability density varies with distance from the nucleus and depends on principal quantum number n and angular momentum quantum number l. Radial nodes (where R = 0) increase with n and determine orbital size and penetration. The radial component completely determines the spatial extent and electron density distribution in orbitals.

## How It's Best Learned
Solve the radial Schrödinger equation explicitly for hydrogen; plot radial probability density for 1s, 2s, and 2p orbitals to visualize nodes and shells. Compare with angular parts to understand complete orbital shapes.

## Explainer

From your prerequisite work on hydrogen atom wavefunctions, you know that the full solution to the Schrödinger equation for hydrogen separates into a radial part R(r) and an angular part Y(θ,φ) — the spherical harmonics. The **radial wavefunction** R(r) carries the information about how the electron's probability of being found varies with distance from the nucleus. It depends on two quantum numbers: the principal quantum number **n** (which sets the energy and overall size) and the angular momentum quantum number **l** (which sets the orbital shape: s, p, d, ...).

The mathematical form of R(r) involves an exponential decay (e^(−r/na₀), where a₀ is the Bohr radius) multiplied by a polynomial in r. The exponential ensures the wavefunction goes to zero at large distances — the electron is bound. The polynomial part creates **radial nodes**, spherical shells where R(r) = 0 and the probability density vanishes. The number of radial nodes is **n − l − 1**. So the 1s orbital (n=1, l=0) has zero radial nodes, the 2s (n=2, l=0) has one, the 3s (n=3, l=0) has two, and the 2p (n=2, l=1) has zero. These nodes have physical significance: they represent distances from the nucleus where there is exactly zero probability of finding the electron.

The quantity you most often want is not R(r) itself but the **radial probability density** P(r) = r²|R(r)|². The r² factor comes from the volume element in spherical coordinates — there is more volume in a thin shell at large r than at small r, so even though R(r) may be largest near the nucleus, the probability of finding the electron peaks at some finite distance. For the 1s orbital, P(r) peaks at r = a₀, the Bohr radius — confirming the classical prediction but with a probabilistic interpretation. For the 2s orbital, P(r) has two maxima separated by the radial node: a small inner lobe close to the nucleus and a larger outer lobe. This inner lobe gives s orbitals greater **penetration** toward the nucleus compared to p or d orbitals of the same n, which is why s electrons experience a higher effective nuclear charge in multi-electron atoms.

Comparing orbitals with the same n but different l reveals the key pattern. The 2s orbital extends closer to the nucleus (due to its inner lobe) than the 2p orbital, even though both have the same energy in hydrogen. The 3s orbital has two radial nodes, the 3p has one, and the 3d has none — each additional unit of angular momentum removes a radial node but replaces it with an angular node. The total number of nodes (radial plus angular) is always n − 1. Understanding radial wavefunctions is essential preparation for multi-electron atoms, where the differences in penetration between orbitals of the same n but different l break the hydrogen-like energy degeneracy and determine the Aufbau filling order.
