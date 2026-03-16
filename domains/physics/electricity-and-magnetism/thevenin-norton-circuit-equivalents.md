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

## Explainer

From Kirchhoff's laws and series-parallel combination, you can already solve any linear circuit — but for a circuit with many components, applying KVL and KCL directly can require solving large systems of equations. Thévenin's theorem offers a drastic shortcut: from the perspective of any pair of terminals, an entire network of resistors and sources looks like just one voltage source in series with one resistor. This is the **Thévenin equivalent**.

To find it, you need two numbers. The **Thévenin voltage** V_th is the open-circuit voltage across the terminals — what a voltmeter would read with nothing connected. This requires the full circuit analysis, but you only have to do it once. The **Thévenin resistance** R_th is the equivalent resistance seen looking back into the circuit with all independent sources turned off (voltage sources replaced by short circuits, current sources by open circuits). For the two-terminal equivalent, R_th = V_th / I_sc, where I_sc is the short-circuit current (the current that flows if you place a wire across the terminals). Once you have V_th and R_th, any load connected to those terminals sees exactly V_th in series with R_th — no matter how complex the original circuit was.

The **Norton equivalent** is the current-source dual: the same circuit appears as a current source I_N = V_th / R_th in parallel with R_N = R_th. Thévenin and Norton are interchangeable representations — a source transformation converts one to the other. The choice between them is purely one of convenience: if your load connects in series with the circuit, Thévenin is more natural; if your load connects in parallel, Norton is. Either way, the terminal behavior is identical.

The real power of these theorems appears when you want to analyze how a circuit responds to different loads. Instead of re-solving the whole circuit for each load value, you compute V_th and R_th once, then use the simple voltage divider V_load = V_th × R_load / (R_th + R_load). The **maximum power transfer theorem** — which builds directly on Thévenin equivalents — states that maximum power is delivered to a load when R_load = R_th. This has concrete engineering implications for amplifier output stages, transmission lines, and sensor circuits. The Thévenin framework reduces a complex matching problem to a one-parameter comparison.
