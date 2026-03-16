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
stage: advanced
status: draft
---

# Thermodynamic Relations in Compressible Flow

## Core Idea
In compressible flow, kinetic energy and enthalpy are interchangeable via the steady-flow equation. Stagnation properties (T₀, h₀, p₀) are constant along streamlines for adiabatic flow. Mach number M = V/a (sound speed a = √γRT) is the key non-dimensional parameter governing flow regime: subsonic (M < 1), transonic (M ≈ 1), supersonic (M > 1).

## Explainer

From the steady-flow energy equation you already know, the total enthalpy of a flowing fluid is the sum of its thermodynamic enthalpy h and its kinetic energy per unit mass V²/2. For an adiabatic flow with no shaft work — a nozzle or diffuser — this total, called the **stagnation enthalpy** h₀ = h + V²/2, is conserved along every streamline. Think of stagnation enthalpy as the "energy budget" of the flow: speed and thermal energy can trade off, but their sum stays fixed. For a calorically perfect gas (constant specific heats), h = cₚT, so stagnation enthalpy maps directly to a **stagnation temperature** T₀ = T + V²/(2cₚ), the temperature the gas would reach if brought to rest adiabatically.

The **speed of sound** a = √(γRT) is where thermodynamics meets wave mechanics. Sound is a pressure wave, and its propagation speed depends on how the gas responds elastically to compression — quantified by γ, the ratio of specific heats. Because γ and R are fluid properties, the sound speed depends only on temperature: hotter gas propagates sound faster. The **Mach number** M = V/a compares the flow speed to the local sound speed and is the single most important parameter in compressible flow. It tells you not just how fast the gas is moving, but how the flow "knows about" downstream conditions. In subsonic flow (M < 1), pressure disturbances can travel upstream and the flow adjusts continuously. In supersonic flow (M > 1), information cannot travel upstream — the flow cannot "feel" what is coming — which leads to fundamentally different behavior such as shock waves.

The stagnation-to-static ratios connect thermodynamics to Mach number through the isentropic relations. For isentropic (adiabatic, reversible) flow: T₀/T = 1 + (γ−1)/2 · M². The pressure and density ratios follow from the isentropic process relations: p₀/p = (T₀/T)^(γ/(γ−1)). These ratios have a clear physical story: as M increases, more of the flow's energy is in kinetic form, so the static (thermodynamic) temperature and pressure drop relative to their stagnation values. At M = 0, stagnation and static properties are identical — as they should be for a fluid at rest. At M = 1, T/T₀ = 2/(γ+1), the so-called **critical temperature ratio**, a landmark value that appears throughout compressible flow analysis.

The power of stagnation properties as a working tool is that they are constant throughout an adiabatic nozzle or diffuser — no matter how the velocity changes. This means you can characterize an entire flow field by just two numbers: the stagnation state (T₀, p₀) and the local Mach number. Given M and the stagnation state, you can recover all local static properties. The approach is: (1) identify T₀ and p₀ from reservoir or inlet conditions, (2) use the Mach number relation of interest to find local M, (3) invert the isentropic ratios to find T, p, ρ. Every compressible flow calculation in nozzles, diffusers, and flow-with-area-change follows this three-step pattern.
