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
status: draft
---

# SR (Set-Reset) Flip-Flops

## Core Idea
SR flip-flops are the simplest sequential devices: Set forces output to 1, Reset forces output to 0, and neither (or both) leaves state unchanged. They form the basis for all other flip-flop designs.

## How It's Best Learned
Build an SR flip-flop from cross-coupled NOR gates; trace state transitions with a state table.

## Common Misconceptions
SR flip-flops are not edge-triggered—any pulse on Set or Reset causes immediate state change. Simultaneous Set and Reset is undefined behavior.

## Explainer

Up to this point, every circuit you have built with logic gates has been **combinational** — the output depends only on the current inputs. Change the inputs, and the output changes immediately (after gate delays). But a computer needs memory: circuits whose output depends on what happened *before*, not just what is happening now. The **SR flip-flop** is the simplest circuit that crosses this threshold from combinational to **sequential** logic, and it is built from the universal gates you already know.

Take two NOR gates and connect them in a loop: the output of each gate feeds into an input of the other. This **cross-coupled** arrangement creates a circuit with two stable states. Call the outputs Q and Q̄ (Q-bar). When Q is 1, it forces the other NOR gate's output to 0 (since any 1 input to a NOR produces 0), and that 0 feeds back to help keep Q at 1. The circuit is self-reinforcing — it "remembers" which state it is in without any external input holding it there. This is the fundamental mechanism of digital memory: feedback loops that sustain their own state.

The two remaining inputs are **Set (S)** and **Reset (R)**. Pulsing S to 1 forces Q to 1 regardless of its current state — the circuit "sets." Pulsing R to 1 forces Q to 0 — the circuit "resets." When both S and R are 0, the circuit holds whatever state it was last put into. This is the memory behavior: you set it, let go of the input, and the output stays. It is like a light switch that stays up or down after you flip it, unlike a doorbell button that only activates while you press it.

The one problematic case is when both S and R are 1 simultaneously. Both NOR gates are forced to output 0, making Q and Q̄ both 0 — which violates the rule that they should be complements. Worse, when both inputs return to 0, the final state depends on which gate is microscopically faster, making the outcome unpredictable. This **forbidden state** is a real design constraint, not just a theoretical concern. Later flip-flop designs (like the D flip-flop and JK flip-flop) solve this problem by adding input logic that prevents the forbidden combination from ever reaching the cross-coupled core, building on this SR foundation to create the reliable storage elements used throughout modern processors.
