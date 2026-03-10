---
id: cpu-datapath
title: CPU Datapath
domain: computer-science
course: computer-architecture
prerequisites:
- id: arithmetic-logic-unit
  type: hard
- id: registers-and-register-files
  type: hard
- id: multiplexers-and-demultiplexers
  type: hard
- id: instruction-set-architecture
  type: soft
builds-toward:
- cpu-control-unit
- pipelining-fundamentals
tags:
- datapath
- CPU
- fetch-decode-execute
- microarchitecture
stage: formal-systems
status: draft
---

# CPU Datapath

## Core Idea
The CPU datapath is the collection of functional units and interconnects that carry data during instruction execution: the register file, ALU, program counter, instruction register, and data/address buses. Instructions follow a fetch-decode-execute cycle — the program counter addresses instruction memory, the fetched instruction is decoded into control signals, and operands flow through the ALU to produce a result that is written back to a register or memory. The datapath layout determines which operations can be performed and how control signals must be routed.

## How It's Best Learned
Trace a simple MIPS single-cycle datapath for ADD, LOAD, STORE, and BEQ instruction types. Draw the data flow for each and identify which MUX selections and control signals are needed. Build a datapath in a hardware simulator like Logisim.

## Common Misconceptions
- The datapath does not make decisions; all routing choices are determined by control signals from the control unit.
- A single-cycle datapath executes every instruction in one clock cycle, which is correct but inefficient — pipelining splits execution into stages to improve throughput.
