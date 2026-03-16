---
id: phase-diagrams-clausius-clapeyron
title: Phase Diagrams and Clausius-Clapeyron Equation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: clausius-clapeyron-equation
  type: hard
- id: solubility-equilibria
  type: soft
builds-toward:
- chemical-potential-thermodynamics
tags:
- phase-diagram
- clausius-clapeyron
- equilibrium
- transition
stage: advanced
status: draft
---

# Phase Diagrams and Clausius-Clapeyron Equation

## Core Idea
Phase diagrams map equilibrium regions for solid, liquid, and gas phases as functions of temperature and pressure. The Clausius-Clapeyron equation quantitatively describes how phase boundaries shift with temperature based on enthalpy and entropy of phase transitions. Triple points, critical points, and phase boundaries reveal fundamental information about molecular interactions and thermodynamic stability. Phase diagrams predict what form a substance will take under any given conditions.

## Explainer

A **phase diagram** is a map of matter's preferred state. The axes are temperature and pressure, and the regions on the map tell you whether a substance exists as a solid, liquid, or gas under those conditions. The boundary lines between regions represent conditions where two phases coexist in equilibrium — at these boundaries, you can watch ice melting into water or water boiling into steam without the system "choosing" one phase over the other. From your earlier work with equilibrium concepts, you know that equilibrium means the rates of the forward and reverse processes are equal; on a phase boundary, the rate of molecules leaving one phase exactly matches the rate of molecules entering it.

Three special features anchor every phase diagram. The **triple point** is the unique temperature-pressure combination where solid, liquid, and gas all coexist simultaneously — for water, this occurs at 0.01°C and 611 Pa. The **critical point** marks the end of the liquid-gas boundary line; above this temperature and pressure, the distinction between liquid and gas disappears entirely, producing a **supercritical fluid**. The slope of each boundary line tells you how the equilibrium shifts with changing conditions. For most substances, the solid-liquid line slopes to the right (higher pressure favors the denser solid phase), but water is famously anomalous — its solid-liquid line slopes slightly left because ice is less dense than liquid water.

The **Clausius-Clapeyron equation** is what makes these boundary lines quantitative rather than qualitative. You already know the basic form from your prerequisite work: dP/dT = ΔH/(TΔV), which relates the slope of any phase boundary to the enthalpy change and volume change of the transition. For liquid-gas and solid-gas transitions, where the vapor volume is much larger than the condensed phase volume, this simplifies to the integrated form: ln(P₂/P₁) = −ΔH_vap/R × (1/T₂ − 1/T₁). This equation lets you calculate the boiling point at any pressure if you know the enthalpy of vaporization and one reference boiling point. For example, knowing water boils at 100°C at 1 atm and that ΔH_vap = 40.7 kJ/mol, you can predict that water boils at roughly 93°C in Denver (elevation ~1600 m, pressure ~0.83 atm).

The power of combining phase diagrams with the Clausius-Clapeyron equation is that you move from reading a map to calculating the map's contours from thermodynamic data. Every phase boundary encodes a competition between enthalpy (which favors the lower-energy phase) and entropy (which favors the more disordered phase). At low temperatures, enthalpy wins and the ordered phase is stable; at high temperatures, the TΔS term dominates and the disordered phase prevails. The Clausius-Clapeyron equation captures exactly where this balance tips as a function of pressure, giving you predictive control over phase behavior in applications from freeze-drying to supercritical extraction.
