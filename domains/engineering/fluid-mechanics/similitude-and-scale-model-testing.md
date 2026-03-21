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
stage: advanced
status: draft
---

# Similitude and Scale Model Testing

## Core Idea
Geometric, kinematic, and dynamic similarity between prototype and scale model allow controlled experiments to predict full-scale behavior. Froude numbers (gravity-dominated), Reynolds numbers (viscous-dominated), Euler numbers (pressure), and Weber numbers (surface tension) govern different flow regimes. Perfect simultaneous matching of all dimensionless numbers is often impossible; design must prioritize the most important physics and use correction factors for secondary effects.

## Questions

```yaml
- question: "A 1:50 ship model is tested in water at a speed chosen to match the prototype's Froude number. What happens to the Reynolds number in this model test?"
  type: multiple-choice
  options:
    - "Reynolds number is also matched because it is dimensionless, just like Froude number"
    - "Reynolds number increases by a factor of 50 because the model is smaller and flow is more turbulent"
    - "Reynolds number is approximately (1/50)^(3/2) ≈ 0.3% of the full-scale value — severely mismatched"
    - "Reynolds number is irrelevant for ship testing because ships operate at the free surface"
  answer: 2
  explanation: "Froude matching requires V_m = V_p × √(L_m/L_p) = V_p/√50. Reynolds number is Re = VL/ν. At model scale: Re_m = (V_p/√50)(L_p/50)/ν = Re_p × (1/50)^(3/2) ≈ 0.003 Re_p. So Re is only about 0.3% of its full-scale value — viscous effects in the model test are completely different from the prototype. The Froude and Reynolds numbers cannot simultaneously be matched in the same fluid at reduced scale, which is the central challenge of ship model testing."

- question: "An engineer claims that testing a 1:20 aircraft model in a wind tunnel at the same wind speed as the full-scale aircraft automatically matches the Reynolds number. Why is this incorrect?"
  type: multiple-choice
  options:
    - "Reynolds number only applies to internal flows like pipes, not external aerodynamics"
    - "Re = ρVL/μ; with the same fluid and velocity but L scaled by 1/20, Re_model is only 5% of Re_prototype"
    - "The wind tunnel walls create boundary effects that invalidate Reynolds number matching"
    - "Reynolds number is automatically matched whenever geometric similarity is maintained"
  answer: 1
  explanation: "Re = ρVL/μ scales linearly with characteristic length L. With L_m = L_p/20, V_m = V_p, and the same fluid (same ρ and μ), Re_m = Re_p/20. The model test has only 5% of the full-scale Reynolds number — viscous effects are far more prominent in the model than in the prototype. To recover Re matching at reduced scale, engineers must compensate elsewhere: increasing fluid density (pressurized tunnel), using a denser gas, or increasing velocity. Same fluid at same speed does not give Re matching when size changes."

- question: "Pressurizing a wind tunnel increases air density, which raises the Reynolds number at a given velocity and model size, partially compensating for the reduction in Reynolds number caused by scale reduction."
  type: true-false
  answer: true
  explanation: "Re = ρVL/μ, so increasing ρ (by pressurizing the tunnel) directly increases Re at constant V and L. Dynamic viscosity μ is nearly independent of pressure at moderate pressures, so the ratio ρ/μ = 1/ν (kinematic viscosity) increases approximately in proportion to pressure. A tunnel pressurized to 5 atm gives Re roughly 5 times higher than the same tunnel at 1 atm, allowing closer Re matching with a smaller model. This is the principle behind pressurized wind tunnels like those at NASA Langley and the ETW in Europe."

- question: "Once geometric similarity between a model and prototype is achieved, dynamic similarity follows automatically — you do not need to separately match any dimensionless numbers."
  type: true-false
  answer: false
  explanation: "Geometric similarity — matching the shape — is necessary but far from sufficient for dynamic similarity. The flow physics depend on force ratios captured in dimensionless numbers: Re (inertia vs. viscosity), Fr (inertia vs. gravity), We (inertia vs. surface tension), Ma (inertia vs. compressibility). Two geometrically identical shapes at different scales can have completely different flow regimes (e.g., laminar vs. turbulent) if Re is not matched. Dynamic similarity requires matching all physically significant dimensionless groups, not just the geometry."

- question: "Why is it generally impossible to simultaneously match both the Reynolds number and the Froude number when testing a ship model in water, and how do engineers address this limitation in practice?"
  type: short-answer
  answer: "Fr = V/√(gL) requires V_m = V_p√(L_m/L_p). Re = VL/ν requires V_m = V_p(L_p/L_m)(ν_m/ν_p). For these to be equal simultaneously: √(L_m/L_p) = (L_p/L_m)(ν_m/ν_p), giving ν_m/ν_p = (L_m/L_p)^(3/2). For a 1:50 model, ν_m must be √50^3 ≈ 1/350 of water's kinematic viscosity — no practical fluid achieves this. Engineers resolve the conflict by matching Fr (which governs wave-making resistance, the dominant physical phenomenon) and using empirical friction correlations (the ITTC line) to separately estimate and correct for the mismatched viscous drag component."
  explanation: "This is the classic 'Froude-Reynolds dilemma' in naval architecture. The fundamental incompatibility arises because the two dimensionless numbers have different velocity scaling laws at fixed scale ratio and fluid. The engineering solution — matching the dominant physics and applying corrections for the rest — is the standard approach across all scale testing. Which number to prioritize depends on what drives the system: Fr for ships and open-channel hydraulics, Re for submerged bodies, Ma for supersonic aerodynamics."
```

