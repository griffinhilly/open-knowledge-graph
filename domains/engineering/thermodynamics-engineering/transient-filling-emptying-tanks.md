---
id: transient-filling-emptying-tanks
title: Transient Filling and Emptying Processes
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: control-volume-transient-processes
  type: hard
- id: first-law-open-systems
  type: hard
tags:
- transient
- filling
- emptying
- tank
- pressurization
stage: formal-systems
status: draft
---

# Transient Filling and Emptying Processes

## Core Idea
Tank filling and emptying involve unsteady accumulation of mass and energy. For isentropic filling with inlet enthalpy h_in: dU/dt = ṁ_in h_in. Tank temperature and pressure rise until equilibrium (h_tank reaches h_in). Emptying to atmosphere requires careful thermodynamic analysis since exiting gas expands against atmospheric pressure. Critical conditions occur when downstream pressure equals sonic conditions.

## Questions

```yaml
- question: "An evacuated rigid tank is filled with air (γ = 1.4) from a large supply reservoir at 300 K, with no heat transfer to the surroundings. What is the final equilibrium temperature inside the tank?"
  type: multiple-choice
  options:
    - "300 K — the gas equilibrates to the supply temperature"
    - "214 K — the gas cools as it expands into the vacuum"
    - "420 K — the final temperature is γ × T_supply = 1.4 × 300 K"
    - "600 K — the tank doubles in temperature because of the compression work"
  answer: 2
  explanation: "For adiabatic filling of an evacuated rigid tank, the unsteady energy balance integrates to u_final = h_in (specific internal energy equals inlet enthalpy). For an ideal gas, u = c_v T and h = c_p T, so T_final = (c_p/c_v) × T_supply = γ × T_supply = 1.4 × 300 = 420 K. The extra energy comes from flow work — the supply line pushes the gas into the tank, doing P·v work on each parcel entering. This counterintuitive temperature rise has no external heat source — it is purely a consequence of the enthalpy accounting in the unsteady first law."

- question: "Why does the gas in a tank filled from a supply line at constant temperature end up hotter than the supply, even with no external heat transfer?"
  type: multiple-choice
  options:
    - "Friction between incoming gas molecules and the tank walls converts kinetic energy to heat"
    - "The compression of already-present gas by incoming gas raises the temperature through the ideal gas law"
    - "Each parcel of gas entering the tank carries not just internal energy but also flow work (P·v), which is part of its enthalpy. This extra energy is deposited in the tank as the supply line pushes gas through the inlet"
    - "The tank walls reflect thermal radiation back into the gas, heating it above supply temperature"
  answer: 2
  explanation: "The key is that flowing streams carry enthalpy h = u + Pv, not just internal energy u. The supply line does Pv work pushing each unit mass of gas into the tank, and this work becomes internal energy of the gas in the tank. The energy balance d(mu)/dt = ṁ_in × h_in integrates to u_final = h_in = u_in + P_in v_in — the extra Pv term is the flow work. This is not friction or compression of existing gas; it is the thermodynamic accounting of what it costs to push mass through a boundary."

- question: "The energy delivered to a rigid tank by an entering gas stream is proportional to the stream's enthalpy per unit mass, not its internal energy per unit mass."
  type: true-false
  answer: true
  explanation: "This is the central insight of the transient filling problem. The unsteady open-system first law reads dU/dt = Q̇ − Ẇ + ṁ_in h_in − ṁ_out h_out. Inlet streams contribute their enthalpy h = u + Pv, not just u, because the flow work Pv is done by the upstream fluid pushing the parcel through the boundary. In a rigid tank (no shaft work, often adiabatic), the accumulating internal energy equals the enthalpy of all mass that entered — hence u_final = h_in for an initially empty tank."

- question: "An evacuated rigid tank filled adiabatically from a constant-temperature supply will reach exactly the supply temperature at equilibrium."
  type: true-false
  answer: false
  explanation: "The final temperature is γ × T_supply (1.4× for air), not T_supply. The supply temperature is the temperature of the incoming gas at the source, but once the gas enters the tank, the flow work from the supply line deposits additional energy. The final specific internal energy equals the inlet enthalpy: u_final = h_in = c_p T_supply, so T_final = (c_p/c_v) T_supply = γ T_supply. Reaching exactly the supply temperature would only occur if the filling were reversible and isothermal — which requires heat rejection during filling."

- question: "Explain why u_final = h_in (not u_in) when an evacuated rigid tank is filled adiabatically, and what physical phenomenon causes this result."
  type: short-answer
  answer: "The unsteady energy balance for a rigid adiabatic control volume is d(mu)/dt = ṁ_in × h_in. Integrating from empty to full: m_final × u_final = m_final × h_in, so u_final = h_in. The reason h_in rather than u_in appears is that the supply line must do flow work (Pv work per unit mass) to push each parcel of gas through the inlet against the pressure inside the tank. This flow work is part of the enthalpy h = u + Pv. It is deposited as internal energy in the tank, raising the temperature above the supply temperature."
  explanation: "The distinction between u and h is the essential thermodynamic point: internal energy is what a mass stores in place, but enthalpy is what a flowing stream carries — because moving mass through a pressure boundary always involves flow work. Every open-system energy analysis (steady or unsteady) accounts for enthalpy at flow boundaries, never internal energy alone. Students who apply closed-system intuition (where u matters) to open systems make systematic errors in filling/emptying and steady-flow problems alike."
```

