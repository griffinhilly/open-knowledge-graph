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
stage: advanced
status: validated
---

# Selection Rules for Atomic Transitions

## Core Idea
Not all transitions are equally probable; selection rules constrain allowed transitions. For electric dipole radiation: Δℓ = ±1 and Δmℓ = 0, ±1. These arise from conservation of angular momentum and the tensor properties of the dipole operator. Forbidden transitions can occur via weaker mechanisms (magnetic dipole, quadrupole), producing forbidden lines in spectra.

## Questions

```yaml
- question: "A hydrogen atom is in the 2s excited state (n=2, ℓ=0). Why doesn't it rapidly decay to the 1s ground state (n=1, ℓ=0) via electric dipole radiation?"
  type: multiple-choice
  options:
    - "The energy difference between 2s and 1s is too small to produce a detectable photon"
    - "The 2s → 1s transition requires Δℓ = 0, which violates the electric dipole selection rule Δℓ = ±1 — the emitted photon must carry 1ℏ of angular momentum, which the atom cannot supply with this transition"
    - "The 2s state has no orbital angular momentum, so it cannot couple to the electromagnetic field at all"
    - "The 2s → 1s transition is forbidden because the principal quantum number change Δn = 1 is too small"
  answer: 1
  explanation: "Angular momentum must be conserved. A photon carries 1ℏ of angular momentum, so the atom must change its orbital angular momentum by exactly 1ℏ — requiring Δℓ = ±1. The 2s state has ℓ = 0 and the 1s state has ℓ = 0, so Δℓ = 0: the atom cannot supply the angular momentum the photon needs. The transition is electric dipole forbidden. The 2s state is therefore metastable, with a much longer lifetime than states that can decay via allowed transitions."

- question: "Why do forbidden spectral lines appear prominently in emission nebulae but are essentially unobservable in laboratory plasmas at similar temperatures?"
  type: multiple-choice
  options:
    - "Nebulae contain different elements than laboratory plasmas, so the forbidden lines come from exotic atoms not present in the lab"
    - "In nebulae, particle densities are so low that atoms in metastable states decay via the slow forbidden transitions before collisions can de-excite them; in lab plasmas, collisions occur far faster than the radiative decay"
    - "The high magnetic fields in nebulae relax the selection rules, allowing normally forbidden transitions to proceed rapidly"
    - "Forbidden lines are at infrared wavelengths that ground-based telescopes detect but lab spectrometers cannot"
  answer: 1
  explanation: "Forbidden transitions have radiative lifetimes roughly 10⁵–10⁸ times longer than allowed transitions — milliseconds to hours instead of nanoseconds. In a lab plasma, collisions happen on timescales of microseconds or less, so an atom in a metastable state is almost always collisionally de-excited before it can radiate. In nebulae, number densities may be 10⁴ particles/cm³ or less (vs. ~10¹⁹/cm³ in lab air), and the mean time between collisions is long enough that the slow radiative decay wins. The green lines of [O III] in planetary nebulae are a famous example."

- question: "A transition labeled 'electric dipole forbidden' can rarely occur under any circumstances."
  type: true-false
  answer: false
  explanation: "Electric dipole forbidden means the dominant electric dipole mechanism is unavailable — not that the transition is impossible. Weaker mechanisms (magnetic dipole, electric quadrupole, and higher multipoles) can still drive the transition, though they are roughly 10⁵–10⁸ times slower. 'Forbidden' in spectroscopy is a relative term: it names the suppression of one specific mechanism, not an absolute prohibition. Metastable states in nebulae exploit exactly this: the weak forbidden mechanism wins when collisions are rare enough."

- question: "The selection rule Δℓ = ±1 for electric dipole transitions arises from conservation of angular momentum: an emitted photon carries angular momentum of exactly 1ℏ, which must be supplied by a change in the atom's orbital angular momentum."
  type: true-false
  answer: true
  explanation: "This is the physical origin of the rule. Photons are spin-1 particles carrying angular momentum of 1ℏ. Total angular momentum (atom + photon) must be conserved during emission, so the atom's angular momentum must change by ±1ℏ. Since ℓ characterizes orbital angular momentum in units of ℏ, this requires Δℓ = ±1. The mathematical formalism — that the transition matrix element ⟨f|r|i⟩ vanishes unless initial and final states have opposite parity, requiring odd Δℓ — implements the same physical constraint."

- question: "Explain the physical origin of the Δℓ = ±1 selection rule. Why does the 2s → 1s transition in hydrogen violate it, and what is the physical fate of hydrogen atoms trapped in the 2s metastable state in a very low-density environment?"
  type: short-answer
  answer: "The selection rule arises from angular momentum conservation: photons carry 1ℏ of angular momentum, so the atom must change its orbital angular momentum by 1ℏ, requiring Δℓ = ±1. The 2s → 1s transition has Δℓ = 0 (both states have ℓ = 0), so it cannot proceed via electric dipole radiation — the atom cannot supply the angular momentum the photon requires. In a very low-density environment, a hydrogen atom in the 2s state can eventually decay by simultaneously emitting two photons (two-photon decay), which share the energy and angular momentum between them, allowing Δℓ = 0 with no single-photon angular momentum constraint. The 2s state has a lifetime of about 0.12 seconds via this mechanism — enormously long compared to typical allowed transitions (~nanoseconds)."
  explanation: "The two-photon decay of the 2s state is astrophysically important: it contributes to the diffuse emission of hydrogen nebulae and was historically significant for understanding atomic physics. The key conceptual point is that 'forbidden' means 'forbidden via the dominant mechanism' — exotic alternative decay channels always exist but are much slower."
```

