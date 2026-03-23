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
status: validated
---

# Enthalpy and Its Physical Significance

## Core Idea
Enthalpy (H = U + PV) combines internal energy with flow work. It is the appropriate state function for processes at constant pressure, where the heat absorbed equals the enthalpy change: Q_p = ΔH. Enthalpy is particularly useful in engineering for open systems like compressors and turbines.

## Questions

```yaml
- question: "A chemist burns methane in an open flame at atmospheric pressure and measures 890 kJ/mol of heat released. A second chemist burns the same amount in a sealed bomb calorimeter (constant volume) and measures 883 kJ/mol. Why do these differ, and which value is ΔH_combustion?"
  type: multiple-choice
  options:
    - "The bomb calorimeter is more accurate; both should be reported as ΔH_combustion"
    - "The open flame value (890 kJ/mol) is ΔH — it includes the PΔV expansion work done against the atmosphere, while the bomb calorimeter measures ΔU at constant volume"
    - "The bomb calorimeter measures ΔH; the open flame value is distorted by convective heat loss to the surroundings"
    - "The values measure the same quantity — the difference is experimental error from the two setups"
  answer: 1
  explanation: "At constant pressure (open flame), Q_p = ΔH — the heat released includes both the change in internal energy and the expansion work done against the atmosphere (PΔV). At constant volume (bomb calorimeter), no expansion work occurs and Q_v = ΔU. Since combustion produces gas, volume increases, and PΔV > 0, so |ΔH| > |ΔU|. ΔH_combustion refers to the constant-pressure measurement, which is what 'heat of combustion' means in standard thermochemistry tables."

- question: "An engineer writing a steady-state energy balance for a steam turbine should use which energy quantity for the steam entering and leaving, and why?"
  type: multiple-choice
  options:
    - "Internal energy U, because it accounts for all the thermal and kinetic energy stored in the steam"
    - "Either U or H — the PV term is a constant that cancels in the energy balance"
    - "Enthalpy H, because flowing steam carries both internal energy and the flow work (PV) needed to push it through the inlet and outlet against the prevailing pressure"
    - "Internal energy U, because turbines operate at constant volume"
  answer: 2
  explanation: "In open systems with flowing fluids, the energy carried by each mass element includes its internal energy U plus the work done to push it into (or pull it out of) the control volume — the flow work PV. Enthalpy H = U + PV automatically captures both. This is why all steady-flow energy balances (turbines, compressors, nozzles, heat exchangers) use H rather than U. Turbines do not operate at constant volume — they are open systems with continuous flow."

- question: "Enthalpy is a useful thermodynamic quantity only in chemistry; engineers working with machines and flow systems should use internal energy instead."
  type: true-false
  answer: false
  explanation: "The opposite is true for open systems. Engineers use enthalpy routinely for steady-flow devices because the PV flow-work term is physically significant whenever fluid enters or exits a control volume. Turbines, compressors, pumps, nozzles, and heat exchangers are all analyzed using enthalpy. Internal energy is more natural for closed systems where no mass crosses the boundary (e.g., a piston-cylinder with a sealed piston)."

- question: "For a chemical reaction conducted at constant pressure, the heat released or absorbed by the reaction equals the change in enthalpy — no separate calculation of expansion work against the atmosphere is needed."
  type: true-false
  answer: true
  explanation: "This is the defining practical utility of enthalpy: Q_p = ΔH. The derivation is Q_p = ΔU + PΔV (first law at constant pressure), and since H = U + PV, ΔH = ΔU + PΔV = Q_p. The PΔV work is already built into ΔH, so measuring the heat at constant pressure directly gives ΔH. This is why standard enthalpies of formation and reaction are tabulated — constant-pressure calorimetry is the universal lab method."

- question: "What is the physical meaning of the PV term in H = U + PV, and why does it make enthalpy more natural than internal energy for most chemical reactions?"
  type: short-answer
  answer: "The PV term represents flow work — the energy required to push a quantity of fluid into or out of a region against the ambient pressure. In an open container at atmospheric pressure, any gas-producing reaction must push the atmosphere back (doing PΔV work), which is energy that leaves the system as work rather than heat. Internal energy U tracks total stored energy, but not this unavoidable atmospheric work. Enthalpy builds in PΔV so that Q_p = ΔH directly, without a separate expansion-work correction. Since most lab chemistry happens at constant pressure, H is the more practical currency."
  explanation: "The heuristic is simple: choose U when volume is fixed (no expansion work), choose H when pressure is fixed (expansion work is automatic). Both are state functions, so Hess's law applies to both — but for constant-pressure processes, enthalpy is the one that equals the directly measurable heat."
```

## Explainer

From internal energy and the first law, you know that the energy change of a closed system is ΔU = Q − W, where W = PΔV for a simple expansion against a constant pressure. If you do a reaction or process at constant volume (a sealed bomb calorimeter, say), no expansion work is done and all the heat appears as ΔU. But most chemistry and much engineering happens at constant pressure — in open containers, in the atmosphere. At constant pressure, some of the energy released by a reaction goes into pushing the atmosphere back (PΔV work), and that work is not available as heat. **Enthalpy** H = U + PV is defined precisely to keep track of this.

At constant pressure: ΔH = ΔU + PΔV. The first law gives Q_p = ΔU + PΔV = ΔH. So the heat absorbed at constant pressure equals the enthalpy change — full stop, no need to separately track expansion work. This makes enthalpy the natural energy currency for chemistry. When you burn methane at atmospheric pressure and measure the heat released, you are measuring ΔH_combustion. When you dissolve a salt in water and the solution gets cold, you are experiencing an endothermic ΔH_dissolution. Chemists tabulate **standard enthalpies of formation** (ΔH°_f) precisely because constant-pressure calorimetry is universal in lab settings.

The PV term in H has a concrete physical meaning in open systems: it represents **flow work**, the energy required to push a unit of fluid into (or out of) a control volume against the prevailing pressure. Imagine a turbine: high-pressure steam enters, does work on the blades, and low-pressure steam exits. For the steady-flow energy balance, you must account not just for the internal energy of the steam but also for the work done to push the fluid through the inlet and outlet. The enthalpy H = U + PV automatically includes this flow work, which is why engineers always use H (not U) when writing energy balances for compressors, turbines, nozzles, and heat exchangers.

A useful heuristic: choose U when volume is fixed; choose H when pressure is fixed. Both are **state functions** — their values depend only on the current thermodynamic state, not on how you got there. This means you can use Hess's law: ΔH for a reaction is the same regardless of the reaction pathway, allowing you to add known ΔH values for sub-reactions to compute ΔH for a reaction you can't measure directly. This additivity, combined with tabulated formation enthalpies, makes it straightforward to compute heats of reaction for almost any process in chemistry and chemical engineering.
