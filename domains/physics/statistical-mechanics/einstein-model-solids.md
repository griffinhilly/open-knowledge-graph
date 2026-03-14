---
id: einstein-model-solids
title: Einstein Model of Solids
domain: physics
course: statistical-mechanics
prerequisites:
- id: heat-capacity-of-gases
  type: hard
- id: partition-function-definition
  type: soft
builds-toward:
- debye-model-solids
tags:
- solids
- phonons
- heat-capacity
stage: advanced
status: draft
---

# Einstein Model of Solids

## Core Idea
The Einstein model treats N atoms as 3N independent harmonic oscillators all with frequency ω_E. Heat capacity C_V = 3Nk (Θ_E/T)^2 exp(−Θ_E/T) / [exp(−Θ_E/T)−1]^2, where Θ_E = ℏω_E/k. It captures the high-temperature limit C_V = 3R but predicts C_V → 0 too steeply at low T, lacking the T^3 behavior of the Debye model.
