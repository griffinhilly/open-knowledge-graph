---
id: transient-response-rl-circuits
title: Transient Response in RL Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-parallel-inductor-networks
  type: hard
- id: dc-analysis-steady-state
  type: hard
builds-toward:
- transient-response-rlc-circuits
tags:
- transients
- rl-circuits
- time-domain
stage: formal-systems
status: draft
---

# Transient Response in RL Circuits

## Core Idea
RL transients describe current changes when inductors energize or de-energize through resistors. The current in a series RL circuit follows i(t) = I_f + (I_i - I_f)·exp(-t/τ), where τ = L/R is the time constant. Inductors oppose current changes, resulting in exponential approach to steady-state current. RL transients appear in switching power supplies, motor control, and relay circuits.

## Explainer

You already know from inductor analysis that an inductor opposes changes in current — its terminal voltage is v = L · di/dt, so an instantaneous current jump would require infinite voltage. This means **the current through an inductor cannot change instantaneously**. That single physical fact is the entire source of RL transient behavior. When you flip a switch, the circuit must negotiate a smooth transition from its initial current to its final steady-state current, and that negotiation plays out over time.

Consider a series RL circuit where a voltage source V is connected at t = 0 with the inductor initially carrying no current. KVL gives V = i·R + L·di/dt. The steady-state solution (di/dt → 0) is simply i_f = V/R — the inductor looks like a wire at DC. But the initial condition forces i(0) = 0. The solution that satisfies both is: i(t) = I_f · (1 − e^(−t/τ)), where τ = L/R is the **time constant**. After one time constant, the current has reached 63.2% of its final value. After 5τ, it's within 1% of I_f and the transient is effectively over. The time constant τ has a clean physical interpretation: larger inductance means more "inertia" against current change; larger resistance means faster dissipation and quicker approach to steady state.

The general formula i(t) = I_f + (I_i − I_f) · e^(−t/τ) handles all cases, including those where current starts at a nonzero value. The three quantities you need are the initial current I_i (determined by continuity — the current just before the switch event), the final current I_f (determined by DC steady state with the new circuit), and the time constant τ = L/R (determined by the Thévenin resistance seen by the inductor after the switch event). Once you have these three, the entire transient waveform follows. This "three-element recipe" is the universal method for first-order RL transients.

When a current-carrying inductor is suddenly disconnected from its source, a **voltage spike** appears at the inductor terminals. The inductor tries to maintain current through whatever path is available — if none exists, the voltage climbs until an arc occurs or a protective clamp absorbs the energy. Relay coils, motor windings, and solenoids routinely produce these spikes, which can destroy switching transistors. The classic protection solution is a **freewheeling diode** placed in parallel with the inductor: it provides a safe current path and allows the stored magnetic energy (½LI²) to dissipate harmlessly in the resistance during turn-off. Recognizing and managing inductive voltage spikes is one of the most practical skills from RL transient analysis.
