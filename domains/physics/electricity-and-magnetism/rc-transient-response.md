---
id: rc-transient-response
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dc-circuit-analysis
  type: hard
builds-toward:
- rl-transient-response
tags:
- rc-circuit
- transient
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
In an RC circuit, capacitor charge evolves as Q(t) = Q₀(1 − e^(−t/τ)) during charging and Q(t) = Q₀e^(−t/τ) during discharging, where τ = RC is the time constant. Current decays exponentially: I(t) = (V/R)e^(−t/τ). The time constant characterizes the speed of charge redistribution; larger R or C gives slower response.

## Explainer

From your DC circuit analysis, you know that a capacitor stores charge Q = CV and blocks steady-state current in equilibrium. But what happens between the instant you connect a capacitor to a voltage source and the moment it reaches equilibrium? That interval — the **transient response** — is governed by the interplay between R and C.

Consider charging a capacitor from a battery of voltage V through a resistor R. At the instant the circuit closes (t = 0), the capacitor is uncharged, so it looks like a wire: all the voltage appears across R and the initial current is I₀ = V/R. As charge accumulates on the capacitor, the voltage across it grows, leaving less voltage for the resistor, which reduces the current. Less current means slower charging. The process is self-limiting: the more charge on the capacitor, the harder it is to add more. This feedback is described by the differential equation RC(dV_C/dt) + V_C = V, whose solution is V_C(t) = V(1 − e^(−t/τ)) with **τ = RC** the time constant. The charge follows the same shape: Q(t) = CV(1 − e^(−t/τ)).

The **time constant τ** is the single most important quantity in RC transient analysis. After one time constant, the capacitor has reached about 63% of its final charge (since 1 − e^(−1) ≈ 0.63); after 5τ, it is within 1% of fully charged — effectively complete. A large R means current flows slowly, so charging takes longer. A large C means more charge must be delivered to reach a given voltage, again slowing the process. Both increase τ = RC proportionally.

Discharging is the mirror image. If a fully charged capacitor (initial charge Q₀) is connected to a resistor with the battery removed, the excess charge drives a current that exponentially drains the capacitor: Q(t) = Q₀ e^(−t/τ). The current starts at I₀ = V₀/R and decays at the same rate. In both cases, the exponential curve is the signature of a system with a restoring rate proportional to its displacement from equilibrium — the same mathematical form as Newton's cooling law, population decay, and countless other natural processes. Recognizing this exponential fingerprint and reading off τ from a graph is a core skill that extends directly to RL circuits and, later, to resonant LC circuits.
