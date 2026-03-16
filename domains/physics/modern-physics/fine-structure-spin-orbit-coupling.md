---
id: fine-structure-spin-orbit-coupling
title: 'Fine Structure: Spin-Orbit Coupling and Doublet Splitting'
domain: physics
course: modern-physics
prerequisites:
- id: electron-spin-magnetic-moment
  type: hard
- id: relativistic-dynamics-acceleration
  type: soft
- id: fine-structure-hydrogen
  type: soft
builds-toward:
- hyperfine-structure-nuclear-magnetic
tags:
- spin-orbit-coupling
- relativistic-effects
- atomic-structure
stage: advanced
status: draft
---

# Fine Structure: Spin-Orbit Coupling and Doublet Splitting

## Core Idea
The spin-orbit interaction arises from relativistic effects: an electron moving through an electric field E experiences a magnetic field B that couples to its spin. The energy shift is proportional to S·L = (J² − L² − S²)/2, causing levels with the same (n,ℓ) but different j = ℓ ± 1/2 to split. The hydrogen 2p level splits into 2P₁/₂ and 2P₃/₂ states, confirming relativistic corrections.

## How It's Best Learned
Derive the spin-orbit coupling energy from the relativistic interaction of spin magnetic moment with the electric field of the nucleus. Calculate splittings for hydrogen low-n states and compare with observed spectral line splitting.

## Common Misconceptions
Spin-orbit coupling is a relativistic effect, not explained by a classical spinning charge in a magnetic field. The coupling depends on how fast the electron orbits (higher ℓ means smaller effect in hydrogen). The term 'Thomas precession' refers to an essential relativistic correction in deriving the factor of 1/2.

## Explainer

You know that an electron has spin angular momentum **S** and an associated magnetic moment **μ_s** = −g_s μ_B **S**/ℏ. You also know that the hydrogen 2p level has orbital angular momentum **L** with quantum number ℓ = 1. The question is: do **S** and **L** interact? The answer is yes, and the mechanism is relativistic.

In the electron's rest frame, the proton is moving — and a moving charge produces not just an electric field but also a magnetic field. This magnetic field **B** felt by the electron is proportional to the electric field **E** of the nucleus crossed with the electron's velocity: **B** ~ **v** × **E**/c². The electron's spin magnetic moment sits in this field with energy −**μ_s** · **B**. Expanding this out, **v** × **E** is proportional to the orbital angular momentum **L** (since **L** = m **r** × **v** and **E** points radially), so the interaction energy is proportional to **S** · **L**. This is the **spin-orbit coupling term**.

There is a subtlety: a naive derivation gives H_SO = (e²/2m²c²r³) **S**·**L**, but the correct relativistic treatment introduces a factor of 1/2 from **Thomas precession** — a purely relativistic kinematic effect that arises because the electron's rest frame is non-inertial (it accelerates in a circular orbit). Without the Thomas factor the prediction would be twice the observed splitting. With it, the spin-orbit Hamiltonian is H_SO = (1/2)(e²/2m²c²r³) **S**·**L**.

To find the energy eigenvalues, use the identity **S**·**L** = (J² − L² − S²)/2, where **J** = **L** + **S** is the **total angular momentum**. The quantum numbers j, ℓ, s are good quantum numbers for the perturbed Hamiltonian, replacing mℓ and ms. For a 2p electron (ℓ=1, s=1/2), j can be 3/2 or 1/2. The expectation value of **S**·**L** = ℏ²[j(j+1) − ℓ(ℓ+1) − s(s+1)]/2 differs for the two j values, so the single 2p level splits into 2P₃/₂ and 2P₁/₂ states separated by a small energy. This **doublet splitting** is directly observed as the closely spaced pair of lines in the hydrogen spectrum, and its measured magnitude matches the relativistic spin-orbit prediction — one of the early confirmations that special relativity and quantum mechanics must be unified.
