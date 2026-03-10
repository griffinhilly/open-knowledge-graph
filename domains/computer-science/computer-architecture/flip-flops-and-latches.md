---
id: flip-flops-and-latches
title: Flip-Flops and Latches
domain: computer-science
course: computer-architecture
prerequisites:
- id: logic-gates-and-circuits
  type: hard
- id: combinational-circuit-design
  type: soft
builds-toward:
- registers-and-register-files
- finite-state-machines
- sequential-circuit-design
tags:
- flip-flop
- latch
- sequential-logic
- memory
- clock
stage: formal-systems
status: draft
---

# Flip-Flops and Latches

## Core Idea
Latches and flip-flops are bistable memory elements that store a single bit. A latch is level-sensitive: its output can change whenever the enable signal is active. A flip-flop is edge-triggered: its output changes only on the rising or falling edge of a clock signal. The D flip-flop (data or delay) is the most common type: it captures its D input at the clock edge and holds it until the next edge. Flip-flops are the fundamental building blocks of registers, counters, and all sequential digital circuits.

## How It's Best Learned
Build an SR latch from NOR gates and observe its feedback behavior. Compare a D latch and D flip-flop, focusing on when output changes relative to clock and data. Use timing diagrams to visualize setup time, hold time, and propagation delay.

## Common Misconceptions
- Latches are not broken flip-flops — they are intentionally level-sensitive and used in specific contexts, but edge-triggered flip-flops are preferred for synchronous design.
- The clock does not directly hold the stored value; the feedback loop within the flip-flop maintains state between clock edges.
