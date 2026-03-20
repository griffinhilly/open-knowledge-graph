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
stage: formal-systems
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

## Explainer

You already know that current is the flow of charge and that resistance is opposition to that flow. Ohm's law, **V = IR**, says that in many materials these three quantities are locked in a simple linear relationship: double the voltage, double the current; double the resistance, halve the current. The law is deceptively simple in form but its implications ripple through every circuit you will ever analyze.

The causal direction matters. Voltage (potential difference, maintained by a battery or power supply) *drives* current through a resistance. Writing R = V/I is a *definition* of resistance from a measurement — apply V, measure I, compute R — not a statement that resistance is caused by voltage. For an ohmic material like a metal resistor, R is a constant property of the material and geometry, independent of what V or I you choose. This constancy is what it means to be ohmic: the V-I graph is a straight line through the origin, with slope equal to resistance.

The microscopic picture behind Ohm's law helps explain where it comes from and why it fails. In a metal, free electrons constantly scatter off vibrating ions. Voltage accelerates electrons between collisions, but collisions constantly reset their drift velocity. The result is a steady average drift speed proportional to the applied field — and therefore a current proportional to voltage. Temperature matters because hotter ions vibrate more, causing more frequent collisions and higher resistance. This is why real resistors heat up and why the resistance of incandescent bulbs changes dramatically from cold to operating temperature.

Ohm's law fails for many important devices. A **diode** conducts almost no current until voltage exceeds a threshold, then conducts heavily — its V-I curve is exponential, not linear. A **transistor** uses a small control signal to modulate a large current. Neither is well described by a single fixed resistance. The word "non-ohmic" is not a flaw — diodes and transistors are precisely useful *because* they violate Ohm's law. Understanding where Ohm's law applies (metal resistors, over a limited temperature range) versus where it breaks down (semiconductor devices, plasmas, superconductors) is essential for working with real circuits.
