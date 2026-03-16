---
id: combination-series-parallel-networks
title: Combination Series-Parallel Networks and Reduction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: series-circuits-resistance-voltage
  type: hard
- id: parallel-circuits-conductance-current
  type: hard
builds-toward:
- thevenin-norton-circuit-equivalents
tags:
- circuit analysis
- network analysis
- reduction
stage: formal-systems
status: draft
---

# Combination Series-Parallel Networks and Reduction

## Core Idea
Real circuits contain both series and parallel combinations. Analysis proceeds by identifying sub-networks and combining them systematically using appropriate rules. The circuit is reduced step by step by replacing series and parallel sub-networks with equivalent resistances until a simple expression is obtained.

## How It's Best Learned
Start with circuits having one or two combinations. Draw the circuit, identify sub-networks, calculate equivalent resistance, and verify with measurements.

## Common Misconceptions
- There is only one way to combine resistors (different orderings work if done correctly).
- After combining, ignore which elements were combined (labeling prevents confusion).
- All series or parallel combinations are obvious (careful analysis is required).

## Explainer

Real circuits rarely consist of purely series or purely parallel elements. Most practical networks mix both, and the key to analyzing them is a systematic reduction strategy: identify a sub-network that is purely series or purely parallel, replace it with its equivalent resistance, then repeat until the circuit collapses to a single equivalent resistance between two terminals.

The rules you already know are the building blocks. From series circuits, you know that resistances in series add directly: R_eq = R₁ + R₂ + ... because the same current flows through each and voltages add. From parallel circuits, you know that conductances add: 1/R_eq = 1/R₁ + 1/R₂ + ... because the same voltage appears across each and currents add. In a combination network, you apply whichever rule applies to each sub-group, one step at a time.

Consider a concrete example: two 6 Ω resistors in parallel, connected in series with a 4 Ω resistor, powered by a 12 V source. Step 1: combine the parallel pair — 1/R_eq = 1/6 + 1/6 = 1/3, so R_eq = 3 Ω. Step 2: add the series resistor — 3 + 4 = 7 Ω total. Step 3: find total current — I = 12/7 ≈ 1.71 A. This current flows through the 4 Ω resistor, dropping 4 × 1.71 ≈ 6.86 V, leaving 12 − 6.86 ≈ 5.14 V across the parallel pair — which each 6 Ω resistor shares. At each step, you reduce the network to something simpler.

**The reduction method** is not the only approach, but it is the most intuitive one for networks without loops that cannot be decomposed (those require Kirchhoff's laws or more advanced techniques like node-voltage analysis). The discipline of labeling which elements you have combined prevents errors when you later need to find voltage drops or branch currents across individual components. Once you have the total equivalent resistance, work backward: restore each reduction step, use the known current or voltage at that stage, and find the quantities of interest for each element. Combination analysis is the bridge between simple single-rule circuits and the full generality of circuit theory.

