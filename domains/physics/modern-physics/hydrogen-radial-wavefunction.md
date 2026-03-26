---
id: hydrogen-radial-wavefunction
title: Radial Wavefunctions and Probability Distributions in Hydrogen
domain: physics
course: modern-physics
prerequisites:
- id: hydrogen-atom-schrodinger-solution
  type: hard
builds-toward:
- electron-cloud-orbital-shapes
tags:
- quantum-mechanics
- hydrogen
- orbitals
stage: advanced
status: validated
---

# Radial Wavefunctions and Probability Distributions in Hydrogen

## Core Idea
The radial wavefunction R(r) describes how the electron probability amplitude varies with distance from the nucleus. The radial probability density P(r) = r²|R(r)|² peaks at the most probable radius, which for the 1s orbital is the Bohr radius a₀ ≈ 0.53 Å. Higher-n and higher-ℓ states have wavefunctions peaked at larger radii and may have nodes (radial zeros) where the wavefunction changes sign.

## How It's Best Learned
Plot radial wavefunctions and radial probability densities for low quantum numbers. Identify the most probable radius for each state. Understand the physical meaning of nodes and relate to the number of radial nodes = n − ℓ − 1.

## Common Misconceptions
The most probable radius is not where the wavefunction amplitude is largest (it's where r²|R(r)|² is largest). The Bohr radius a₀ is most probable only for the 1s state; for excited states, the most probable radius is larger.

## Questions

```yaml
- question: "For the hydrogen 1s orbital, the wavefunction amplitude |R(r)|² is actually largest at r = 0 — right at the nucleus. Yet the most probable location for the electron is at r = a₀ ≈ 0.53 Å. Why aren't these contradictory?"
  type: multiple-choice
  options:
    - "The 1s wavefunction has a node at r = 0, making |R(r)|² zero there"
    - "The probability of finding the electron in a shell at radius r is proportional to r²|R(r)|², which is zero at r = 0 because the spherical shell has zero area there"
    - "The nucleus electrostatically repels the electron, pushing probability density outward"
    - "There is a normalization convention that sets the wavefunction to zero at the origin"
  answer: 1
  explanation: "The probability of finding the electron in a thin shell between r and r + dr is the radial probability density P(r) = r²|R(r)|² times dr — not |R(r)|² times dr. The r² factor comes from the surface area of the spherical shell (4πr²). At r = 0, the shell has zero area, so P(r) = 0 regardless of how large |R(r)|² is there. The peak of P(r) is pushed outward to a₀, where the product of large wavefunction amplitude and large shell area is maximized. This is purely a geometric effect, not physics that 'pushes' the electron away from the nucleus."

- question: "The 2s and 2p orbitals have the same principal quantum number (n = 2), but 2s electrons can 'penetrate' closer to the nucleus than 2p electrons. What accounts for this difference?"
  type: multiple-choice
  options:
    - "2s electrons have higher energy than 2p electrons, giving them more kinetic energy to overcome nuclear repulsion"
    - "The angular momentum quantum number ℓ creates a centrifugal-like barrier term ℓ(ℓ+1)/r² in the effective radial potential that suppresses near-nucleus probability for 2p electrons"
    - "The 2s orbital has more radial nodes than 2p, forcing its probability outward toward larger r"
    - "2p electrons are heavier due to carrying angular momentum, increasing their effective mass near the nucleus"
  answer: 1
  explanation: "In the effective radial potential, angular momentum contributes a term ℓ(ℓ+1)ℏ²/(2mr²) that acts like a centrifugal barrier, repelling radial probability away from r = 0 for any ℓ > 0. For 2p (ℓ=1), this barrier is nonzero, suppressing probability near the nucleus. For 2s (ℓ=0), there is no such barrier, so the 2s wavefunction can reach the nucleus. This penetration means 2s electrons experience more of the nuclear charge (less shielding by inner electrons), which lowers their energy below 2p in multi-electron atoms — driving the energy-level splitting that underlies the periodic table."

- question: "The Bohr radius a₀ ≈ 0.53 Å is the most probable electron-nucleus distance for most hydrogen orbitals (most values of n and ℓ)."
  type: true-false
  answer: false
  explanation: "The Bohr radius a₀ is the most probable radius only for the 1s (n=1, ℓ=0) orbital, where the radial probability density P(r) = r²|R(r)|² peaks at exactly a₀. For excited states (higher n), the peak of P(r) moves to larger radii — roughly n²a₀ for states with ℓ = n−1. This is why electrons in higher shells are farther from the nucleus, have lower ionization energies, and are more available for chemical bonding. The Bohr model accidentally got the most probable radius right for the ground state."

- question: "For the 1s hydrogen orbital, the radial probability density P(r) = r²|R(r)|² equals zero at r = 0, even though the wavefunction amplitude |R(r)|² is nonzero there."
  type: true-false
  answer: true
  explanation: "At r = 0, the factor r² = 0, so P(r) = r² × |R(r)|² = 0, regardless of the nonzero value of |R(r)|². The physical interpretation: the probability of finding the electron in a shell of vanishing thickness at r = 0 is zero because the shell has zero volume. This is purely geometric. The wavefunction *amplitude* is nonzero at the nucleus (s orbitals have nonzero electron density at the nucleus, which matters for hyperfine structure in atomic physics), but the *probability of finding the electron in a shell* there is zero."

- question: "Explain why the most probable radius for the hydrogen 1s electron is NOT where the wavefunction amplitude |R(r)|² is largest, and what quantity must instead be maximized to find the most probable radius."
  type: short-answer
  answer: "The probability of finding the electron in a thin shell at radius r is proportional to the shell's volume, which is 4πr²dr. The relevant quantity is the radial probability density P(r) = r²|R(r)|², not |R(r)|² alone. For 1s, |R(r)|² is maximum at r = 0 (the wavefunction peaks at the nucleus), but P(r) = 0 there because the shell area r² = 0. The most probable radius is where P(r) — the product of large wavefunction amplitude and large shell area — is maximized. For 1s, this occurs at r = a₀, the Bohr radius."
  explanation: "This is one of the most important distinctions in quantum mechanics and is often missed by students familiar with the Bohr model. The Bohr model treats the electron as orbiting at a fixed radius; quantum mechanics gives a probability distribution. The most probable radius is a property of the radial *probability density* P(r), not the wavefunction itself. The r² geometric factor is what causes these to differ and is why even for the simplest orbital, finding the electron requires integrating over spherical shells rather than reading off the wavefunction amplitude."
```

## Explainer

From solving the Schrödinger equation for hydrogen, you know that the full wavefunction ψ_{n,ℓ,m}(r,θ,φ) separates into a radial part R_{n,ℓ}(r) and an angular part Y_ℓ^m(θ,φ). The angular parts — the spherical harmonics — determine the shape of the orbital (s, p, d...) and the orientation of its lobes. The **radial wavefunction** R_{n,ℓ}(r) determines something equally important but less visually dramatic: how the probability amplitude depends on distance from the nucleus. Everything about atomic size, average distances, and radial structure is encoded in R_{n,ℓ}(r).

The probability of finding the electron in a thin shell between r and r + dr is not simply |R(r)|²dr — there is a crucial geometric factor. A shell of radius r has surface area 4πr², so the volume element in the shell is 4πr²dr. The **radial probability density** is therefore P(r) = r²|R(r)|², and the most probable radius is where this — not |R(r)|² alone — is maximum. The distinction matters because |R(r)|² is largest right at the nucleus for s orbitals (ℓ = 0), where it is nonzero, while P(r) = r²|R(r)|² is zero at r = 0 because the shell area vanishes. The peak of P(r) is pulled outward from the nucleus: for the 1s state, it occurs exactly at the Bohr radius a₀ ≈ 0.53 Å, confirming that the Bohr model correctly predicted the most probable distance even though its underlying picture was wrong.

The structure of the radial wavefunction becomes richer for higher quantum numbers. For a given principal quantum number n and orbital angular momentum quantum number ℓ, there are (n − ℓ − 1) **radial nodes** — values of r where R(r) = 0 and the wavefunction changes sign. For the 1s orbital (n=1, ℓ=0), there are zero nodes; the 2s (n=2, ℓ=0) has one node; the 3s has two. The 2p (n=2, ℓ=1) has zero radial nodes because ℓ takes one of the available quantum numbers away. Radial nodes slice the electron distribution into concentric shells of alternating sign — the electron has significant probability in multiple radially separated regions. These nodes are the radial analogue of the nodal planes in angular wavefunctions and represent regions of destructive quantum interference.

The interplay between n and ℓ controls atomic size and chemical behavior. Higher n pushes the peak of P(r) to larger r: the 2s electron is on average much farther from the nucleus than the 1s electron, which is why the second shell's electrons are more easily ionized and more available for bonding. Higher ℓ at the same n also shifts probability outward because angular momentum creates a centrifugal-like barrier near the nucleus (a term ℓ(ℓ+1)/r² in the effective potential). This is why 2s electrons have some probability close to the nucleus (they can "penetrate" the inner shell and feel more nuclear charge) while 2p electrons are more shielded — a difference that drives the splitting of energy levels in multi-electron atoms and the buildup of the periodic table.
