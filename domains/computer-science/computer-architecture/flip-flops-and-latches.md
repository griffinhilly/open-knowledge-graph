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

## Questions

```yaml
- question: "A D latch has its enable signal held high for 100 nanoseconds while the D input toggles between 0 and 1 multiple times. What does the output Q do during this period?"
  type: multiple-choice
  options:
    - "Q remains at the value captured when enable first went high"
    - "Q changes only at the end of the enable pulse, capturing the final D value"
    - "Q continuously tracks the D input — the latch is transparent while enable is high"
    - "Q enters an indeterminate state because D is changing"
  answer: 2
  explanation: "A latch is level-sensitive: while enable is high, the output Q continuously follows the D input — this is called being 'transparent.' This is the fundamental distinction from a flip-flop. A D flip-flop would capture D only at the rising (or falling) clock edge and hold it regardless of subsequent D changes. The transparency of latches is what makes them problematic in synchronous design: signals can 'race' through multiple latches in a single clock phase."

- question: "A D flip-flop's D input changes value 10 nanoseconds before the rising clock edge and remains stable for 5 nanoseconds after. The setup time is 8 ns and hold time is 3 ns. What happens?"
  type: multiple-choice
  options:
    - "The flip-flop correctly captures the new D value — both setup and hold times are satisfied"
    - "The flip-flop enters metastability — the setup time requirement is violated"
    - "The flip-flop captures the old D value — data that arrives that late cannot be captured"
    - "The flip-flop enters metastability — the hold time requirement is violated"
  answer: 0
  explanation: "Setup time requires D to be stable for 8 ns before the clock edge — D changed 10 ns before the edge, so it has been stable for 10 ns (satisfied). Hold time requires D to remain stable 3 ns after the clock edge — it stays stable 5 ns after (satisfied). Both constraints are met, so the flip-flop correctly captures the new D value. Metastability only occurs when D changes too close to or during the clock edge, violating setup or hold time."

- question: "The clock signal in a synchronous circuit is what maintains the stored bit value in a flip-flop between clock edges."
  type: true-false
  answer: false
  explanation: "The bit value is maintained by the internal feedback loop, not by the clock. Between clock edges, the clock may be low, but the stored value is held by the cross-coupled feedback in the circuit — the same mechanism as the SR latch. The clock's role is to control WHEN a new value is captured. Once captured, the feedback loop holds the value independently of what the clock is doing."

- question: "Edge-triggered flip-flops are preferred over level-sensitive latches for synchronous digital design."
  type: true-false
  answer: true
  explanation: "Edge triggering gives precise, predictable state changes synchronized to a single moment per clock cycle. Level-sensitive latches are 'transparent' whenever enable is high, creating windows where signals can race through multiple stages unexpectedly. Synchronous design requires that all state changes happen at known, coordinated moments so that timing analysis is tractable. Flip-flops, by sampling exactly at the clock edge, make timing analysis well-defined: signals must be stable within the setup/hold window, and propagation delays are bounded by the clock period."

- question: "Explain how the feedback structure inside a flip-flop allows it to maintain a stored value indefinitely between clock edges."
  type: short-answer
  answer: "The flip-flop contains a cross-coupled feedback loop (inherited from the SR latch) where the output of each gate feeds back into the input of the other. This creates two stable states: Q=1,Q̄=0 and Q=0,Q̄=1. Once the circuit settles into one state, the feedback reinforces itself — each gate's output keeps the other gate in a consistent state. This self-reinforcing loop persists regardless of what happens at the data input or clock, holding the bit until the next active clock edge causes the circuit to capture a new value."
  explanation: "Feedback is what distinguishes sequential circuits from combinational ones. In a combinational circuit, outputs are functions of current inputs only. In a bistable flip-flop, the feedback loop is the storage mechanism: it creates memory that persists even when inputs change. The clock edge momentarily connects the data input to the feedback loop, updating the stored value, then the loop closes again to hold the new state. This also explains why setup/hold times matter: if D changes during the capture window, the feedback loop receives inconsistent inputs and can enter a metastable state between 0 and 1."
```

## Explainer

From your work with logic gates, you know that combinational circuits produce outputs determined entirely by their current inputs — change the inputs, the outputs change. But a computer needs **memory**: circuits that hold a value even after the input that produced it is gone. Flip-flops and latches are the simplest circuits that achieve this, and they do it through a single powerful idea — **feedback**.

The most basic memory element is the **SR latch**, built from two cross-coupled NOR gates (or NAND gates). Each gate's output feeds into the other gate's input, creating a stable loop. This feedback means the circuit has two stable states: one where Q = 1 and Q̄ = 0, and one where Q = 0 and Q̄ = 1. Once the circuit settles into one state, it stays there — the feedback reinforces itself. The Set input forces Q to 1; the Reset input forces Q to 0. When neither is active, the latch **remembers** its last commanded state. This is how one bit of information persists in hardware.

The problem with a raw SR latch is that its output changes the moment an input changes — there is no coordination with the rest of the circuit. In a digital system with many interconnected components, you need all state changes to happen at predictable, synchronized moments. A **gated latch** adds an enable signal: the latch only responds to its inputs when enable is active (high). A **D latch** simplifies this further by having a single data input D, which is captured whenever enable is high. But a level-sensitive latch is transparent — while enable is high, the output tracks the input continuously, which can cause timing problems when one latch's output feeds another latch's input in the same clock phase.

The **D flip-flop** solves this with **edge triggering**. Instead of being transparent while the clock is high, a D flip-flop captures its input only at the precise moment of a clock edge (typically the rising edge). One common implementation is the **master-slave** design: two D latches in series, where the first (master) is transparent when the clock is low and the second (slave) is transparent when the clock is high. At the rising clock edge, the master closes (freezing its captured value) and the slave opens (passing that value to the output). The result is that the output changes exactly once per clock cycle, at the clock edge, regardless of how the D input varies between edges.

Edge-triggered flip-flops are the foundation of **synchronous digital design**. Every register in a processor, every bit of a counter, every state element in a finite state machine is built from flip-flops. Two critical timing parameters govern their use: **setup time** (how long the D input must be stable before the clock edge) and **hold time** (how long it must remain stable after the clock edge). Violating these constraints causes **metastability** — the flip-flop enters an undefined state between 0 and 1, which can propagate errors through the entire system. Understanding setup and hold times is essential when you move on to designing registers, state machines, and pipelined processors, where every clock edge must find valid, stable data at every flip-flop input.
