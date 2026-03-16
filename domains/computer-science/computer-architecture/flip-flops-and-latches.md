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
status: validated
---

# Flip-Flops and Latches

## Core Idea
Latches and flip-flops are bistable memory elements that store a single bit. A latch is level-sensitive: its output can change whenever the enable signal is active. A flip-flop is edge-triggered: its output changes only on the rising or falling edge of a clock signal. The D flip-flop (data or delay) is the most common type: it captures its D input at the clock edge and holds it until the next edge. Flip-flops are the fundamental building blocks of registers, counters, and all sequential digital circuits.

## How It's Best Learned
Build an SR latch from NOR gates and observe its feedback behavior. Compare a D latch and D flip-flop, focusing on when output changes relative to clock and data. Use timing diagrams to visualize setup time, hold time, and propagation delay.

## Common Misconceptions
- Latches are not broken flip-flops — they are intentionally level-sensitive and used in specific contexts, but edge-triggered flip-flops are preferred for synchronous design.
- The clock does not directly hold the stored value; the feedback loop within the flip-flop maintains state between clock edges.

## Explainer

From your work with logic gates, you know that combinational circuits produce outputs determined entirely by their current inputs — change the inputs, the outputs change. But a computer needs **memory**: circuits that hold a value even after the input that produced it is gone. Flip-flops and latches are the simplest circuits that achieve this, and they do it through a single powerful idea — **feedback**.

The most basic memory element is the **SR latch**, built from two cross-coupled NOR gates (or NAND gates). Each gate's output feeds into the other gate's input, creating a stable loop. This feedback means the circuit has two stable states: one where Q = 1 and Q̄ = 0, and one where Q = 0 and Q̄ = 1. Once the circuit settles into one state, it stays there — the feedback reinforces itself. The Set input forces Q to 1; the Reset input forces Q to 0. When neither is active, the latch **remembers** its last commanded state. This is how one bit of information persists in hardware.

The problem with a raw SR latch is that its output changes the moment an input changes — there is no coordination with the rest of the circuit. In a digital system with many interconnected components, you need all state changes to happen at predictable, synchronized moments. A **gated latch** adds an enable signal: the latch only responds to its inputs when enable is active (high). A **D latch** simplifies this further by having a single data input D, which is captured whenever enable is high. But a level-sensitive latch is transparent — while enable is high, the output tracks the input continuously, which can cause timing problems when one latch's output feeds another latch's input in the same clock phase.

The **D flip-flop** solves this with **edge triggering**. Instead of being transparent while the clock is high, a D flip-flop captures its input only at the precise moment of a clock edge (typically the rising edge). One common implementation is the **master-slave** design: two D latches in series, where the first (master) is transparent when the clock is low and the second (slave) is transparent when the clock is high. At the rising clock edge, the master closes (freezing its captured value) and the slave opens (passing that value to the output). The result is that the output changes exactly once per clock cycle, at the clock edge, regardless of how the D input varies between edges.

Edge-triggered flip-flops are the foundation of **synchronous digital design**. Every register in a processor, every bit of a counter, every state element in a finite state machine is built from flip-flops. Two critical timing parameters govern their use: **setup time** (how long the D input must be stable before the clock edge) and **hold time** (how long it must remain stable after the clock edge). Violating these constraints causes **metastability** — the flip-flop enters an undefined state between 0 and 1, which can propagate errors through the entire system. Understanding setup and hold times is essential when you move on to designing registers, state machines, and pipelined processors, where every clock edge must find valid, stable data at every flip-flop input.
