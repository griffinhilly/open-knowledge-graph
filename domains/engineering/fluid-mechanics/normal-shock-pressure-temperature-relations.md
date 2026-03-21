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
stage: advanced
status: draft
---

# Normal Shock Wave Relations: Pressure, Temperature, and Density

## Core Idea
Across a normal shock, pressure, temperature, and density jump discontinuously while entropy increases irreversibly. Shock relations derived from conservation of mass, momentum, and energy provide algebraic equations relating upstream and downstream states to shock Mach number. Stronger shocks (higher M₁) produce larger pressure and temperature jumps, critical for hypersonic vehicle design and high-speed inlet analysis.

## Questions

```yaml
- question: "A normal shock passes through air at M₁ = 2.5. After the shock, which statement about stagnation quantities is correct?"
  type: multiple-choice
  options:
    - "Both stagnation temperature and stagnation pressure are conserved because the shock does no work on the gas"
    - "Stagnation temperature is conserved because the shock is adiabatic, but stagnation pressure decreases because entropy increases irreversibly inside the shock"
    - "Stagnation pressure is conserved by energy conservation, but stagnation temperature drops because kinetic energy is lost in deceleration"
    - "Both stagnation temperature and stagnation pressure decrease because the flow is decelerated and loses total energy"
  answer: 1
  explanation: "A normal shock is adiabatic — no heat crosses the shock boundary — so total enthalpy h₀ = c_p T₀ is conserved, and stagnation temperature T₀ is unchanged. However, entropy is generated irreversibly inside the shock (viscous dissipation in the thin shock zone), and stagnation pressure is directly linked to entropy via the second law: any entropy increase reduces stagnation pressure (p₀₂/p₀₁ < 1). Option A is the classic misconception: 'no work done' does not prevent entropy production. The shock generates entropy without doing work or transferring heat."

- question: "As the upstream Mach number M₁ increases without limit, what happens to the density ratio ρ₂/ρ₁ across the normal shock?"
  type: multiple-choice
  options:
    - "It increases without bound, proportionally to M₁², as the shock compresses the gas ever harder"
    - "It approaches a finite limit of (γ+1)/(γ−1), approximately 6 for air (γ = 1.4)"
    - "It approaches 1, as extremely strong shocks force both sides to the same density"
    - "It grows linearly with M₁ because mass flux conservation requires proportional density increase"
  answer: 1
  explanation: "While pressure and temperature ratios grow without bound as M₁ → ∞, density has a finite upper limit (γ+1)/(γ−1) ≈ 6 for air. The physical reason: as shock strength increases, temperature rises so dramatically that further pressure increases are absorbed by temperature rather than density (via the ideal gas law p = ρRT). The gas becomes too hot to compress much further. This density limit is important for hypersonic reentry vehicles — the shock-compressed air cannot be packed arbitrarily densely, which constrains heat transfer models."

- question: "Stagnation temperature is conserved across a normal shock, meaning if you brought the gas to rest isentropically before and after the shock, you would measure the same temperature in both cases."
  type: true-false
  answer: true
  explanation: "True. A normal shock is adiabatic — no heat transfer occurs across the shock boundary. By the energy equation for adiabatic flow, total enthalpy h₀ = h + V²/2 is conserved. Since h₀ = c_p T₀ for a perfect gas, stagnation temperature T₀ is the same upstream and downstream. The shock converts kinetic energy to thermal energy (static temperature rises, velocity falls), but the total — what you'd measure if you decelerated the gas to rest — is unchanged. This is why stagnation temperature is also called 'total temperature': it includes both the static temperature and the kinetic energy equivalent."

- question: "Stronger normal shocks (higher M₁) recover more stagnation pressure than weaker ones, which is why supersonic inlets use a single strong normal shock to efficiently decelerate incoming flow."
  type: true-false
  answer: false
  explanation: "False — this is exactly backwards. Stronger shocks generate more entropy and therefore lose more stagnation pressure. At M₁ = 1.5, p₀₂/p₀₁ ≈ 0.93 (7% loss). At M₁ = 3.0, p₀₂/p₀₁ ≈ 0.33 (67% loss). This is precisely why high-performance supersonic inlets use a series of weaker oblique shocks to decelerate flow gradually, with each weak shock producing less entropy than one strong normal shock. Stagnation pressure recovery is a critical measure of inlet efficiency — losses here degrade engine thrust and fuel economy."

- question: "Why do supersonic inlet designs use a series of oblique shocks rather than a single normal shock to decelerate flow from supersonic to subsonic speeds?"
  type: short-answer
  answer: "Each shock wave generates entropy irreversibly, and stagnation pressure loss is proportional to entropy production. A single strong normal shock at high Mach number produces far more entropy — and loses far more stagnation pressure — than multiple weaker shocks accomplishing the same total deceleration in stages. By using oblique shocks to progressively reduce the Mach number in steps, each shock operates at a lower local Mach number and produces less entropy. The cumulative stagnation pressure recovered through a multi-shock system is substantially higher than any single-shock design. The final weak normal shock closes out the deceleration to subsonic. Higher stagnation pressure recovery means more thrust from the same fuel and air."
  explanation: "The mathematics confirms this: stagnation pressure ratio p₀₂/p₀₁ approaches 1 as shock strength approaches zero (isentropic limit). Splitting one strong shock into N weaker shocks, each operating at a lower Mach number, improves total p₀ recovery. In the limit of infinitely many infinitesimally weak shocks, the deceleration becomes isentropic — a theoretical maximum. Real inlets approximate this with 2–4 oblique shocks. The tradeoff is mechanical complexity against thermodynamic efficiency."
```

