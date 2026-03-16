---
id: d-flip-flop-design
title: D (Data) Flip-Flop and Edge Triggering
domain: computer-science
course: computer-architecture
prerequisites:
- id: sr-flip-flop-design
  type: hard
builds-toward:
- registers-and-register-files
- counters-design-analysis
tags:
- flip-flops
- d-latch
- edge-triggered
- sequential
stage: formal-systems
status: draft
---

# D (Data) Flip-Flop and Edge Triggering

## Core Idea
D flip-flops capture a single data bit at the rising (or falling) edge of a clock signal, isolating input changes from affecting output until the next clock pulse. This edge-triggered behavior is essential for synchronous digital design.

## How It's Best Learned
Compare D latch (level-triggered) with edge-triggered D flip-flop; observe timing diagrams showing setup and hold time requirements.

## Common Misconceptions
D flip-flops respond to input changes only at the clock edge, not continuously. Setup and hold time violations cause metastable states.

## Explainer

From your study of the SR flip-flop, you know that sequential circuits can store a single bit of state — they "remember" a value even after the input that set it is removed. But the SR flip-flop has an awkward problem: setting both S and R to 1 simultaneously produces undefined behavior. The **D flip-flop** solves this elegantly by using a single data input (D) and a clock signal. The idea is simple: whatever value D holds at the moment the clock transitions (the **clock edge**) gets captured and held at the output Q until the next clock edge. Between edges, changes to D are ignored.

The distinction between **level-triggered** and **edge-triggered** behavior is central. A D *latch* is level-triggered: it is "transparent" whenever the clock is high, meaning the output follows the input continuously during that entire period. This creates a problem in sequential circuits where one latch's output feeds into another's input — if both are transparent simultaneously, data can race through multiple stages in a single clock cycle, producing unpredictable results. An edge-triggered D *flip-flop* avoids this by capturing data only during the instantaneous transition of the clock (typically the rising edge, from 0 to 1). A common implementation uses two D latches in a **master-slave** configuration: the master latch captures D while the clock is low, and the slave latch transfers the master's value to the output when the clock goes high. At no point are both latches transparent at the same time.

For edge-triggering to work correctly, the data input must be stable during a narrow window around the clock edge. The **setup time** is how long before the clock edge D must be stable; the **hold time** is how long after the edge D must remain stable. If either requirement is violated, the flip-flop can enter a **metastable state** — an electrical condition between 0 and 1 where the output oscillates or settles unpredictably. Metastability is not a logic error but a physical one, and it is a major concern when signals cross between different clock domains.

D flip-flops are the fundamental storage element in synchronous digital design. A CPU register is simply a row of D flip-flops sharing a common clock — on each clock edge, all flip-flops capture their inputs simultaneously, updating the register's stored value in lockstep. Counters chain flip-flops so that each one's output clocks the next. The entire discipline of synchronous design rests on the guarantee that D flip-flops provide: data moves through the system one clock edge at a time, in a controlled and predictable sequence.
