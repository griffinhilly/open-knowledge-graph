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
stage: formal-systems
status: validated
---

# Exergy (Availability) Balance for Control Volumes

## Core Idea
Exergy balance extends the second law to control volumes, quantifying the maximum useful work available from a stream or device relative to the environment. The exergy balance is Ėx_in - Ėx_out = Ẇ_useful,max - Ẇ_actual + T₀Ṡ_gen. Exergy destruction due to irreversibility determines true thermodynamic efficiency and identifies optimization opportunities.

## Questions

```yaml
- question: "A first-law energy analysis of a power plant shows 65% of fuel energy is 'lost,' with most of that attributed to heat rejected in the condenser. An exergy analysis then reveals that the combustor — not the condenser — is responsible for the largest avoidable losses. Why does the first-law analysis fail to identify the combustor as the priority for efficiency improvement?"
  type: multiple-choice
  options:
    - "First-law analysis ignores the combustor because it is not a heat exchanger"
    - "First-law analysis tracks energy quantity but not quality — it cannot distinguish unavoidable heat rejection from irreversible destruction of useful work potential"
    - "The combustor operates at such high temperatures that calorimetric measurements are unreliable"
    - "Entropy generation in the combustor is zero because the reaction is exothermic"
  answer: 1
  explanation: "The first law says energy is conserved — it accounts for where energy goes but not how much useful work potential is destroyed along the way. Condenser heat rejection is 'large' by energy accounting but mostly unavoidable. The combustor destroys enormous exergy because high-temperature combustion is inherently irreversible (large entropy generation at high T). Only exergy analysis — which penalizes entropy generation via T₀Ṡ_gen — reveals this distinction."

- question: "What is the physical meaning of the term T₀Ṡ_gen in the exergy balance for a control volume?"
  type: multiple-choice
  options:
    - "The heat transferred to the environment at the dead-state temperature T₀"
    - "The maximum shaft work the device could produce under reversible conditions"
    - "The rate at which useful work potential is irretrievably destroyed by irreversible processes inside the control volume"
    - "The entropy of the fluid stream entering the system boundary"
  answer: 2
  explanation: "T₀Ṡ_gen is the exergy destruction rate: the product of the dead-state temperature and the entropy generation rate. Since entropy generation is always ≥ 0 (second law), T₀Ṡ_gen ≥ 0 — exergy can only be destroyed, never created by irreversibility. It quantifies the gap between what a reversible device would deliver and what the real device actually delivers: the irretrievable penalty for friction, mixing, heat transfer across gradients, and other irreversibilities."

- question: "Exergy is destroyed whenever heat is transferred across a finite temperature difference, even though the total energy involved is conserved."
  type: true-false
  answer: true
  explanation: "True. The first law is satisfied — energy is conserved in the heat transfer. But heat flowing from a hot reservoir to a cold one generates entropy (Ṡ_gen = Q/T_cold − Q/T_hot > 0 for finite ΔT), and that entropy generation destroys exergy at rate T₀Ṡ_gen. This is why heat exchangers with large temperature differences are significant sources of exergy destruction even when no energy is 'lost.'"

- question: "A device that converts 95% of its input energy into useful output (near-perfect first-law efficiency) must also have near-perfect second-law (exergy) efficiency."
  type: true-false
  answer: false
  explanation: "False. A throttle valve, for example, converts essentially 100% of its inlet enthalpy into outlet enthalpy (ΔH ≈ 0, first-law efficiency ≈ 100%) yet destroys significant exergy through irreversible pressure drop. The second-law efficiency measures how close actual performance is to the reversible limit in terms of useful work potential, not energy quantity. A device can be first-law efficient while performing far below its thermodynamic optimum."

- question: "Explain why exergy destruction — rather than energy 'loss' — is the appropriate diagnostic for identifying where to invest in efficiency improvements in a complex thermodynamic system."
  type: short-answer
  answer: "Energy is conserved by the first law, so it is never truly 'lost' — it merely changes form or location. In a power plant, most of the energy that leaves as condenser heat is unavoidable and not improvable. Exergy destruction, T₀Ṡ_gen, measures only the irreversible penalty: the work potential permanently destroyed by irreversibilities such as friction, heat transfer across temperature gradients, and mixing. By computing exergy destruction for each component, engineers can rank them by how much avoidable loss each causes, and direct investment toward those with the greatest improvement potential. Without this, optimization efforts may target large energy flows that are actually unavoidable rather than the smaller but improvable irreversibilities."
  explanation: "The key insight is that second-law analysis converts the second law from a qualitative principle ('irreversibility costs you something') into a quantitative accounting tool. Component-by-component exergy destruction accounting gives engineers a ranked list of thermodynamic liabilities, which is impossible to construct from energy balances alone."
```