## Explainer

From your study of spectral lines and transitions, you know that atoms emit photons when electrons drop to lower energy levels, with each photon's wavelength determined by the energy difference. But you may have noticed that not every conceivable transition actually appears in spectra — some lines that would be energetically allowed are simply absent or very weak. **Selection rules** explain which transitions are strongly allowed and which are suppressed, using conservation laws and quantum symmetry arguments.

The dominant mechanism for photon emission is **electric dipole radiation**: the oscillating electric dipole moment of the atom couples to the electromagnetic field. A photon carries angular momentum of exactly 1ℏ (photons are spin-1 particles). For the total angular momentum of the atom-plus-photon system to be conserved during emission, the atom's angular momentum must change by exactly 1ℏ. Since the orbital angular momentum quantum number ℓ characterizes angular momentum in units of ℏ, the rule is **Δℓ = ±1**: the electron must move between subshells differing by one unit. A transition from 2p to 1s (ℓ: 1→0) is allowed; from 2s to 1s (ℓ: 0→0) is not, because the emitted photon cannot carry zero angular momentum. The rule **Δmℓ = 0, ±1** governs the projection along the quantization axis, corresponding to whether the photon is linearly or circularly polarized.

These rules arise mathematically from the requirement that the **transition matrix element** ⟨f|r|i⟩ (the dipole moment integrated against the wavefunctions of initial and final states) be nonzero. The position operator r has odd parity, so the initial and final states must have opposite parity for the integral to survive — since parity of atomic orbitals goes as (−1)^ℓ, this requires Δℓ to be odd, and Δℓ = ±1 is the leading term. Transitions with Δℓ = 0 or |Δℓ| > 1 have zero electric dipole matrix elements and are called **electric dipole forbidden**.

Forbidden does not mean impossible — it means the electric dipole mechanism is unavailable, and weaker mechanisms must take over. **Magnetic dipole** and **electric quadrupole** transitions can occur with Δℓ = 0 or Δℓ = ±2, but they are roughly 10⁵ to 10⁸ times slower than allowed transitions. In laboratory settings, atoms in excited states that can only decay via forbidden transitions have long radiative lifetimes; in dense gases, collisions depopulate them first and the lines never appear. But in **nebulae** — where densities are so low that collisions are rare — forbidden lines are some of the brightest features in the optical spectrum. The green lines of ionized oxygen in planetary nebulae, for instance, are forbidden transitions invisible in any lab but dominant in space. Selection rules thus connect quantum symmetry to what you actually observe when you look at a spectrum.
