---
id: compressible-flow-thermodynamic-relations
title: Thermodynamic Relations in Compressible Flow
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: steady-flow-energy-equation-engineering
  type: soft
builds-toward:
- isentropic-flow-with-area-change
- shock-waves-compressible-flow-analysis
tags:
- compressible-flow
- thermodynamics
- isentropic
- mach
stage: formal-systems
status: validated
---

# Thermodynamic Relations in Compressible Flow

## Core Idea
In compressible flow, kinetic energy and enthalpy are interchangeable via the steady-flow equation. Stagnation properties (T₀, h₀, p₀) are constant along streamlines for adiabatic flow. Mach number M = V/a (sound speed a = √γRT) is the key non-dimensional parameter governing flow regime: subsonic (M < 1), transonic (M ≈ 1), supersonic (M > 1).

## Questions

```yaml
- question: "A gas accelerates through an adiabatic converging nozzle, increasing from M = 0.3 to M = 0.7. What happens to the static temperature of the gas?"
  type: multiple-choice
  options:
    - "It increases, because faster-moving gas carries more thermal energy"
    - "It stays the same, because temperature is a state property independent of velocity"
    - "It decreases, because kinetic energy increases at the expense of internal thermal energy"
    - "It equals the stagnation temperature throughout the nozzle"
  answer: 2
  explanation: "The key is the conservation of stagnation enthalpy h₀ = h + V²/2 = cₚT + V²/2. Because the flow is adiabatic, h₀ (and therefore T₀) is constant. As the gas accelerates, V²/2 increases, so cₚT must decrease — static temperature falls. This is counterintuitive to students who associate 'more energy' with 'higher temperature,' but kinetic energy and thermal energy are both forms of energy that trade off within a fixed total budget. Option A reverses the trade-off; option D confuses static and stagnation temperature."

- question: "Why can pressure disturbances not travel upstream in supersonic flow?"
  type: multiple-choice
  options:
    - "Supersonic flow compresses the gas so much that pressure waves cannot form"
    - "Viscosity increases at high Mach numbers, damping out all disturbances"
    - "The flow velocity exceeds the local speed of sound, so pressure waves propagating upstream are swept downstream faster than they can advance"
    - "Shocks at the inlet absorb all pressure information before it can propagate"
  answer: 2
  explanation: "Pressure disturbances propagate as sound waves at speed a relative to the fluid. Upstream propagation requires the wave to move against the flow. In subsonic flow (V < a), a wave traveling at speed a in the upstream direction still makes net upstream progress, so information reaches all parts of the flow. In supersonic flow (V > a), the flow sweeps any wave downstream faster than the wave can travel upstream — net upstream speed is negative. The flow is literally outrunning its own pressure signals. This is why supersonic flow cannot 'feel' downstream conditions and behaves fundamentally differently, leading to phenomena like shock waves."

- question: "Stagnation temperature remains constant along a streamline in an adiabatic nozzle, even as the local flow velocity changes dramatically."
  type: true-false
  answer: true
  explanation: "This is the direct consequence of energy conservation for adiabatic, no-work flow. The steady-flow energy equation gives h₀ = h + V²/2 = const along a streamline when there is no heat transfer and no shaft work. Because h = cₚT for a calorically perfect gas, T₀ = T + V²/(2cₚ) is also constant. The stagnation temperature represents the total thermal equivalent of the flow's energy — it can be partitioned between internal energy (static temperature) and kinetic energy differently at different locations, but the total is conserved."

- question: "At M = 1 (sonic flow), the static temperature equals the stagnation temperature because most kinetic energy has been converted into thermal energy at the throat."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. At M = 1, the flow is moving at the speed of sound — it has significant kinetic energy. The isentropic relation gives T/T₀ = 2/(γ+1), which for air (γ = 1.4) yields T/T₀ = 0.833. Static temperature is about 17% lower than stagnation temperature at the sonic point. Static temperature equals stagnation temperature only at M = 0 (a fluid at rest), where all energy is internal. As M increases, an increasing fraction of the total energy is kinetic, so static temperature progressively drops below stagnation temperature."

- question: "Why is Mach number — rather than flow speed alone — the key parameter governing compressible flow behavior?"
  type: short-answer
  answer: "Mach number M = V/a compares flow speed to the local speed of sound, which is the speed at which pressure information propagates through the fluid. What matters physically is not how fast the gas moves in an absolute sense, but whether it moves faster or slower than its own pressure signals. Below M = 1, pressure disturbances can travel in all directions, the flow 'knows' about downstream conditions, and gradual adjustments occur. Above M = 1, no pressure information travels upstream, the flow is blind to what lies ahead, and fundamentally different phenomena (shock waves, expansion fans) emerge. Two flows at the same speed but different temperatures have different sound speeds and thus different Mach numbers — and completely different physics."
  explanation: "A concrete example: air at 300 m/s and 300 K has a ≈ 347 m/s, so M ≈ 0.86 (subsonic). The same 300 m/s air at 200 K has a ≈ 283 m/s, so M ≈ 1.06 (supersonic) — with shocks and discontinuous pressure changes. The speed is identical, but the physics is completely different because the Mach number crosses 1. This is why all the governing equations of compressible flow are written in terms of M, not V."
```

