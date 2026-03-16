---
id: clausius-clapeyron-phase-boundary
title: Clausius-Clapeyron Equation and Phase Boundaries
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: entropy-definition-and-calculation
  type: soft
tags:
- phase-equilibrium
- clausius-clapeyron
- phase-diagrams
stage: formal-systems
status: draft
---

# Clausius-Clapeyron Equation and Phase Boundaries

## Core Idea
The Clausius-Clapeyron equation (dP/dT = L/(T·ΔV)) relates the slope of a phase boundary to the latent heat and volume change. It predicts how vapor pressure changes with temperature and explains why phase diagrams have their characteristic shape. This equation is crucial for understanding phase equilibria.

## How It's Best Learned
Derive it from thermodynamic relations. Use it to calculate vapor pressure at different temperatures for substances like water.

## Common Misconceptions
- Assuming the equation applies unchanged across wide temperature ranges; it's most accurate over narrow ranges.
- Forgetting the temperature dependence of latent heat.

## Explainer

From phase transitions, you know that at a phase boundary — say, the liquid-vapor line on a pressure-temperature diagram — two phases coexist in equilibrium. The **Clausius-Clapeyron equation** answers the question: how does this coexistence pressure change as temperature changes? In other words, what is the slope dP/dT of the phase boundary line?

The derivation flows directly from thermodynamic equilibrium. At any point on the phase boundary, the chemical potentials of the two phases must be equal: μ₁(T, P) = μ₂(T, P). Moving along the boundary, both sides must change equally: dμ₁ = dμ₂. Using the thermodynamic identity dμ = −s dT + v dP (where s is molar entropy and v is molar volume), this gives −s₁ dT + v₁ dP = −s₂ dT + v₂ dP, which rearranges to dP/dT = (s₂ − s₁)/(v₂ − v₁) = ΔS/ΔV. Since the latent heat L = T·ΔS (the heat absorbed at constant temperature during the phase transition), the result is the **Clausius-Clapeyron equation**: dP/dT = L/(T·ΔV).

The equation explains the qualitative shape of phase diagrams. For vaporization, ΔV > 0 (gas is much larger than liquid) and L > 0 (heat is absorbed), so the liquid-vapor boundary always has a positive slope. For melting of most substances, ΔV > 0 and L > 0, giving a steeply positive slope for the solid-liquid boundary. Water is famously anomalous: ice is less dense than liquid water, so ΔV < 0 upon melting, making the solid-liquid slope slightly negative — pressure slightly lowers the melting point. This is why ice skating works: high pressure under the blade lowers the melting point slightly (though viscous heating is actually the dominant effect).

For liquid-vapor equilibria with ideal-gas vapor, ΔV ≈ RT/P, and the Clausius-Clapeyron equation becomes d(ln P)/dT = L/(RT²), which integrates to the **integrated Clausius-Clapeyron equation**: ln(P₂/P₁) = −(L/R)(1/T₂ − 1/T₁). This is how you calculate vapor pressure at any temperature given the latent heat — a central tool in atmospheric science, chemical engineering, and any system involving phase equilibria. The approximation holds well over moderate temperature ranges but breaks down where L changes significantly with T or where the vapor deviates from ideal gas behavior.
