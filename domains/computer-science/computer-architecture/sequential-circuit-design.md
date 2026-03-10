---
id: sequential-circuit-design
title: Sequential Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: finite-state-machines
  type: hard
- id: registers-and-register-files
  type: soft
- id: boolean-algebra
  type: soft
- id: logic-gates-and-circuits
  type: soft
builds-toward:
- cpu-datapath
- cpu-control-unit
tags:
- sequential-circuits
- counters
- shift-registers
- synchronous-design
stage: formal-systems
status: draft
---

# Sequential Circuit Design

## Core Idea
Sequential circuit design applies FSM theory to build concrete hardware components: counters (which cycle through a sequence of binary states), shift registers (which shift stored bits on each clock edge), and more complex sequencing circuits. Synchronous design — where all flip-flops share a common clock — is the dominant methodology because it simplifies timing analysis and prevents race conditions. Design proceeds by specifying the state diagram, deriving excitation equations, and mapping to physical flip-flops and gates.

## How It's Best Learned
Design a 3-bit binary up-counter and a Johnson counter from FSM principles. Build a parallel-load shift register and trace its operation. Use a logic simulator to verify timing and identify any setup/hold violations.

## Common Misconceptions
- Sequential circuits are not simply combinational circuits plus memory — the feedback from state elements fundamentally changes the circuit's behavior.
- Asynchronous design is not simpler despite lacking a clock; it is harder to get right due to race conditions and metastability.
