---
id: elastic-deformation-and-moduli-materials
title: Elastic Deformation and Elastic Moduli
domain: engineering
course: materials-science
prerequisites:
- id: stress-and-strain-fundamentals
  type: hard
builds-toward:
- plastic-deformation-yielding-materials
- fracture-mechanics-analysis
- toughness-and-ductility-materials
- ceramic-composite-materials
tags:
- young-modulus
- shear-modulus
- poisson-ratio
- elastic-constants
stage: formal-systems
status: draft
---

# Elastic Deformation and Elastic Moduli

## Core Idea
Elastic deformation is reversible—the material returns to its original shape when load is removed. Young's modulus (E) measures resistance to tensile/compressive strain, shear modulus (G) measures resistance to shear strain, and Poisson's ratio (ν) describes lateral contraction during tensile loading. These elastic constants are material properties dependent on bonding type and crystal structure, and define the linear (Hookean) deformation regime.

## Explainer

From your prerequisite work on stress and strain, you know how to compute axial stress σ = F/A and axial strain ε = ΔL/L₀. Elastic deformation is simply the regime where these two quantities are proportional: **σ = Eε**. This is Hooke's Law, and E — **Young's modulus** — is the proportionality constant. Physically, you can think of E as measuring how much the average interatomic spacing stretches per unit of applied stress. Small strains in the elastic regime correspond to moving up the sides of the atomic bond energy well you studied in bonding — the relationship is linear because the well is approximately parabolic near its minimum.

The reversibility of elastic deformation follows directly from this picture. You are not breaking or rearranging bonds; you are stretching them. Remove the load, and the bond energy pulls the atoms back to their equilibrium spacing. The moment you exceed the elastic limit, bonds in some regions begin to slip or break permanently, and the deformation is no longer recoverable — that is plastic deformation, which lies beyond this topic. The hallmark of elastic behavior on a stress-strain curve is the initial linear segment that passes through the origin; E is the slope of that segment.

**Poisson's ratio** ν captures a subtlety: when you pull on a material axially, it narrows laterally. This is not a separate phenomenon but a consequence of the same atomic bond stretching. As bonds elongate axially, the material's volume tends toward conservation (for metals, nearly so), which requires contraction in the transverse directions. Poisson's ratio is defined as ν = −ε_lateral / ε_axial. Most engineering materials have ν between 0.25 and 0.35; rubber is close to 0.5 (nearly incompressible); cork is near 0. Knowing ν is essential whenever stress in multiple directions matters — biaxial loading of pressure vessels, for instance.

**Shear modulus** G relates shear stress τ to shear strain γ by τ = Gγ, exactly analogous to Young's modulus for axial loading. For isotropic materials, E, G, and ν are not independent: the relation G = E / [2(1 + ν)] links them. This means you only need two elastic constants to fully describe isotropic elastic behavior — a powerful simplification. The three moduli form a complete vocabulary for small reversible deformation under any combination of loads, and they are fundamental inputs to every structural analysis, from beam deflection calculations to finite element models.
