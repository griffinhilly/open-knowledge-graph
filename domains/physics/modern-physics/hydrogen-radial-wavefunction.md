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
status: draft
---

# Radial Wavefunctions and Probability Distributions in Hydrogen

## Core Idea
The radial wavefunction R(r) describes how the electron probability amplitude varies with distance from the nucleus. The radial probability density P(r) = r²|R(r)|² peaks at the most probable radius, which for the 1s orbital is the Bohr radius a₀ ≈ 0.53 Å. Higher-n and higher-ℓ states have wavefunctions peaked at larger radii and may have nodes (radial zeros) where the wavefunction changes sign.

## How It's Best Learned
Plot radial wavefunctions and radial probability densities for low quantum numbers. Identify the most probable radius for each state. Understand the physical meaning of nodes and relate to the number of radial nodes = n − ℓ − 1.

## Common Misconceptions
The most probable radius is not where the wavefunction amplitude is largest (it's where r²|R(r)|² is largest). The Bohr radius a₀ is most probable only for the 1s state; for excited states, the most probable radius is larger.

## Explainer

From solving the Schrödinger equation for hydrogen, you know that the full wavefunction ψ_{n,ℓ,m}(r,θ,φ) separates into a radial part R_{n,ℓ}(r) and an angular part Y_ℓ^m(θ,φ). The angular parts — the spherical harmonics — determine the shape of the orbital (s, p, d...) and the orientation of its lobes. The **radial wavefunction** R_{n,ℓ}(r) determines something equally important but less visually dramatic: how the probability amplitude depends on distance from the nucleus. Everything about atomic size, average distances, and radial structure is encoded in R_{n,ℓ}(r).

The probability of finding the electron in a thin shell between r and r + dr is not simply |R(r)|²dr — there is a crucial geometric factor. A shell of radius r has surface area 4πr², so the volume element in the shell is 4πr²dr. The **radial probability density** is therefore P(r) = r²|R(r)|², and the most probable radius is where this — not |R(r)|² alone — is maximum. The distinction matters because |R(r)|² is largest right at the nucleus for s orbitals (ℓ = 0), where it is nonzero, while P(r) = r²|R(r)|² is zero at r = 0 because the shell area vanishes. The peak of P(r) is pulled outward from the nucleus: for the 1s state, it occurs exactly at the Bohr radius a₀ ≈ 0.53 Å, confirming that the Bohr model correctly predicted the most probable distance even though its underlying picture was wrong.

The structure of the radial wavefunction becomes richer for higher quantum numbers. For a given principal quantum number n and orbital angular momentum quantum number ℓ, there are (n − ℓ − 1) **radial nodes** — values of r where R(r) = 0 and the wavefunction changes sign. For the 1s orbital (n=1, ℓ=0), there are zero nodes; the 2s (n=2, ℓ=0) has one node; the 3s has two. The 2p (n=2, ℓ=1) has zero radial nodes because ℓ takes one of the available quantum numbers away. Radial nodes slice the electron distribution into concentric shells of alternating sign — the electron has significant probability in multiple radially separated regions. These nodes are the radial analogue of the nodal planes in angular wavefunctions and represent regions of destructive quantum interference.

The interplay between n and ℓ controls atomic size and chemical behavior. Higher n pushes the peak of P(r) to larger r: the 2s electron is on average much farther from the nucleus than the 1s electron, which is why the second shell's electrons are more easily ionized and more available for bonding. Higher ℓ at the same n also shifts probability outward because angular momentum creates a centrifugal-like barrier near the nucleus (a term ℓ(ℓ+1)/r² in the effective potential). This is why 2s electrons have some probability close to the nucleus (they can "penetrate" the inner shell and feel more nuclear charge) while 2p electrons are more shielded — a difference that drives the splitting of energy levels in multi-electron atoms and the buildup of the periodic table.
