---
id: thermodynamic-availability-exergy
title: Thermodynamic Availability and Exergy
domain: physics
course: thermodynamics
prerequisites:
- id: second-law-of-thermodynamics
  type: hard
- id: gibbs-free-energy
  type: soft
tags:
- second-law
- useful-work
- efficiency
stage: advanced
status: draft
---

# Thermodynamic Availability and Exergy

## Core Idea
Availability (or exergy) is the maximum useful work that can be extracted from a system as it comes into equilibrium with the environment at (T_0, P_0); it is defined as Ψ = (U - U_0) - T_0(S - S_0) + P_0(V - V_0). Unlike the first law's internal energy, availability accounts for the second law and distinguishes between reversible (maximum) and irreversible work. Thermodynamic availability is crucial for assessing the true efficiency of real processes and the economic value of fuels and energy resources.

## How It's Best Learned
Calculate availability for various systems relative to environmental conditions. Compare with work actually obtained from real processes. Identify sources of irreversibility.

## Common Misconceptions
- Thinking all internal energy can be converted to useful work (second law forbids this).
- Confusing availability with enthalpy or Gibbs free energy.
- Assuming availability is the same regardless of environmental conditions (it depends on T_0, P_0).

## Explainer

The second law of thermodynamics tells you that not all energy is equally useful: heat at low temperature cannot be fully converted to work, while work can be fully converted to heat. But how do you put a precise number on how much useful work a given system can deliver? **Availability** (also called **exergy**) is that number. It is the maximum useful work extractable as the system is brought reversibly into complete equilibrium with the environment — the **dead state** at temperature T₀ and pressure P₀.

The formula Ψ = (U − U₀) − T₀(S − S₀) + P₀(V − V₀) has three terms that each carry physical meaning. The first, U − U₀, is the internal energy above the dead state — the first law's contribution. The second, −T₀(S − S₀), is a second-law correction: entropy above the dead state represents "disorder" that the environment at T₀ cannot use, so it subtracts from availability; entropy below the dead state means the system has more order than the environment, which is itself useful. The third, P₀(V − V₀), accounts for the work the atmosphere does on you when the system contracts: you cannot count that as your useful output since you had to push back against P₀ to get it. The combination is exactly the maximum work you can extract after accounting for both thermodynamic limits.

The connection to Gibbs free energy your prerequisite introduced is illuminating. At constant temperature T₀ and pressure P₀, availability reduces to the Gibbs free energy difference: Ψ = G − G₀. This is why Gibbs free energy is the right criterion for chemical equilibrium — it tells you when no more useful work can be extracted. Availability is the generalization to arbitrary temperatures and pressures, tracking useful work potential across any process that ends at the dead state.

In practice, availability analysis reveals where real processes waste work. The **exergy destruction** in any irreversible process equals T₀ times the entropy generated: W_destroyed = T₀ΔS_gen. A heat exchanger with a temperature cross, a throttle valve, a compressor with friction — all generate entropy and therefore destroy availability irreversibly. By computing the availability entering and leaving each component of an engineering system, you can rank the biggest sources of inefficiency and prioritize improvements. This is why exergy analysis has become standard in the design of power plants, refrigeration systems, and chemical processes — it answers not just "how efficient is this?" but "where exactly is the potential for improvement?"
