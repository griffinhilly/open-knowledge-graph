---
id: elastic-deformation-moduli
title: Elastic Deformation and Elastic Moduli
domain: engineering
course: materials-science
prerequisites:
- id: atomic-bonding-materials
  type: hard
- id: stress-strain-behavior
  type: hard
builds-toward:
- plastic-deformation-slip-systems
- yield-strength-tensile-properties
tags:
- elastic-deformation
- youngs-modulus
- stiffness
stage: formal-systems
status: draft
---

# Elastic Deformation and Elastic Moduli

## Core Idea
Elastic deformation is reversible distortion of the crystal structure under applied stress, where atoms are temporarily displaced from equilibrium positions and return when stress is removed. Young's modulus, shear modulus, and bulk modulus quantify material stiffness and are directly related to the strength and character of atomic bonding. Elastic moduli typically decrease with increasing temperature and can show significant anisotropy in non-cubic crystals.

## Explainer

From your study of stress-strain behavior, you know that when stress is plotted against strain, the initial region is linear and reversible — remove the load and the material returns to its original shape. The slope of that linear region is **Young's modulus** E, with units of GPa. From your study of atomic bonding, you now have the tools to understand where E comes from at the atomic scale and why different materials have vastly different stiffnesses.

Imagine two bonded atoms as a ball-and-spring pair. The spring represents the interatomic bond, and its stiffness is determined by the curvature of the potential energy well at the equilibrium spacing. A strong, narrow well (like a covalent or ionic bond) corresponds to a stiff spring; a shallow, wide well (like van der Waals interaction) corresponds to a soft spring. **Young's modulus is essentially the stiffness constant of the interatomic spring, scaled up from atomic dimensions to macroscopic dimensions.** Covalent diamonds have E ≈ 1,000 GPa because carbon-carbon bonds are extremely stiff. Steels are around 200 GPa (strong metallic bonds). Aluminum is 70 GPa (weaker metallic bonds, lighter atoms). Polymers range from 0.001 to 5 GPa because van der Waals forces between polymer chains are very soft. This hierarchy is entirely predictable from bonding type.

The three elastic moduli each probe a different mode of deformation. **Young's modulus** E governs uniaxial tension or compression. **Shear modulus** G governs distortion under shear stress. **Bulk modulus** K governs volumetric compression under hydrostatic pressure. For an isotropic material, these three are not independent: G = E / [2(1+ν)] and K = E / [3(1−2ν)], where ν is **Poisson's ratio** — the ratio of lateral contraction to axial elongation under tension. Most metals have ν ≈ 0.3, meaning if you stretch a rod by 1%, its diameter shrinks by about 0.3%.

Temperature dependence follows directly from the atomic model: at higher temperatures, atoms vibrate with greater amplitude, effectively sampling a wider region of the potential energy well. Because potential wells are asymmetric (repulsion rises more steeply than attraction falls), the average atomic spacing increases with temperature (thermal expansion), and the effective spring stiffness softens. This is why turbine blades operating at 1000°C must be designed with reduced modulus values, and why high-temperature materials such as refractory ceramics (alumina, zirconia) are valued precisely because their strong ionic/covalent bonds maintain stiffness at elevated temperatures. In non-cubic crystals like titanium or wood, the modulus is different in different crystallographic directions — a consequence of bond density varying with orientation. Recognizing this anisotropy prevents design errors when using single-crystal or textured polycrystalline materials.