## Explainer

Dimensional analysis gave you a powerful insight: any physical flow situation is fully characterized by its dimensionless groups (pi groups), and two systems are **dynamically similar** if all their dimensionless groups match. Similitude applies this to physical scale modeling. Instead of building and testing a full-size aircraft or bridge, you construct a smaller model, match the critical dimensionless numbers, measure forces or pressures on the model, and then scale those results to predict full-scale behavior. The scaling laws follow directly from dimensional analysis: if two systems share the same pi groups, their behavior is identical in dimensionless terms, and all physical quantities scale predictably with the model-to-prototype ratios.

Three levels of similarity must hold for a valid model test. **Geometric similarity** means the model and prototype have identical shape — every linear dimension scaled by the same ratio λ (e.g., λ = 1/50 for a 1:50 model). Areas scale as λ², volumes as λ³. **Kinematic similarity** means the velocity field has the same pattern at corresponding locations — flow streamlines have the same shape. **Dynamic similarity** is the hardest requirement: all relevant dimensionless force ratios must match. The **Reynolds number** Re = ρVL/μ governs the ratio of inertial to viscous forces. The **Froude number** Fr = V/√(gL) governs the ratio of inertial to gravitational forces and controls free-surface and wave phenomena. The **Weber number** We = ρV²L/σ governs surface tension effects at small scales.

The fundamental challenge is that you generally cannot match all dimensionless numbers simultaneously when you change scale. Consider a 1:50 ship model tested in water. To match the Froude number (critical for wave-making resistance), model speed must be V_m = V_p/√50 ≈ 14% of full-scale speed. But Reynolds number at model scale becomes Re_m = Re_p × (1/50)^(3/2) ≈ 0.3% of full-scale Re — vastly different viscous behavior. Matching both simultaneously would require testing in a fluid with kinematic viscosity √50 ≈ 7 times smaller than water. No such fluid is practical for large models. The engineering resolution is to **deliberately mismatch** the secondary dimensionless number and apply empirical corrections — for ships, the total resistance is decomposed into wave drag (matched via Froude) and viscous drag (extrapolated using the ITTC friction line from Re).

The same principle applies across domains. For low-speed aerodynamics where Re dominates, wind tunnels are pressurized (increasing ρ and hence Re at the same V and L) or use dense gases. For supersonic flows, Mach number similarity overrides Re matching. For hydraulic structures like spillways, Froude number governs and Re is accepted as mismatched (with surface tension corrections applied if model scale is too small). Selecting which dimensionless number to match — and what corrections to apply for the rest — is the core engineering judgment in scale model test design. The scaling laws flow directly from the pi groups your prerequisite study established: once you identify which force ratio governs the physics, you know which dimensionless number to preserve and how measured model quantities convert to prototype predictions.
