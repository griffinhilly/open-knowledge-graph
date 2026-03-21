---
id: einstein-coefficients-light-absorption-emission
title: Einstein Coefficients for Light Absorption and Emission
domain: chemistry
course: physical-chemistry
prerequisites:
- id: selection-rules-spectroscopy
  type: hard
- id: electronic-spectroscopy-theory
  type: hard
builds-toward:
- fluorescence-quantum-yield-lifetime
tags:
- spectroscopy
- photon-processes
- quantum-mechanics
stage: advanced
status: draft
---

# Einstein Coefficients for Light Absorption and Emission

## Core Idea
Einstein coefficients A₂₁ (spontaneous emission), B₂₁ (stimulated emission), and B₁₂ (absorption) relate rates of quantum transitions to photon density. These coefficients connect microscopic quantum mechanics to macroscopic phenomena like molar absorptivity. The relation A₂₁/B₂₁ = 8πhν³/c³ emerges from thermodynamic equilibrium arguments.

## Questions

```yaml
- question: "A fluorescent molecule has absorbed a photon and is now in an excited electronic state. It is placed in a completely dark enclosure with no external radiation. Which process can still occur?"
  type: multiple-choice
  options:
    - "Spontaneous emission — the molecule emits a photon and returns to the ground state with no radiation field required"
    - "Stimulated emission — an incoming photon triggers the transition, but since the enclosure is dark, no emission can occur"
    - "Absorption — the molecule can absorb another photon from the vacuum fluctuations in the enclosure"
    - "Neither emission nor absorption — all three Einstein processes require an external photon field to function"
  answer: 0
  explanation: "Spontaneous emission (coefficient A₂₁) is the only Einstein process that does not require an external radiation field. Its rate equals A₂₁·N₂ — proportional only to the number of molecules in the excited state, with no dependence on radiation density ρ(ν). Stimulated emission (B₂₁) and absorption (B₁₂) both have rate expressions containing ρ(ν) and therefore require photons to be present. The everyday phenomenon of fluorescence — objects glowing in the dark after prior light exposure — is precisely spontaneous emission operating with no external radiation field."

- question: "Why is achieving X-ray laser operation far more technologically difficult than visible-light laser operation, even when population inversion can in principle be created at both wavelengths?"
  type: multiple-choice
  options:
    - "The A₂₁/B₂₁ ratio scales as ν³, so at X-ray frequencies spontaneous emission is overwhelmingly faster than stimulated emission, making it nearly impossible to build up coherent amplification"
    - "X-ray photons violate the selection rules that allow stimulated emission, so only spontaneous processes are permitted at those frequencies"
    - "Population inversion is thermodynamically forbidden at X-ray frequencies because the excited-state energy exceeds the thermal energy of the medium"
    - "B₂₁ becomes negative at high frequencies, meaning stimulated emission actively competes against population inversion"
  answer: 0
  explanation: "The fundamental relation A₂₁/B₂₁ = 8πhν³/c³ shows that spontaneous emission grows as the cube of frequency relative to stimulated emission. At X-ray frequencies (ν ~ 10¹⁸ Hz), A₂₁ is enormous — excited molecules decay spontaneously in femtoseconds, far faster than stimulated amplification can build up. To achieve X-ray lasing, population inversion must be created and maintained on timescales shorter than this spontaneous lifetime, requiring ultra-intense ultrashort pump pulses (e.g., free-electron lasers). At radio frequencies the same relation holds in reverse: A₂₁ ≈ 0, spontaneous emission is negligible, and coherent stimulated processes dominate naturally."

- question: "For two non-degenerate quantum energy levels, the Einstein coefficient for absorption B₁₂ equals the coefficient for stimulated emission B₂₁."
  type: true-false
  answer: true
  explanation: "Einstein derived this symmetry from requiring that, at thermal equilibrium, absorption and emission balance to reproduce the Planck blackbody radiation law. For non-degenerate levels, B₁₂ = B₂₁: a photon of the right frequency is equally likely to stimulate absorption (lower→upper state) as to stimulate emission (upper→lower state) per molecule in the relevant state. In ordinary matter absorption dominates not because B₁₂ > B₂₁, but because the ground state population N₁ far exceeds the excited population N₂ at thermal equilibrium. Population inversion (N₂ > N₁) is required to flip this balance and achieve net amplification."

- question: "In a laser medium at thermal equilibrium — with no pumping — stimulated emission dominates over absorption because B₁₂ equals B₂₁ and both processes are equally probable."
  type: true-false
  answer: false
  explanation: "Equal B coefficients mean equal probability *per molecule in the relevant state*, but net rates depend on both the coefficient and the population. At thermal equilibrium, the Boltzmann distribution ensures the lower state is always more populated than the upper (N₁ > N₂ for any finite temperature). So absorption rate (∝ B₁₂·N₁·ρ) exceeds stimulated emission rate (∝ B₂₁·N₂·ρ) because N₁ > N₂. For stimulated emission to dominate — enabling laser amplification — the system must be driven far from equilibrium by pumping to achieve population inversion N₂ > N₁. Equilibrium and amplification are mutually exclusive."

- question: "How do the Einstein coefficients connect the microscopic quantum mechanics of a molecule to macroscopic spectroscopic observables measured in the laboratory?"
  type: short-answer
  answer: "The absorption coefficient B₁₂ is proportional to the square of the transition dipole moment — the quantum mechanical quantity governing how strongly the molecule couples to light. Experimentally, B₁₂ is directly proportional to the molar absorptivity (extinction coefficient ε) measured by UV-Vis spectroscopy: a strongly allowed transition has large B₁₂ and large ε; a forbidden transition has small B₁₂ and small ε. The spontaneous emission coefficient A₂₁ determines the radiative lifetime τ_rad = 1/A₂₁ — the average time before an excited molecule emits spontaneously, which can be compared to the measured fluorescence lifetime to quantify non-radiative decay pathways."
  explanation: "This bridge between quantum mechanics and laboratory measurement is the core practical significance of Einstein's framework. By measuring ε experimentally, one calculates B₁₂; from A₂₁/B₂₁ = 8πhν³/c³ and B₁₂ = B₂₁, one derives A₂₁ and the radiative lifetime. Comparing the radiative lifetime to the observed fluorescence lifetime reveals how much excited-state population is lost to non-radiative processes (heat, intersystem crossing). The Einstein coefficients thus unify quantum transition theory, blackbody radiation, spectroscopy, and laser physics into a single coherent framework."
```

