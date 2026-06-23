---
id: first-order-transient-circuits
title: First-Order Transient Circuit Response
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: thevenin-norton-equivalents
  type: hard
- id: differential-equations-intro-separable
  type: hard
- id: rc-circuits
  type: soft
- id: rl-circuits
  type: soft
- id: first-order-linear-odes
  type: hard
- id: transient-response-rc-circuits
  type: soft
builds-toward:
- second-order-transient-circuits
tags:
- transient-response
- RC
- RL
- time-constant
- natural-response
- step-response
stage: formal-systems
status: validated
---

# First-Order Transient Circuit Response

## Core Idea
First-order circuits containing a single capacitor or inductor plus resistors are governed by a first-order linear ODE whose solution is an exponential. The time constant is τ = RC for RC circuits and τ = L/R for RL circuits, where R is the Thevenin resistance seen by the storage element. The complete response equals the natural response (decaying exponential driven by initial conditions) plus the forced response (due to sources). A shortcut formula v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ) applies to any DC-forced first-order circuit.

## How It's Best Learned
Use Thevenin equivalents to find τ systematically for any RC or RL topology. Practice identifying initial conditions at t = 0⁺ using continuity of capacitor voltage and inductor current, and final conditions at t → ∞ by treating C as open and L as short in DC steady state.

## Common Misconceptions
- Computing τ from the nominal component values rather than from the Thevenin resistance seen by the storage element.
- Setting initial conditions from the circuit after switching rather than just before (at t = 0⁻).
- Confusing natural and step response — both are exponential but driven by different initial and final conditions.

## Questions

```yaml
- question: "An RC circuit has a capacitor C, a resistor R1 in series between the source and the capacitor, and a resistor R2 in parallel with the capacitor. After zeroing all independent sources, what resistance should be used to compute the time constant τ?"
  type: multiple-choice
  options:
    - "R1 alone — only the series resistor limits charging current into the capacitor"
    - "R2 alone — only the parallel resistor directly discharges the capacitor"
    - "R1 + R2 — add all resistors in the circuit"
    - "R1 in parallel with R2 — the Thevenin resistance seen from the capacitor's terminals, with sources zeroed"
  answer: 3
  explanation: "The time constant τ = R_th × C, where R_th is the Thevenin resistance seen from the capacitor's terminals with all independent sources zeroed (voltage sources replaced with short circuits, current sources with open circuits). Looking into the capacitor's terminals with the source zeroed: R1 connects from one terminal through the source (now a short) to ground, while R2 connects from one terminal to ground — so R1 and R2 are in parallel from the capacitor's perspective. R_th = R1 ‖ R2. Using only R1 or R2 misidentifies which resistors actually form the discharge/charge path seen by the storage element — the most common mistake in computing τ."

- question: "A capacitor in a circuit holds 8V just before a switch opens at t = 0. The switch opening disconnects the voltage source. What is the capacitor voltage v(0⁺) immediately after the switch opens?"
  type: multiple-choice
  options:
    - "0V — the switch opening removes the source, so the capacitor immediately starts from zero"
    - "8V — capacitor voltage cannot change instantaneously, so it remains at its pre-switching value"
    - "The supply voltage — the capacitor immediately charges to match the new circuit configuration"
    - "Indeterminate — you need to solve the differential equation to find the initial value"
  answer: 1
  explanation: "Capacitor voltage cannot change instantaneously — this is the continuity condition. The capacitor stores energy in its electric field (E = ½CV²), and instantaneous change would require infinite power (P = C dV/dt → ∞ if dV is finite and dt → 0). Therefore v(0⁺) = v(0⁻) = 8V, the value just before switching. The initial condition for the transient response is always taken from the circuit state just before the switching event (t = 0⁻), not after. This is the second most common mistake after computing τ from the wrong resistance."

- question: "The natural response of a first-order RC circuit (with no external source, only initial stored energy) is a special case of the general shortcut formula v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ), obtained by setting v(∞) = 0."
  type: true-false
  answer: true
  explanation: "When there is no source, the circuit eventually reaches v(∞) = 0 (all stored energy dissipated into the resistor). Substituting into the shortcut formula: v(t) = 0 + [v(0⁺) − 0]·e^(−t/τ) = v(0⁺)·e^(−t/τ). This is exactly the natural response — a pure exponential decay from the initial stored energy. Similarly, the step response (capacitor initially uncharged, source applied) is the case v(0⁺) = 0: v(t) = v(∞)·(1 − e^(−t/τ)). Both are special cases of the same unified formula, which shows that the apparent distinction between them is superficial."

- question: "To find the initial condition v(0⁺) for a first-order transient circuit, you should analyze the circuit in its new configuration — after the switch has changed — and compute the initial value from that."
  type: true-false
  answer: false
  explanation: "Initial conditions must be taken from the circuit state just before switching (t = 0⁻), not after. Capacitor voltage and inductor current cannot change instantaneously (continuity conditions), so v_C(0⁺) = v_C(0⁻) and i_L(0⁺) = i_L(0⁻). The pre-switching circuit (which may be a completely different topology) gives you the value of the stored energy. Using the post-switching circuit to find initial conditions is the common error — it would give you the final (t → ∞) value, not the initial one, completely inverting the transient response."

- question: "What three values do you need to apply the shortcut formula v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ) for a DC-forced first-order circuit? Explain how to find each one."
  type: short-answer
  answer: "The three values are: (1) v(0⁺): the initial condition, found by analyzing the circuit just before switching (t = 0⁻) and using continuity — capacitor voltage cannot jump, so v(0⁺) = v(0⁻). (2) v(∞): the final DC steady-state value, found by treating the capacitor as an open circuit (or inductor as a short circuit) at t → ∞ and solving the resulting resistive circuit. (3) τ: the time constant, found by computing the Thevenin resistance seen by the storage element with all independent sources zeroed — τ = R_th × C for RC, τ = L / R_th for RL."
  explanation: "The power of this shortcut formula is that it converts a differential equation problem into three straightforward circuit analysis steps. Once you have the three numbers, you substitute and the exponential trajectory is fully determined. The formula unifies all DC-forced first-order responses — natural, step, and mixed — into a single expression. The key errors are: (1) reading the initial condition from the wrong circuit instant, (2) computing τ from nominal component values rather than the Thevenin equivalent, and (3) finding the final value incorrectly by forgetting to treat C as open or L as short at DC steady state."
```

