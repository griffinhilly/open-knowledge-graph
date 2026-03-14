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
