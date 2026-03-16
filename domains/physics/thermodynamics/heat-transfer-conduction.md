---
id: heat-transfer-conduction
title: 'Heat Transfer: Conduction'
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: thermal-expansion
  type: soft
builds-toward:
- heat-transfer-convection
- heat-transfer-radiation
tags:
- conduction
- heat-transfer
- thermal-conductivity
- fourier-law
stage: concrete-operations
status: validated
---
# Heat Transfer: Conduction

## Core Idea
Conduction is the transfer of heat through direct molecular collisions without bulk movement of matter. The rate of heat flow is given by Fourier's law: P = kA(ΔT/L), where k is the thermal conductivity of the material, A is cross-sectional area, ΔT is the temperature difference, and L is thickness. Metals are excellent conductors because free electrons transport energy efficiently; insulators like wood and fiberglass have low k values.

## How It's Best Learned
Compare thermal conductivities of materials and interpret why a metal doorknob feels colder than a wooden door at the same room temperature. Solve steady-state conduction problems in layered materials (R-value problems) by analogy with electrical resistance in series.

## Common Misconceptions
- A metal object does not have a lower temperature than a wooden one at the same room temperature — it just conducts heat away from your hand faster, making it feel colder.
- Thermal conductivity and electrical conductivity are correlated in metals but not identical.

## Explainer

You know from thermal equilibrium that heat flows from hot regions to cold regions until temperatures equalize. Conduction is the microscopic mechanism by which this happens inside a solid or stationary fluid: energetic molecules collide with their neighbors and pass kinetic energy along, without any bulk flow of matter. The quantitative description is **Fourier's Law**: the rate of heat flow P (in watts) through a material is proportional to the temperature difference, the cross-sectional area, and the inverse of the thickness — P = kA(ΔT/L), where k is the **thermal conductivity** of the material.

The factor k is a material property that varies enormously: copper has k ≈ 400 W/m·K, while air has k ≈ 0.025 W/m·K — a factor of 16,000. This explains why a metal doorknob at 20°C feels cold while a wooden door at the same temperature feels neutral. Your hand is at 37°C; both objects are at 20°C and will extract heat from your hand. But copper extracts it 1,000× faster than wood, so your hand cools rapidly — which your nervous system interprets as "cold." The temperature is the same; the sensation is different because k is different.

Fourier's Law has a direct analogy with Ohm's Law for electricity: P (heat flow rate) corresponds to current I, temperature difference ΔT corresponds to voltage ΔV, and the **thermal resistance** R_th = L/(kA) corresponds to electrical resistance. For composite materials — like a wall made of plaster, insulation, and brick — thermal resistances in series simply add: R_total = R₁ + R₂ + R₃. This is the basis of **R-values** in building insulation: a higher R-value means higher thermal resistance, so less heat escapes in winter. Doubling the thickness doubles R; using a material with half the k also doubles R.

In steady state, the heat current is the same through every layer of a composite wall — just as current is the same through resistors in series. The temperature drops across each layer proportionally to its thermal resistance: most of the temperature drop occurs across the most resistive layer. This is exactly why adding a thin air gap (very low k but also very thin) contributes some insulation, while thick fiberglass batting (low k, large L) contributes much more. Understanding this layered resistance framework lets you design thermal systems — from building envelopes to heat sinks in electronics — using the same intuition you would apply to a resistor network.
