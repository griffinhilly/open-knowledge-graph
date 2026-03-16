---
id: transient-response-rc-circuits-electricity-and-magnetism
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: network-circuit-analysis-methods
  type: hard
- id: differential-equations-intro-separable
  type: hard
builds-toward:
- magnetic-force-moving-charges
tags:
- transient
- rc-circuit
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
RC charging: Q(t) = Q₀(1 − e^(−t/RC)), with time constant τ = RC. RC discharging: Q(t) = Q₀e^(−t/RC). Voltage and current similarly decay exponentially. Time constant determines how quickly the circuit reaches steady state.

## Explainer

From your circuit analysis work, you know how to apply Kirchhoff's laws to find voltages and currents in steady-state networks. But what happens in the moments after you close a switch or change a voltage? That transition — the **transient response** — is what RC circuits are built to reveal. The capacitor is the element that makes things time-dependent: because V_C = Q/C and charge can only accumulate at a finite rate, the capacitor voltage cannot jump instantaneously, and this constraint governs the entire circuit's evolution.

Start with a discharging RC circuit: a capacitor with initial charge Q₀ connected in series with a resistor. Applying Kirchhoff's voltage law gives V_C − V_R = 0, i.e., Q/C = IR = (−dQ/dt)R, which rearranges to dQ/dt = −Q/(RC). You learned to solve exactly this type of separable differential equation in your prerequisite: the solution is Q(t) = Q₀e^(−t/RC). The charge (and therefore the voltage across the capacitor, V_C = Q₀e^(−t/RC)/C) decays **exponentially** toward zero. The current I(t) = −dQ/dt = (Q₀/RC)e^(−t/RC) also decays exponentially, starting at a maximum and falling to zero as the capacitor empties.

The **time constant** τ = RC encodes the characteristic timescale. At t = τ, the charge has fallen to e⁻¹ ≈ 37% of its initial value; at t = 2τ it is about 14%; at t = 5τ it is effectively zero (less than 1%). The units check out: ohms × farads = (V/A) × (C/V) = C/(C/s) = seconds. A large resistance slows the discharge because less current can flow; a large capacitance slows it because more charge must be removed. The charging case is the mirror image: connect a capacitor through a resistor to a battery of EMF ε, and Q(t) = Q₀(1 − e^(−t/RC)), approaching its equilibrium value Q₀ = Cε asymptotically, never quite reaching it in finite time.

The exponential form is not just a mathematical accident — it is the signature of any system where the rate of change is proportional to the current state. The same differential equation describes radioactive decay, Newton's law of cooling, and many biological processes. Recognizing this pattern — first-order linear ODE with constant coefficients → exponential solution → time constant = 1/(coefficient) — lets you read off the transient behavior by inspection once you have the governing equation. In circuit design, τ = RC is the key design parameter: filters, timers, signal-shaping networks, and analog integrators all work by choosing R and C to set the desired timescale of response.
