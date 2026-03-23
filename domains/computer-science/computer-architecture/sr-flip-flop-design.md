---
id: sr-flip-flop-design
title: SR (Set-Reset) Flip-Flops
domain: computer-science
course: computer-architecture
prerequisites:
- id: universal-logic-gates
  type: hard
builds-toward:
- d-flip-flop-design
- registers-and-register-files
tags:
- flip-flops
- sr
- latches
- sequential
stage: formal-systems
status: validated
---

# SR (Set-Reset) Flip-Flops

## Core Idea
SR flip-flops are the simplest sequential devices: Set forces output to 1, Reset forces output to 0, and neither (or both) leaves state unchanged. They form the basis for all other flip-flop designs.

## How It's Best Learned
Build an SR flip-flop from cross-coupled NOR gates; trace state transitions with a state table.

## Common Misconceptions
SR flip-flops are not edge-triggered—any pulse on Set or Reset causes immediate state change. Simultaneous Set and Reset is undefined behavior.

## Questions

```yaml
- question: "What property of the SR flip-flop circuit creates its memory behavior?"
  type: multiple-choice
  options:
    - "Using NOR gates, which naturally produce stable outputs independent of input history"
    - "Cross-coupled feedback, where each gate's output feeds into the other gate's input"
    - "Having two separate input lines (S and R) rather than a single control input"
    - "A built-in clock signal that synchronizes and holds state between pulses"
  answer: 1
  explanation: "Memory comes from feedback: each NOR gate's output drives an input of the other, creating a self-reinforcing loop. When Q = 1, it forces the other gate's output to 0, which in turn allows Q to stay at 1 — even after the Set input returns to 0. This is what crosses the threshold from combinational to sequential logic: the output depends on history, not just current inputs. Options A, C, and D all misidentify the source; notably, the basic SR latch has no clock."

- question: "What happens when both S and R inputs of an SR flip-flop are simultaneously set to 1?"
  type: multiple-choice
  options:
    - "The circuit enters a safe hold state, waiting until one input drops to 0"
    - "Reset takes priority — Q becomes 0 and Q̄ becomes 1"
    - "Both outputs become 0, violating complementarity, and the next state is unpredictable when inputs return to 0"
    - "Both outputs become 1, creating maximum excitation of the circuit"
  answer: 2
  explanation: "When S = R = 1, both NOR gates are forced to output 0, making Q = Q̄ = 0 — a violation of the intended complementary relationship. Worse, when both inputs return to 0, the final stable state depends on microscopic timing differences between the gates, making it unpredictable. This forbidden state is a real design constraint: later flip-flop designs (D, JK) add input logic that prevents this combination from ever reaching the cross-coupled core."

- question: "The SR flip-flop is a sequential circuit because its output depends on more than just the current values of S and R."
  type: true-false
  answer: true
  explanation: "When S = R = 0, the output Q can be either 0 or 1 — depending on which input was last activated. The same current inputs (S=0, R=0) produce different outputs depending on history. This history-dependence is the defining property of sequential logic. A combinational circuit's output is a pure function of its current inputs; a sequential circuit's output is a function of current inputs and stored state."

- question: "An SR flip-flop will hold its output state indefinitely after power is removed, since the cross-coupled feedback sustains itself."
  type: true-false
  answer: false
  explanation: "SR flip-flops require continuous power to maintain state — they are volatile storage elements. The cross-coupled feedback loop sustains state only while the NOR gates are actively powered. Remove power and the state is lost. This contrasts with non-volatile memory (like a mechanical switch or flash storage) that retains state without power. The 'memory' of an SR flip-flop is purely electrical and transient."

- question: "Explain how cross-coupling two NOR gates creates a circuit that remembers a past input, in a way a single NOR gate cannot."
  type: short-answer
  answer: "A single NOR gate has no memory — its output changes immediately with its inputs and reverts to 0 as soon as inputs go to 0. Cross-coupling creates a feedback loop: each gate's output drives an input of the other. When Set is pulsed to 1, Q is forced to 1, which then drives an input of the second gate, keeping its output (Q̄) at 0. That 0 feeds back to help maintain Q at 1 — even after the Set input returns to 0. The two gates lock each other into a self-sustaining state. This feedback is the mechanism of digital memory: the present output influences the gate's own inputs, which sustains the output indefinitely."
  explanation: "The key insight is that feedback introduces time-dependence. Without feedback, logic gates are purely reactive — they respond to current inputs with no history. The cross-coupled loop creates a causal cycle: the present output shapes the next input, which shapes the next output. This self-referential structure is the basis of all digital memory, from SR latches to SRAM cells in modern processors."
```

## Explainer

Up to this point, every circuit you have built with logic gates has been **combinational** — the output depends only on the current inputs. Change the inputs, and the output changes immediately (after gate delays). But a computer needs memory: circuits whose output depends on what happened *before*, not just what is happening now. The **SR flip-flop** is the simplest circuit that crosses this threshold from combinational to **sequential** logic, and it is built from the universal gates you already know.

Take two NOR gates and connect them in a loop: the output of each gate feeds into an input of the other. This **cross-coupled** arrangement creates a circuit with two stable states. Call the outputs Q and Q̄ (Q-bar). When Q is 1, it forces the other NOR gate's output to 0 (since any 1 input to a NOR produces 0), and that 0 feeds back to help keep Q at 1. The circuit is self-reinforcing — it "remembers" which state it is in without any external input holding it there. This is the fundamental mechanism of digital memory: feedback loops that sustain their own state.

The two remaining inputs are **Set (S)** and **Reset (R)**. Pulsing S to 1 forces Q to 1 regardless of its current state — the circuit "sets." Pulsing R to 1 forces Q to 0 — the circuit "resets." When both S and R are 0, the circuit holds whatever state it was last put into. This is the memory behavior: you set it, let go of the input, and the output stays. It is like a light switch that stays up or down after you flip it, unlike a doorbell button that only activates while you press it.

The one problematic case is when both S and R are 1 simultaneously. Both NOR gates are forced to output 0, making Q and Q̄ both 0 — which violates the rule that they should be complements. Worse, when both inputs return to 0, the final state depends on which gate is microscopically faster, making the outcome unpredictable. This **forbidden state** is a real design constraint, not just a theoretical concern. Later flip-flop designs (like the D flip-flop and JK flip-flop) solve this problem by adding input logic that prevents the forbidden combination from ever reaching the cross-coupled core, building on this SR foundation to create the reliable storage elements used throughout modern processors.
