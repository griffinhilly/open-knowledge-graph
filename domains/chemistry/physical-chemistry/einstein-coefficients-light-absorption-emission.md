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

## Explainer

From electronic spectroscopy and selection rules, you know that molecules absorb photons to jump between quantized energy levels and that not all transitions are allowed. The Einstein coefficients put this picture on a quantitative footing by assigning a specific rate to each type of photon process. There are exactly three ways a molecule can exchange energy with a radiation field, and each has its own coefficient.

**Absorption** (coefficient B₁₂) is the process you are most familiar with: a molecule in a lower state (level 1) absorbs a photon of the right frequency and jumps to a higher state (level 2). The rate of absorption is proportional to both the number of molecules in the lower state and the **radiation energy density** ρ(ν) at the transition frequency: rate = B₁₂ · N₁ · ρ(ν). **Stimulated emission** (coefficient B₂₁) is the reverse: an incoming photon of the right frequency triggers a molecule in the upper state to drop down, emitting a second photon identical to the first. Its rate has the same form: rate = B₂₁ · N₂ · ρ(ν). Both of these processes require the radiation field to be present — no photons, no absorption or stimulated emission.

**Spontaneous emission** (coefficient A₂₁) is different: a molecule in the excited state drops to the lower state and emits a photon even without any external radiation present. Its rate depends only on how many molecules are in the upper state: rate = A₂₁ · N₂. This is the process responsible for fluorescence and the glow of hot objects. Einstein showed that all three coefficients are related by requiring that, at thermal equilibrium, absorption and emission must balance to reproduce the Planck blackbody radiation law. This yields the fundamental relation A₂₁/B₂₁ = 8πhν³/c³, which reveals that spontaneous emission becomes overwhelmingly dominant at high frequencies (UV and beyond) because of the ν³ dependence.

The practical significance of these coefficients is that they bridge quantum mechanics and laboratory measurements. The B₁₂ coefficient is directly proportional to the **molar absorptivity** (extinction coefficient) that you measure in a UV-Vis experiment, while A₂₁ determines the **radiative lifetime** of an excited state — the average time a molecule stays excited if spontaneous emission is the only decay channel. For non-degenerate levels, B₁₂ = B₂₁, meaning absorption and stimulated emission are equally probable per molecule. This symmetry is the foundation of laser operation: if you can create a **population inversion** (N₂ > N₁), stimulated emission dominates over absorption, and the medium amplifies light rather than absorbing it.
