---
id: first-law-closed-systems
title: First Law of Thermodynamics for Closed Systems
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: energy-conservation-mechanical-systems
  type: soft
- id: energy-conservation-applications
  type: hard
builds-toward:
- first-law-open-systems
- rankine-cycle-thermodynamic-analysis
- brayton-cycle-gas-turbine
- otto-cycle-spark-ignition-engine
- refrigeration-thermodynamic-analysis
- exergy-concept-availability
tags:
- first-law
- energy-balance
- closed-systems
stage: formal-systems
status: draft
---

# First Law of Thermodynamics for Closed Systems

## Core Idea
The first law for a closed system states that energy change equals heat added minus work done by the system: ΔU = Q - W. This energy balance applies to any system undergoing any process and is the foundation for analyzing turbines, compressors, and heat exchangers with fixed mass. Identifying all forms of work (boundary, shaft) and heat transfer is critical to correct application.

## How It's Best Learned
Write the first law ΔU = Q - W for various processes (isothermal, isobaric, isochoric) and identify which terms vanish. Practice calculating work for boundary-displacement processes (W = ∫P dV) and recognize that polytropic processes (PVⁿ = const) are common idealizations. Always draw the system boundary clearly and identify work and heat at the boundary.

## Common Misconceptions
- The first law applies only to reversible processes; it applies to all processes.
- Work is always done by expanding gases and against compressing fluids; work can be done on a gas by compression or by a gas through expansion or shaft rotation.
- ΔU depends on the path taken; internal energy is a state function and depends only on initial and final states.

## Questions

```yaml
- question: "A gas sealed in a rigid container (fixed volume) absorbs 300 J of heat. What is the change in internal energy?"
  type: multiple-choice
  options: ["ΔU = 0 J", "ΔU = 300 J", "ΔU = -300 J", "Cannot be determined without knowing the pressure"]
  answer: 1
  explanation: "In a rigid container, the volume cannot change, so no boundary work is done: W = ∫P dV = 0. Applying the first law, ΔU = Q − W = 300 − 0 = 300 J. All the heat input goes directly into raising the internal energy. Pressure data is irrelevant here because work is zero regardless of pressure when volume is fixed."

- question: "If the same gas is compressed from state A to state B quickly (irreversibly) and then slowly (quasi-statically), the change in internal energy ΔU will be different for the two processes."
  type: true-false
  answer: false
  explanation: "Internal energy U is a state function — it depends only on the thermodynamic state (temperature, pressure, composition), not on the path taken to reach that state. Both processes end at state B, so ΔU = U_B − U_A is identical. What differs between the two processes is the work W and heat Q exchanged with the surroundings, which must change together to keep ΔU the same."

- question: "A piston-cylinder device contains steam that is heated while the piston moves outward. Identify Q and W in ΔU = Q − W and explain the sign of each."
  type: short-answer
  answer: "Q is positive because heat is added to the system (heat flows in). W is positive because the system does work on the surroundings as the piston expands outward (W = ∫P dV > 0 for expansion). ΔU equals Q minus W, so the internal energy increase is the net of heat added minus work done by the steam."
  explanation: "The sign convention ΔU = Q − W treats heat added to the system as positive and work done by the system as positive. Expansion does positive work on the surroundings, reducing internal energy relative to what heat alone would provide. If the steam expands a lot, it may do nearly as much work as the heat added, resulting in a small ΔU despite significant Q."
```

## Explainer

The first law of thermodynamics for a closed system is an energy balance: the change in a system's internal energy equals the heat transferred into the system minus the work done by the system. Written compactly: ΔU = Q − W. This single equation governs steam engines, refrigerators, internal combustion engines, and any other device where a fixed mass of working fluid absorbs or releases energy.

A **closed system** has fixed mass — no matter crosses the boundary — but energy can cross as heat or work. The system boundary is a conceptual surface you draw around the substance of interest. Heat Q is energy transfer driven by a temperature difference across that boundary; it is positive when flowing in. Work W is energy transfer through mechanical interaction (a moving piston, a rotating shaft); it is positive when the system does work on the surroundings. Getting the sign convention right and drawing a clear boundary before writing any equations prevents most first-law errors.

The most important thing to understand about internal energy U is that it is a **state function**: it depends only on the thermodynamic state (characterized by properties like temperature and pressure), not on how the system arrived at that state. This means ΔU = U_final − U_initial, full stop — the path does not matter. Contrast this with Q and W individually, which are path-dependent. A slow isothermal compression and a fast irreversible compression between the same two states will have different Q and different W, but the same ΔU. This is why the first law is so powerful: even when you do not know the details of a process, you can compute ΔU from any convenient path.

For boundary work in a simple compressible system, W = ∫P dV. Three process types are especially common: **isochoric** (constant volume, dV = 0, so W = 0 and ΔU = Q), **isobaric** (constant pressure, W = PΔV), and **isothermal** (constant temperature, ΔU = 0 for an ideal gas, so Q = W). The polytropic process PVⁿ = constant generalizes all three: n = 0 is isobaric, n = 1 is isothermal for ideal gases, n = γ is adiabatic (no heat transfer), and n → ∞ is isochoric. Recognizing which process applies tells you immediately which terms in ΔU = Q − W are zero or simplified, making the calculation tractable.
