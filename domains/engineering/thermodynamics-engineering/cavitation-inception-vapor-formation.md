---
id: cavitation-inception-vapor-formation
title: Cavitation, Vapor Formation, and Flow Choking
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: two-phase-homogeneous-flow-equilibrium
  type: hard
- id: clausius-clapeyron-vapor-pressure
  type: hard
tags:
- cavitation
- vapor-formation
- choking
- sonic-flow
- critical-pressure
stage: advanced
status: draft
---

# Cavitation, Vapor Formation, and Flow Choking

## Core Idea
Cavitation occurs when local static pressure falls below saturation pressure, causing liquid to vaporize suddenly. In pumps and turbines, vapor bubbles collapse on higher-pressure regions, causing erosion and noise. Critical pressure for choking (sonic flow) in a nozzle occurs when dP/dM = 0, limiting mass flow rate. Cavitation number σ = (P - P_sat)/(0.5ρV²) predicts inception conditions.

## Explainer

From the Clausius-Clapeyron relation you already know, the saturation pressure P_sat is the pressure at which liquid and vapor coexist at a given temperature — it is a property of the fluid, not the flow. Cavitation exploits this fact in a destructive way: if you accelerate a liquid fast enough, Bernoulli's equation tells you the local static pressure must drop. If that local pressure drops below P_sat for the liquid's current temperature, the liquid has no choice but to begin forming vapor — it is effectively boiling, not from heat, but from a pressure drop. The vapor forms as **cavitation bubbles** that nucleate at surface defects or dissolved gas pockets.

The danger is not the bubble formation itself — it is the collapse. As the bubbles travel downstream into higher-pressure regions, the surrounding liquid pressure exceeds P_sat again and the vapor condenses almost instantaneously. The implosion is violent: inward-rushing liquid forms microscopic jets that strike adjacent solid surfaces at extremely high local stresses, pitting metal over time and generating audible crackling noise. Pump impellers, propeller blades, and turbine runners are the classic victims. The **cavitation number** σ = (P_ref − P_sat)/(½ρV²) quantifies the margin above inception: σ > σ_critical means you are safe; as σ approaches zero, cavitation begins. Engineers design to keep σ high by raising system pressure, reducing flow velocity, or selecting fluids with lower P_sat.

Flow **choking** is a related but distinct phenomenon that occurs in compressible or two-phase flows through converging nozzles. At the throat, flow reaches a critical condition (Mach 1 for gas flow; a critical void fraction in two-phase flow) beyond which the mass flow rate cannot increase regardless of how much the downstream pressure is reduced. The condition dP/dM = 0 — pressure gradient vanishes with respect to Mach number — marks this limit. In two-phase flows, choking is even more complex because the presence of vapor dramatically lowers the effective sonic velocity of the mixture, so choking can occur at velocities far below the liquid sonic speed.

Connecting both phenomena: in a pump operating near cavitation inception, vapor formation in the suction passage can choke the flow path, causing a sudden collapse in pump performance called **cavitation breakdown**. The head-flow curve shows a sharp knee where efficiency drops rapidly. This is why the **Net Positive Suction Head Available (NPSHA)** must exceed the **NPSH Required (NPSHR)** by a design margin — the engineer ensures that even at the lowest-pressure point in the suction line, P_local remains comfortably above P_sat.
