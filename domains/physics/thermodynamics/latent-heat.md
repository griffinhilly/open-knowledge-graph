---
id: latent-heat
title: Latent Heat
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: specific-heat-capacity
  type: hard
builds-toward:
  - phase-diagrams
tags:
- latent-heat
- heat-of-fusion
- heat-of-vaporization
- phase-change
- Q=mL
stage: abstract-reasoning
status: validated
---
# Latent Heat

## Core Idea
Latent heat (L) is the heat per unit mass absorbed or released during a phase transition at constant temperature: Q = mL. The latent heat of fusion (L_f) applies to melting/freezing; the latent heat of vaporization (L_v) applies to boiling/condensation. For water: L_f = 334 kJ/kg and L_v = 2260 kJ/kg — vaporization requires about 7 times more energy than melting. The large L_v of water makes steam burns far more severe than boiling-water burns of equal mass.

## How It's Best Learned
Include latent heat in calorimetry problems: calculate the heat needed to convert 100 g of ice at −10°C to steam at 110°C, accounting for three temperature ramps (Q = mcΔT) and two phase transitions (Q = mL).

## Common Misconceptions
- Latent heat is not 'hidden' in a mysterious sense — the energy goes into breaking intermolecular bonds, increasing potential energy rather than kinetic energy.
- Condensation releases latent heat — when steam condenses on skin, it releases L_v ≈ 2260 kJ/kg, which is why steam scalds are so dangerous.

## Explainer

From specific heat capacity you know that adding heat to a substance normally raises its temperature via Q = mcΔT. Latent heat is what happens at the *boundary* between two phases: you add heat but the temperature does not change. This seems paradoxical until you remember what temperature measures — the average kinetic energy of molecules. During a phase transition, the energy you add goes entirely into overcoming intermolecular forces (potential energy), not into speeding molecules up. The temperature is stuck at the transition point until the phase change is complete, then resumes rising once all the material has transformed.

The word "latent" comes from Latin for "hidden" — the energy is stored in the changed molecular configuration and is not visible as temperature. When ice melts, you supply L_f = 334 kJ/kg to break the rigid hydrogen-bond lattice of ice into the more disordered liquid structure. When water boils, you supply a far larger L_v = 2260 kJ/kg to completely separate molecules from the liquid into gas phase — you are not just disrupting close-range order but pulling molecules far enough apart that intermolecular attractions become negligible. The seven-fold difference between L_v and L_f reflects how much more dramatically vaporization disrupts molecular arrangements compared to melting.

The formula Q = mL is deceptively simple to use once you have it, but the real skill is integrating it correctly into multi-stage calorimetry problems. Consider converting 100 g of ice at −10°C to steam at 110°C. There are five stages: (1) warming ice from −10°C to 0°C (Q = mcΔT with c_ice ≈ 2.09 kJ/kg·K), (2) melting at 0°C (Q = mL_f), (3) warming water from 0°C to 100°C (Q = mcΔT with c_water ≈ 4.18 kJ/kg·K), (4) vaporizing at 100°C (Q = mL_v), and (5) warming steam from 100°C to 110°C (Q = mcΔT with c_steam ≈ 2.01 kJ/kg·K). The vaporization step alone (226 kJ) accounts for nearly 80% of the total energy — dwarfing all the temperature-change stages combined.

The reverse process is equally important. Condensation releases L_v; freezing releases L_f. This is why steam burns are so much worse than boiling-water burns of equal mass: the steam condenses on your skin and instantly deposits 2260 kJ/kg *before* the resulting water even begins to cool. It is also why humid air feels so cold when wet: evaporation from your skin absorbs latent heat. Phase transitions are enormous energy stores and releases — a fact that drives weather (thunderstorms release latent heat of condensation that powers convection), engineering (steam engines, refrigerators, heat pumps all work by cycling a substance through phase transitions), and biology (sweating cools by latent heat of vaporization).
