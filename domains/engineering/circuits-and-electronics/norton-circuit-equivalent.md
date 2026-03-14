---
id: norton-circuit-equivalent
title: Norton Equivalent Circuits
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
- norton
- equivalent-circuit
- current-source
- duality
stage: formal-systems
status: draft
---

# Norton Equivalent Circuits

## Core Idea
Norton's theorem is the dual of Thévenin's: any linear circuit simplifies to a current source I_N in parallel with resistance R_N. Norton current is the short-circuit current, and Norton resistance equals Thévenin resistance. The two theorems are interchangeable via I_N = V_th/R_th, providing flexibility in circuit analysis.