## Explainer

From your study of normal shock waves and Mach number effects, you know that a normal shock is a thin discontinuity across which supersonic flow abruptly becomes subsonic. What the **Rankine-Hugoniot relations** — the shock relations — provide is a precise algebraic accounting of how much each property changes. The derivation applies conservation of mass, momentum, and energy across a thin control volume straddling the shock, along with the perfect-gas equation of state. The result is a set of equations expressing the downstream-to-upstream ratios of pressure, temperature, density, and Mach number entirely as functions of the upstream Mach number M₁.

The qualitative pattern is worth memorizing. Across a normal shock, pressure, temperature, and density all increase discontinuously. The Mach number drops from supersonic (M₁ > 1) to always subsonic (M₂ < 1). **Stagnation temperature** is conserved — the shock is adiabatic, so no heat crosses the boundary — but **stagnation pressure** decreases because entropy is generated irreversibly inside the shock. This entropy increase is the thermodynamic signature of the shock's irreversibility: no work is done on the fluid, no heat is added, yet entropy rises. The stronger the shock (larger M₁), the greater the entropy production and the greater the stagnation pressure loss.

The **normal shock table** encodes these relationships numerically. For any M₁, you can read off p₂/p₁, T₂/T₁, ρ₂/ρ₁, M₂, and the stagnation pressure ratio p₀₂/p₀₁. At M₁ = 1, all ratios equal 1 — infinitesimally weak shock, no change. As M₁ → ∞, pressure and temperature ratios grow without bound, but ρ₂/ρ₁ approaches a finite limit of (γ+1)/(γ−1) ≈ 6 for air. This density limit has a physical interpretation: the temperature rise increases pressure enough to resist further compression regardless of shock strength.

The engineering application that makes these relations critical is **supersonic inlet design**. In a jet engine flying at supersonic speed, air must be decelerated to subsonic conditions before entering the compressor. If a single strong normal shock accomplishes all the deceleration, the stagnation pressure loss is enormous — degrading thrust and fuel efficiency significantly. This is why military aircraft inlets use oblique shocks (your next topic) to perform the deceleration in multiple gentler steps, each producing lower entropy, recovering more stagnation pressure before the final, weakened normal shock closes out the deceleration.
