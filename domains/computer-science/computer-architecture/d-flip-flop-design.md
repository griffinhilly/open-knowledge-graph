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
status: validated
---

# D (Data) Flip-Flop and Edge Triggering

## Core Idea
D flip-flops capture a single data bit at the rising (or falling) edge of a clock signal, isolating input changes from affecting output until the next clock pulse. This edge-triggered behavior is essential for synchronous digital design.

## How It's Best Learned
Compare D latch (level-triggered) with edge-triggered D flip-flop; observe timing diagrams showing setup and hold time requirements.

## Common Misconceptions
D flip-flops respond to input changes only at the clock edge, not continuously. Setup and hold time violations cause metastable states.

## Questions

```yaml
- question: "A D flip-flop's input D changes from 0 to 1 at t=2ns, then back to 0 at t=4ns, then to 1 at t=6ns. The rising clock edge occurs at t=5ns. What is the output Q immediately after the clock edge?"
  type: multiple-choice
  options:
    - "1 — because D was 1 for the most recent transition before the clock edge"
    - "0 — because D is 0 at the moment of the rising clock edge"
    - "1 — because D was 1 for longer during the clock cycle than it was 0"
    - "Undefined — because D changed multiple times during the cycle"
  answer: 1
  explanation: "An edge-triggered D flip-flop captures exactly the value of D at the instant of the clock's rising edge — and only at that instant. At t=5ns, D is 0, so Q becomes 0. All earlier values of D during the cycle are irrelevant. This is the defining behavior of edge triggering: D can toggle freely between clock edges without affecting the output. A D latch would behave differently — it would track D continuously while its enable signal is high."

- question: "Why does using level-triggered D latches instead of edge-triggered D flip-flops cause problems in sequential circuits?"
  type: multiple-choice
  options:
    - "D latches consume significantly more power than flip-flops"
    - "During the transparent phase, data can race through multiple stages in one clock cycle, causing unpredictable behavior"
    - "D latches cannot store a logic 1 value reliably"
    - "D latches require two clock signals while flip-flops only need one"
  answer: 1
  explanation: "When a D latch is 'transparent' (enabled), its output follows its input continuously. If one latch's output feeds the next latch's input and both are simultaneously transparent, data can propagate through multiple stages in a single clock cycle — a 'race through' condition that breaks the assumption that each stage updates exactly once per cycle. Edge-triggered flip-flops eliminate this by limiting data capture to the instantaneous clock transition, ensuring the circuit advances exactly one step per clock edge."

- question: "A D flip-flop is level-triggered, meaning its output follows the input continuously whenever the clock is high."
  type: true-false
  answer: false
  explanation: "This describes a D *latch*, not a D *flip-flop*. An edge-triggered D flip-flop captures the input only during the brief moment the clock transitions (typically the rising edge from 0 to 1). Between clock edges, the flip-flop's output is held stable regardless of changes to D. The level-triggered vs. edge-triggered distinction is precisely what separates a latch from a flip-flop — it is the most important conceptual difference between the two devices."

- question: "Violating a D flip-flop's setup time requirement — changing D too close to the rising clock edge — can cause the flip-flop to output a voltage between valid 0 and 1 levels."
  type: true-false
  answer: true
  explanation: "This is called metastability. If D is changing at the moment the clock edge arrives, the internal circuitry may not settle cleanly to a valid logic level. Instead, the output can become 'stuck' at an intermediate voltage for an unpredictably long time before resolving. Metastability is not a logic error but a physical analog phenomenon, and it is a genuine design concern — especially when signals cross between different clock domains."

- question: "What fundamental problem does edge-triggering solve, and how does the master-slave D flip-flop design achieve edge-triggered behavior?"
  type: short-answer
  answer: "Edge-triggering solves the 'race through' problem: with level-triggered latches, multiple stages can be simultaneously transparent, allowing data to ripple through the entire circuit in one clock cycle uncontrollably. The master-slave design uses two latches in series: the master captures D while the clock is low (slave is opaque), then the slave transfers the master's value to the output when the clock goes high (master becomes opaque). At no point are both latches transparent simultaneously, so data advances exactly one stage per clock edge."
  explanation: "The core guarantee of synchronous design is that each storage element updates exactly once per clock cycle. Level-triggered latches violate this by being transparent for a finite window. Edge-triggering creates a single discrete moment of data transfer. The master-slave configuration enforces this by ensuring one latch is always opaque — data cannot race through because there is always a closed gate blocking the path."
```

## Explainer

From your study of the SR flip-flop, you know that sequential circuits can store a single bit of state — they "remember" a value even after the input that set it is removed. But the SR flip-flop has an awkward problem: setting both S and R to 1 simultaneously produces undefined behavior. The **D flip-flop** solves this elegantly by using a single data input (D) and a clock signal. The idea is simple: whatever value D holds at the moment the clock transitions (the **clock edge**) gets captured and held at the output Q until the next clock edge. Between edges, changes to D are ignored.

The distinction between **level-triggered** and **edge-triggered** behavior is central. A D *latch* is level-triggered: it is "transparent" whenever the clock is high, meaning the output follows the input continuously during that entire period. This creates a problem in sequential circuits where one latch's output feeds into another's input — if both are transparent simultaneously, data can race through multiple stages in a single clock cycle, producing unpredictable results. An edge-triggered D *flip-flop* avoids this by capturing data only during the instantaneous transition of the clock (typically the rising edge, from 0 to 1). A common implementation uses two D latches in a **master-slave** configuration: the master latch captures D while the clock is low, and the slave latch transfers the master's value to the output when the clock goes high. At no point are both latches transparent at the same time.

For edge-triggering to work correctly, the data input must be stable during a narrow window around the clock edge. The **setup time** is how long before the clock edge D must be stable; the **hold time** is how long after the edge D must remain stable. If either requirement is violated, the flip-flop can enter a **metastable state** — an electrical condition between 0 and 1 where the output oscillates or settles unpredictably. Metastability is not a logic error but a physical one, and it is a major concern when signals cross between different clock domains.

D flip-flops are the fundamental storage element in synchronous digital design. A CPU register is simply a row of D flip-flops sharing a common clock — on each clock edge, all flip-flops capture their inputs simultaneously, updating the register's stored value in lockstep. Counters chain flip-flops so that each one's output clocks the next. The entire discipline of synchronous design rests on the guarantee that D flip-flops provide: data moves through the system one clock edge at a time, in a controlled and predictable sequence.
