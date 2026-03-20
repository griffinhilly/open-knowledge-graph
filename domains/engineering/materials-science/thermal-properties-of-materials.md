---
id: thermal-properties-of-materials
title: Thermal Properties of Materials
domain: engineering
course: materials-science
prerequisites:
- id: heat-transfer-conduction
  type: hard
- id: crystal-structure-basics
  type: soft
- id: thermal-expansion
  type: soft
- id: specific-heat-capacity
  type: soft
- id: heat-capacity-calorimetry
  type: soft
builds-toward:
- heat-treatment-of-steels
tags:
- thermal-conductivity
- thermal-expansion
- heat-capacity
- thermal-properties
stage: advanced
status: validated
---

# Thermal Properties of Materials

## Core Idea
Thermal properties — heat capacity, thermal conductivity, and thermal expansion coefficient — govern how materials respond to temperature changes and heat flow. Heat capacity reflects the energy stored in atomic vibrations (phonons); for most solids above room temperature, it approaches 3R per mole of atoms (Dulong-Petit law). Thermal conductivity in metals is dominated by electron transport; in ceramics and polymers, by phonon transport, making them better insulators. The thermal expansion coefficient quantifies lattice dilation and must be matched between joined dissimilar materials to avoid thermal stress cracking. These properties drive materials selection for heat sinks, thermal barrier coatings, and precision instruments.

## How It's Best Learned
Compare thermal conductivity values across metals, ceramics, and polymers and explain the differences in terms of dominant heat carriers. Calculate thermal stress in a bimetallic strip from the expansion coefficient mismatch.

## Common Misconceptions
- Diamond has the highest thermal conductivity of any material (higher than copper) because of its exceptionally stiff covalent bonds enabling efficient phonon transport, despite being an electrical insulator.
- A lower thermal expansion coefficient is not always desirable — it depends on the application and whether the material must be matched to a substrate.

## Explainer

From your study of heat conduction, you know that temperature gradients drive heat flow, and from specific heat capacity, you know that different materials store different amounts of thermal energy per degree of temperature rise. Thermal properties of materials extend this picture by connecting macroscopic thermal behavior to atomic-scale physics — and the atomic picture explains why metals, ceramics, and polymers behave so differently from one another.

**Heat capacity** (or specific heat, J/kg·K) measures how much energy a material absorbs per unit mass per degree of temperature increase. In a solid, thermal energy is stored in atomic vibrations — the atoms oscillate around their equilibrium positions, and each vibrational mode stores energy. The **Dulong-Petit law** predicts that at sufficiently high temperatures, each atom contributes 3kT of energy regardless of what element it is, giving a molar heat capacity of 3R ≈ 25 J/mol·K. This is why most metals have similar molar heat capacities. The practical specific heat (per kg) differs because atomic mass varies — lighter atoms mean more atoms per kilogram, so materials like aluminum have higher specific heat per kilogram than heavier metals like lead, even though both approach 3R per mole.

**Thermal conductivity** (W/m·K) measures how efficiently a material transports heat. This is where material classes diverge dramatically. In metals, free electrons are the dominant heat carriers — the same electrons that carry electrical current also carry thermal energy, which is why electrical and thermal conductivity track together in metals (Wiedemann-Franz law). In ceramics and crystalline insulators, there are no free electrons, so heat must be carried by **phonons** — quantized lattice vibrations. Phonon transport is less efficient than electron transport, making ceramics and polymers thermal insulators relative to metals. Diamond is the striking exception: its extremely stiff covalent bonds and lightweight carbon atoms create phonons that travel exceptionally fast and scatter very little, giving thermal conductivity ~5× higher than copper despite being an electrical insulator.

**Thermal expansion** arises from an asymmetry in interatomic potential: atoms are easier to push apart than to push together, so as they vibrate more vigorously at higher temperature, their average separation increases. Materials with deep, steep potential wells (strong, stiff bonds) expand less — ceramics and refractory metals have low thermal expansion coefficients; polymers with weak van der Waals forces expand dramatically. The engineering consequence is **thermal stress**: when two bonded materials with different expansion coefficients are heated or cooled, each wants to expand or contract by a different amount but is constrained by the other. The resulting stress is σ = E · Δα · ΔT, where Δα is the mismatch in expansion coefficients and E is the elastic modulus. This drives the design of solder joints in electronics, ceramic coatings on metal turbine blades, and glass-to-metal seals in vacuum systems — all of which require careful matching of expansion coefficients to survive thermal cycling without cracking.
