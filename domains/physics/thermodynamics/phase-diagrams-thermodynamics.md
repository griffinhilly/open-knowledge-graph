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

## Questions

```yaml
- question: "You start with water vapor at very high temperature and gradually increase pressure while keeping the temperature constant above the critical temperature. Which of the following correctly describes what happens?"
  type: multiple-choice
  options:
    - "The vapor crosses the liquid-vapor boundary and becomes liquid"
    - "The vapor undergoes a sharp phase transition to supercritical fluid"
    - "The vapor continuously densifies into a supercritical fluid with no distinct phase transition"
    - "The vapor cannot be compressed above the critical temperature"
  answer: 2
  explanation: "Above the critical temperature, the liquid-vapor boundary no longer exists — it ends at the critical point. Increasing pressure continuously densifies the fluid without any sharp transition or latent heat. This 'going around' the critical point is a key feature of supercritical fluids: you can move between gas-like and liquid-like densities continuously. Option A is wrong because the liquid-vapor boundary only exists below the critical temperature."

- question: "Why does increasing pressure cause ice to melt, a behavior opposite to almost all other solids?"
  type: multiple-choice
  options:
    - "Water has an unusually high latent heat of fusion, so pressure supplies the needed energy"
    - "Ice is less dense than liquid water, so the solid-liquid boundary has a negative slope"
    - "The triple point of water is below atmospheric pressure, forcing melting at high pressure"
    - "Ice has stronger hydrogen bonds than liquid water, which are broken by pressure"
  answer: 1
  explanation: "The Clausius-Clapeyron equation dP/dT = L / (TΔv) governs the slope of phase boundaries. For the solid-liquid transition, Δv = v_liquid − v_solid. For most substances, solids are denser than liquids (Δv > 0), giving a positive slope. But for water, ice is less dense than liquid water (Δv < 0), so the slope is negative — increasing pressure pushes the boundary leftward (toward lower temperature), meaning ice melts under increased pressure at constant temperature. This negative slope is what makes ice skating and pressure-induced melting possible."

- question: "The critical point and the triple point of a substance occur at the same pressure and temperature."
  type: true-false
  answer: false
  explanation: "These are entirely different features of a phase diagram. The triple point is the unique P-T coordinate where all three phases (solid, liquid, vapor) coexist in equilibrium — for water it is at 273.16 K and 0.006 atm. The critical point marks where the liquid-vapor boundary terminates; above it, the substance is a supercritical fluid. For water the critical point is at 647 K and 218 atm. They cannot coincide because the triple point is at the intersection of three phase boundaries, while the critical point is the endpoint of one."

- question: "At pressures below the triple point of a substance, heating a solid will cause it to sublimate directly to vapor without passing through a liquid phase."
  type: true-false
  answer: true
  explanation: "The triple point is the minimum pressure at which the liquid phase can exist. Below this pressure, the liquid-vapor boundary does not exist — the phase diagram goes directly from solid to vapor. Heating a solid at such low pressures causes sublimation (solid → vapor), bypassing the liquid phase entirely. This is exactly how freeze-drying works: food is frozen and placed in a vacuum below water's triple-point pressure (0.006 atm), so the ice sublimes rather than melting."

- question: "Why is water's phase diagram considered anomalous compared to most other substances, and what physical property of water causes this anomaly?"
  type: short-answer
  answer: "For most substances, the solid is denser than the liquid, so the solid-liquid boundary has a positive slope — increasing pressure favors the denser solid phase. Water is anomalous because ice is less dense than liquid water (due to hydrogen bonding creating an open crystalline lattice). This means Δv for melting is negative, flipping the Clausius-Clapeyron slope to negative: the solid-liquid line tilts to the left. Practical consequence: ice melts under pressure rather than solidifying."
  explanation: "The anomaly has significant physical consequences beyond phase diagrams — it's why ice floats (insulating aquatic life beneath frozen surfaces), why glaciers flow, and why pipes burst when water freezes. The underlying cause is hydrogen bonding: when water freezes, molecules lock into a hexagonal lattice that is actually more open (lower density) than the disordered arrangement in liquid water."
```

## Explainer

From phase transitions and latent heat, you know that matter can exist in different phases — solid, liquid, gas — and that crossing between them requires an exchange of energy (latent heat) at a fixed temperature and pressure. A **phase diagram** is the map that tells you which phase is stable at any given combination of pressure P and temperature T. Reading this map is a fundamental skill for anyone working with materials, fluids, or thermodynamics.

The most important features are the **phase boundary curves**. Each curve separates two regions of the diagram where different phases are stable. Along the curve itself, both phases coexist in equilibrium — you can have liquid water and steam side by side at 100°C and 1 atm because you're on the liquid-vapor boundary. The slope of each boundary is given by the **Clausius-Clapeyron equation**: dP/dT = L / (TΔv), where L is the latent heat and Δv is the volume change across the transition. For vaporization, ΔV is large and positive (gas is much less dense than liquid), so the liquid-vapor curve has a gentle positive slope. For melting, ΔV is small, and the sign matters: for most substances ice is denser than liquid, so ΔV > 0 and the solid-liquid boundary slopes gently right. For water, the reverse is true — ice is less dense than liquid water — so ΔV < 0, the slope is negative, and increasing pressure melts ice. This is why ice skating works and why the solid-liquid line in water's phase diagram is the unusual one.

The **triple point** is the unique P-T combination where solid, liquid, and vapor all coexist simultaneously. For water it is at 273.16 K and 611.7 Pa (0.006 atm). Below this pressure, liquid water cannot exist: heating ice at low pressure takes it directly from solid to vapor (sublimation), bypassing the liquid phase entirely. This is how freeze-drying works — food is frozen and placed in a vacuum below the triple-point pressure, so the ice sublimes directly rather than melting. The triple point is used to define the Kelvin temperature scale: 273.16 K is assigned to water's triple point by international convention.

The **critical point** marks the end of the liquid-vapor boundary. Below the critical temperature and pressure, liquid and vapor are distinct phases separated by a boundary with a latent heat. Above the critical point, there is no distinction — the substance exists as a **supercritical fluid** with properties interpolating between liquid (high density, dissolvable) and gas (flows easily). You can travel from the liquid region to the gas region without crossing any phase boundary by going around the critical point: increase temperature above T_c while in the liquid phase, then reduce pressure, and you arrive in the gas phase without ever undergoing a sharp transition. This continuous path is impossible for the solid-liquid or solid-vapor boundaries, because there are no critical points there (for most substances). Supercritical CO₂ (above 31°C, 73 atm) is industrially used as a solvent in coffee decaffeination and pharmaceutical extraction, because its density can be tuned continuously between gas-like and liquid-like values.
