---
id: full-adder-and-carry-logic
title: Full Adder and Carry Propagation
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-logic-implementation
  type: hard
- id: adder-circuits
  type: soft
builds-toward:
- carry-lookahead-adder-design
- arithmetic-logic-unit-design-details
tags:
- arithmetic
- adder
- carry-propagation
stage: formal-systems
status: draft
---

# Full Adder and Carry Propagation

## Core Idea
A full adder adds three bits (two operand bits plus carry-in) and produces a sum and carry-out. Cascading full adders creates a ripple-carry adder that adds multi-bit numbers, but the carry propagation delay grows linearly with bit width, creating a performance bottleneck in high-speed arithmetic.
