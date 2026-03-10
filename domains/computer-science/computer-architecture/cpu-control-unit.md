---
id: cpu-control-unit
title: CPU Control Unit
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: finite-state-machines
  type: hard
- id: instruction-set-architecture
  type: hard
builds-toward:
- pipelining-fundamentals
tags:
- control-unit
- hardwired-control
- microprogramming
- control-signals
stage: formal-systems
status: draft
---

# CPU Control Unit

## Core Idea
The control unit decodes each instruction's opcode and generates the control signals that orchestrate data movement through the datapath: register reads/writes, ALU function select, memory enables, and MUX selections. Hardwired control implements the control logic directly as combinational/sequential circuits — fast but inflexible. Microprogrammed control stores microinstructions in a ROM and interprets them — slower but easier to modify. Modern high-performance CPUs use hardwired control, while microprogramming suits complex ISAs or updatable firmware.

## How It's Best Learned
Build a truth-table-based control unit for a small ISA of 5–10 instructions. Trace how each opcode produces a unique pattern of control signals. Compare hardwired and microprogrammed implementations by examining the control logic for a multi-cycle processor.

## Common Misconceptions
- The control unit does not perform arithmetic; it only generates the signals that tell the datapath what to do.
- Microprogramming is not the same as writing software; microcode controls individual hardware signals at a level below any programming language.
