---
id: transport-phenomena-gases
title: Transport Properties of Gases
domain: chemistry
course: physical-chemistry
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: maxwell-boltzmann-distribution
  type: hard
- id: rms-speed-and-kinetic-energy
  type: soft
builds-toward:
- diffusion-and-ficks-laws
tags:
- viscosity
- thermal-conductivity
- diffusion
- mean-free-path
- collision-diameter
stage: advanced
status: draft
---

# Transport Properties of Gases

## Core Idea
Transport properties describe how momentum (viscosity), energy (thermal conductivity), and matter (diffusion) move through gases. All three are governed by molecular collisions characterized by the mean free path λ = 1/(√2·π·d²·N/V) and the mean speed c̄ = (8kT/πm)^(1/2). Viscosity η = (1/3)ρc̄λ increases with temperature as √T (unlike liquids), because faster molecules carry momentum more effectively even as the mean free path shortens. Thermal conductivity κ = (1/3)ρc̄λC_V/M is proportional to η. Chapman-Enskog theory provides more accurate expressions using Lennard-Jones collision integrals that account for the real intermolecular potential.

## How It's Best Learned
Verify the √T temperature dependence of gas viscosity from kinetic theory, then compare to experimental data for N₂ and Ar. Observe that the predicted (η₁/η₂) = (m₁/m₂)^(1/2) mass ratio is approximately correct for isomers.

## Common Misconceptions
- Expecting gas viscosity to decrease with temperature (as liquids do); gas viscosity increases with T because momentum transport improves.
- Thinking all transport coefficients are independent; they are all related through the same mean free path and speed.
