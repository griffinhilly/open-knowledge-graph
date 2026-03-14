---
id: transient-response-rc-circuits
title: Transient Response in RC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-parallel-capacitor-networks
  type: hard
- id: dc-analysis-steady-state
  type: hard
builds-toward:
- transient-response-rlc-circuits
- first-order-transient-circuits
tags:
- transients
- rc-circuits
- time-domain
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
RC transients describe how voltage and current evolve when capacitors charge or discharge through resistors. The voltage across a charging capacitor in a series RC circuit follows v(t) = V_f + (V_i - V_f)·exp(-t/τ), where τ = RC is the time constant. Understanding these exponential responses is critical for analyzing circuit startup behavior, filter transients, and timing circuits.

## How It's Best Learned
Build a simple RC circuit with a battery, resistor, and capacitor. Measure or calculate the charging voltage at several time intervals and verify the exponential curve. Observe how doubling the resistance or capacitance changes the time constant.

## Common Misconceptions
Students often assume the capacitor charges to full voltage instantly or linearly rather than exponentially. Some confuse the time constant τ with the total charging time—the capacitor theoretically charges forever, reaching about 63% at t = τ and 95% at t = 3τ.
