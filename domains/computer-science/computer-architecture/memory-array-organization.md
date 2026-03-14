---
id: memory-array-organization
title: Memory Array Organization and Access
domain: computer-science
course: computer-architecture
prerequisites:
- id: decoders-multiplexers
  type: hard
- id: d-flip-flop-design
  type: soft
builds-toward:
- memory-address-decoding
- cache-design-principles
tags:
- memory
- arrays
- addressing
- organization
stage: formal-systems
status: draft
---

# Memory Array Organization and Access

## Core Idea
Memory arrays arrange storage cells (flip-flops or capacitors) in a 2D grid, using row and column decoders to select individual cells. Address lines are split between row and column to reduce decoder complexity.

## How It's Best Learned
Design a 4×4 bit memory array with row/column decoders; trace address-to-cell selection.

## Common Misconceptions
Both row and column decoders must be active to select one cell. Larger arrays use hierarchical decoding, not monolithic decoders.
