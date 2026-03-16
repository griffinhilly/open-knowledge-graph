---
id: two-phase-homogeneous-flow-equilibrium
title: Two-Phase Flow and Homogeneous Equilibrium Model
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressible-flow-isentropic-flow
  type: hard
- id: saturated-superheated-property-regions
  type: hard
- id: gibbs-phase-rule-multicomponent
  type: soft
builds-toward:
- cavitation-inception-vapor-formation
tags:
- two-phase
- homogeneous-equilibrium
- quality
- slip-ratio
- pressure-drop
stage: advanced
status: draft
---

# Two-Phase Flow and Homogeneous Equilibrium Model

## Core Idea
The homogeneous equilibrium model assumes liquid and vapor move together (slip ratio = 1) in thermal and mechanical equilibrium. Properties are quality-weighted: v = v_f + x(v_g - v_f). This simplification works for slow processes; rapid flashing or separation requires slip-flow models. Application to choked flow, pump cavitation, and turbine exit conditions is essential in power engineering.

## Explainer

When vapor and liquid coexist in a flowing system — inside a boiling tube, downstream of a throttle valve, at the exit of a steam turbine — you have **two-phase flow**. In principle, liquid and vapor can move at different velocities, forming complex structures like bubbles, slugs, or annular films. But in many engineering calculations, especially near thermodynamic equilibrium, a powerful simplification works: assume the two phases travel together at the same velocity and are always in thermal equilibrium with each other. This is the **homogeneous equilibrium model (HEM)**.

The HEM's defining assumption is that the **slip ratio** S = vᵥ/vₗ = 1 — vapor and liquid velocities are identical. With this, the two-phase mixture behaves as a single pseudo-fluid whose properties are quality-weighted averages. Specific volume becomes **v = vₗ + x(vᵥ − vₗ)**, where x is **quality** (vapor mass fraction) and vₗ, vᵥ are the saturated liquid and vapor specific volumes from your property tables. Similarly, enthalpy: **h = hₗ + x hₗᵥ**, and entropy: **s = sₗ + x sₗᵥ**. These mixing rules, which you've already used when working with saturated property regions, now apply to a flowing mixture. The full toolbox of single-phase compressible-flow analysis — continuity, momentum, and energy equations — carries over directly, using mixture properties in place of single-phase ones.

The HEM is particularly powerful for **choked flow** calculations. Recall from compressible flow that choking occurs when the local flow velocity reaches the speed of sound, creating a maximum in mass flow rate that no downstream pressure reduction can exceed. In two-phase flow, the **mixture speed of sound** is dramatically lower than in either pure phase alone — sometimes only a few meters per second, compared to ~1500 m/s in liquid water. This happens because the mixture combines the high compressibility of vapor (which compresses readily under pressure) with the high density of liquid, and low sound speed results from high compressibility at moderate density. Choking at low velocities explains why two-phase relief valves and rupture discs behave very differently from single-phase devices, and why HEM is the standard first model in nuclear and process safety analysis for sizing pressure-relief systems.

The limits of the HEM are as important as its application. The assumption S = 1 breaks down when flow velocities are high, when the pipe is vertical (buoyancy drives vapor upward), or when liquid-vapor density ratios are large. In these regimes, vapor rises above liquid due to buoyancy-driven **slip**, and the actual void fraction (volume fraction of vapor) exceeds the HEM prediction — meaning less liquid is present than the model assumes. For design cases requiring high accuracy, engineers use void-fraction correlations (such as the Lockhart-Martinelli parameter) or full two-fluid models that track each phase separately. But the HEM provides the essential baseline: a rapid, closed-form estimate of mixture properties, pressure drop, and choking conditions that is exact in the equilibrium limit and usefully conservative in many safety applications.
