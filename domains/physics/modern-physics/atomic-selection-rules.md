---
id: atomic-selection-rules
title: Selection Rules for Atomic Transitions
domain: physics
course: modern-physics
prerequisites:
- id: spectral-lines-transitions-wavelength
  type: hard
builds-toward:
- jj-coupling-atoms
tags:
- quantum
- spectroscopy
- transitions
stage: abstract-reasoning
status: draft
---

# Selection Rules for Atomic Transitions

## Core Idea
Not all transitions are equally probable; selection rules constrain allowed transitions. For electric dipole radiation: Δℓ = ±1 and Δmℓ = 0, ±1. These arise from conservation of angular momentum and the tensor properties of the dipole operator. Forbidden transitions can occur via weaker mechanisms (magnetic dipole, quadrupole), producing forbidden lines in spectra.

## Explainer

From your study of spectral lines and transitions, you know that atoms emit photons when electrons drop to lower energy levels, with each photon's wavelength determined by the energy difference. But you may have noticed that not every conceivable transition actually appears in spectra — some lines that would be energetically allowed are simply absent or very weak. **Selection rules** explain which transitions are strongly allowed and which are suppressed, using conservation laws and quantum symmetry arguments.

The dominant mechanism for photon emission is **electric dipole radiation**: the oscillating electric dipole moment of the atom couples to the electromagnetic field. A photon carries angular momentum of exactly 1ℏ (photons are spin-1 particles). For the total angular momentum of the atom-plus-photon system to be conserved during emission, the atom's angular momentum must change by exactly 1ℏ. Since the orbital angular momentum quantum number ℓ characterizes angular momentum in units of ℏ, the rule is **Δℓ = ±1**: the electron must move between subshells differing by one unit. A transition from 2p to 1s (ℓ: 1→0) is allowed; from 2s to 1s (ℓ: 0→0) is not, because the emitted photon cannot carry zero angular momentum. The rule **Δmℓ = 0, ±1** governs the projection along the quantization axis, corresponding to whether the photon is linearly or circularly polarized.

These rules arise mathematically from the requirement that the **transition matrix element** ⟨f|r|i⟩ (the dipole moment integrated against the wavefunctions of initial and final states) be nonzero. The position operator r has odd parity, so the initial and final states must have opposite parity for the integral to survive — since parity of atomic orbitals goes as (−1)^ℓ, this requires Δℓ to be odd, and Δℓ = ±1 is the leading term. Transitions with Δℓ = 0 or |Δℓ| > 1 have zero electric dipole matrix elements and are called **electric dipole forbidden**.

Forbidden does not mean impossible — it means the electric dipole mechanism is unavailable, and weaker mechanisms must take over. **Magnetic dipole** and **electric quadrupole** transitions can occur with Δℓ = 0 or Δℓ = ±2, but they are roughly 10⁵ to 10⁸ times slower than allowed transitions. In laboratory settings, atoms in excited states that can only decay via forbidden transitions have long radiative lifetimes; in dense gases, collisions depopulate them first and the lines never appear. But in **nebulae** — where densities are so low that collisions are rare — forbidden lines are some of the brightest features in the optical spectrum. The green lines of ionized oxygen in planetary nebulae, for instance, are forbidden transitions invisible in any lab but dominant in space. Selection rules thus connect quantum symmetry to what you actually observe when you look at a spectrum.
