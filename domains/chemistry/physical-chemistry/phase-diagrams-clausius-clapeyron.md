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
stage: formal-systems
status: validated
---

# Phase Diagrams and Clausius-Clapeyron Equation

## Core Idea
Phase diagrams map equilibrium regions for solid, liquid, and gas phases as functions of temperature and pressure. The Clausius-Clapeyron equation quantitatively describes how phase boundaries shift with temperature based on enthalpy and entropy of phase transitions. Triple points, critical points, and phase boundaries reveal fundamental information about molecular interactions and thermodynamic stability. Phase diagrams predict what form a substance will take under any given conditions.

## Questions

```yaml
- question: "Water's solid-liquid phase boundary has a negative slope on a P-T diagram — it tilts left as pressure increases. What physical property of water causes this anomaly?"
  type: multiple-choice
  options:
    - "Water has an unusually high enthalpy of vaporization compared to other small molecules"
    - "Ice is less dense than liquid water, so increased pressure destabilizes the solid and favors melting"
    - "Hydrogen bonds in liquid water are stronger than in ice, making the liquid thermodynamically preferred"
    - "The critical point for water occurs at an exceptionally high temperature and pressure"
  answer: 1
  explanation: "For most substances the solid is denser than the liquid, so increasing pressure favors the solid phase and the solid-liquid line slopes right (positive slope). Water is anomalous because ice is less dense than liquid water — pressure therefore favors the denser liquid, and the melting point actually decreases as pressure rises, producing a negative slope. This is why ice melts under the blade of an ice skate."

- question: "A substance has a large positive enthalpy of vaporization (ΔH_vap). Compared to a substance with a small ΔH_vap, how will its vapor pressure respond to a given temperature increase?"
  type: multiple-choice
  options:
    - "Vapor pressure will change very little because the large enthalpy barrier slows evaporation"
    - "Vapor pressure will decrease because high ΔH_vap stabilizes the liquid phase"
    - "Vapor pressure will increase more steeply because the large ΔH_vap amplifies the temperature dependence"
    - "Vapor pressure is independent of ΔH_vap; only molar mass determines how it changes with temperature"
  answer: 2
  explanation: "From the integrated Clausius-Clapeyron equation, ln(P₂/P₁) = −ΔH_vap/R × (1/T₂ − 1/T₁), a larger ΔH_vap multiplies the right-hand side, so the same temperature change produces a larger change in ln(P). High-ΔH_vap substances have vapor pressure curves that rise steeply with temperature. The common misconception is confusing 'hard to boil' (high boiling point) with 'vapor pressure changes slowly.'"

- question: "At the triple point of a substance, all three phases — solid, liquid, and gas — coexist in thermodynamic equilibrium simultaneously."
  type: true-false
  answer: true
  explanation: "The triple point is the unique temperature-pressure combination where the free energies of all three phases are equal, so all three phases can coexist. For water this is 0.01°C and 611 Pa. It is the only point where the solid-liquid, liquid-gas, and solid-gas boundary lines all meet."

- question: "Above the critical temperature, applying sufficient pressure to a gas will eventually condense it into a distinct liquid phase."
  type: true-false
  answer: false
  explanation: "Above the critical temperature, the liquid-gas phase boundary no longer exists — the distinction between liquid and gas disappears entirely. Compressing a gas above its critical temperature produces a supercritical fluid, which has properties intermediate between liquid and gas, but no phase transition occurs. You can only condense a gas into a liquid if the temperature is below the critical temperature."

- question: "Why does water boil at a lower temperature in Denver than at sea level, and how does the Clausius-Clapeyron equation explain this quantitatively?"
  type: short-answer
  answer: "Denver's higher altitude means lower atmospheric pressure. The boiling point is the temperature at which vapor pressure equals atmospheric pressure, so lower pressure means the vapor pressure threshold is reached at a lower temperature. The Clausius-Clapeyron equation, ln(P₂/P₁) = −ΔH_vap/R × (1/T₂ − 1/T₁), lets you calculate the new boiling point from the known boiling point at sea level, ΔH_vap, and the reduced pressure at altitude."
  explanation: "This connects the abstract equation to a concrete, observable phenomenon. The equation shows that pressure and boiling temperature are locked together via ΔH_vap: lower P means lower T_boil. This is why pressure cookers work in reverse — elevated pressure raises the boiling point above 100°C, cooking food faster."
```

## Explainer

A **phase diagram** is a map of matter's preferred state. The axes are temperature and pressure, and the regions on the map tell you whether a substance exists as a solid, liquid, or gas under those conditions. The boundary lines between regions represent conditions where two phases coexist in equilibrium — at these boundaries, you can watch ice melting into water or water boiling into steam without the system "choosing" one phase over the other. From your earlier work with equilibrium concepts, you know that equilibrium means the rates of the forward and reverse processes are equal; on a phase boundary, the rate of molecules leaving one phase exactly matches the rate of molecules entering it.

Three special features anchor every phase diagram. The **triple point** is the unique temperature-pressure combination where solid, liquid, and gas all coexist simultaneously — for water, this occurs at 0.01°C and 611 Pa. The **critical point** marks the end of the liquid-gas boundary line; above this temperature and pressure, the distinction between liquid and gas disappears entirely, producing a **supercritical fluid**. The slope of each boundary line tells you how the equilibrium shifts with changing conditions. For most substances, the solid-liquid line slopes to the right (higher pressure favors the denser solid phase), but water is famously anomalous — its solid-liquid line slopes slightly left because ice is less dense than liquid water.

The **Clausius-Clapeyron equation** is what makes these boundary lines quantitative rather than qualitative. You already know the basic form from your prerequisite work: dP/dT = ΔH/(TΔV), which relates the slope of any phase boundary to the enthalpy change and volume change of the transition. For liquid-gas and solid-gas transitions, where the vapor volume is much larger than the condensed phase volume, this simplifies to the integrated form: ln(P₂/P₁) = −ΔH_vap/R × (1/T₂ − 1/T₁). This equation lets you calculate the boiling point at any pressure if you know the enthalpy of vaporization and one reference boiling point. For example, knowing water boils at 100°C at 1 atm and that ΔH_vap = 40.7 kJ/mol, you can predict that water boils at roughly 93°C in Denver (elevation ~1600 m, pressure ~0.83 atm).

The power of combining phase diagrams with the Clausius-Clapeyron equation is that you move from reading a map to calculating the map's contours from thermodynamic data. Every phase boundary encodes a competition between enthalpy (which favors the lower-energy phase) and entropy (which favors the more disordered phase). At low temperatures, enthalpy wins and the ordered phase is stable; at high temperatures, the TΔS term dominates and the disordered phase prevails. The Clausius-Clapeyron equation captures exactly where this balance tips as a function of pressure, giving you predictive control over phase behavior in applications from freeze-drying to supercritical extraction.