## Explainer

You know from capacitor and inductor theory that these elements store energy — a capacitor stores it in an electric field (voltage), an inductor in a magnetic field (current). You also know from first-order ODE theory that the equation dx/dt + (1/τ)x = f(t) has an exponential solution. First-order transient analysis is where these two threads meet: a single-capacitor or single-inductor circuit, when disturbed, responds with a decaying exponential whose time constant τ tells you how fast the energy dissipates into resistors.

The key first step is to replace all the resistors in the circuit with their **Thevenin equivalent** as seen from the terminals of the storage element. This reduces any complicated resistor network to a single equivalent resistance R_th in series (for RC) or in parallel (for RL). The time constant then follows immediately: τ = R_th · C for a capacitor, τ = L / R_th for an inductor. One τ represents the time to decay about 63% of the way toward the final value; five τ is engineering convention for "effectively done." The Thevenin approach is why you needed that prerequisite — it converts any first-order problem into the same canonical form, regardless of circuit topology.

The complete response has two parts. The **natural response** accounts for initial stored energy draining away: if a capacitor starts at voltage v₀ with no source, it decays as v₀·e^(−t/τ). The **forced response** (or particular solution) accounts for external sources driving the circuit toward a new steady state. For a DC source, the forced response is simply the DC steady-state value v(∞), found by treating the capacitor as an open circuit and the inductor as a short circuit at t → ∞. The total solution combines both: v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ).

This **shortcut formula** is worth internalizing because it reduces every DC-forced first-order problem to finding three numbers: the initial value v(0⁺), the final value v(∞), and the time constant τ. Initial conditions follow from continuity: capacitor voltage and inductor current cannot jump instantaneously, so v(0⁺) = v(0⁻) — the value just before switching. The formula then fills in the exponential trajectory between the known initial and final states. Once you see that the natural response and step response are just two special cases of the same formula (one with v(∞) = 0, one with v(0⁺) = 0), the apparent distinction between them dissolves.
