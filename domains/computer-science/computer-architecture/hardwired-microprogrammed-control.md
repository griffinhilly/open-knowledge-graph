---
id: hardwired-microprogrammed-control
title: Hardwired vs. Microprogrammed Control
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-control-path-design
  type: hard
builds-toward:
- instruction-pipeline-organization
- superscalar-and-vliw-design
tags:
- control
- hardwired
- microprogrammed
- microcode
stage: formal-systems
status: draft
---

# Hardwired vs. Microprogrammed Control

## Core Idea
Hardwired control uses combinational logic and state machines to generate signals directly; microprogrammed control stores sequences of control words in a ROM and executes them sequentially. Hardwired is fast but inflexible; microprogrammed is slower but easier to modify.

## How It's Best Learned
Design a simple 4-instruction hardwired controller; then sketch how the same logic would be encoded as microcode.

## Common Misconceptions
Microcode is not the same as machine code—it is internal CPU control logic. Both approaches can execute the same instruction set.
