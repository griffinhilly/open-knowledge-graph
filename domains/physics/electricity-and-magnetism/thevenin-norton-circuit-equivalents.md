---
id: thevenin-norton-circuit-equivalents
title: Thévenin and Norton Circuit Equivalents
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: combination-series-parallel-networks
  type: hard
- id: kirchhoffs-rules
  type: hard
builds-toward:
- maximum-power-transfer
tags:
- circuit analysis
- equivalence
- network reduction
stage: formal-systems
status: draft
---

# Thévenin and Norton Circuit Equivalents

## Core Idea
Any linear circuit can be replaced by a Thévenin equivalent: a voltage source V_th in series with resistance R_th. Equivalently, it can be represented as a Norton equivalent: current source I_N = V_th/R_th in parallel with R_N = R_th. These equivalents greatly simplify analysis by replacing complex networks with simple elements when analyzing terminal behavior.

## How It's Best Learned
For a given circuit, calculate V_th (open-circuit voltage), I_sc (short-circuit current), and R_th = V_th/I_sc. Verify equivalence by comparing terminal characteristics for different load resistances.

## Common Misconceptions
- Thévenin and Norton are fundamentally different (they are equivalent representations).
- Thévenin resistance is the internal resistance of an actual voltage source (it is the equivalent resistance seen looking into the circuit).
- These equivalents apply to nonlinear circuits (they only apply to linear circuits).
