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
status: validated
---

# Clausius-Clapeyron Equation and Phase Boundaries

## Core Idea
The Clausius-Clapeyron equation (dP/dT = L/(T·ΔV)) relates the slope of a phase boundary to the latent heat and volume change. It predicts how vapor pressure changes with temperature and explains why phase diagrams have their characteristic shape. This equation is crucial for understanding phase equilibria.

## How It's Best Learned
Derive it from thermodynamic relations. Use it to calculate vapor pressure at different temperatures for substances like water.

## Common Misconceptions
- Assuming the equation applies unchanged across wide temperature ranges; it's most accurate over narrow ranges.
- Forgetting the temperature dependence of latent heat.

## Questions

```yaml
- question: "Water's solid-liquid phase boundary has a slightly negative slope — increasing pressure lowers the melting point. The Clausius-Clapeyron equation predicts this because:"
  type: multiple-choice
  options:
    - "The latent heat of melting for water is negative, meaning ice releases heat when it melts"
    - "Ice is less dense than liquid water, so ΔV upon melting is negative, making dP/dT negative"
    - "The entropy of ice is higher than the entropy of liquid water at the melting point"
    - "The equation does not apply to solid-liquid boundaries, only to liquid-vapor equilibria"
  answer: 1
  explanation: "The Clausius-Clapeyron equation gives dP/dT = L/(T·ΔV). For melting, L > 0 (heat is absorbed) and T > 0. The sign of dP/dT therefore depends entirely on ΔV = V_liquid − V_solid. For water, ice floats — it is less dense than liquid water, meaning V_solid > V_liquid, so ΔV < 0 upon melting. This makes dP/dT negative: the solid-liquid boundary slopes left on a P-T diagram. This is anomalous; for most substances ice sinks, ΔV > 0, and the slope is positive."

- question: "You use the integrated Clausius-Clapeyron equation to predict the vapor pressure of a liquid at 200°C using data collected at 100°C. Your prediction differs significantly from the measured value. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The integrated form assumes constant latent heat L and ideal gas vapor — both approximations break down over large temperature ranges"
    - "The equation can only predict lower pressures than the reference point, never higher ones"
    - "You should have used the differential form dP/dT for any prediction outside the reference temperature"
    - "The Clausius-Clapeyron equation applies only to water and not to other liquids"
  answer: 0
  explanation: "The integrated form ln(P₂/P₁) = −(L/R)(1/T₂ − 1/T₁) assumes two things: (1) the latent heat L is constant over the temperature range, and (2) the vapor obeys the ideal gas law (so ΔV ≈ RT/P). Both assumptions become progressively less valid as the temperature range grows. Over a 100°C span, L can change significantly and vapor non-ideality can become substantial. The equation is most accurate over narrow temperature ranges where these approximations hold."

- question: "The positive slope of the liquid-vapor boundary on a phase diagram follows directly from the Clausius-Clapeyron equation: for vaporization, both the latent heat L and the volume change ΔV are positive, giving dP/dT > 0."
  type: true-false
  answer: true
  explanation: "For vaporization: L > 0 (heat is absorbed as liquid becomes gas), T > 0 (absolute temperature), and ΔV > 0 (gas occupies vastly more volume than liquid). So dP/dT = L/(T·ΔV) = (+)/(+·+) > 0. This positive slope means that as temperature increases, the equilibrium vapor pressure increases — boiling point rises with pressure (as familiar from pressure cookers) and falls with altitude (lower atmospheric pressure). The shape of every liquid-vapor boundary on a phase diagram follows from this simple sign analysis."

- question: "The Clausius-Clapeyron equation is derived from the condition that one phase is always more stable than the other — which is why it describes the region where only one phase can exist."
  type: true-false
  answer: false
  explanation: "The Clausius-Clapeyron equation is derived from exactly the opposite condition: the two phases must have equal chemical potentials along the phase boundary (μ₁ = μ₂), meaning neither is more stable — they coexist in equilibrium. Moving along the boundary while maintaining this equality (dμ₁ = dμ₂) and applying dμ = −s dT + v dP gives ΔS/ΔV = dP/dT = L/(T·ΔV). The equation describes the phase boundary itself — the locus of (T, P) points where coexistence occurs — not the single-phase regions on either side."

- question: "Explain how the Clausius-Clapeyron equation is derived from thermodynamic principles. What condition must hold at any point on a phase boundary, and how does that condition lead to dP/dT = L/(T·ΔV)?"
  type: short-answer
  answer: "At any point on a phase boundary, the two phases are in thermodynamic equilibrium, which requires their chemical potentials to be equal: μ₁(T,P) = μ₂(T,P). As we move along the boundary (changing both T and P together), this equality must be maintained: dμ₁ = dμ₂. Using the thermodynamic identity dμ = −s dT + v dP for each phase and setting them equal: −s₁ dT + v₁ dP = −s₂ dT + v₂ dP. Rearranging gives dP/dT = (s₂ − s₁)/(v₂ − v₁) = ΔS/ΔV. Since the latent heat L = T·ΔS (heat exchanged at constant T during the phase transition), this becomes dP/dT = L/(T·ΔV)."
  explanation: "The key conceptual move is recognizing that the phase boundary is defined by equal chemical potentials. This equality as a constraint on (T,P) is what gives the boundary its shape. The Clausius-Clapeyron equation then tells you the slope of that boundary in terms of directly measurable quantities (latent heat and volume change). This is a beautiful example of how thermodynamic equilibrium conditions generate quantitative predictions about macroscopic phase behavior."
```

