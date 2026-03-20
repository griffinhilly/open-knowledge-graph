---
id: subcooled-liquid-and-superheated-vapor
title: Subcooled Liquid and Superheated Vapor
domain: physics
course: thermodynamics
prerequisites:
- id: phase-diagrams
  type: hard
- id: temperature-and-thermal-equilibrium
  type: soft
tags:
- phase-state
- subcooled
- superheated
- properties
stage: advanced
status: draft
---

# Subcooled Liquid and Superheated Vapor

## Core Idea
Subcooled liquid is a liquid below its saturation temperature at a given pressure; it is compressed slightly from the saturated state. Superheated vapor is a vapor above its saturation temperature; it is further from the two-phase boundary. Both regions contain single-phase substances with unique properties that depend on temperature and pressure.

## Explainer

From your study of phase diagrams, you know that matter can exist as a liquid, vapor, or two-phase mixture depending on its temperature and pressure. The **saturation curve** on a P-T diagram marks the boundary between single-phase liquid and single-phase vapor regions. On the saturation curve itself, liquid and vapor coexist in equilibrium, and temperature and pressure are not independent — fixing one fixes the other. Step off the saturation curve in either direction, and you enter single-phase territory where temperature and pressure are independently specifiable.

A **subcooled liquid** (also called compressed liquid) is a liquid that sits to the left of the saturation curve — at a temperature below the saturation temperature for its current pressure. Think of liquid water at 20°C and atmospheric pressure: the saturation temperature at 1 atm is 100°C, so the water is 80°C below boiling. It has no tendency to vaporize. The "sub-cooled" name emphasizes that it has been cooled below its boiling point, while "compressed" emphasizes that its pressure exceeds the saturation pressure at its current temperature. In engineering calculations, a useful approximation treats subcooled liquid properties (specific volume, internal energy, enthalpy) as equal to the corresponding saturated liquid values at the same temperature — the deviation is small because liquids are nearly incompressible and properties change slowly with pressure.

A **superheated vapor** is a vapor that sits to the right of the saturation curve — at a temperature above the saturation temperature for its current pressure. Steam at 200°C and 1 atm is superheated: at that pressure, the saturation temperature is 100°C, so the steam is 100°C hotter than needed to maintain vapor phase. It has no tendency to condense. Superheating matters enormously in engineering: steam turbines use superheated steam to avoid water droplet formation on turbine blades (which causes erosion) and to extract more work. Unlike subcooled liquids, superheated vapor properties cannot be approximated simply — they must be read from steam tables or computed using an equation of state, because real vapor behavior departs significantly from ideal gas predictions near the saturation curve.

The practical skill is locating a substance's state on the phase diagram given its temperature and pressure, then choosing the right property table. If T < T_sat(P), you have subcooled liquid; use the compressed liquid table (or approximate with saturated liquid at T). If T > T_sat(P), you have superheated vapor; use the superheated vapor table. If T = T_sat(P), you are on the saturation curve and must specify quality x = m_vapor/m_total to pin down the state. This three-way discrimination — subcooled, saturated, superheated — is the entry point for nearly every thermodynamic cycle calculation in engineering practice.
