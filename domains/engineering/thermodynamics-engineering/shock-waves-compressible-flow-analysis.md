---
id: shock-waves-compressible-flow-analysis
title: Normal Shock Waves and Shock Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: normal-shock-waves
  type: hard
- id: isentropic-flow-with-area-change
  type: soft
tags:
- shock-waves
- compressible-flow
- entropy-generation
stage: advanced
status: draft
---

# Normal Shock Waves and Shock Analysis

## Core Idea
Normal shock waves are thin regions where supersonic flow decelerates to subsonic with large irreversible entropy increase. Rankine-Hugoniot relations govern pressure, temperature, and velocity jumps across the shock. Stagnation pressure always drops; entropy always increases. Shock location and strength significantly affect inlet pressure recovery in supersonic vehicles and compressor inlet conditions.

## Questions

```yaml
- question: "Across a normal shock wave, which of the following quantities is conserved (remains unchanged)?"
  type: multiple-choice
  options:
    - "Static pressure — the shock is thin so static pressure must equalize"
    - "Stagnation pressure — energy is conserved so total pressure must be constant"
    - "Stagnation temperature — the process is adiabatic so total enthalpy is conserved"
    - "Entropy — the flow through a shock is isentropic for a perfect gas"
  answer: 2
  explanation: "Stagnation temperature is conserved across a normal shock because the shock process is adiabatic — no heat is added or removed. Energy conservation (h₀ = h + V²/2 = constant) directly implies stagnation enthalpy and stagnation temperature are unchanged. However, stagnation pressure is NOT conserved: the irreversible viscous mixing inside the shock generates entropy, and entropy increase reduces stagnation pressure. Static pressure, density, and temperature all increase across the shock. A normal shock is decidedly not isentropic."

- question: "A supersonic aircraft inlet must decelerate incoming flow from Mach 2.5 to subsonic before it enters the engine. Why do designers use a series of oblique shocks rather than a single normal shock?"
  type: multiple-choice
  options:
    - "Oblique shocks are easier to create geometrically in an inlet duct"
    - "A single normal shock at Mach 2.5 produces a greater entropy rise and stagnation pressure loss than multiple weaker shocks; more but weaker shocks means less total entropy production and higher pressure recovery"
    - "Normal shocks always decelerate flow to exactly Mach 1, not to subsonic speeds, making them useless for inlet design"
    - "Oblique shocks avoid the flow separation that always occurs with normal shocks"
  answer: 1
  explanation: "Entropy rise across a shock increases nonlinearly with upstream Mach number. A single strong normal shock at M=2.5 produces much more entropy (and stagnation pressure loss) than the sum of multiple weaker shocks that achieve the same total deceleration. By decelerating gradually through a sequence of oblique shocks, each at a lower Mach number, the designer keeps each individual shock weak, minimizing entropy production at each step. The cumulative stagnation pressure loss is substantially less, preserving more total pressure for the engine and improving thrust and efficiency."

- question: "Stagnation temperature is conserved across a normal shock wave."
  type: true-false
  answer: true
  explanation: "Stagnation temperature T₀ = T(1 + (γ−1)/2 · M²) is conserved because the flow through a shock is adiabatic — no heat is transferred. Energy conservation (h₀ = constant) directly implies constant stagnation temperature. This is distinct from stagnation pressure, which is NOT conserved because entropy increases. The distinction between stagnation temperature (conserved) and stagnation pressure (not conserved) is central to shock analysis."

- question: "A stronger normal shock (higher upstream Mach number) produces less stagnation pressure loss than a weaker shock, because stronger shocks are more efficient at decelerating flow."
  type: true-false
  answer: false
  explanation: "The opposite is true. Stronger shocks produce greater entropy rises, which directly correspond to greater stagnation pressure losses. At M₁ = 1 (vanishingly weak shock), stagnation pressure loss is zero and entropy rise is negligible. As M₁ increases, both entropy rise and stagnation pressure drop grow rapidly and nonlinearly. This is precisely why supersonic inlet design avoids strong normal shocks — a single shock at high Mach number wastes far more stagnation pressure than a series of weaker shocks achieving the same total deceleration."

- question: "Why does stagnation pressure always drop across a normal shock, and why does this matter for jet engine performance?"
  type: short-answer
  answer: "Stagnation pressure represents the maximum static pressure recoverable if the flow were decelerated isentropically to rest. Across a shock, the process is irreversible — violent viscous and thermal mixing generates entropy. The second law requires entropy to increase, and for an adiabatic process, entropy increase is thermodynamically equivalent to stagnation pressure decrease. Once stagnation pressure is lost, it cannot be recovered downstream. For a jet engine, the inlet must deliver air at the highest possible stagnation pressure to the compressor — higher inlet stagnation pressure means higher achievable compression ratio and greater thrust. Every unit of stagnation pressure lost in the inlet directly reduces engine performance."
  explanation: "This connection between irreversibility (entropy generation), stagnation pressure loss, and engine efficiency is the thermodynamic core of compressible flow analysis. It explains inlet design (minimize shock strength), nozzle design (avoid internal shocks), and why total pressure recovery is the key figure of merit for supersonic propulsion systems."
```

