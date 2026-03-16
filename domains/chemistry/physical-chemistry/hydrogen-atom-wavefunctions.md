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
- id: schrodinger-equation-intro
  type: soft
- id: wavefunction-and-probability
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
status: validated
---

# Hydrogen Atom Wavefunctions and Atomic Orbitals

## Core Idea
The hydrogen atom is the only multi-particle system with an exact analytical solution to the Schrödinger equation. The wavefunctions ψ_{nlm} are products of radial functions R_{nl}(r) and spherical harmonics Y_l^m(θ,φ), each labeled by three quantum numbers: principal (n), angular momentum (l), and magnetic (m). Energy levels depend only on n and go as E_n = −13.6/n² eV. The radial probability distribution P(r) = r²|R_{nl}|² reveals where electrons are most likely to be found, directly explaining orbital shapes and the concept of shells.

## How It's Best Learned
Plot radial probability distributions for s, p, and d orbitals and count nodes — n−l−1 radial nodes and l angular nodes. Connect each quantum number to a physical property: n → energy and size, l → shape, m → orientation.

## Common Misconceptions
- Conflating the orbital wavefunction (which can be negative) with the orbital shape (which is a surface of |ψ|²).
- Assuming the Bohr model radii match the most probable radius for all orbitals — they match only for s states.

## Questions

```yaml
- question: "The 2p wavefunction ψ_{210} has regions where its value is negative (below the nodal plane). What is the probability of finding the electron in one of those negative-ψ regions?"
  type: multiple-choice
  options:
    - "Negative, because probability tracks the sign of ψ"
    - "Zero, because negative ψ means the electron is excluded"
    - "Positive and nonzero, because probability density is |ψ|², which is always ≥ 0"
    - "Equal to the probability in the positive-ψ lobe, because |ψ|² is symmetric"
  answer: 2
  explanation: "The wavefunction ψ itself can be negative — it is a mathematical amplitude, not a probability. Probability density is |ψ|², which is always non-negative. A negative lobe of ψ has the same |ψ|² as a positive lobe of equal magnitude, so the electron is found there with equal probability. The sign of ψ matters only when wavefunctions interfere (e.g., in bonding/antibonding combinations), not for single-orbital probabilities."

- question: "In the hydrogen atom, the 2s and 2p orbitals have the same energy (they are degenerate) because energy depends only on the principal quantum number n."
  type: true-false
  answer: true
  explanation: "For the pure hydrogen atom (one electron, no electron-electron repulsion), the Coulomb potential has a special symmetry that makes all subshells with the same n exactly degenerate: E_n = −13.6/n² eV regardless of l. This accidental degeneracy is unique to hydrogen. In multi-electron atoms, electron-electron repulsion breaks this, making 2s lower in energy than 2p."

- question: "Why does the radial probability distribution P(r) = r²|R_{nl}(r)|² include an r² factor, rather than simply plotting |R_{nl}(r)|²?"
  type: short-answer
  answer: "The r² factor accounts for the increasing volume of thin spherical shells as radius grows. A shell of thickness dr at radius r has volume 4πr² dr. Even if |R_{nl}|² decreases with r, the shell volume grows, so the actual probability of finding the electron in that shell is proportional to r²|R_{nl}|². Plotting just |R_{nl}|² would give the amplitude at a single point, not the probability in a shell — which is the physically meaningful quantity for locating the electron."
  explanation: "This distinction is critical: the 1s wavefunction has its maximum amplitude at r = 0, but the most probable radius (peak of P(r)) is at the Bohr radius a₀ because the r² factor overwhelms the exponential decay near the nucleus. Students who skip the r² factor incorrectly conclude that s-orbital electrons are most likely found at the nucleus."
```

## Explainer

The hydrogen atom holds a unique place in quantum chemistry: it is the only atom for which the Schrödinger equation can be solved exactly, producing closed-form wavefunctions. Everything you know about atomic orbitals — their shapes, their quantum numbers, their energies — derives directly from this solution.

The wavefunction ψ_{nlm}(r,θ,φ) factors into two independent pieces: a radial part R_{nl}(r) that depends only on distance from the nucleus, and an angular part Y_l^m(θ,φ) — a spherical harmonic — that describes the directional shape. The three quantum numbers encode distinct physical information: n determines the energy (E_n = −13.6/n² eV) and the overall size of the orbital; l determines the shape (l = 0 is spherical, l = 1 has a dumbbell shape, l = 2 is cloverleaf); and m determines orientation in space. Notice that for hydrogen, only n matters for energy — all the l and m sub-levels with the same n are exactly degenerate, a special symmetry of the 1/r Coulomb potential that disappears in multi-electron atoms.

Nodes are the zeros of the wavefunction — surfaces where the electron has exactly zero probability density. A radial node is a sphere where R_{nl} = 0; there are n−l−1 of them. An angular node is a plane or cone where Y_l^m = 0; there are l of them. Total nodes = n−1. The 2p orbital (n=2, l=1) has zero radial nodes and one angular node (the nodal plane). The 3d orbital (n=3, l=2) has zero radial nodes and two angular nodes. Counting nodes is a powerful consistency check.

A critical conceptual distinction: the wavefunction ψ can take negative values, but this does not mean the electron is "excluded" from those regions. Probability density is |ψ|², which is always non-negative. A negative lobe of ψ is just as accessible to the electron as a positive lobe of the same magnitude. The sign of ψ carries phase information that only becomes observable when two orbitals interact — it determines whether overlap leads to bonding (same sign, constructive) or antibonding (opposite sign, destructive) combinations.

Finally, to correctly describe where the electron actually lives, use the radial probability distribution P(r) = r²|R_{nl}|² rather than |ψ|² alone. The r² factor accounts for the fact that a thin spherical shell of thickness dr has a volume 4πr² dr that grows with radius. For the 1s orbital, the wavefunction amplitude is largest at r = 0, but the most probable radius (the peak of P(r)) is the Bohr radius a₀ = 0.529 Å — because near the nucleus, the small shell volume makes electron detection unlikely despite high amplitude. This is the quantitative picture behind the familiar statement that "electrons occupy orbitals" rather than "electrons sit at the nucleus."
