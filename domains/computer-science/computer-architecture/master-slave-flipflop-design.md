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

## Questions

```yaml
- question: "In a master-slave flip-flop, when does the slave latch's output (the flip-flop's final output) change?"
  type: multiple-choice
  options:
    - "Continuously, whenever the input changes and the clock is high"
    - "During the entire low phase of the clock, as the slave latch tracks the master"
    - "At the clock edge — when the clock transitions and the slave latch opens"
    - "At both clock edges, once for each latch"
  answer: 2
  explanation: "Edge-triggered behavior is the whole point of the master-slave design. The master latch captures the input during one clock phase (say, clock high), then closes. When the clock transitions to low, the slave latch opens and copies the master's stored value to the output — a single, clean output transition at the clock edge. During the rest of the cycle, the output holds steady regardless of input changes. The output never tracks the input continuously, which is what made the single transparent latch problematic."

- question: "A 1-bit transparent latch is connected so that its output feeds through an inverter back to its own input. The enable pin is held permanently high. What behavior results?"
  type: multiple-choice
  options:
    - "The output cleanly toggles between 0 and 1 at a stable frequency"
    - "The output oscillates uncontrollably because the feedback loop races through the enabled latch"
    - "The output holds its initial value indefinitely because the latch ignores feedback"
    - "The output always settles to 0 regardless of initial conditions"
  answer: 1
  explanation: "When a transparent latch is enabled, its output follows its input. With feedback through an inverter, the output feeds an inverted copy of itself back to the input — while the latch is transparent, the value immediately changes, which inverts again, which changes again. This creates a race-through condition: the value oscillates at the speed of the propagation delays, not at any controlled clock frequency. This is exactly the problem master-slave flip-flops solve: the slave latch is always opaque when the master is transparent, breaking the feedback path."

- question: "In a master-slave flip-flop, when the master latch is transparent (actively capturing the input), the slave latch is opaque (holding its previous value)."
  type: true-false
  answer: true
  explanation: "True. The master and slave latches have complementary enable signals — when one is transparent, the other is opaque. This is the core of the design. While the master captures whatever is at the input, the slave holds its previous value and presents a stable output to the rest of the circuit. When the clock transitions, the master closes and the slave opens, cleanly passing the captured value to the output. This handoff ensures the output changes exactly once per clock edge."

- question: "The master-slave flip-flop design eliminates setup time and hold time requirements because the two-latch structure prevents any timing violations from affecting the output."
  type: true-false
  answer: false
  explanation: "False. The master-slave flip-flop still has setup time (the input must be stable before the capturing clock edge) and hold time (the input must remain stable for a brief period after the edge) requirements. If the input changes too close to the clock edge, the master latch may capture an indeterminate value, causing metastability — the flip-flop enters a state between 0 and 1 that takes an unpredictably long time to resolve. The two-latch structure prevents race-through on feedback paths but does not make the flip-flop immune to violations of its input timing constraints."

- question: "Explain why cascading two transparent latches with complementary enable signals produces edge-triggered behavior, when a single transparent latch does not."
  type: short-answer
  answer: "A single transparent latch passes its input directly to its output while enabled — any change at the input immediately propagates through. With feedback paths (as in a register or counter), this creates race-through. In the master-slave design, the master and slave are never both transparent simultaneously: when one is open, the other is locked. The master captures the input during one clock phase; when the clock transitions, the master locks and the slave opens — copying the master's captured value to the output in a single, fast transition. The output then holds until the next clock edge. The key is that the input and output are always separated by at least one opaque latch, so there is no direct path from input to output except through the clock edge."
  explanation: "This separation of 'capture phase' and 'output phase' is what all edge-triggered registers exploit. Modern flip-flops achieve the same result with fewer transistors using transmission gate designs, but the master-slave principle — alternating opaque/transparent latches — is the conceptual foundation."
```

## Explainer

You already understand how a **transparent latch** works: when its enable signal is high, the output follows the input; when enable goes low, the output holds its last captured value. This level-sensitive behavior is useful, but it creates a serious problem in synchronous circuits. If a latch's output feeds back (directly or through other logic) to its own input while it is transparent, the data can race through the feedback loop multiple times in a single clock phase, producing unpredictable results. The master-slave flip-flop solves this problem elegantly by chaining two latches with complementary enable signals.

The **master latch** is enabled when the clock is high and the **slave latch** is enabled when the clock is low (or vice versa, depending on the design convention). During the first half of the clock cycle, the master latch is transparent — it captures whatever value appears at the input. Meanwhile, the slave latch is opaque, holding its previous value and presenting a stable output to the rest of the circuit. When the clock transitions, the master latch closes (freezing the captured value) and the slave latch opens, passing the master's stored value to the output. The net effect is that the output changes exactly once per clock cycle, at the clock edge, regardless of how the input wiggles during the rest of the cycle.

This **edge-triggered behavior** is what makes the master-slave flip-flop the fundamental building block of synchronous digital design. Consider a simple example: a 1-bit register that feeds back to an inverter and then to its own input. With a transparent latch, the value would oscillate uncontrollably while the latch is enabled. With a master-slave flip-flop, the current value is read on one edge and the inverted value is written on the next edge — the circuit toggles cleanly, once per cycle, producing a divide-by-two frequency divider. This same principle scales to counters, shift registers, and the register files inside processors.

There are practical costs to the master-slave approach. The two-latch structure doubles the transistor count compared to a single latch, and the **setup time** (how early the input must be stable before the capturing edge) and **hold time** (how long it must remain stable after the edge) impose constraints on the surrounding logic. Violating these timing requirements causes **metastability**, where the flip-flop enters an indeterminate state between 0 and 1. Understanding these constraints is essential as you move toward designing synchronous counters and more complex sequential circuits.
