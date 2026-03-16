---
id: virial-equation-and-intermolecular-forces
title: Virial Equation and Intermolecular Forces
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
- id: compressibility-factor-and-reduced-properties
  type: soft
tags:
- real-gases
- virial-expansion
- intermolecular-forces
stage: formal-systems
status: draft
---

# Virial Equation and Intermolecular Forces

## Core Idea
The virial equation (PV = nRT(1 + B/V + C/V² + ...)) corrects for deviations from ideal behavior. The virial coefficients (B, C, ...) depend on temperature and account for intermolecular forces. For modest pressures and densities, the B term dominates; it becomes more important as pressure increases.

## Explainer

The ideal gas law — PV = nRT — is the foundation you already know. It works beautifully for gases at low pressures and high temperatures, where molecules are far apart and rarely interact. But in the real world, molecules have size and they attract or repel each other. When gas molecules are compressed into smaller volumes, these effects become impossible to ignore. The **virial equation** is the systematic way to account for those deviations, and it does so by adding correction terms to the ideal gas law in a power series in 1/V.

The virial expansion is written PV = nRT(1 + B/V + C/V² + ...). Each term is a successive correction. The **second virial coefficient B** captures the effect of pairwise interactions between molecules — attraction at moderate distances and repulsion at very short distances (the Lennard-Jones potential describes this shape). When B is negative, attractions dominate and the gas is more compressed than the ideal law predicts; when B is positive, repulsions dominate. For most common gases near room temperature, B is small and negative. The **third virial coefficient C** accounts for three-body interactions, which only matter at very high densities; in most engineering problems C and higher terms are negligible.

The beauty of the virial expansion is its direct connection to molecular physics. Unlike the empirical Van der Waals equation, the virial coefficients can in principle be calculated from the intermolecular potential — the function describing how two molecules interact as a function of separation distance. This means macroscopic gas behavior (pressure, volume, temperature) is directly tied to the microscopic physics of molecular attraction and repulsion. The coefficients also depend on temperature: as temperature rises and molecules move faster, thermal energy overcomes intermolecular attraction and B tends toward less-negative values, eventually becoming positive at the **Boyle temperature**.

The compressibility factor Z = PV/nRT that you may have encountered gives the virial equation its most compact form: Z = 1 + B/V + C/V² + .... When volume is large (low pressure), all correction terms vanish and Z approaches 1, recovering ideal behavior. This is why the ideal gas law works at low pressures — it is simply the virial equation with all correction terms too small to matter. At high pressures, Z deviates significantly from 1, and the virial expansion (truncated at the B term) gives the first quantitative correction. The sign of that correction — whether Z is above or below 1 — tells you immediately whether repulsive or attractive forces dominate at that temperature and density.