## Explainer

Your prerequisite on transient control volumes established the general unsteady energy balance: d(m·u)/dt = Q̇ − Ẇ + Σṁ_in·h_in − Σṁ_out·h_out. Filling and emptying problems are the canonical applications of this equation, and they reveal something surprising: a rigid tank being filled with gas can end up at a *higher temperature* than the supply line, even with no external heat source. Understanding why requires careful attention to what the unsteady energy balance is actually tracking.

For **filling** a rigid, initially evacuated tank from a supply line at constant enthalpy h_in (common assumption when the supply is a large reservoir), there is no work (rigid walls), and no outlet flow: d(m·u)/dt = ṁ_in·h_in. Integrating from empty to full: m_final·u_final = m_final·h_in, so u_final = h_in = u_in + P_in·v_in. The final specific internal energy equals the inlet enthalpy — not the inlet internal energy. The extra P·v term represents the flow work done by the supply line pushing the gas into the tank. For an ideal gas, u = c_v·T and h = c_p·T, so T_final/T_supply = h_in/u_in = c_p/c_v = γ. For air (γ = 1.4), the tank temperature reaches 1.4 times the supply temperature — a 40% temperature rise with no external heating. This counterintuitive result is purely a consequence of flow work, which your steady-flow first-law experience may have caused you to overlook.

For **emptying** a tank, the situation inverts. As gas escapes, it does work pushing itself out through the orifice, and the remaining gas in the tank expands. For isentropic emptying, the gas in the tank undergoes an isentropic expansion — so temperature drops as pressure drops. At any instant, the escaping gas carries away enthalpy h_exit > u_remaining (because the enthalpy includes the P·v flow work), so the internal energy per unit mass of the remaining gas decreases. The limiting case of emptying to vacuum is isentropic cooling. In practice, heat transfer from the tank walls partially counteracts this cooling, making the real process somewhere between isentropic and isothermal.

Setting up a transient tank problem requires identifying the system boundary carefully. The control volume is the tank interior; its boundary is fixed (rigid walls), so Ẇ = 0. The mass balance dm/dt = ṁ_in − ṁ_out must be integrated alongside the energy balance — usually numerically unless simplifying assumptions (ideal gas, constant inlet enthalpy, no heat transfer) allow an analytic solution. The integration proceeds from an initial state (P₀, T₀, m₀) forward in time until an equilibrium or emptying condition is reached. Critical conditions for emptying (choked flow when the orifice downstream pressure drops to P*= P·(2/(γ+1))^(γ/(γ-1))) limit the mass flow rate and determine how quickly a tank depressurizes.

Real engineering applications are everywhere. Filling a SCUBA tank, pressurizing a pipeline from a supply manifold, a tire puncture, a nitrogen purge of a chemical vessel — all require transient control volume analysis. The insight from this topic is that **enthalpy, not internal energy, is the energy currency of flowing streams**: inlet streams bring h_in per unit mass, outlet streams carry away h_out per unit mass, and the tank stores u. Confusing h and u leads to systematic errors in both temperature and energy predictions. With this understanding, you can apply the unsteady first law to any configuration — tanks with heat exchange, tanks with multiple inlets, or tanks exhausting through turbines — by carefully accounting for each enthalpy flow term.
