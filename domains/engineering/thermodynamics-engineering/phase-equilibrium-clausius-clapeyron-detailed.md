---
id: phase-equilibrium-clausius-clapeyron-detailed
title: Phase Equilibrium and Clausius-Clapeyron Equation
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: clausius-clapeyron-vapor-pressure
  type: hard
- id: pure-substance-phase-diagrams
  type: soft
- id: clausius-clapeyron-equation
  type: hard
builds-toward:
- saturated-superheated-property-regions
- psychrometric-analysis-humid-air
- vapor-compression-refrigeration-cycles
tags:
- phase-equilibrium
- clausius-clapeyron
- saturation
- transitions
stage: advanced
status: draft
---

# Phase Equilibrium and Clausius-Clapeyron Equation

## Core Idea
The Clausius-Clapeyron equation dp/dT = h_fg / (T(v_g - v_f)) describes saturation pressure change with temperature during phase transitions. It enables vapor pressure calculation from latent heat and underpins all two-phase thermodynamic processes. For small pressure changes near saturation, vapor pressure grows approximately exponentially with temperature.

## Explainer

From your study of phase diagrams, you know that saturation pressure and saturation temperature are not independent: fix one and the other is determined. The Clausius-Clapeyron equation is the quantitative law governing that relationship — it tells you the slope of any phase boundary on a P-T diagram, expressed in terms of properties you can measure.

Deriving it requires one key idea from equilibrium thermodynamics: at a phase boundary, the **Gibbs free energy** of the two phases is equal, and this equality must remain true as you move along the boundary. Differentiating this condition and using the thermodynamic identity dG = V dP − S dT gives dp/dT = ΔS / ΔV between the phases. Substituting ΔS = h_fg / T (where h_fg is the **latent heat of vaporization** and T is the saturation temperature) yields the full Clausius-Clapeyron equation: dp/dT = h_fg / (T Δv), where Δv = v_g − v_f is the specific volume change on vaporization. The physical meaning is clear: the saturation pressure rises steeply with temperature when the latent heat is large (lots of energy in the phase transition) or the volume change is small.

For liquid-vapor transitions over a limited temperature range, Δv ≈ v_g (the liquid volume is negligible compared to vapor), and treating the vapor as ideal gas gives v_g ≈ RT/P. Substituting and integrating yields the **approximate Clausius-Clapeyron relation**: ln(P₂/P₁) ≈ (h_fg/R) × (1/T₁ − 1/T₂). This logarithmic form says that vapor pressure grows roughly exponentially with temperature — which is why a small increase in boiling temperature corresponds to a large increase in pressure, and why pressure cookers cook food faster. Water's saturation pressure roughly doubles for every 20°C rise near 100°C.

The practical reach of this equation is wide. In refrigeration and heat pump cycles, the working fluid cycles between two saturation states, and the Clausius-Clapeyron equation governs where those states sit on the P-T diagram. In meteorology, it underpins the Clausius-Clapeyron scaling of atmospheric water vapor with temperature (roughly +7% per °C warming), which drives changes in precipitation intensity with climate. In engineering property tables, tabulated saturation data is consistent with this equation — you can use it to interpolate between table entries or to check the physical consistency of a new refrigerant's properties. The equation is also the gateway to understanding the solid-liquid boundary slope: for water, Δv is slightly negative on melting (ice is less dense than water), so dp/dT is negative — ice melts under pressure, a fact that has real engineering and geophysical consequences.