## Explainer

From phase transitions, you know that at a phase boundary — say, the liquid-vapor line on a pressure-temperature diagram — two phases coexist in equilibrium. The **Clausius-Clapeyron equation** answers the question: how does this coexistence pressure change as temperature changes? In other words, what is the slope dP/dT of the phase boundary line?

The derivation flows directly from thermodynamic equilibrium. At any point on the phase boundary, the chemical potentials of the two phases must be equal: μ₁(T, P) = μ₂(T, P). Moving along the boundary, both sides must change equally: dμ₁ = dμ₂. Using the thermodynamic identity dμ = −s dT + v dP (where s is molar entropy and v is molar volume), this gives −s₁ dT + v₁ dP = −s₂ dT + v₂ dP, which rearranges to dP/dT = (s₂ − s₁)/(v₂ − v₁) = ΔS/ΔV. Since the latent heat L = T·ΔS (the heat absorbed at constant temperature during the phase transition), the result is the **Clausius-Clapeyron equation**: dP/dT = L/(T·ΔV).

The equation explains the qualitative shape of phase diagrams. For vaporization, ΔV > 0 (gas is much larger than liquid) and L > 0 (heat is absorbed), so the liquid-vapor boundary always has a positive slope. For melting of most substances, ΔV > 0 and L > 0, giving a steeply positive slope for the solid-liquid boundary. Water is famously anomalous: ice is less dense than liquid water, so ΔV < 0 upon melting, making the solid-liquid slope slightly negative — pressure slightly lowers the melting point. This is why ice skating works: high pressure under the blade lowers the melting point slightly (though viscous heating is actually the dominant effect).

For liquid-vapor equilibria with ideal-gas vapor, ΔV ≈ RT/P, and the Clausius-Clapeyron equation becomes d(ln P)/dT = L/(RT²), which integrates to the **integrated Clausius-Clapeyron equation**: ln(P₂/P₁) = −(L/R)(1/T₂ − 1/T₁). This is how you calculate vapor pressure at any temperature given the latent heat — a central tool in atmospheric science, chemical engineering, and any system involving phase equilibria. The approximation holds well over moderate temperature ranges but breaks down where L changes significantly with T or where the vapor deviates from ideal gas behavior.