## Explainer

From your study of isentropic flow with area change, you know that supersonic flow in a converging-diverging nozzle accelerates smoothly so long as boundary conditions are favorable. But what happens when supersonic flow encounters an abrupt obstacle or a back pressure that the flow cannot accommodate isentropically? The answer is a **shock wave** — a nearly discontinuous jump in flow properties that happens across a layer only a few mean-free-paths thick. Understanding shocks means understanding what the conservation equations demand when isentropic adjustment is impossible.

A **normal shock** stands perpendicular to the flow direction. Across it, three conservation laws apply simultaneously: conservation of mass (ρ₁V₁ = ρ₂V₂), conservation of momentum (p₁ + ρ₁V₁² = p₂ + ρ₂V₂²), and conservation of energy (h₁ + V₁²/2 = h₂ + V₂²/2). These three equations, combined with the equation of state for a perfect gas, give the **Rankine-Hugoniot relations** that express all downstream conditions purely as functions of the upstream Mach number M₁. The key results: pressure, temperature, and density all jump upward across the shock; velocity drops sharply; and M₂ < 1 always (supersonic flow always exits a normal shock as subsonic). You can look up these ratios in normal shock tables indexed by M₁.

The thermodynamics of the shock is what distinguishes it from isentropic flow. Because the process is irreversible — violent viscous and thermal mixing in an extremely thin region — **entropy increases** across the shock. On the h-s diagram, the downstream state lies to the right of the upstream state on the same stagnation enthalpy line (total enthalpy is conserved since the flow is adiabatic). Stagnation temperature is conserved, but **stagnation pressure drops** — this is the key performance penalty. Stagnation pressure represents the maximum pressure recoverable if the flow were decelerated isentropically; losing it means you cannot fully recover the flow's kinetic energy, which directly reduces thrust in a jet engine inlet or nozzle efficiency in a wind tunnel.

The strength of the shock is entirely determined by the upstream Mach number. At M₁ = 1, the shock degenerates to a vanishingly weak disturbance with zero entropy rise — this is the limit connecting shock analysis back to isentropic flow. As M₁ increases, pressure ratio and entropy rise grow rapidly. This is why supersonic inlet design tries to decelerate flow through a series of weaker oblique shocks rather than one strong normal shock: the entropy penalty of multiple weak shocks is lower than the penalty of a single strong one, preserving more stagnation pressure for the engine.

When working shock problems numerically, the approach is: identify M₁ from upstream conditions, use normal shock tables (or Mach-specific formulas) to find all property ratios across the shock, then apply isentropic flow relations separately on each side if the regions before and after the shock are themselves isentropic. Shocks are not isentropic, but the flow approaching the shock and the flow downstream of the shock (if no further shocks occur) may each be treated as isentropic within their respective regions.
