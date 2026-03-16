---
id: dielectric-susceptibility-constant
title: Dielectric Susceptibility and Permittivity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dielectric-materials-polarization
  type: hard
builds-toward:
- energy-density-electric-field
tags:
- susceptibility
- permittivity
- relative
stage: formal-systems
status: draft
---

# Dielectric Susceptibility and Permittivity

## Core Idea
Polarization is P = ε₀χₑE, where χₑ is electric susceptibility. The relative permittivity εᵣ = 1 + χₑ gives total field E = E₀/εᵣ inside dielectric. Capacitance with dielectric: C = εᵣε₀A/d.

## How It's Best Learned
Compare capacitance with and without dielectric. Measure field reduction and relate to susceptibility values in reference tables.

## Explainer

When you studied dielectric polarization, you learned that an electric field applied to an insulating material causes microscopic dipoles — either permanent molecular dipoles that align, or induced charge displacements — to line up with the field. The result is a net bound surface charge on the dielectric that partially cancels the free charges on the capacitor plates. **Electric susceptibility** χₑ (chi-sub-e) is the number that quantifies how strongly a material polarizes: the polarization field P is related to the applied field E by P = ε₀χₑE. A large χₑ means the material polarizes easily and creates a large opposing field; a small χₑ means the material barely responds.

The connection to the total field inside the material is direct. The bound surface charge creates a field that opposes the applied field, reducing the net field inside the dielectric. Accounting for both the free charge field and the opposing bound charge field gives a total field E = E₀/(1 + χₑ). The combination (1 + χₑ) appears so frequently that we give it a name: the **relative permittivity** εᵣ = 1 + χₑ, sometimes called the **dielectric constant**. Vacuum has χₑ = 0 and εᵣ = 1. Water has χₑ ≈ 79 and εᵣ ≈ 80, meaning water's dipoles polarize so strongly that the field inside water is reduced to about 1/80 of its free-space value — which is why water is such an effective solvent for ionic compounds.

The practical payoff for capacitors is immediate. A parallel-plate capacitor with no dielectric has C₀ = ε₀A/d. Insert a dielectric filling the gap and the field inside drops by a factor of εᵣ, which means the voltage V = Ed drops by the same factor for the same stored charge Q. Since C = Q/V, the capacitance increases to C = εᵣε₀A/d = εᵣC₀. The dielectric effectively allows more charge to be stored at the same voltage — it multiplies the capacitance by the dielectric constant. This is precisely why real capacitors are packed with ceramic, polymer, or electrolytic dielectric materials: a few grams of high-εᵣ material can replace what would otherwise require a much larger physical structure, and the field energy stored in the electric field U = ½CV² scales up accordingly.