## Explainer

Your prerequisite on exergy established the concept of **availability**: the maximum useful work extractable from a system as it comes into equilibrium with its environment — the **dead state** at temperature T₀ and pressure P₀. Your study of steady-flow control volumes gave you the energy balance: energy in equals energy out plus work done, with enthalpy carrying energy across boundaries. Exergy balance for control volumes fuses these two ideas: it asks not just where energy goes, but how much of it remains *useful* after each process step.

The key departure from energy balance is that exergy, unlike energy, is *destroyed* by irreversibility. Energy is conserved (first law); exergy is not. Every irreversible process — friction, heat transfer across a temperature gradient, mixing, pressure drop through a valve — destroys exergy at a rate Ẋ_destroyed = T₀·Ṡ_gen. The entropy generation rate Ṡ_gen comes from your second-law prerequisite: it is always ≥ 0, with equality only for reversible processes. So the exergy balance for a steady-flow control volume is: Ẋ_in − Ẋ_out − Ẋ_destroyed = 0, where Ẋ_destroyed = T₀·Ṡ_gen quantifies the irreversibility. This term is what distinguishes real devices from ideal ones.

The **flow exergy** carried by a fluid stream is ψ = (h − h₀) − T₀(s − s₀) + V²/2 + gz — the specific exergy per unit mass. Notice it combines enthalpy departure from the dead state (the "thermomechanical" part), an entropy penalty scaled by T₀, plus kinetic and potential energy terms. When a stream enters a turbine at high exergy and leaves at lower exergy, the difference should appear as useful shaft work. If actual shaft work is less than the exergy drop, the shortfall is exergy destruction — it went to raising entropy, irretrievably lost. Applying the exergy balance to a turbine: Ẋ_in − Ẋ_out = Ẇ_actual + T₀Ṡ_gen. The first term is what you could theoretically extract; the second is what you actually get; the third is what irreversibility cost you.

This analysis is how engineers pinpoint where thermodynamic losses occur in complex systems. A first-law energy analysis of a power plant might show 35% efficiency and conclude that 65% of energy is "lost" — but most of that loss is heat rejected to the condenser, which is *supposed* to happen. An exergy analysis reveals the *avoidable* losses: where real processes deviate from reversible ones, expressed as T₀Ṡ_gen for each component. The combustor typically destroys the most exergy (high-temperature combustion is inherently irreversible), followed by heat exchangers with large temperature differences. This component-by-component **exergy destruction accounting** is the diagnostic tool that guides where to invest in efficiency improvement.

The **second-law efficiency** (or exergy efficiency) defined as η_II = Ẇ_actual / Ẇ_max = 1 − Ẋ_destroyed/Ẋ_in gives a true measure of how well a device approaches its thermodynamic limit. A heat pump with η_II = 0.7 is performing 70% as well as a reversible heat pump in the same conditions — a meaningful benchmark that the first-law COP cannot provide alone. The exergy balance thus closes the loop between the three prerequisites: it uses the entropy generation framework from the second law, applies it to steady-flow streams from control volume analysis, and measures deviations from the ideal exergy potential you defined in your exergy prerequisite.
