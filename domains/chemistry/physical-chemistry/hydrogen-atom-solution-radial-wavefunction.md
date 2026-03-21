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

## Questions

```yaml
- question: "The 3s orbital has n=3, l=0 and the 3p orbital has n=3, l=1. How many radial nodes does each have, and what does the difference tell us?"
  type: multiple-choice
  options:
    - "3s has 3 nodes, 3p has 3 nodes — principal quantum number alone determines node count"
    - "3s has 2 nodes, 3p has 1 node — greater angular momentum replaces radial nodes with angular nodes"
    - "3s has 1 node, 3p has 2 nodes — angular orbitals have more complex radial structure"
    - "3s has 0 nodes, 3p has 1 node — s orbitals are nodeless because they are spherically symmetric"
  answer: 1
  explanation: "Radial nodes = n − l − 1. For 3s: 3 − 0 − 1 = 2 radial nodes. For 3p: 3 − 1 − 1 = 1 radial node. The pattern reveals a conservation of total nodes: both have n − 1 = 2 total nodes, but 3p trades a radial node for an angular node (the nodal plane through the nucleus). This trade-off has a physical consequence: the extra inner lobe in 3s gives it greater nuclear penetration, which matters enormously in multi-electron atoms where s electrons experience higher effective nuclear charge."

- question: "The radial wavefunction R(r) of the 1s orbital is largest at r = 0 (right at the nucleus). Yet the radial probability density P(r) peaks at r = a₀, not r = 0. Why?"
  type: multiple-choice
  options:
    - "The 1s wavefunction has a node at r = 0 that cancels the probability density"
    - "The Pauli exclusion principle prevents the electron from being at the nucleus"
    - "P(r) = r²|R(r)|² includes an r² factor from spherical volume elements — at r = 0 this factor is zero, so even a large R(r) gives zero probability"
    - "The electron's kinetic energy diverges at r = 0, making that region classically forbidden"
  answer: 2
  explanation: "The probability of finding the electron in a thin shell of thickness dr at radius r is P(r) dr = r²|R(r)|² dr. The r² comes from the volume element 4πr² dr in spherical coordinates — there is simply more volume in a shell at large r than at small r. Even though |R(r)|² is largest at the origin, the r² factor is zero there, so P(0) = 0. Moving outward, the r² factor grows while R(r) decreases exponentially; the product peaks at r = a₀ for the 1s orbital. This is why the Bohr model's prediction of r = a₀ emerges from the correct quantum mechanical treatment."

- question: "The radial probability density P(r) for the 1s orbital peaks at a distance from the nucleus, not at r = 0, even though the radial wavefunction R(r) is largest at r = 0."
  type: true-false
  answer: true
  explanation: "True. P(r) = r²|R(r)|² incorporates a volume-element factor r² that goes to zero at the origin. This means that despite R(1s) being maximum at r = 0, the actual probability of finding the electron in a thin spherical shell peaks at r = a₀. The distinction between |R(r)|² (probability density per unit volume) and P(r) (probability per unit radial distance) is essential for correctly interpreting orbital structure."

- question: "Going from an s orbital to a p orbital of the same principal quantum number (e.g., 2s → 2p) always increases the number of radial nodes."
  type: true-false
  answer: false
  explanation: "False — it decreases radial nodes. Radial nodes = n − l − 1, so higher angular momentum l means fewer radial nodes. For n = 2: the 2s has 2 − 0 − 1 = 1 radial node, while the 2p has 2 − 1 − 1 = 0 radial nodes. The total node count (radial + angular) stays fixed at n − 1 = 1 for both; the 2p trades its radial node for an angular nodal plane. A common misconception is that more complex orbitals must have more nodes overall — in fact, total nodes depend only on n."

- question: "Why do 2s and 2p electrons in a multi-electron atom experience different effective nuclear charges, even though both have n = 2 and both have zero radial nodes — wait, that's not right. Explain the actual difference in nuclear penetration between 2s and 2p orbitals."
  type: short-answer
  answer: "The 2s orbital has one radial node and a small but nonzero inner lobe of electron density close to the nucleus, giving 2s electrons significant probability of being found near the nucleus. The 2p orbital has no radial nodes but has an angular nodal plane through the nucleus, with zero probability at r = 0 and a radial probability distribution that stays farther from the nucleus. The inner lobe of 2s allows it to 'penetrate' past the shielding electrons to feel a higher effective nuclear charge, making 2s lower in energy than 2p in multi-electron atoms (breaking the hydrogen-like n = 2 degeneracy)."
  explanation: "In hydrogen, 2s and 2p are degenerate — they have the same energy. In multi-electron atoms, inner electrons shield the outer electrons from the full nuclear charge. But penetration (probability of being close to the nucleus) varies with orbital shape. The inner lobe of the 2s radial probability distribution gives 2s electrons a higher effective nuclear charge than 2p electrons, lowering the 2s energy relative to 2p. This penetration-and-shielding argument explains the Aufbau filling order and why, for example, 4s fills before 3d."
```

## Explainer

From your prerequisite work on hydrogen atom wavefunctions, you know that the full solution to the Schrödinger equation for hydrogen separates into a radial part R(r) and an angular part Y(θ,φ) — the spherical harmonics. The **radial wavefunction** R(r) carries the information about how the electron's probability of being found varies with distance from the nucleus. It depends on two quantum numbers: the principal quantum number **n** (which sets the energy and overall size) and the angular momentum quantum number **l** (which sets the orbital shape: s, p, d, ...).

The mathematical form of R(r) involves an exponential decay (e^(−r/na₀), where a₀ is the Bohr radius) multiplied by a polynomial in r. The exponential ensures the wavefunction goes to zero at large distances — the electron is bound. The polynomial part creates **radial nodes**, spherical shells where R(r) = 0 and the probability density vanishes. The number of radial nodes is **n − l − 1**. So the 1s orbital (n=1, l=0) has zero radial nodes, the 2s (n=2, l=0) has one, the 3s (n=3, l=0) has two, and the 2p (n=2, l=1) has zero. These nodes have physical significance: they represent distances from the nucleus where there is exactly zero probability of finding the electron.

The quantity you most often want is not R(r) itself but the **radial probability density** P(r) = r²|R(r)|². The r² factor comes from the volume element in spherical coordinates — there is more volume in a thin shell at large r than at small r, so even though R(r) may be largest near the nucleus, the probability of finding the electron peaks at some finite distance. For the 1s orbital, P(r) peaks at r = a₀, the Bohr radius — confirming the classical prediction but with a probabilistic interpretation. For the 2s orbital, P(r) has two maxima separated by the radial node: a small inner lobe close to the nucleus and a larger outer lobe. This inner lobe gives s orbitals greater **penetration** toward the nucleus compared to p or d orbitals of the same n, which is why s electrons experience a higher effective nuclear charge in multi-electron atoms.

Comparing orbitals with the same n but different l reveals the key pattern. The 2s orbital extends closer to the nucleus (due to its inner lobe) than the 2p orbital, even though both have the same energy in hydrogen. The 3s orbital has two radial nodes, the 3p has one, and the 3d has none — each additional unit of angular momentum removes a radial node but replaces it with an angular node. The total number of nodes (radial plus angular) is always n − 1. Understanding radial wavefunctions is essential preparation for multi-electron atoms, where the differences in penetration between orbitals of the same n but different l break the hydrogen-like energy degeneracy and determine the Aufbau filling order.
