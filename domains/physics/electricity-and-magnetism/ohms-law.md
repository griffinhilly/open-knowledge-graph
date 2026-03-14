---
id: ohms-law
title: Ohm's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
builds-toward:
- dc-circuits-series-parallel
- electric-power
tags:
- ohms-law
- voltage
- current
- resistance
- circuits
stage: abstract-reasoning
status: validated
---

# Ohm's Law

## Core Idea
Ohm's law states that for many conducting materials (ohmic materials), the current through a device is proportional to the voltage across it: V = IR. The constant of proportionality R is the resistance, measured in ohms (Ω = V/A). Ohm's law is an empirical relationship, not a fundamental law — it holds for metals over a wide temperature range but breaks down for semiconductors, diodes, and other nonlinear devices.

## How It's Best Learned
Verify Ohm's law experimentally (or through simulation) by plotting V vs. I for resistors — a straight line through the origin with slope R. Then identify non-ohmic devices (LEDs, diodes) where V-I curves are nonlinear.

## Common Misconceptions
- Ohm's law is not universal; many important devices are non-ohmic.
- Voltage causes current, not the other way around — R = V/I is a definition of resistance, not a causal statement.
- Resistance does not depend on V or I for ohmic materials, but it does depend on temperature.
