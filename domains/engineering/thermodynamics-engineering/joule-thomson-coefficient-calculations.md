---
id: joule-thomson-coefficient-calculations
title: Joule-Thomson Coefficient and Inversion Curve
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: throttling-joule-thomson-effect
  type: hard
- id: real-gas-thermodynamics-engineering
  type: hard
tags:
- joule-thomson-coefficient
- inversion
- cooling
- heating
- real-gas
stage: advanced
status: draft
---

# Joule-Thomson Coefficient and Inversion Curve

## Core Idea
The Joule-Thomson coefficient μ = (∂T/∂P)_h = (1/Cp)[T(∂V/∂T)_p - V] can be positive (cooling) or negative (heating) depending on the relative magnitudes of molecular volume and intermolecular attraction. The inversion curve defines the locus where μ = 0. Most gases cool below their inversion temperature (useful in liquefiers); some hydrocarbons have multiple inversion regions complicating natural gas processing.

## Explainer

From your study of throttling processes, you know that passing a gas through a valve or porous plug at steady state conserves enthalpy: the enthalpy entering equals the enthalpy leaving, so Δh = 0. For an ideal gas, enthalpy depends only on temperature, so an isenthalpic process has no temperature change. But for a real gas, enthalpy also depends on pressure through intermolecular interactions — and this is where the **Joule-Thomson effect** comes from.

The **Joule-Thomson coefficient** μ_JT = (∂T/∂P)_h tells you how much the temperature changes per unit pressure drop at constant enthalpy. If μ > 0, the gas cools as pressure drops — which is the familiar, useful behavior. If μ < 0, the gas heats as pressure drops. The sign depends on a competition: intermolecular attractions tend to cool the gas as molecules separate (they must do work against the attractive potential), while the finite volume of molecules (repulsion at short range) tends to heat it. At low temperatures and moderate pressures, attractions win and μ > 0. At very high temperatures or pressures, repulsion dominates and μ < 0.

The **inversion curve** is the locus of (T, P) states where μ = 0 — the boundary between cooling and heating behavior. Most common gases (nitrogen, oxygen, methane, argon) have their **inversion temperature** well above room temperature at low pressure, meaning they cool upon throttling under typical conditions. Hydrogen and helium are exceptions: at room temperature they are *above* their inversion temperature, so throttling actually heats them. This is why liquefying hydrogen requires pre-cooling (below its ~200 K inversion temperature) before the throttle stage can work. The Linde-Hampson liquefaction cycle exploits exactly this: the gas must be in the μ > 0 regime for the throttle to produce cooling, which is then recovered by a heat exchanger to pre-cool the incoming gas.

Calculating μ requires real-gas data: either equation-of-state coefficients or generalized correlations. The formula μ = (1/Cp)[T(∂V/∂T)_p − V] involves the isobaric thermal expansion of the gas. For an ideal gas, T(∂V/∂T)_p = T(R/P) = V exactly, so the bracket is zero and μ = 0 — no Joule-Thomson effect, as expected. For a van der Waals gas, the calculation yields a closed-form inversion curve that captures the qualitative shape. In practice, the inversion curve for engineering calculations comes from accurate equations of state like Peng-Robinson, and μ is evaluated numerically as part of refrigeration and liquefaction system design.
