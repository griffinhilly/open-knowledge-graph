---
id: series-parallel-inductor-networks
title: Series and Parallel Inductor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: series-parallel-resistor-analysis
  type: soft
builds-toward:
- transient-response-rl-circuits
- impedance-admittance-networks
- series-resonance-characteristics
- parallel-resonance-characteristics
tags:
- inductors
- reactive-circuits
- energy-storage
stage: formal-systems
status: draft
---

# Series and Parallel Inductor Networks

## Core Idea
Inductors in series sum directly: L_eq = L₁ + L₂ + ... Inductors in parallel sum reciprocals: 1/L_eq = 1/L₁ + 1/L₂ + ... These relationships mirror resistor behavior. Series inductors share total applied voltage and all carry the same current; parallel inductors share voltage and distribute current inversely to inductance. Inductor networks are critical in power supply design and tuned circuits.
