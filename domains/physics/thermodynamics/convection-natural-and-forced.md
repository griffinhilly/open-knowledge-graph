---
id: convection-natural-and-forced
title: 'Convective Heat Transfer: Natural and Forced'
domain: physics
course: thermodynamics
prerequisites:
- id: heat-transfer-conduction-fourier
  type: soft
tags:
- heat-transfer
- convection
- fluid-motion
stage: formal-systems
status: validated
---

# Convective Heat Transfer: Natural and Forced

## Core Idea
Convection transfers heat through the motion of a fluid (liquid or gas). Natural convection arises from density differences due to heating; forced convection uses external means (fans, pumps). The heat transfer rate is proportional to surface area and temperature difference, characterized by a convection coefficient h.

## Questions

```yaml
- question: "You are cooling a circuit board with a fan blowing air at 5 m/s. You replace the fan with a more powerful one blowing at 20 m/s. What happens to the convection coefficient h?"
  type: multiple-choice
  options:
    - "h stays the same — h is a property of air and doesn't depend on flow speed"
    - "h decreases — faster air has less time to absorb heat from the surface"
    - "h increases — higher velocity improves convective heat transfer"
    - "h is undefined for forced convection — it only applies to natural convection"
  answer: 2
  explanation: "The convection coefficient h is not a fixed material property — it depends on flow conditions including velocity. Higher velocity reduces the thermal boundary layer thickness, increasing heat transfer. Empirical correlations for forced convection express Nu (and thus h) as a function of the Reynolds number, which increases with velocity: Nu = C Re^m Pr^n. Option A is the most common misconception: treating h like thermal conductivity k, which is a fixed material property. h encodes the geometry, flow pattern, velocity, and fluid properties all together."

- question: "What drives fluid motion in natural convection?"
  type: multiple-choice
  options:
    - "An external pump or fan imposing a flow on the fluid"
    - "The temperature gradient alone, which directly pushes fluid from hot to cold regions"
    - "Density differences in the fluid caused by temperature-dependent expansion"
    - "Pressure differences imposed by the geometry of the enclosure"
  answer: 2
  explanation: "Natural convection is driven by buoyancy: a heated fluid expands, becomes less dense, and rises — while cooler, denser fluid sinks to replace it. The buoyancy force is ρgβΔT (thermal expansion coefficient β times the temperature difference). Option B is subtly wrong: temperature gradient alone doesn't move fluid; it must first cause a density change, which then creates buoyancy. This is why the governing dimensionless number is the Grashof number Gr = gβΔTL³/ν² — it explicitly contains β, the link between temperature and density."

- question: "Newton's law of cooling states that the rate of convective heat transfer is proportional to the surface area and the temperature difference between the surface and the surrounding fluid."
  type: true-false
  answer: true
  explanation: "Newton's law of cooling is Q̇ = hA(T_s − T_∞), where A is surface area and (T_s − T_∞) is the temperature difference between the surface and the bulk fluid. This proportionality is the defining relationship for convection analysis, with h encoding everything about how efficiently the flow removes heat. Doubling the area or doubling the temperature difference doubles the heat transfer rate (holding h constant)."

- question: "The convection coefficient h is a fixed property of the fluid material, like thermal conductivity, and can be looked up from standard tables given the fluid type."
  type: true-false
  answer: false
  explanation: "This is a critical distinction: thermal conductivity k is a material property (a number like 0.6 W/m·K for water at 20°C), but the convection coefficient h is a system property. It depends on the fluid, yes, but also on flow velocity, surface geometry, whether flow is laminar or turbulent, and the size of the surface. Typical h values span three orders of magnitude: ~10 W/(m²·K) for still air, ~100 for forced air, ~1000 for flowing water, and ~10,000 for boiling water. There is no single 'h for air' — only h for air under specific conditions."

- question: "What is the convection coefficient h, and why is it fundamentally different from thermal conductivity k?"
  type: short-answer
  answer: "The convection coefficient h (W/m²·K) quantifies the effectiveness of convective heat transfer between a surface and a fluid, encoding all the complexity of the flow — velocity, turbulence, fluid properties, and geometry — into a single number for use in Newton's law of cooling: Q̇ = hA(T_s − T_∞). Thermal conductivity k (W/m·K) is a material property: a fixed constant for a given material at a given temperature, governing heat diffusion through a stationary medium via Fourier's law. The key difference is that k is intrinsic to the material and does not change with flow conditions, while h is extrinsic — it characterizes the flow situation and can vary by orders of magnitude for the same fluid depending on velocity and geometry."
  explanation: "The Nusselt number Nu = hL/k_fluid bridges the two: it expresses the ratio of total (convective + conductive) heat transfer to what pure conduction through the fluid would give. Empirical correlations for Nu as a function of Re and Pr allow engineers to determine h from measurable flow conditions."
```

## Explainer

From your study of conduction, you know that heat flows through stationary matter by molecular diffusion — governed by Fourier's law, Q̇ = −kA(dT/dx). Convection is fundamentally different: heat is carried not by molecular diffusion alone but by the **bulk motion of the fluid itself**. Warm fluid near a hot surface expands, becomes less dense, rises (or moves), and is replaced by cooler fluid — this continuous renewal is what makes convection so much more efficient than conduction for most engineering applications.

In **forced convection**, an external agent drives the flow: a pump moves coolant through a pipe, a fan blows air over a circuit board, or a car moves through air. The heat transfer rate obeys **Newton's law of cooling**: Q̇ = hA(T_s − T_∞), where T_s is the surface temperature, T_∞ is the bulk fluid temperature far from the surface, A is the surface area, and h is the **convection coefficient** (also called the heat transfer coefficient). The coefficient h is the key quantity — it encodes everything about the fluid flow pattern, fluid properties, and geometry. It is not a material property like thermal conductivity; it depends on velocity, fluid viscosity, density, specific heat, and the geometry of the surface. Typical values range from ~10 W/(m²·K) for free air to ~10,000 W/(m²·K) for boiling water.

In **natural (free) convection**, the fluid motion is driven entirely by buoyancy — the density variation caused by the temperature difference itself. Heated fluid near the surface expands and rises; cooler, denser fluid sinks to take its place. The driving force is the buoyancy force ρgβΔT (where β is the thermal expansion coefficient), balanced by viscous drag. The characteristic dimensionless number is the **Grashof number** Gr = gβΔTL³/ν², the ratio of buoyancy to viscous forces. Compare this to forced convection's Reynolds number Re = ρVL/μ. When Gr/Re² ≫ 1, natural convection dominates; when Gr/Re² ≪ 1, forced convection dominates; when they are comparable, both matter and the situation is mixed.

The convection coefficient h is typically determined experimentally or via dimensional analysis using the **Nusselt number** Nu = hL/k_fluid — the ratio of total heat transfer to what conduction alone would give. Empirical correlations express Nu as a function of the relevant dimensionless groups: Nu = C Re^m Pr^n for forced convection, or Nu = C (Gr·Pr)^n for natural convection, where **Prandtl number** Pr = ν/α = (viscous diffusivity)/(thermal diffusivity) characterizes the fluid. Water has Pr ≈ 7 (thermal boundary layer thinner than velocity boundary layer), air has Pr ≈ 0.7, oils can have Pr > 100. These correlations are the engineer's practical tool: measure or estimate the flow conditions, look up the correlation, compute h, and Newton's law of cooling gives you the heat transfer rate.
