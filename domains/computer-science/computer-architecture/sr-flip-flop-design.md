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
