---
id: similitude-and-scale-model-testing
title: Similitude and Scale Model Testing
domain: engineering
course: fluid-mechanics
prerequisites:
- id: dimensional-analysis-and-similarity
  type: hard
- id: reynolds-number
  type: hard
builds-toward:
- pump-affinity-laws-and-similarity
tags:
- similitude
- modeling
- scaling
stage: formal-systems
status: draft
---

# Similitude and Scale Model Testing

## Core Idea
Geometric, kinematic, and dynamic similarity between prototype and scale model allow controlled experiments to predict full-scale behavior. Froude numbers (gravity-dominated), Reynolds numbers (viscous-dominated), Euler numbers (pressure), and Weber numbers (surface tension) govern different flow regimes. Perfect simultaneous matching of all dimensionless numbers is often impossible; design must prioritize the most important physics and use correction factors for secondary effects.

## Explainer

Dimensional analysis gave you a powerful insight: any physical flow situation is fully characterized by its dimensionless groups (pi groups), and two systems are **dynamically similar** if all their dimensionless groups match. Similitude applies this to physical scale modeling. Instead of building and testing a full-size aircraft or bridge, you construct a smaller model, match the critical dimensionless numbers, measure forces or pressures on the model, and then scale those results to predict full-scale behavior. The scaling laws follow directly from dimensional analysis: if two systems share the same pi groups, their behavior is identical in dimensionless terms, and all physical quantities scale predictably with the model-to-prototype ratios.

Three levels of similarity must hold for a valid model test. **Geometric similarity** means the model and prototype have identical shape — every linear dimension scaled by the same ratio λ (e.g., λ = 1/50 for a 1:50 model). Areas scale as λ², volumes as λ³. **Kinematic similarity** means the velocity field has the same pattern at corresponding locations — flow streamlines have the same shape. **Dynamic similarity** is the hardest requirement: all relevant dimensionless force ratios must match. The **Reynolds number** Re = ρVL/μ governs the ratio of inertial to viscous forces. The **Froude number** Fr = V/√(gL) governs the ratio of inertial to gravitational forces and controls free-surface and wave phenomena. The **Weber number** We = ρV²L/σ governs surface tension effects at small scales.

The fundamental challenge is that you generally cannot match all dimensionless numbers simultaneously when you change scale. Consider a 1:50 ship model tested in water. To match the Froude number (critical for wave-making resistance), model speed must be V_m = V_p/√50 ≈ 14% of full-scale speed. But Reynolds number at model scale becomes Re_m = Re_p × (1/50)^(3/2) ≈ 0.3% of full-scale Re — vastly different viscous behavior. Matching both simultaneously would require testing in a fluid with kinematic viscosity √50 ≈ 7 times smaller than water. No such fluid is practical for large models. The engineering resolution is to **deliberately mismatch** the secondary dimensionless number and apply empirical corrections — for ships, the total resistance is decomposed into wave drag (matched via Froude) and viscous drag (extrapolated using the ITTC friction line from Re).

The same principle applies across domains. For low-speed aerodynamics where Re dominates, wind tunnels are pressurized (increasing ρ and hence Re at the same V and L) or use dense gases. For supersonic flows, Mach number similarity overrides Re matching. For hydraulic structures like spillways, Froude number governs and Re is accepted as mismatched (with surface tension corrections applied if model scale is too small). Selecting which dimensionless number to match — and what corrections to apply for the rest — is the core engineering judgment in scale model test design. The scaling laws flow directly from the pi groups your prerequisite study established: once you identify which force ratio governs the physics, you know which dimensionless number to preserve and how measured model quantities convert to prototype predictions.
