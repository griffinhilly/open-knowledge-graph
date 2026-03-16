---
id: capacitance-definition
title: Capacitance and Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: conductors-electrostatic-behavior
  type: hard
builds-toward:
- parallel-plate-capacitor-formula
- capacitor-circuits-series-parallel
tags:
- capacitance
- device
- charge-voltage
stage: formal-systems
status: draft
---

# Capacitance and Capacitors

## Core Idea
Capacitance C is defined as C = Q/V, where Q is magnitude of charge on each plate and V is potential difference. Capacitance depends only on geometry and material; higher capacitance means more charge storage for given voltage.

## Explainer

Recall from your study of conductors that when charge is placed on an isolated conductor, it redistributes until the surface is an equipotential. A capacitor exploits this property deliberately: two conductors placed close together, carrying equal and opposite charges, create a well-defined electric field in the gap between them — and therefore a well-defined potential difference. **Capacitance** is simply the ratio of how much charge you stored to how much voltage it cost you: C = Q/V. A larger capacitance means you get more charge per volt — the device is better at storing charge.

What determines capacitance? Purely geometry (and the material between the plates). Consider two parallel plates of area A separated by distance d. The electric field between them is E = σ/ε₀ = Q/(ε₀A), and the potential difference is V = Ed = Qd/(ε₀A). So C = Q/V = ε₀A/d. This result is telling: bigger plates (more area) increase C because more charge can spread out; smaller gap (less distance) increases C because the same charge creates less voltage drop. Neither the charge Q nor the voltage V appears — capacitance is a purely geometric property, like resistance is a property of a resistor's dimensions.

The connection to potential energy — your prerequisite — is direct. You know that assembling a charge distribution requires work, which is stored as potential energy. For a capacitor, the energy stored is U = ½QV = ½CV² = Q²/(2C). The factor of ½ appears because you don't deposit all charge at the full final voltage; you start at V = 0 and build up to the final V. This energy lives in the electric field between the plates. When you discharge a capacitor through a circuit, that stored field energy becomes the work done on the charges.

The key conceptual shift in this topic is treating capacitance as a property of the geometry, not of the charge or voltage. You can double Q and V doubles proportionally; C stays the same. This invariance is what makes capacitance a useful circuit parameter — it is a fixed characteristic of the device, like mass or resistance. In circuits, capacitors appear wherever you need to store energy, smooth out voltage fluctuations, or block DC while passing AC — all consequences of this fundamental charge-per-volt relationship.
