---
id: heat-transfer-radiation
title: 'Heat Transfer: Radiation'
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: electromagnetic-waves
  type: soft
builds-toward:
- carnot-efficiency
tags:
- radiation
- heat-transfer
- stefan-boltzmann
- blackbody
- emissivity
stage: formal-systems
status: draft
---

# Heat Transfer: Radiation

## Core Idea
Thermal radiation is energy emitted as electromagnetic waves by any object with temperature above absolute zero; it requires no medium and can travel through vacuum. The power radiated by an ideal blackbody follows the Stefan-Boltzmann law: P = σAT⁴, where σ = 5.67 × 10⁻⁸ W/m²K⁴. Real objects emit P = εσAT⁴, where ε is the emissivity (0 to 1). The net power exchanged between an object and its environment is P_net = εσA(T⁴ - T_env⁴).

## How It's Best Learned
Explore how the T⁴ dependence makes radiation dominant at high temperatures. Compare how dark (high ε) versus shiny (low ε) surfaces absorb and emit radiation differently — this explains why matte black objects heat up faster in sunlight.

## Common Misconceptions
- All objects both emit and absorb thermal radiation simultaneously — in equilibrium they emit and absorb at equal rates.
- Radiation is not limited to visible light; most thermal radiation from room-temperature objects is infrared.
