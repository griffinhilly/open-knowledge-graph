---
id: brunnauer-emmett-teller-bET-theory
title: BET Theory and Multilayer Adsorption
domain: chemistry
course: physical-chemistry
prerequisites:
- id: langmuir-adsorption-model
  type: hard
- id: adsorption-thermodynamics-entropy
  type: hard
tags:
- bet
- adsorption
- multilayer
- surface-area
stage: advanced
status: draft
---

# BET Theory and Multilayer Adsorption

## Core Idea
The Brunauer-Emmett-Teller (BET) theory extends the Langmuir model to multilayer adsorption by assuming each adsorbed layer exhibits properties of bulk liquid (except the first layer, which binds to surface). This allows calculation of surface area from nitrogen adsorption isotherms, a standard characterization technique for porous materials and catalysts. BET surface area differs from geometric surface area when pores are present.

## Explainer

From the Langmuir adsorption model, you understand how gas molecules bind to a surface: each surface site can hold one molecule, and coverage increases with pressure until a monolayer saturates the surface. But real adsorption isotherms often do not level off cleanly at a monolayer — instead, the amount adsorbed keeps rising as molecules begin to stack on top of already-adsorbed molecules. The **BET theory** (Brunauer, Emmett, and Teller, 1938) extends the Langmuir framework to account for this **multilayer adsorption**, and it has become the standard method for measuring surface areas of catalysts, adsorbents, and porous materials.

The central assumption of BET theory is that the first layer of molecules adsorbs onto the surface with a characteristic energy of adsorption (related to the molecule-surface interaction), while each subsequent layer adsorbs with the energy of **liquefaction** — essentially, molecules in the second layer and beyond are sticking to other adsorbed molecules, not to the surface itself. This is a natural extension of Langmuir's site-based thinking: the first layer fills by the same equilibrium logic, but now each occupied site can serve as a new "surface" for the next layer. The result is the BET equation, which relates the amount adsorbed to the relative pressure P/P₀ (where P₀ is the saturation vapor pressure) and two parameters: the monolayer capacity (Vm) and the BET constant C, which reflects the strength of the surface-molecule interaction relative to molecule-molecule interactions.

In practice, you measure an adsorption isotherm by exposing your material to nitrogen gas at 77 K (liquid nitrogen temperature) and recording how much gas adsorbs at each pressure. The BET equation is then linearized: plotting P/[V(P₀ − P)] versus P/P₀ gives a straight line in the relative pressure range of roughly 0.05 to 0.35. The slope and intercept yield Vm and C. From Vm — the volume of gas needed to form exactly one complete monolayer — you calculate the **BET surface area** by multiplying the number of adsorbed molecules by the cross-sectional area of a single nitrogen molecule (0.162 nm²). This procedure is so standardized that "BET surface area" is essentially synonymous with surface area measurement in materials science.

The BET model has important limitations inherited from and beyond its Langmuir ancestry. It assumes a uniform, flat surface (no pore-size effects on layering), treats all layers beyond the first as identical to bulk liquid, and breaks down at very low pressures (where surface heterogeneity matters) and very high pressures (where capillary condensation in pores dominates). For microporous materials like zeolites, where pore widths are comparable to molecular diameters, the BET surface area can be physically misleading — it reports a number, but the concept of layered adsorption does not apply in pores only a few molecules wide. Despite these caveats, BET analysis remains indispensable because it provides a reproducible, comparable measure of available surface across vastly different materials.
