---
id: exergy-balance-control-volume
title: Exergy (Availability) Balance for Control Volumes
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: exergy-concept-availability
  type: hard
- id: control-volume-steady-flow
  type: hard
- id: second-law-thermodynamics-entropy
  type: hard
builds-toward:
- second-law-efficiency-exergy-based
- chemical-exergy-fuel-combustion
tags:
- exergy
- availability
- second-law
- irreversibility
- optimal-work
stage: advanced
status: draft
---

# Exergy (Availability) Balance for Control Volumes

## Core Idea
Exergy balance extends the second law to control volumes, quantifying the maximum useful work available from a stream or device relative to the environment. The exergy balance is Ėx_in - Ėx_out = Ẇ_useful,max - Ẇ_actual + T₀Ṡ_gen. Exergy destruction due to irreversibility determines true thermodynamic efficiency and identifies optimization opportunities.

## Explainer

Your prerequisite on exergy established the concept of **availability**: the maximum useful work extractable from a system as it comes into equilibrium with its environment — the **dead state** at temperature T₀ and pressure P₀. Your study of steady-flow control volumes gave you the energy balance: energy in equals energy out plus work done, with enthalpy carrying energy across boundaries. Exergy balance for control volumes fuses these two ideas: it asks not just where energy goes, but how much of it remains *useful* after each process step.

The key departure from energy balance is that exergy, unlike energy, is *destroyed* by irreversibility. Energy is conserved (first law); exergy is not. Every irreversible process — friction, heat transfer across a temperature gradient, mixing, pressure drop through a valve — destroys exergy at a rate Ẋ_destroyed = T₀·Ṡ_gen. The entropy generation rate Ṡ_gen comes from your second-law prerequisite: it is always ≥ 0, with equality only for reversible processes. So the exergy balance for a steady-flow control volume is: Ẋ_in − Ẋ_out − Ẋ_destroyed = 0, where Ẋ_destroyed = T₀·Ṡ_gen quantifies the irreversibility. This term is what distinguishes real devices from ideal ones.

The **flow exergy** carried by a fluid stream is ψ = (h − h₀) − T₀(s − s₀) + V²/2 + gz — the specific exergy per unit mass. Notice it combines enthalpy departure from the dead state (the "thermomechanical" part), an entropy penalty scaled by T₀, plus kinetic and potential energy terms. When a stream enters a turbine at high exergy and leaves at lower exergy, the difference should appear as useful shaft work. If actual shaft work is less than the exergy drop, the shortfall is exergy destruction — it went to raising entropy, irretrievably lost. Applying the exergy balance to a turbine: Ẋ_in − Ẋ_out = Ẇ_actual + T₀Ṡ_gen. The first term is what you could theoretically extract; the second is what you actually get; the third is what irreversibility cost you.

This analysis is how engineers pinpoint where thermodynamic losses occur in complex systems. A first-law energy analysis of a power plant might show 35% efficiency and conclude that 65% of energy is "lost" — but most of that loss is heat rejected to the condenser, which is *supposed* to happen. An exergy analysis reveals the *avoidable* losses: where real processes deviate from reversible ones, expressed as T₀Ṡ_gen for each component. The combustor typically destroys the most exergy (high-temperature combustion is inherently irreversible), followed by heat exchangers with large temperature differences. This component-by-component **exergy destruction accounting** is the diagnostic tool that guides where to invest in efficiency improvement.

The **second-law efficiency** (or exergy efficiency) defined as η_II = Ẇ_actual / Ẇ_max = 1 − Ẋ_destroyed/Ẋ_in gives a true measure of how well a device approaches its thermodynamic limit. A heat pump with η_II = 0.7 is performing 70% as well as a reversible heat pump in the same conditions — a meaningful benchmark that the first-law COP cannot provide alone. The exergy balance thus closes the loop between the three prerequisites: it uses the entropy generation framework from the second law, applies it to steady-flow streams from control volume analysis, and measures deviations from the ideal exergy potential you defined in your exergy prerequisite.
