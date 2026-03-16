---
id: electromotive-force-batteries
title: Electromotive Force (EMF) and Batteries
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: ohms-law-circuits
  type: hard
builds-toward:
- kirchhoff-circuit-laws-rules
tags:
- emf
- battery
- energy-source
stage: formal-systems
status: draft
---

# Electromotive Force (EMF) and Batteries

## Core Idea
Electromotive force (EMF) ε is the work per unit charge a battery (or other source) does; EMF creates and maintains potential difference. Real batteries have internal resistance r; terminal voltage V = ε − Ir decreases with current.

## Explainer

From your study of potential energy, you know that moving charges uphill in a potential field requires work. In a circuit, current flows from high to low potential through the external load, dissipating energy. But something must continuously pump charge back from low to high potential to sustain the current — that something is the **electromotive force**. Despite the name, EMF is not a force; it is energy per unit charge (measured in volts), representing the work done by the source (chemical, mechanical, thermal) per coulomb moved through it. A 12 V car battery does 12 joules of work for every coulomb it drives around the circuit.

The idealized battery maintains a fixed potential difference ε across its terminals regardless of the current drawn. Real batteries do not behave this way. Every real battery has **internal resistance** r — resistance inside the battery itself due to the ionic solution and electrodes. When current I flows, there is a voltage drop Ir within the battery, so the actual terminal voltage is V = ε − Ir. Draw more current and the terminal voltage sags. This is why a nearly dead battery reads 12 V when disconnected but might only sustain 9 V when trying to start a car engine. The EMF is still 12 V; the internal resistance has increased, causing a larger voltage drop at the high current demanded.

You already know from Ohm's law that V = IR for a resistor. Combining that with the battery model gives you the complete single-loop circuit: ε = I(R + r). The total driving EMF equals the total resistive voltage drop across both the external load R and the internal resistance r. Rearranging, I = ε/(R + r). Notice the limiting cases: if r → 0 (ideal battery), I = ε/R as you would naively expect; if R → 0 (short circuit), I = ε/r, which can be dangerously large since r is small.

The power perspective ties it together. The battery delivers power P = εI. Of this, P_load = I²R goes to the external load doing useful work, and P_lost = I²r is wasted as heat inside the battery. Maximum power is delivered to the load when R = r — a result called the maximum power transfer theorem that will reappear in circuit analysis. The EMF concept is the bridge between the energy-source view (chemistry pumping charge) and the circuit-analysis view (voltage sources driving currents through resistances); mastering it is essential before you move to multi-loop circuits with Kirchhoff's laws.
