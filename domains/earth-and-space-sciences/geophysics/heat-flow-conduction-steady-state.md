---
id: heat-flow-conduction-steady-state
title: Heat Conduction and Steady-State Heat Flow
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geothermal-gradient-crustal-heat-flow
  type: hard
- id: thermal-conductivity-and-rocks
  type: hard
builds-toward:
- mantle-adiabat-temperature
- crustal-age-and-cooling-curves
tags:
- geothermics
- heat-flow
- conduction
stage: advanced
status: draft
---

# Heat Conduction and Steady-State Heat Flow

## Core Idea
Heat flow is governed by Fourier's law: q = −k(dT/dz), where k is thermal conductivity. In steady state, heat flow is constant with depth and depends on the geothermal gradient and rock conductivity. Continental heat flow (~60 mW/m²) exceeds oceanic heat flow (~82 mW/m² at young ridges, decreasing with age) due to differences in crustal thickness and radioactive heat production.

## Explainer

You already understand two key ingredients: the **geothermal gradient** (temperature increases with depth, typically 25–30°C per kilometer in continental crust) and **thermal conductivity** (different rocks transmit heat at different rates, with crystalline rocks like granite conducting better than porous sediments). Steady-state heat conduction ties these together with a single equation that governs how thermal energy moves through the lithosphere.

**Fourier's law of heat conduction** states that heat flux q equals the negative product of thermal conductivity k and the temperature gradient dT/dz: q = −k(dT/dz). The negative sign simply means heat flows from hot to cold — downward-increasing temperature drives heat upward toward the surface. The units work out to watts per square meter (W/m²), and typical surface heat flow values are on the order of tens of milliwatts per square meter. Think of it like water flowing through a pipe: the temperature gradient is the pressure difference driving the flow, and thermal conductivity is how wide the pipe is. A steep gradient or a highly conductive rock produces more heat flow; a shallow gradient or an insulating rock produces less.

**Steady state** means that the temperature at every point is constant in time — heat entering the bottom of any layer equals heat leaving the top. This is a reasonable approximation for old, thermally equilibrated continental crust, but it breaks down where thermal transients matter (young oceanic lithosphere cooling from a hot ridge, or regions recently disturbed by magmatic intrusion). In steady state with no internal heat sources, heat flow is the same at every depth — measure it at the surface, and you know it throughout the column. When radioactive heat production is present (as in granitic continental crust, which is enriched in uranium, thorium, and potassium), the steady-state equation gains a source term: heat flow increases with depth because each layer of rock adds its own radiogenic contribution to the upward flux.

This framework explains a key observation in global geophysics. Continental crust has high radioactive heat production concentrated in the upper crust, so a significant fraction of continental surface heat flow (~60 mW/m²) is generated within the crust itself. Oceanic crust has very little radioactive heat production, so nearly all oceanic heat flow comes from the cooling mantle below. Young oceanic lithosphere near mid-ocean ridges has very high heat flow because the mantle is hot and close to the surface, but this decreases predictably with the square root of crustal age as the lithosphere thickens and cools — a transient process that steady-state analysis alone cannot capture, but which the steady-state framework helps benchmark. Measuring heat flow in boreholes (temperature gradient plus laboratory conductivity measurements on core samples) remains the primary method for constraining the thermal state of the lithosphere.
