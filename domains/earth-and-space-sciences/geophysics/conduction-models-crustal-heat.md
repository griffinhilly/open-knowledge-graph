---
id: conduction-models-crustal-heat
title: Conduction Models and Thermal Equation Solutions
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: heat-flow-measurement-geothermal
  type: hard
- id: thermal-conductivity-and-rocks
  type: hard
builds-toward:
- lithospheric-thermal-evolution
- subduction-zone-thermal-structure
tags:
- heat
- conduction
- thermal
- models
stage: advanced
status: draft
---

# Conduction Models and Thermal Equation Solutions

## Core Idea
The heat-diffusion equation (∂T/∂t = κ ∇²T) governs crustal temperatures. Analytical and numerical solutions for 1D cooling, steady-state conduction, and layered models yield temperature-depth profiles that compare with observations.

## Questions

```yaml
- question: "A borehole in a granitic region shows a steeper geothermal gradient near the surface than at depth, even though the rock's thermal conductivity is uniform with depth. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The mantle contributes more heat near the surface than at depth"
    - "Radioactive heat production concentrated in the upper crust creates a parabolic temperature profile with steeper gradients near the surface"
    - "Recent climate warming has elevated surface temperatures, creating a transient anomaly near the surface"
    - "Denser rock at depth has lower thermal diffusivity, causing heat to pile up near the surface"
  answer: 1
  explanation: "The steady-state heat equation with internal heat production (∂²T/∂z² = −A/κ) yields a parabolic temperature-depth profile. Because radiogenic elements (U, Th, K) are concentrated in granitic upper crust, heat is added throughout that upper layer — not just at the base. Each successive depth interval must conduct both the heat from below and the locally generated heat, causing the gradient to be steepest at the surface and decrease with depth. Option A is backwards; option C is a real transient effect but doesn't explain a systematic depth trend; option D confuses diffusivity with conductivity."

- question: "According to the half-space cooling model for oceanic lithosphere, if you compare ocean floor at age T to ocean floor at age 4T, you expect the deeper seafloor (age 4T) to be deeper by a factor of:"
  type: multiple-choice
  options:
    - "4 — depth is proportional to plate age"
    - "2 — depth is proportional to the square root of plate age"
    - "16 — depth is proportional to the square of plate age"
    - "1.4 — depth grows only logarithmically with age"
  answer: 1
  explanation: "The half-space cooling model predicts that lithospheric thickness (and therefore bathymetric depth) scales as √(κt), where κ is thermal diffusivity and t is plate age. So if age quadruples (4T vs T), depth increases by √4 = 2. This square-root dependence on age is one of the model's key testable predictions, confirmed by bathymetric surveys of young oceanic crust. Option A (linear) would apply if the lithosphere cooled at a constant rate, which it does not."

- question: "In the steady-state conduction model with no internal heat sources, the geothermal gradient (temperature change per unit depth) is the same at all depths within a layer of uniform thermal conductivity."
  type: true-false
  answer: true
  explanation: "With no heat production and steady state, the heat diffusion equation reduces to ∂²T/∂z² = 0, which means the second derivative of temperature with respect to depth is zero. This implies a linear temperature-depth profile — the gradient is constant. The surface heat flow equals thermal conductivity times this constant gradient. Any deviation from linearity (curved profile) signals either internal heat production or a transient, time-dependent process."

- question: "Thermal diffusivity and thermal conductivity are the same physical quantity expressed in different units."
  type: true-false
  answer: false
  explanation: "They are distinct properties. Thermal conductivity (k, units W m⁻¹ K⁻¹) measures how readily a material conducts heat. Thermal diffusivity (κ, units m² s⁻¹) measures how quickly a temperature disturbance propagates through a material, and equals k / (ρ Cₚ), where ρ is density and Cₚ is specific heat capacity. A material can have high conductivity but low diffusivity if it also has high heat capacity per unit volume. Both appear in the heat equation, but they govern different aspects of thermal behavior."

- question: "Explain why adding radioactive heat production to the steady-state conduction model causes the geothermal gradient to be steeper near the surface than at depth, even when thermal conductivity is uniform."
  type: short-answer
  answer: "In steady state with heat production A (W m⁻³), the 1D heat equation is k ∂²T/∂z² = −A. This means the temperature profile is parabolic, not linear. Physically, heat generated throughout the upper crust must all ultimately flow upward to the surface. The shallow depths must conduct not only the heat arriving from below, but also all the radiogenic heat produced above them. Because more total heat flux passes through shallower depths, the gradient (heat flux / conductivity) is steeper near the surface. At the base of the heat-producing layer, only the deeper heat flow (from the mantle) remains, so the gradient steps down to a lower value."
  explanation: "This explains why surface heat flow varies between geological provinces with similar mantle heat flux. Granitic continents generate more crustal heat (high U, Th, K content) than oceanic or mafic settings, producing higher surface heat flow and steeper upper-crustal gradients even with the same mantle input."
```

## Explainer

From your work on heat flow measurements, you know that the geothermal gradient — the rate of temperature increase with depth — can be measured in boreholes, and that surface heat flow equals the product of thermal conductivity and that gradient. But a single measurement at one depth gives you a snapshot, not an explanation. To understand *why* temperatures vary the way they do throughout the crust, you need a physical model of how heat moves. In the solid crust, the dominant mechanism is **conduction**: heat energy transfers from hotter to cooler regions through molecular vibrations and electron interactions in the rock matrix, without any bulk movement of material.

The governing equation for conductive heat transfer is the **heat-diffusion equation**, written in one dimension as ∂T/∂t = κ ∂²T/∂z², where T is temperature, t is time, z is depth, and κ is **thermal diffusivity** — a material property equal to thermal conductivity divided by the product of density and specific heat capacity. This equation says that the rate of temperature change at any point depends on how curved the temperature profile is at that point. If the temperature-depth curve is straight (constant gradient), no change occurs and the system is in steady state. If the curve bends — for instance, because heat-producing radioactive elements are concentrated in the upper crust — temperature evolves over time toward a new equilibrium.

The simplest and most widely used model is **steady-state conduction with no internal heat sources**: temperature increases linearly with depth, and the gradient equals the surface heat flow divided by thermal conductivity. This model explains the first-order observation that deeper rocks are hotter, but it fails to match real borehole data in detail because it ignores radioactive heat production. Adding a heat-production term A to the equation gives ∂²T/∂z² = −A/κ in steady state, which yields a curved (parabolic) temperature profile with steeper gradients near the surface where radiogenic elements like uranium, thorium, and potassium are concentrated. This explains why surface heat flow varies between geological provinces even when mantle heat flux is similar — granitic upper crusts with high radioactivity produce more heat than mafic ones.

For problems involving time-dependent processes — such as the cooling of oceanic lithosphere as it moves away from a mid-ocean ridge, or the thermal relaxation of crust after tectonic thickening — the full time-dependent diffusion equation must be solved. The classic **half-space cooling model** treats the lithosphere as a semi-infinite solid initially at mantle temperature, cooled from above by the ocean. The solution involves the error function and predicts that ocean depth increases as the square root of plate age, a prediction that matches bathymetric observations remarkably well for young oceanic crust. More complex scenarios, such as layered crusts with different thermal conductivities or transient heating by magmatic intrusions, require numerical methods — typically finite-difference or finite-element approaches that discretize the depth axis and step forward in time. These computational solutions allow geophysicists to test whether a proposed thermal history is consistent with observed heat flow, metamorphic mineral assemblages, and thermochronological data.
