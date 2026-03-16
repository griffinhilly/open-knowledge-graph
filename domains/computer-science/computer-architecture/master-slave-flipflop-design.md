---
id: master-slave-flipflop-design
title: Master-Slave Flip-Flop Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: transparent-latch-design
  type: hard
builds-toward:
- synchronous-counter-design
tags:
- flipflop
- edge-triggered
- sequential-logic
stage: formal-systems
status: draft
---

# Master-Slave Flip-Flop Design

## Core Idea
Master-slave flip-flops cascade two transparent latches: master captures on one clock edge, slave captures the master's output on the opposite edge. This provides edge-triggered behavior and eliminates race conditions.

## Explainer

You already understand how a **transparent latch** works: when its enable signal is high, the output follows the input; when enable goes low, the output holds its last captured value. This level-sensitive behavior is useful, but it creates a serious problem in synchronous circuits. If a latch's output feeds back (directly or through other logic) to its own input while it is transparent, the data can race through the feedback loop multiple times in a single clock phase, producing unpredictable results. The master-slave flip-flop solves this problem elegantly by chaining two latches with complementary enable signals.

The **master latch** is enabled when the clock is high and the **slave latch** is enabled when the clock is low (or vice versa, depending on the design convention). During the first half of the clock cycle, the master latch is transparent — it captures whatever value appears at the input. Meanwhile, the slave latch is opaque, holding its previous value and presenting a stable output to the rest of the circuit. When the clock transitions, the master latch closes (freezing the captured value) and the slave latch opens, passing the master's stored value to the output. The net effect is that the output changes exactly once per clock cycle, at the clock edge, regardless of how the input wiggles during the rest of the cycle.

This **edge-triggered behavior** is what makes the master-slave flip-flop the fundamental building block of synchronous digital design. Consider a simple example: a 1-bit register that feeds back to an inverter and then to its own input. With a transparent latch, the value would oscillate uncontrollably while the latch is enabled. With a master-slave flip-flop, the current value is read on one edge and the inverted value is written on the next edge — the circuit toggles cleanly, once per cycle, producing a divide-by-two frequency divider. This same principle scales to counters, shift registers, and the register files inside processors.

There are practical costs to the master-slave approach. The two-latch structure doubles the transistor count compared to a single latch, and the **setup time** (how early the input must be stable before the capturing edge) and **hold time** (how long it must remain stable after the edge) impose constraints on the surrounding logic. Violating these timing requirements causes **metastability**, where the flip-flop enters an indeterminate state between 0 and 1. Understanding these constraints is essential as you move toward designing synchronous counters and more complex sequential circuits.
