---
id: enthalpy-definition-and-significance
title: Enthalpy and Its Physical Significance
domain: physics
course: thermodynamics
prerequisites:
- id: internal-energy-microscopic-view
  type: hard
- id: heat-and-internal-energy
  type: soft
tags:
- enthalpy
- state-function
- open-systems
stage: formal-systems
status: draft
---

# Enthalpy and Its Physical Significance

## Core Idea
Enthalpy (H = U + PV) combines internal energy with flow work. It is the appropriate state function for processes at constant pressure, where the heat absorbed equals the enthalpy change: Q_p = ΔH. Enthalpy is particularly useful in engineering for open systems like compressors and turbines.

## Explainer

From internal energy and the first law, you know that the energy change of a closed system is ΔU = Q − W, where W = PΔV for a simple expansion against a constant pressure. If you do a reaction or process at constant volume (a sealed bomb calorimeter, say), no expansion work is done and all the heat appears as ΔU. But most chemistry and much engineering happens at constant pressure — in open containers, in the atmosphere. At constant pressure, some of the energy released by a reaction goes into pushing the atmosphere back (PΔV work), and that work is not available as heat. **Enthalpy** H = U + PV is defined precisely to keep track of this.

At constant pressure: ΔH = ΔU + PΔV. The first law gives Q_p = ΔU + PΔV = ΔH. So the heat absorbed at constant pressure equals the enthalpy change — full stop, no need to separately track expansion work. This makes enthalpy the natural energy currency for chemistry. When you burn methane at atmospheric pressure and measure the heat released, you are measuring ΔH_combustion. When you dissolve a salt in water and the solution gets cold, you are experiencing an endothermic ΔH_dissolution. Chemists tabulate **standard enthalpies of formation** (ΔH°_f) precisely because constant-pressure calorimetry is universal in lab settings.

The PV term in H has a concrete physical meaning in open systems: it represents **flow work**, the energy required to push a unit of fluid into (or out of) a control volume against the prevailing pressure. Imagine a turbine: high-pressure steam enters, does work on the blades, and low-pressure steam exits. For the steady-flow energy balance, you must account not just for the internal energy of the steam but also for the work done to push the fluid through the inlet and outlet. The enthalpy H = U + PV automatically includes this flow work, which is why engineers always use H (not U) when writing energy balances for compressors, turbines, nozzles, and heat exchangers.

A useful heuristic: choose U when volume is fixed; choose H when pressure is fixed. Both are **state functions** — their values depend only on the current thermodynamic state, not on how you got there. This means you can use Hess's law: ΔH for a reaction is the same regardless of the reaction pathway, allowing you to add known ΔH values for sub-reactions to compute ΔH for a reaction you can't measure directly. This additivity, combined with tabulated formation enthalpies, makes it straightforward to compute heats of reaction for almost any process in chemistry and chemical engineering.
