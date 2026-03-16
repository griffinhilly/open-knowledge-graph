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

## Explainer

You've studied the linearity property of circuits: responses scale proportionally with sources, and superposition holds. Thévenin's theorem is one of the most powerful consequences of linearity. It says that no matter how tangled a network of resistors and sources looks internally, from the perspective of any two terminals it behaves exactly like a single voltage source in series with a single resistor. Everything inside the box collapses to just two numbers: **V_th** and **R_th**.

Why does this work? Because the circuit is linear, the voltage at the output terminals must be a linear function of the current drawn from those terminals: V = V_oc − I·R_th. This is the equation of a straight line in V-I space, and a straight-line I-V relationship is precisely what a voltage source in series with a resistor produces. The intercept on the voltage axis (where I = 0) is the **open-circuit voltage V_th** — the terminal voltage when nothing is connected. The slope of the line is the **Thévenin resistance R_th** — how much the terminal voltage drops per unit of current drawn. These two quantities completely characterize how the circuit interacts with any external load.

Finding **V_th** is usually straightforward: remove the load, leave the terminals open-circuited, and calculate the voltage across those open terminals using whatever circuit analysis techniques fit (node voltage, mesh current, superposition). Finding **R_th** requires more care. The standard method is to deactivate all independent sources — **zero them** by replacing voltage sources with short circuits (wires) and current sources with open circuits (breaks) — and then measure the resistance seen looking into the terminals. With ideal sources zeroed, you're left with a resistor network whose equivalent resistance is R_th. If the circuit contains only independent sources, this always works. (If it contains dependent sources, R_th must be found by applying a test source and computing the ratio V_test/I_test, because zeroing dependent sources is invalid.)

The practical power of Thévenin equivalents is that they decouple the source network from the load. Suppose you're designing a sensor interface and want to know how a variable load resistor will affect the sensor output. Without Thévenin, you'd solve the whole circuit for each load value. With Thévenin, you reduce the source network once to V_th and R_th, then treat all load variations as a simple voltage divider: V_load = V_th · R_L / (R_th + R_L). The theorem scales up beautifully — multi-battery power supplies, IC output stages, audio amplifier outputs, and transmission line models are all routinely reduced to Thévenin equivalents to analyze how they interact with their loads. The **maximum power transfer theorem** (a direct consequence) states that maximum power is delivered to a load when R_L = R_th — you can only derive this cleanly because the Thévenin framework makes R_th visible as a distinct quantity.


