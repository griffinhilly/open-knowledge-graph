---
id: normal-shock-pressure-temperature-relations
title: 'Normal Shock Wave Relations: Pressure, Temperature, and Density'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: normal-shock-waves
  type: hard
- id: mach-number-compressibility-effects
  type: hard
builds-toward:
- oblique-shock-deflection-angles
tags:
- shocks
- discontinuity
- property-changes
stage: formal-systems
status: draft
---

# Normal Shock Wave Relations: Pressure, Temperature, and Density

## Core Idea
Across a normal shock, pressure, temperature, and density jump discontinuously while entropy increases irreversibly. Shock relations derived from conservation of mass, momentum, and energy provide algebraic equations relating upstream and downstream states to shock Mach number. Stronger shocks (higher M₁) produce larger pressure and temperature jumps, critical for hypersonic vehicle design and high-speed inlet analysis.

## Explainer

From your study of normal shock waves and Mach number effects, you know that a normal shock is a thin discontinuity across which supersonic flow abruptly becomes subsonic. What the **Rankine-Hugoniot relations** — the shock relations — provide is a precise algebraic accounting of how much each property changes. The derivation applies conservation of mass, momentum, and energy across a thin control volume straddling the shock, along with the perfect-gas equation of state. The result is a set of equations expressing the downstream-to-upstream ratios of pressure, temperature, density, and Mach number entirely as functions of the upstream Mach number M₁.

The qualitative pattern is worth memorizing. Across a normal shock, pressure, temperature, and density all increase discontinuously. The Mach number drops from supersonic (M₁ > 1) to always subsonic (M₂ < 1). **Stagnation temperature** is conserved — the shock is adiabatic, so no heat crosses the boundary — but **stagnation pressure** decreases because entropy is generated irreversibly inside the shock. This entropy increase is the thermodynamic signature of the shock's irreversibility: no work is done on the fluid, no heat is added, yet entropy rises. The stronger the shock (larger M₁), the greater the entropy production and the greater the stagnation pressure loss.

The **normal shock table** encodes these relationships numerically. For any M₁, you can read off p₂/p₁, T₂/T₁, ρ₂/ρ₁, M₂, and the stagnation pressure ratio p₀₂/p₀₁. At M₁ = 1, all ratios equal 1 — infinitesimally weak shock, no change. As M₁ → ∞, pressure and temperature ratios grow without bound, but ρ₂/ρ₁ approaches a finite limit of (γ+1)/(γ−1) ≈ 6 for air. This density limit has a physical interpretation: the temperature rise increases pressure enough to resist further compression regardless of shock strength.

The engineering application that makes these relations critical is **supersonic inlet design**. In a jet engine flying at supersonic speed, air must be decelerated to subsonic conditions before entering the compressor. If a single strong normal shock accomplishes all the deceleration, the stagnation pressure loss is enormous — degrading thrust and fuel efficiency significantly. This is why military aircraft inlets use oblique shocks (your next topic) to perform the deceleration in multiple gentler steps, each producing lower entropy, recovering more stagnation pressure before the final, weakened normal shock closes out the deceleration.
