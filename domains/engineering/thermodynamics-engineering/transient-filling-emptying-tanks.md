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
stage: advanced
status: draft
---

# Transient Filling and Emptying Processes

## Core Idea
Tank filling and emptying involve unsteady accumulation of mass and energy. For isentropic filling with inlet enthalpy h_in: dU/dt = ṁ_in h_in. Tank temperature and pressure rise until equilibrium (h_tank reaches h_in). Emptying to atmosphere requires careful thermodynamic analysis since exiting gas expands against atmospheric pressure. Critical conditions occur when downstream pressure equals sonic conditions.

## Explainer

Your prerequisite on transient control volumes established the general unsteady energy balance: d(m·u)/dt = Q̇ − Ẇ + Σṁ_in·h_in − Σṁ_out·h_out. Filling and emptying problems are the canonical applications of this equation, and they reveal something surprising: a rigid tank being filled with gas can end up at a *higher temperature* than the supply line, even with no external heat source. Understanding why requires careful attention to what the unsteady energy balance is actually tracking.

For **filling** a rigid, initially evacuated tank from a supply line at constant enthalpy h_in (common assumption when the supply is a large reservoir), there is no work (rigid walls), and no outlet flow: d(m·u)/dt = ṁ_in·h_in. Integrating from empty to full: m_final·u_final = m_final·h_in, so u_final = h_in = u_in + P_in·v_in. The final specific internal energy equals the inlet enthalpy — not the inlet internal energy. The extra P·v term represents the flow work done by the supply line pushing the gas into the tank. For an ideal gas, u = c_v·T and h = c_p·T, so T_final/T_supply = h_in/u_in = c_p/c_v = γ. For air (γ = 1.4), the tank temperature reaches 1.4 times the supply temperature — a 40% temperature rise with no external heating. This counterintuitive result is purely a consequence of flow work, which your steady-flow first-law experience may have caused you to overlook.

For **emptying** a tank, the situation inverts. As gas escapes, it does work pushing itself out through the orifice, and the remaining gas in the tank expands. For isentropic emptying, the gas in the tank undergoes an isentropic expansion — so temperature drops as pressure drops. At any instant, the escaping gas carries away enthalpy h_exit > u_remaining (because the enthalpy includes the P·v flow work), so the internal energy per unit mass of the remaining gas decreases. The limiting case of emptying to vacuum is isentropic cooling. In practice, heat transfer from the tank walls partially counteracts this cooling, making the real process somewhere between isentropic and isothermal.

Setting up a transient tank problem requires identifying the system boundary carefully. The control volume is the tank interior; its boundary is fixed (rigid walls), so Ẇ = 0. The mass balance dm/dt = ṁ_in − ṁ_out must be integrated alongside the energy balance — usually numerically unless simplifying assumptions (ideal gas, constant inlet enthalpy, no heat transfer) allow an analytic solution. The integration proceeds from an initial state (P₀, T₀, m₀) forward in time until an equilibrium or emptying condition is reached. Critical conditions for emptying (choked flow when the orifice downstream pressure drops to P*= P·(2/(γ+1))^(γ/(γ-1))) limit the mass flow rate and determine how quickly a tank depressurizes.

Real engineering applications are everywhere. Filling a SCUBA tank, pressurizing a pipeline from a supply manifold, a tire puncture, a nitrogen purge of a chemical vessel — all require transient control volume analysis. The insight from this topic is that **enthalpy, not internal energy, is the energy currency of flowing streams**: inlet streams bring h_in per unit mass, outlet streams carry away h_out per unit mass, and the tank stores u. Confusing h and u leads to systematic errors in both temperature and energy predictions. With this understanding, you can apply the unsteady first law to any configuration — tanks with heat exchange, tanks with multiple inlets, or tanks exhausting through turbines — by carefully accounting for each enthalpy flow term.
