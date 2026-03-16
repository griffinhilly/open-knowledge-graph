---
id: stress-and-strain-fundamentals
title: Stress and Strain Fundamentals
domain: engineering
course: materials-science
prerequisites:
- id: force-vectors-components-resultants
  type: hard
- id: vectors-in-3d
  type: soft
builds-toward:
- elastic-deformation-and-moduli-materials
- plastic-deformation-yielding-materials
- fatigue-stress-cycles-and-failure
- polymer-mechanical-properties
tags:
- stress
- strain
- deformation
- loading
- definitions
stage: formal-systems
status: draft
---

# Stress and Strain Fundamentals

## Core Idea
Stress (force per unit area) and strain (deformation per unit dimension) are the fundamental measures of mechanical loading and material response. Engineering stress/strain are based on original dimensions, while true stress/strain account for changing cross-section. Different loading types (tensile, compressive, shear) produce different stress and strain states that must be distinguished for proper material analysis.

## Explainer

When you studied force vectors, you dealt with forces as external actions on rigid bodies. Materials science requires a different framing: we care not about the total force but about how intensely that force is distributed through the material's cross-section. That intensity is **stress**. Formally, **normal stress** σ = F/A₀, where F is the force component perpendicular to the cross-sectional area A₀. The units are Pascals (N/m²) or psi. This normalization by area is what makes stress a material property measure rather than a structural one — a thin wire and a thick rod both carrying 1000 N have very different stresses, and only the stress predicts whether the material will yield.

The material's geometric response to stress is **strain**. **Normal strain** ε = ΔL/L₀, the change in length divided by the original length, is dimensionless and represents the fractional elongation or compression. These are "engineering" definitions because they use the original dimensions A₀ and L₀. They work well for small deformations — the elastic range most structures operate in. For large deformations, such as metal forming, the cross-section shrinks significantly as the material stretches, so the actual stress on the material is higher than the engineering stress. **True stress** σ_true = F/A (using the instantaneous area) and **true strain** ε_true = ln(L/L₀) account for this. The two converge at small strains and diverge substantially past the yield point.

Not all loading is axial. **Shear stress** τ = F/A acts parallel to the cross-section rather than perpendicular to it, and produces **shear strain** γ, the angular distortion of a right angle. A structural bolt in shear, a shaft in torsion, and the adhesive joint between two plates are all loaded primarily in shear. The ratio of shear stress to shear strain defines the **shear modulus** G, just as the ratio of normal stress to normal strain in the elastic range defines Young's modulus E. These two moduli are related through Poisson's ratio ν — the three are not independent for isotropic materials.

The most important habit in mechanical analysis is correctly identifying the loading type before applying any formula. Tensile and compressive normal stresses drive yielding and fracture perpendicular to the load. Shear stresses drive slip on crystallographic planes in metals and delamination in composites. Bending creates a combination — tensile stress on one face, compressive on the other, with the transition at the neutral axis. Every subsequent topic in mechanical behavior — elastic moduli, yielding criteria, fatigue, fracture mechanics — builds on these definitions, so getting the sign conventions and dimensional analysis right from the start prevents cascading errors downstream.
