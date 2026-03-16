---
id: thermal-expansion-linear-and-volumetric
title: 'Thermal Expansion: Linear and Volumetric'
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
tags:
- thermal-effects
- dimensional-changes
- materials
stage: formal-systems
status: draft
---

# Thermal Expansion: Linear and Volumetric

## Core Idea
Solids and liquids expand when heated. Linear expansion follows ΔL = αL₀ΔT; volumetric expansion follows ΔV = βV₀ΔT, where α and β are material-specific coefficients. Thermal stress arises when expansion is constrained, making this critical in engineering design.

## How It's Best Learned
Calculate dimensional changes for real materials over temperature ranges. Observe how different materials have vastly different expansion coefficients.

## Common Misconceptions
- Assuming linear and volumetric coefficients are always related by β ≈ 3α; this is only true for isotropic materials.
- Forgetting to use absolute temperature changes.

## Explainer

From your study of temperature and thermal equilibrium, you know that temperature measures the average kinetic energy of atoms and molecules. As a solid heats up, its atoms vibrate more energetically about their equilibrium positions. The key insight is that interatomic potentials are not perfectly symmetric — the repulsive wall at short distances is steeper than the attractive tail at large distances. This asymmetry means that as vibration amplitude increases, the average position of each atom shifts slightly outward. The result is macroscopic expansion: the material gets bigger as it gets hotter. This is the microscopic origin of thermal expansion.

For a slender rod of initial length L₀ heated by ΔT, the fractional change in length is proportional to ΔT: **ΔL = αL₀ΔT**, where **α** is the **linear thermal expansion coefficient**, measured in K⁻¹. The value of α is a material property determined by the shape of the interatomic potential: materials with stiff, deep potential wells (like diamond or invar steel alloys) have very small α; softer materials like aluminum or polymers have large α. For a three-dimensional object, the same logic applies in all three directions simultaneously, giving **ΔV = βV₀ΔT**, where **β** is the **volumetric (cubic) thermal expansion coefficient**. For isotropic materials — those with the same properties in all directions — each dimension expands by α, so the volume expands by approximately β ≈ 3α (using the binomial approximation (1 + αΔT)³ ≈ 1 + 3αΔT for small αΔT). For anisotropic materials (crystals with different properties in different directions), β = α_x + α_y + α_z, which need not equal 3α.

The engineering consequences of differential thermal expansion are pervasive. Bridges and railroad tracks have expansion joints — deliberate gaps — to prevent buckling when heated in summer. Bimetallic strips bond two metals with different α values; when heated, the strip curves because one side grows faster than the other, creating a simple thermostatic switch. In concrete construction, steel reinforcing bars are chosen to have an α close to that of concrete (≈12 × 10⁻⁶ K⁻¹) to avoid cracking from differential expansion. When expansion is mechanically constrained (a pipe fixed at both ends, for example), the material cannot expand freely, so internal **thermal stress** builds up instead: σ = EαΔT, where E is Young's modulus. Calculating this stress — and designing to keep it below the material's yield strength — is a routine requirement in mechanical and civil engineering.

The linear expansion formula ΔL = αL₀ΔT is linear in ΔT, which is a valid approximation for moderate temperature changes. Over large temperature ranges, α itself varies with temperature, requiring integration: L(T) = L₀ exp(∫α(T)dT). For most engineering calculations at temperatures not too far from ambient, the constant-α approximation is adequate. The key skill is identifying whether you need ΔL (a length change along one dimension) or ΔV (a total volume change) and choosing the correct coefficient — a common error is using α when the geometry requires β.
