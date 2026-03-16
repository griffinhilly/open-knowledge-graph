---
id: radiative-convective-equilibrium
title: Radiative-Convective Equilibrium
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: adiabatic-processes
  type: hard
- id: first-law-of-thermodynamics
  type: soft
- id: radiation-heat-transfer-stefan-boltzmann
  type: soft
builds-toward:
- two-layer-energy-balance
- general-circulation-models
tags:
- radiative-transfer
- energy-balance
- atmospheric-structure
- climate-modeling
stage: advanced
status: draft
---

# Radiative-Convective Equilibrium

## Core Idea
Radiative-convective equilibrium describes how the atmosphere self-adjusts its temperature profile to balance radiative cooling with convective heat transport. The troposphere becomes statically unstable if it cools too rapidly with height, triggering convection that carries heat upward until a stable lapse rate is reached. This equilibrium profile is fundamental to understanding how the climate system responds to radiative perturbations.

## Explainer

From your study of radiative transfer, you know that the atmosphere absorbs and emits longwave radiation at every level, and that this radiative exchange tends to cool the middle troposphere while warming the surface. If radiation were the only process moving energy vertically, the resulting temperature profile — called the **radiative equilibrium profile** — would have an extremely steep lapse rate in the lower atmosphere, far steeper than what we actually observe. The surface would be scorching and the upper troposphere frigid. This is where your understanding of adiabatic processes becomes essential.

A steep lapse rate means that a parcel of air lifted even slightly would find itself warmer and less dense than its surroundings, making it buoyant. The atmosphere in radiative equilibrium is therefore **statically unstable**: it cannot maintain that temperature profile because convection spontaneously kicks in. Rising thermals and organized convective cells carry heat upward far more efficiently than radiation alone can in the lower atmosphere. This convective mixing adjusts the lapse rate toward the **adiabatic lapse rate** — roughly 6.5°C per kilometer in Earth's moist troposphere, much gentler than the radiative-only profile.

**Radiative-convective equilibrium (RCE)** is the balanced state that emerges when both processes operate together. In the lower troposphere, convection dominates the vertical heat transport and sets the lapse rate near the moist adiabat. In the upper troposphere and stratosphere, where the air is stable and dry, radiative transfer dominates and the temperature profile is determined by the balance of absorbed and emitted radiation. The boundary between these regimes roughly corresponds to the tropopause. Think of it as a division of labor: convection handles the heavy lifting below, radiation handles the fine-tuning above.

Why does this matter for climate? When you add greenhouse gases, the atmosphere's radiative cooling becomes less efficient — it takes a higher altitude (and therefore colder temperature) for outgoing longwave radiation to escape to space. The radiative part of the equilibrium shifts, but convection still enforces the same lapse rate in the troposphere. The result is that the entire tropospheric temperature profile lifts: the surface warms, the troposphere warms, and the stratosphere actually cools (because it radiates more efficiently to space with more CO₂). RCE is the simplest framework that captures this greenhouse warming mechanism, and it forms the conceptual backbone of every general circulation model used in climate projections.
