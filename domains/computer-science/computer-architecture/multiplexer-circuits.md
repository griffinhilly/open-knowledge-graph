---
id: multiplexer-circuits
title: Multiplexers and Demultiplexers
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-logic-implementation
  type: hard
- id: binary-number-system
  type: soft
builds-toward:
- barrel-shifter-design
- memory-address-decoding
tags:
- multiplexing
- data-selection
- routing
stage: formal-systems
status: draft
---

# Multiplexers and Demultiplexers

## Core Idea
A multiplexer (MUX) selects one of many inputs based on control signals (select lines), while a demultiplexer routes a single input to one of many outputs. An n-to-1 multiplexer needs log₂(n) select lines. These are fundamental for routing data and are used in ALUs, memory addressing, and register selection.
