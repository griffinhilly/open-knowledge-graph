---
id: series-parallel-resistor-analysis
title: Series and Parallel Resistor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
- id: kirchhoff-current-law
  type: hard
builds-toward:
- dc-analysis-steady-state
- series-parallel-capacitor-networks
- series-parallel-inductor-networks
- impedance-admittance-networks
tags:
- circuit-topology
- resistive-circuits
- network-analysis
stage: formal-systems
status: draft
---

# Series and Parallel Resistor Networks

## Core Idea
Resistors in series sum their resistances: R_eq = R₁ + R₂ + ... Resistors in parallel sum reciprocals: 1/R_eq = 1/R₁ + 1/R₂ + ... Real circuits often contain both series and parallel sections, which can be simplified by iteratively combining adjacent elements. This systematic reduction technique simplifies analysis while preserving circuit behavior.
