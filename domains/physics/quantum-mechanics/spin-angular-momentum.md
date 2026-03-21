---
id: spin-angular-momentum
title: Spin Angular Momentum
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: spin-quantum-number
  type: soft
builds-toward:
- total-angular-momentum
tags:
- spin
- angular-momentum
stage: advanced
status: draft
---

# Spin Angular Momentum

## Core Idea
Spin is intrinsic angular momentum with no classical analog. Electrons have s = ½, obeying [Ŝ_i, Ŝ_j] = iℏ ε_{ijk} Ŝ_k. The spin magnetic moment couples to magnetic fields.

## Questions

```yaml
- question: "Silver atoms have one outer electron in an l = 0 orbital. In the Stern-Gerlach experiment, a beam of silver atoms was deflected into exactly two discrete spots. Why does this result require half-integer spin?"
  type: multiple-choice
  options:
    - "Two spots indicate that silver has two outer electrons, each contributing one unit of angular momentum"
    - "Since l = 0 means no orbital angular momentum, the two spots must come from an intrinsic angular momentum with 2s + 1 = 2 possible z-projections, requiring s = 1/2 — integer spin would give an odd number of spots or no splitting"
    - "Two spots appear whenever a beam is split by a magnetic field gradient, regardless of the angular momentum of the atoms"
    - "The two spots correspond to spin-up and spin-down electrons, and any electron will produce exactly two spots regardless of its orbital state"
  answer: 1
  explanation: "The number of spots equals 2s + 1 (the number of distinct m_s values). With l = 0, orbital angular momentum cannot explain the splitting. Two spots means 2s + 1 = 2, so s = 1/2. An s = 1 particle would give 3 spots; s = 0 would give 1 (no splitting). The experiment rules out all integer values of s and proves that half-integer angular momentum is a physical reality — not a mathematical curiosity."

- question: "Which statement best captures what it means to say an electron has spin s = 1/2?"
  type: multiple-choice
  options:
    - "The electron physically rotates about its own axis, and the rotation rate corresponds to half a full turn per unit time"
    - "The electron's intrinsic angular momentum is quantized, with z-component taking only values +ℏ/2 or −ℏ/2; this is a fundamental property with no classical rotating-object analog"
    - "The electron has half the angular momentum of a proton, which has spin 1"
    - "The electron orbit contributes angular momentum of ℏ/2 per revolution around the nucleus"
  answer: 1
  explanation: "Spin is not rotation. An electron is pointlike — it has no extended structure that could rotate. The 'spin' quantum number s = 1/2 is an intrinsic property like mass or charge, meaning it cannot be changed by any interaction. The mathematical structure is identical to orbital angular momentum (same commutator algebra), but the physical interpretation is fundamentally different: there is no classical picture of what is spinning."

- question: "The spin quantum number s = 1/2 for an electron is a fixed, unchangeable property, similar to its mass and charge."
  type: true-false
  answer: true
  explanation: "s is intrinsic — it characterizes the type of particle and cannot be altered by external fields, temperature, or any interaction. What can change is m_s (the spin projection along a chosen axis), which takes values +1/2 or −1/2. For example, a magnetic field or a measurement can flip an electron from spin-up to spin-down (changing m_s), but the value s = 1/2 is invariant."

- question: "Because orbital angular momentum and spin obey the same commutator algebra [Ĵ_i, Ĵ_j] = iℏ ε_{ijk} Ĵ_k, spin must take the same integer values (l = 0, 1, 2, ...) as orbital angular momentum."
  type: true-false
  answer: false
  explanation: "The commutator algebra alone allows any non-negative half-integer value (0, 1/2, 1, 3/2, ...). Orbital angular momentum is restricted to integers by an *additional* requirement: the spatial wavefunction must be single-valued under a 2π rotation (ψ must return to itself, not −ψ). Spin states live in a separate spin Hilbert space where no such single-valuedness constraint applies, so s = 1/2 is mathematically consistent. Nature uses this freedom: electrons, protons, and neutrons all have s = 1/2."

- question: "Why is spin called 'intrinsic' angular momentum, and why is the picture of an electron physically spinning on its axis incorrect?"
  type: short-answer
  answer: "Spin is 'intrinsic' because it is a permanent, unchangeable property of a particle — it does not arise from any motion or configuration and cannot be removed. The 'electron spinning' picture fails because the electron is a pointlike particle with no spatial extent, so there is nothing extended to rotate. Furthermore, if you tried to model the electron's observed magnetic moment as classical rotation, the surface of the electron would need to move faster than the speed of light. Spin is a purely quantum mechanical property with no classical analog."
  explanation: "This is one of the places where quantum mechanics simply cannot be understood by analogy to classical mechanics. The algebra of spin is the same as orbital angular momentum, which tempts people to imagine physical rotation. But the derivation of that algebra from commutation relations does not require any rotating object — it only requires the abstract structure of the operators. Spin is the clearest example of a quantum property that must be accepted on its own mathematical and experimental terms."
```

## Explainer

You already know from commutation relations that the algebra [L̂_i, L̂_j] = iℏ ε_{ijk} L̂_k completely determines what values orbital angular momentum can take: the magnitude squared is L² = ℏ²l(l+1) with l = 0, 1, 2, … and the z-component is m_l ℏ with m_l ranging in integer steps from −l to +l. Spin obeys exactly the same algebra — [Ŝ_i, Ŝ_j] = iℏ ε_{ijk} Ŝ_k — but with a crucial difference: the quantum number s need not be an integer. The algebraic derivation allows s to be any non-negative half-integer: 0, 1/2, 1, 3/2, …

For electrons (and protons, neutrons, and quarks), s = 1/2. This is an intrinsic property like mass or charge — you cannot change it by any interaction, and it has no classical analog. A spinning charged ball would give orbital angular momentum, but spin is not rotation of any extended object; the electron is pointlike. The two spin states are m_s = +1/2 (**spin-up**, often written |↑⟩ or |+⟩) and m_s = −1/2 (**spin-down**, |↓⟩ or |−⟩). The full quantum state of an electron requires specifying both its spatial wavefunction ψ(r) and its spin state — the total Hilbert space is a tensor product of the spatial and spin spaces.

Spin has a physical observable consequence through the **spin magnetic moment**: **μ_s** = −g_s μ_B **S**/ℏ, where μ_B = eℏ/2m_e is the Bohr magneton and g_s ≈ 2 is the electron's g-factor (the factor of 2 is a relativistic effect, predicted exactly by the Dirac equation and corrected to ≈ 2.002319… by quantum electrodynamics). In a magnetic field B along z, the interaction energy is −μ_z B = g_s μ_B m_s B, which splits the two spin states by ΔE = g_s μ_B B. This is the basis of **electron spin resonance (ESR)** and, for nuclear spins, **MRI**.

The Stern-Gerlach experiment provided the first direct evidence for spin. A beam of silver atoms — each with one outer electron in an l = 0 orbital, so no orbital angular momentum — was deflected into exactly two spots when passed through an inhomogeneous magnetic field. Classical physics predicts a continuous spread; quantum mechanics with s = 1/2 predicts exactly two deflections, corresponding to m_s = ±1/2. This 2s+1 = 2 splitting, with no s = 0 explanation possible, was the experimental proof of half-integer angular momentum. Spin is not a metaphor or approximation — it is a discrete, measurable property of particles, and its algebra is the same commutator structure you already know.


