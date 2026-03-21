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

## Questions

```yaml
- question: "A switch closes at t = 0, connecting a 12V source to a series RL circuit with R = 4Ω and L = 2H. The inductor was initially unenergized. What is the current immediately after the switch closes?"
  type: multiple-choice
  options:
    - "3 A — the steady-state value V/R"
    - "6 A — the initial rate of change V/L"
    - "0 A — the inductor opposes instantaneous current change"
    - "1.5 A — the average of initial and final values"
  answer: 2
  explanation: "Inductor current cannot change instantaneously because an instantaneous jump would require infinite voltage (v = L di/dt). Since the initial current is 0 A before the switch closes, it must remain 0 A immediately after. The current then grows exponentially toward the steady-state value of 3 A (V/R = 12/4) with time constant τ = L/R = 0.5 s. The misconception in option A is treating the circuit as having instantly reached DC steady state."

- question: "An inductor carrying 500 mA is suddenly disconnected by opening a switch, with no alternative current path provided. What happens?"
  type: multiple-choice
  options:
    - "The current drops instantly to zero as the magnetic field collapses"
    - "The current decays exponentially to zero through the inductor's winding resistance"
    - "A large voltage spike appears across the switch terminals as the inductor attempts to sustain current with no available path"
    - "The inductor stores the energy indefinitely until a path is provided"
  answer: 2
  explanation: "An inductor cannot accept instantaneous current interruption — it will generate whatever voltage is necessary to maintain current flow. With no path available, the voltage at the switch terminals climbs rapidly (theoretically to infinity) until an arc forms or the energy is dissipated through parasitic breakdown. This is the inductive voltage spike problem. In practice it destroys unprotected transistors in switching circuits. The solution is a freewheeling diode that provides a controlled current path for the decaying inductor current."

- question: "After exactly one time constant (τ = L/R), the current in an RL circuit has reached 100% of its final steady-state value."
  type: true-false
  answer: false
  explanation: "After one time constant, the current has reached approximately 63.2% of its final value — not 100%. The exponential formula i(t) = I_f(1 − e^(−t/τ)) approaches I_f asymptotically; it never reaches I_f exactly at a finite time. In practice, the transient is considered 'over' after about 5τ, when the current is within 1% of I_f. This is a common misreading of time constant definitions."

- question: "The current through an inductor cannot change instantaneously because any instantaneous change would require infinite voltage."
  type: true-false
  answer: true
  explanation: "This follows directly from v = L di/dt. An instantaneous current change means dt → 0 while di is finite, making v → ∞. Since infinite voltage is physically unrealizable, current must change continuously and smoothly. This is the single physical constraint that generates all RL transient behavior: the circuit is forced to negotiate a smooth exponential transition from initial to final current, governed by the time constant τ = L/R."

- question: "Explain the 'three-element recipe' for solving any first-order RL transient. What are the three quantities, and why is each one determined independently?"
  type: short-answer
  answer: "The three elements are: (1) I_i, the initial current — determined by the inductor's current just before the switching event, because inductor current cannot jump; (2) I_f, the final (steady-state) current — determined by DC analysis of the new circuit after switching, treating the inductor as a short circuit since di/dt → 0 at steady state; (3) τ = L/R — the time constant determined by the Thévenin resistance seen by the inductor in the new circuit after switching. With these three values, the complete transient is i(t) = I_f + (I_i − I_f) · e^(−t/τ)."
  explanation: "The three quantities are independent because each answers a different question about the circuit: where we start (initial condition via continuity), where we end up (DC steady state), and how fast we get there (the ratio of energy storage to dissipation). Any first-order RL circuit — regardless of source configuration or initial conditions — is fully characterized by these three numbers."
```

## Explainer

You already know from inductor analysis that an inductor opposes changes in current — its terminal voltage is v = L · di/dt, so an instantaneous current jump would require infinite voltage. This means **the current through an inductor cannot change instantaneously**. That single physical fact is the entire source of RL transient behavior. When you flip a switch, the circuit must negotiate a smooth transition from its initial current to its final steady-state current, and that negotiation plays out over time.

Consider a series RL circuit where a voltage source V is connected at t = 0 with the inductor initially carrying no current. KVL gives V = i·R + L·di/dt. The steady-state solution (di/dt → 0) is simply i_f = V/R — the inductor looks like a wire at DC. But the initial condition forces i(0) = 0. The solution that satisfies both is: i(t) = I_f · (1 − e^(−t/τ)), where τ = L/R is the **time constant**. After one time constant, the current has reached 63.2% of its final value. After 5τ, it's within 1% of I_f and the transient is effectively over. The time constant τ has a clean physical interpretation: larger inductance means more "inertia" against current change; larger resistance means faster dissipation and quicker approach to steady state.

The general formula i(t) = I_f + (I_i − I_f) · e^(−t/τ) handles all cases, including those where current starts at a nonzero value. The three quantities you need are the initial current I_i (determined by continuity — the current just before the switch event), the final current I_f (determined by DC steady state with the new circuit), and the time constant τ = L/R (determined by the Thévenin resistance seen by the inductor after the switch event). Once you have these three, the entire transient waveform follows. This "three-element recipe" is the universal method for first-order RL transients.

When a current-carrying inductor is suddenly disconnected from its source, a **voltage spike** appears at the inductor terminals. The inductor tries to maintain current through whatever path is available — if none exists, the voltage climbs until an arc occurs or a protective clamp absorbs the energy. Relay coils, motor windings, and solenoids routinely produce these spikes, which can destroy switching transistors. The classic protection solution is a **freewheeling diode** placed in parallel with the inductor: it provides a safe current path and allows the stored magnetic energy (½LI²) to dissipate harmlessly in the resistance during turn-off. Recognizing and managing inductive voltage spikes is one of the most practical skills from RL transient analysis.
