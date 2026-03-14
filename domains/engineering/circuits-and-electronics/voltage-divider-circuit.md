---
id: voltage-divider-circuit
title: Voltage Divider Principle
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
builds-toward:
- series-parallel-resistor-analysis
- impedance-admittance-networks
tags:
- circuit-analysis
- resistive-circuits
- fundamental
stage: formal-systems
status: draft
---

# Voltage Divider Principle

## Core Idea
The voltage divider principle describes how voltage distributes across series resistors: the voltage across any resistor is proportional to its resistance relative to the total. For series resistors R₁ and R₂ with applied voltage V, the voltage across R₁ is V × (R₁/(R₁+R₂)). This technique simplifies circuit analysis and is widely used in sensor signal conditioning and biasing circuits.
