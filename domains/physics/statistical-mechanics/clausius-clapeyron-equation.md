---
id: clausius-clapeyron-equation
title: Clausius-Clapeyron Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transitions-first-and-second-order
  type: hard
- id: helmholtz-free-energy
  type: hard
builds-toward:
- phase-diagrams
tags:
- phase-transitions
- thermodynamic-relation
- coexistence
stage: advanced
status: draft
---

# Clausius-Clapeyron Equation

## Core Idea
The Clausius-Clapeyron equation dP/dT = L/(T·ΔV) relates the slope of a phase boundary to the latent heat L and volume change ΔV. It explains why ice melts at higher temperatures under pressure (small ΔV gives positive dP/dT) and allows calculation of phase diagrams from thermodynamic data.

## Explainer

From your study of phase transitions, you know that along a coexistence line — say, the liquid-vapor boundary on a phase diagram — two phases are in thermodynamic equilibrium, which means their Gibbs free energies are equal: G_liquid = G_vapor. From your study of Helmholtz free energy, you know that thermodynamic potentials encode all the equilibrium information about a system. The Clausius-Clapeyron equation is the result of asking: how must the pressure change with temperature in order to *stay on the coexistence curve* as you move along it?

The derivation is elegant. Because G_liquid = G_vapor at coexistence, their differentials must also be equal as you move along the boundary: dG_liquid = dG_vapor. Using the thermodynamic identity dG = −S dT + V dP, this gives −S_l dT + V_l dP = −S_v dT + V_v dP. Rearranging: dP/dT = (S_v − S_l) / (V_v − V_l) = ΔS/ΔV. Since latent heat L = T·ΔS at a phase transition (latent heat is the heat absorbed at constant temperature), this becomes the **Clausius-Clapeyron equation**: dP/dT = L / (T·ΔV). The slope of the coexistence curve in the P-T plane is determined by the ratio of the latent heat to the product of temperature and volume change.

The physical content becomes clear through examples. For liquid-vapor transitions, ΔV is large and positive (vapor occupies much more volume than liquid), and L > 0 (vaporization absorbs heat), so dP/dT > 0 — the boiling point rises with pressure. This is why a pressure cooker cooks faster: the elevated pressure raises the boiling point above 100°C, allowing higher cooking temperatures. For solid-liquid transitions, ΔV is typically small and positive (liquids are slightly larger than solids), giving a gently positive slope. Water is the famous exception: ice is *less dense* than liquid water (ΔV < 0), so its solid-liquid coexistence line has a *negative* slope. Increased pressure lowers the melting point of ice — a counterintuitive result that arises from water's anomalous volume expansion on freezing.

For the liquid-vapor boundary specifically, we can simplify further by approximating the vapor as an ideal gas (V_vapor ≈ RT/P) and ignoring V_liquid. This gives d(ln P)/dT = L/RT², which integrates to ln(P₂/P₁) = (L/R)(1/T₁ − 1/T₂) — the approximate form used to estimate vapor pressure changes with temperature. A plot of ln P vs 1/T (a "Clausius-Clapeyron plot") should be linear with slope −L/R, providing a direct experimental method for measuring latent heats from vapor pressure measurements alone.
