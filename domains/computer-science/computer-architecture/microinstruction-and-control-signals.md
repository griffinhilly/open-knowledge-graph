---
id: microinstruction-and-control-signals
title: Microinstruction Format and Control Signals
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-control-unit
  type: hard
- id: instruction-encoding-format
  type: soft
tags:
- control
- microinstruction
- cpu-design
stage: formal-systems
status: draft
---

# Microinstruction Format and Control Signals

## Core Idea
Microinstructions define the control signals (ALU operation, register writes, memory access) executed during each clock cycle. Hardwired control derives these directly from the instruction; microprogrammed control stores microcode in ROM.

## Explainer

From your study of the CPU control unit, you know that the processor must generate the right signals at the right time to orchestrate data movement through the datapath. A **microinstruction** is a single word — a bit pattern — where each bit or group of bits directly controls one piece of the hardware: which registers to read, what operation the ALU should perform, whether to write to memory, whether to update the program counter. Think of it as a row of switches, where each switch enables or disables a specific datapath action for one clock cycle.

A complete machine instruction (like ADD or LOAD) typically requires a sequence of these microinstructions, called a **microprogram**. For example, executing an ADD instruction might take three microinstructions: one to fetch the instruction from memory, one to read source registers and configure the ALU, and one to write the result back. Each microinstruction activates a different combination of control signals. The microprogram for each machine instruction is stored in a small, fast read-only memory called the **control store**. When the processor decodes a machine instruction, it looks up the starting address of the corresponding microprogram and steps through it one microinstruction per clock cycle.

The format of a microinstruction involves a design tradeoff between width and encoding density. In a **horizontal** microinstruction, each control signal gets its own dedicated bit — the word is wide (potentially hundreds of bits) but simple to decode because each bit maps directly to a wire. In a **vertical** microinstruction, control signals are encoded into smaller fields that must be decoded through additional logic, producing narrower words but requiring an extra decoding step. Most real designs use a hybrid approach, grouping mutually exclusive signals (like ALU operations, where only one can be active at a time) into encoded fields while leaving independent signals as direct bits.

The alternative to microprogrammed control is **hardwired control**, where combinational logic circuits directly generate control signals from the instruction opcode and the current cycle. Hardwired control is faster because there is no control store lookup, but it is inflexible — changing or adding instructions requires redesigning the logic. Microprogrammed control trades some speed for enormous flexibility: fixing a bug or adding a new instruction means changing microcode in ROM rather than rewiring hardware. This tradeoff explains why early complex instruction set computers (CISC) favored microprogramming, while simpler RISC architectures could afford hardwired control due to their smaller, more regular instruction sets.
