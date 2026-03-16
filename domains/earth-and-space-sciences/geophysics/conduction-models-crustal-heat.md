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

## Explainer

From your work on heat flow measurements, you know that the geothermal gradient — the rate of temperature increase with depth — can be measured in boreholes, and that surface heat flow equals the product of thermal conductivity and that gradient. But a single measurement at one depth gives you a snapshot, not an explanation. To understand *why* temperatures vary the way they do throughout the crust, you need a physical model of how heat moves. In the solid crust, the dominant mechanism is **conduction**: heat energy transfers from hotter to cooler regions through molecular vibrations and electron interactions in the rock matrix, without any bulk movement of material.

The governing equation for conductive heat transfer is the **heat-diffusion equation**, written in one dimension as ∂T/∂t = κ ∂²T/∂z², where T is temperature, t is time, z is depth, and κ is **thermal diffusivity** — a material property equal to thermal conductivity divided by the product of density and specific heat capacity. This equation says that the rate of temperature change at any point depends on how curved the temperature profile is at that point. If the temperature-depth curve is straight (constant gradient), no change occurs and the system is in steady state. If the curve bends — for instance, because heat-producing radioactive elements are concentrated in the upper crust — temperature evolves over time toward a new equilibrium.

The simplest and most widely used model is **steady-state conduction with no internal heat sources**: temperature increases linearly with depth, and the gradient equals the surface heat flow divided by thermal conductivity. This model explains the first-order observation that deeper rocks are hotter, but it fails to match real borehole data in detail because it ignores radioactive heat production. Adding a heat-production term A to the equation gives ∂²T/∂z² = −A/κ in steady state, which yields a curved (parabolic) temperature profile with steeper gradients near the surface where radiogenic elements like uranium, thorium, and potassium are concentrated. This explains why surface heat flow varies between geological provinces even when mantle heat flux is similar — granitic upper crusts with high radioactivity produce more heat than mafic ones.

For problems involving time-dependent processes — such as the cooling of oceanic lithosphere as it moves away from a mid-ocean ridge, or the thermal relaxation of crust after tectonic thickening — the full time-dependent diffusion equation must be solved. The classic **half-space cooling model** treats the lithosphere as a semi-infinite solid initially at mantle temperature, cooled from above by the ocean. The solution involves the error function and predicts that ocean depth increases as the square root of plate age, a prediction that matches bathymetric observations remarkably well for young oceanic crust. More complex scenarios, such as layered crusts with different thermal conductivities or transient heating by magmatic intrusions, require numerical methods — typically finite-difference or finite-element approaches that discretize the depth axis and step forward in time. These computational solutions allow geophysicists to test whether a proposed thermal history is consistent with observed heat flow, metamorphic mineral assemblages, and thermochronological data.