## Explainer

From electronic spectroscopy and selection rules, you know that molecules absorb photons to jump between quantized energy levels and that not all transitions are allowed. The Einstein coefficients put this picture on a quantitative footing by assigning a specific rate to each type of photon process. There are exactly three ways a molecule can exchange energy with a radiation field, and each has its own coefficient.

**Absorption** (coefficient B₁₂) is the process you are most familiar with: a molecule in a lower state (level 1) absorbs a photon of the right frequency and jumps to a higher state (level 2). The rate of absorption is proportional to both the number of molecules in the lower state and the **radiation energy density** ρ(ν) at the transition frequency: rate = B₁₂ · N₁ · ρ(ν). **Stimulated emission** (coefficient B₂₁) is the reverse: an incoming photon of the right frequency triggers a molecule in the upper state to drop down, emitting a second photon identical to the first. Its rate has the same form: rate = B₂₁ · N₂ · ρ(ν). Both of these processes require the radiation field to be present — no photons, no absorption or stimulated emission.

**Spontaneous emission** (coefficient A₂₁) is different: a molecule in the excited state drops to the lower state and emits a photon even without any external radiation present. Its rate depends only on how many molecules are in the upper state: rate = A₂₁ · N₂. This is the process responsible for fluorescence and the glow of hot objects. Einstein showed that all three coefficients are related by requiring that, at thermal equilibrium, absorption and emission must balance to reproduce the Planck blackbody radiation law. This yields the fundamental relation A₂₁/B₂₁ = 8πhν³/c³, which reveals that spontaneous emission becomes overwhelmingly dominant at high frequencies (UV and beyond) because of the ν³ dependence.

The practical significance of these coefficients is that they bridge quantum mechanics and laboratory measurements. The B₁₂ coefficient is directly proportional to the **molar absorptivity** (extinction coefficient) that you measure in a UV-Vis experiment, while A₂₁ determines the **radiative lifetime** of an excited state — the average time a molecule stays excited if spontaneous emission is the only decay channel. For non-degenerate levels, B₁₂ = B₂₁, meaning absorption and stimulated emission are equally probable per molecule. This symmetry is the foundation of laser operation: if you can create a **population inversion** (N₂ > N₁), stimulated emission dominates over absorption, and the medium amplifies light rather than absorbing it.
