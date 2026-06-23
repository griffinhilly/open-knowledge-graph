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
- id: phase-equilibrium-coexistence
  type: soft
builds-toward:
- phase-diagrams
tags:
- phase-transitions
- thermodynamic-relation
- coexistence
stage: expert
status: validated
---

# Clausius-Clapeyron Equation

## Core Idea
The Clausius-Clapeyron equation dP/dT = L/(T·ΔV) relates the slope of a phase boundary to the latent heat L and volume change ΔV. It explains why ice melts at higher temperatures under pressure (small ΔV gives positive dP/dT) and allows calculation of phase diagrams from thermodynamic data.

## Questions

```yaml
- question: "Water's solid-liquid coexistence curve has a negative slope in the P-T phase diagram, meaning that increasing pressure lowers ice's melting point. What thermodynamic property of water produces this anomaly?"
  type: multiple-choice
  options:
    - "Water has an unusually large latent heat of fusion, which makes the numerator L in the Clausius-Clapeyron equation dominate."
    - "Ice is less dense than liquid water, so ΔV = V_liquid − V_solid is negative, giving dP/dT = L/(T·ΔV) a negative slope."
    - "The melting temperature of ice lies below the triple point, inverting the normal sign convention."
    - "Water's entropy change at melting is negative, unlike most substances."
  answer: 1
  explanation: "The Clausius-Clapeyron equation dP/dT = L/(T·ΔV) shows that the sign of the slope is determined by the sign of ΔV (volume change upon phase transition). For most substances, the solid is denser than the liquid, so ΔV > 0 and the slope is positive. Ice is anomalous: it is less dense than liquid water (due to its open hydrogen-bonded crystal structure), so ΔV < 0, and the slope is negative. L > 0 (melting absorbs heat) and T > 0 always, so the sign of ΔV alone flips the slope."

- question: "The Clausius-Clapeyron equation is derived by requiring which condition to hold as you move along a phase coexistence boundary?"
  type: multiple-choice
  options:
    - "The entropy of the two phases must remain equal at every point on the boundary."
    - "The temperature must remain constant as pressure varies along the boundary."
    - "The Gibbs free energies of the two coexisting phases must remain equal as T and P change together."
    - "The volume change between phases must remain constant along the boundary."
  answer: 2
  explanation: "Two phases coexist when they are in thermodynamic equilibrium: G_1 = G_2. Moving along the coexistence curve means staying on this equilibrium condition, so dG_1 = dG_2 as well. Using dG = −S dT + V dP for each phase and equating gives (S_2 − S_1)dT = (V_2 − V_1)dP, which rearranges to dP/dT = ΔS/ΔV = L/(T·ΔV). The constraint is equal Gibbs free energies, not equal entropies — in fact, the entropy difference ΔS between phases is what produces the latent heat L = TΔS."

- question: "A pressure cooker cooks food faster because the elevated pressure inside lowers the boiling point of water, so the water boils at a lower temperature and less energy is needed."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. For liquid-vapor transitions, ΔV > 0 (vapor is much larger than liquid) and L > 0, so the Clausius-Clapeyron equation gives dP/dT > 0: increasing pressure RAISES the boiling point. A pressure cooker works by sealing steam inside, raising the pressure above atmospheric, which raises the boiling point above 100°C to roughly 120°C. This allows cooking at higher temperatures, speeding up chemical reactions in the food. Lower pressure (like at high altitude) lowers the boiling point, slowing cooking."

- question: "A plot of ln P vs. 1/T for the vapor pressure of a liquid should be approximately linear, with a slope that gives a direct measure of the latent heat of vaporization."
  type: true-false
  answer: true
  explanation: "Integrating the approximate Clausius-Clapeyron equation d(ln P)/dT = L/RT² gives ln P = −L/(RT) + const, so ln P is linear in 1/T with slope −L/R. This is the standard method for measuring latent heats experimentally: measure vapor pressure at several temperatures, plot ln P vs. 1/T, and extract L from the slope. The approximation assumes ideal gas vapor and negligible liquid volume, which holds well far from the critical point."

- question: "Explain where the Clausius-Clapeyron equation comes from. What physical condition defines a coexistence curve, and how does that condition lead to the relation dP/dT = L/(T·ΔV)?"
  type: short-answer
  answer: "A coexistence curve is the locus of (T, P) points where two phases are in thermodynamic equilibrium, meaning their Gibbs free energies are equal: G_1(T,P) = G_2(T,P). Moving along the curve means staying on this equality, so dG_1 = dG_2. Using dG = −S dT + V dP, equality of differentials gives −S_1 dT + V_1 dP = −S_2 dT + V_2 dP, which rearranges to dP/dT = (S_2 − S_1)/(V_2 − V_1) = ΔS/ΔV. Since latent heat L = T·ΔS at a first-order transition, this becomes dP/dT = L/(T·ΔV)."
  explanation: "The key insight is that the coexistence condition (equal Gibbs energies) must be maintained as you move along the boundary. The equation is not an empirical fit — it is an exact thermodynamic consequence of that equilibrium condition."
```

## Explainer

From your study of phase transitions, you know that along a coexistence line — say, the liquid-vapor boundary on a phase diagram — two phases are in thermodynamic equilibrium, which means their Gibbs free energies are equal: G_liquid = G_vapor. From your study of Helmholtz free energy, you know that thermodynamic potentials encode all the equilibrium information about a system. The Clausius-Clapeyron equation is the result of asking: how must the pressure change with temperature in order to *stay on the coexistence curve* as you move along it?

The derivation is elegant. Because G_liquid = G_vapor at coexistence, their differentials must also be equal as you move along the boundary: dG_liquid = dG_vapor. Using the thermodynamic identity dG = −S dT + V dP, this gives −S_l dT + V_l dP = −S_v dT + V_v dP. Rearranging: dP/dT = (S_v − S_l) / (V_v − V_l) = ΔS/ΔV. Since latent heat L = T·ΔS at a phase transition (latent heat is the heat absorbed at constant temperature), this becomes the **Clausius-Clapeyron equation**: dP/dT = L / (T·ΔV). The slope of the coexistence curve in the P-T plane is determined by the ratio of the latent heat to the product of temperature and volume change.

The physical content becomes clear through examples. For liquid-vapor transitions, ΔV is large and positive (vapor occupies much more volume than liquid), and L > 0 (vaporization absorbs heat), so dP/dT > 0 — the boiling point rises with pressure. This is why a pressure cooker cooks faster: the elevated pressure raises the boiling point above 100°C, allowing higher cooking temperatures. For solid-liquid transitions, ΔV is typically small and positive (liquids are slightly larger than solids), giving a gently positive slope. Water is the famous exception: ice is *less dense* than liquid water (ΔV < 0), so its solid-liquid coexistence line has a *negative* slope. Increased pressure lowers the melting point of ice — a counterintuitive result that arises from water's anomalous volume expansion on freezing.

For the liquid-vapor boundary specifically, we can simplify further by approximating the vapor as an ideal gas (V_vapor ≈ RT/P) and ignoring V_liquid. This gives d(ln P)/dT = L/RT², which integrates to ln(P₂/P₁) = (L/R)(1/T₁ − 1/T₂) — the approximate form used to estimate vapor pressure changes with temperature. A plot of ln P vs 1/T (a "Clausius-Clapeyron plot") should be linear with slope −L/R, providing a direct experimental method for measuring latent heats from vapor pressure measurements alone.
