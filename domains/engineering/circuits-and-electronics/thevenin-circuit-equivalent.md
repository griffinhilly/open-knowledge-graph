---
id: thevenin-circuit-equivalent
title: Thévenin Equivalent Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-theorems-linearity
  type: hard
- id: ideal-voltage-and-current-sources
  type: hard
builds-toward:
- maximum-power-transfer
- sinusoidal-steady-state-analysis
tags:
- thevenin
- equivalent-circuit
- source-transformation
stage: formal-systems
status: draft
---

# Thévenin Equivalent Circuits

## Core Idea
Thévenin's theorem states any linear two-terminal circuit simplifies to a voltage source V_th in series with resistance R_th. V_th is the open-circuit voltage at the terminals, and R_th is found by zeroing independent sources and measuring resistance. This powerful simplification enables efficient load analysis and is widely used in circuit design.
