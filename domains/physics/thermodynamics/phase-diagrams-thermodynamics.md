---
id: phase-diagrams-thermodynamics
title: Phase Diagrams
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: latent-heat
  type: soft
tags:
- phase-diagram
- triple-point
- critical-point
- PT-diagram
- supercritical
stage: formal-systems
status: validated
---

# Phase Diagrams

## Core Idea
A phase diagram maps the stable phase of a substance in pressure-temperature space. Phase boundaries are curves along which two phases coexist in equilibrium; crossing a boundary causes a phase transition. All three phases coexist at the unique triple point. Above the critical point, the liquid-gas distinction vanishes and the substance exists as a supercritical fluid. Water's phase diagram is unusual: its solid-liquid boundary has a negative slope, meaning increasing pressure lowers the melting point (due to ice being less dense than liquid water).

## How It's Best Learned
Trace paths on a water phase diagram: heating at 1 atm crosses the melting point at 0°C and boiling point at 100°C. Then trace a path at low pressure crossing directly from solid to vapor (sublimation, as in freeze-drying). Contrast with CO₂, which has a triple point at 5.1 atm so liquid CO₂ cannot exist at atmospheric pressure.

## Common Misconceptions
- The boiling point is not fixed — it depends on pressure; at high altitude (lower pressure) water boils below 100°C.
- The critical point is not the same as the triple point; beyond the critical point you can convert liquid to gas continuously without crossing a phase boundary.

## Explainer

From phase transitions and latent heat, you know that matter can exist in different phases — solid, liquid, gas — and that crossing between them requires an exchange of energy (latent heat) at a fixed temperature and pressure. A **phase diagram** is the map that tells you which phase is stable at any given combination of pressure P and temperature T. Reading this map is a fundamental skill for anyone working with materials, fluids, or thermodynamics.

The most important features are the **phase boundary curves**. Each curve separates two regions of the diagram where different phases are stable. Along the curve itself, both phases coexist in equilibrium — you can have liquid water and steam side by side at 100°C and 1 atm because you're on the liquid-vapor boundary. The slope of each boundary is given by the **Clausius-Clapeyron equation**: dP/dT = L / (TΔv), where L is the latent heat and Δv is the volume change across the transition. For vaporization, ΔV is large and positive (gas is much less dense than liquid), so the liquid-vapor curve has a gentle positive slope. For melting, ΔV is small, and the sign matters: for most substances ice is denser than liquid, so ΔV > 0 and the solid-liquid boundary slopes gently right. For water, the reverse is true — ice is less dense than liquid water — so ΔV < 0, the slope is negative, and increasing pressure melts ice. This is why ice skating works and why the solid-liquid line in water's phase diagram is the unusual one.

The **triple point** is the unique P-T combination where solid, liquid, and vapor all coexist simultaneously. For water it is at 273.16 K and 611.7 Pa (0.006 atm). Below this pressure, liquid water cannot exist: heating ice at low pressure takes it directly from solid to vapor (sublimation), bypassing the liquid phase entirely. This is how freeze-drying works — food is frozen and placed in a vacuum below the triple-point pressure, so the ice sublimes directly rather than melting. The triple point is used to define the Kelvin temperature scale: 273.16 K is assigned to water's triple point by international convention.

The **critical point** marks the end of the liquid-vapor boundary. Below the critical temperature and pressure, liquid and vapor are distinct phases separated by a boundary with a latent heat. Above the critical point, there is no distinction — the substance exists as a **supercritical fluid** with properties interpolating between liquid (high density, dissolvable) and gas (flows easily). You can travel from the liquid region to the gas region without crossing any phase boundary by going around the critical point: increase temperature above T_c while in the liquid phase, then reduce pressure, and you arrive in the gas phase without ever undergoing a sharp transition. This continuous path is impossible for the solid-liquid or solid-vapor boundaries, because there are no critical points there (for most substances). Supercritical CO₂ (above 31°C, 73 atm) is industrially used as a solvent in coffee decaffeination and pharmaceutical extraction, because its density can be tuned continuously between gas-like and liquid-like values.