## Explainer

From the steady-flow energy equation you already know, the total enthalpy of a flowing fluid is the sum of its thermodynamic enthalpy h and its kinetic energy per unit mass V²/2. For an adiabatic flow with no shaft work — a nozzle or diffuser — this total, called the **stagnation enthalpy** h₀ = h + V²/2, is conserved along every streamline. Think of stagnation enthalpy as the "energy budget" of the flow: speed and thermal energy can trade off, but their sum stays fixed. For a calorically perfect gas (constant specific heats), h = cₚT, so stagnation enthalpy maps directly to a **stagnation temperature** T₀ = T + V²/(2cₚ), the temperature the gas would reach if brought to rest adiabatically.

The **speed of sound** a = √(γRT) is where thermodynamics meets wave mechanics. Sound is a pressure wave, and its propagation speed depends on how the gas responds elastically to compression — quantified by γ, the ratio of specific heats. Because γ and R are fluid properties, the sound speed depends only on temperature: hotter gas propagates sound faster. The **Mach number** M = V/a compares the flow speed to the local sound speed and is the single most important parameter in compressible flow. It tells you not just how fast the gas is moving, but how the flow "knows about" downstream conditions. In subsonic flow (M < 1), pressure disturbances can travel upstream and the flow adjusts continuously. In supersonic flow (M > 1), information cannot travel upstream — the flow cannot "feel" what is coming — which leads to fundamentally different behavior such as shock waves.

The stagnation-to-static ratios connect thermodynamics to Mach number through the isentropic relations. For isentropic (adiabatic, reversible) flow: T₀/T = 1 + (γ−1)/2 · M². The pressure and density ratios follow from the isentropic process relations: p₀/p = (T₀/T)^(γ/(γ−1)). These ratios have a clear physical story: as M increases, more of the flow's energy is in kinetic form, so the static (thermodynamic) temperature and pressure drop relative to their stagnation values. At M = 0, stagnation and static properties are identical — as they should be for a fluid at rest. At M = 1, T/T₀ = 2/(γ+1), the so-called **critical temperature ratio**, a landmark value that appears throughout compressible flow analysis.

The power of stagnation properties as a working tool is that they are constant throughout an adiabatic nozzle or diffuser — no matter how the velocity changes. This means you can characterize an entire flow field by just two numbers: the stagnation state (T₀, p₀) and the local Mach number. Given M and the stagnation state, you can recover all local static properties. The approach is: (1) identify T₀ and p₀ from reservoir or inlet conditions, (2) use the Mach number relation of interest to find local M, (3) invert the isentropic ratios to find T, p, ρ. Every compressible flow calculation in nozzles, diffusers, and flow-with-area-change follows this three-step pattern.
