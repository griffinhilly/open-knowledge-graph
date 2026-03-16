---
id: ideal-real-gas-equations-state
title: Ideal and Real Gas Behavior
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressibility-factor-generalized
  type: hard
- id: ideal-gas-law
  type: soft
builds-toward:
- gas-mixture-thermodynamics-daltons
- combustion-stoichiometry-energy-release
tags:
- ideal-gas
- real-gas
- equations
- compressibility
stage: advanced
status: draft
---

# Ideal and Real Gas Behavior

## Core Idea
The ideal gas law Pv = RT assumes negligible intermolecular forces and molecular volume; it fails near saturation and at high pressures. Real gases use compressibility factor Z = Pv/RT and generalized correlations (law of corresponding states) or specific equations (virial, van der Waals). Engineering thermodynamics requires switching between ideal-gas approximations and real-gas corrections based on operating conditions.

## Explainer

The ideal gas law Pv = RT is one of the most useful engineering approximations ever formulated — and like all approximations, its value comes from knowing exactly when it breaks down. You already know the ideal gas law from prerequisites, and you know the **compressibility factor** Z = Pv/RT, which equals 1 for an ideal gas and deviates from 1 when real-gas effects become significant. This topic is about building the intuition for those deviations and the equations engineers use to correct for them.

At the molecular level, the ideal gas model makes two simplifying assumptions: molecules have zero volume, and they exert no intermolecular forces on each other. Both assumptions are reasonable when molecules are far apart — that is, at low pressures and high temperatures where the gas is dilute. As pressure rises, molecules are squeezed together and their finite volume becomes significant: you cannot compress them below a certain minimum. As temperature falls near the saturation curve (or as pressure rises), intermolecular **van der Waals attractions** slow molecules down and pull them together, reducing the pressure below the ideal prediction. These two effects work in opposite directions: volume exclusion pushes Z above 1 (gas harder to compress than ideal); attractions pull Z below 1 (gas easier to compress than ideal). At moderate pressures, attractions often dominate first (Z < 1), while at very high pressures, volume exclusion wins (Z > 1).

The **van der Waals equation** (P + a/v²)(v − b) = RT captures both effects with two constants: *b* accounts for molecular volume (excluded volume correction), and *a/v²* is the pressure reduction due to intermolecular attractions. It is the simplest cubic equation of state and gives qualitative insight into liquid-vapor behavior — including why Z dips below 1 near saturation. More accurate engineering practice uses the **law of corresponding states**: when pressures and temperatures are expressed as reduced variables Pr = P/Pc and Tr = T/Tc (normalized by critical-point values), nearly all gases follow similar Z(Pr, Tr) surfaces. This is the basis for **generalized compressibility charts**, which let you estimate Z for any gas from its critical constants without knowing the specific molecular parameters.

When precision matters, engineers use **virial equations of state** — Z = 1 + B/v + C/v² + ... — which are rigorous power series expansions from statistical mechanics, with coefficients B, C, ... that depend on temperature and the gas species. The second virial coefficient B is the most important correction and is tabulated for common gases. At moderate densities, truncating after B is usually sufficient. For natural gas and petroleum applications, more sophisticated cubic equations (Peng-Robinson, Redlich-Kwong-Soave) are used, calibrated to match both phase equilibria and volumetric behavior across a wide range.

The practical engineering decision is knowing when to bother. As a rule of thumb, ideal-gas treatment is accurate to within 1% for Tr > 2 and Pr < 0.5. Near saturation, or for gases in high-pressure applications (hydrogen storage, supercritical CO₂ cycles, ammonia refrigeration), Z can deviate by 10–30% and real-gas corrections are mandatory. The compressibility factor is the universal diagnostic: check Z first, and if it differs meaningfully from 1.0 at your operating conditions, use the appropriate equation of state.
