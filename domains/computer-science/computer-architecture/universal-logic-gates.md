---
id: universal-logic-gates
title: 'Universal Gates: NOR and NAND'
domain: computer-science
course: computer-architecture
prerequisites:
- id: boolean-algebra-and-laws
  type: hard
builds-toward:
- decoders-multiplexers
- sr-flip-flop-design
tags:
- gates
- universal
- nand
- nor
stage: formal-systems
status: draft
---

# Universal Gates: NOR and NAND

## Core Idea
NAND and NOR gates are universal because any boolean function can be constructed using only NAND gates (or only NOR gates). This property makes them essential for minimizing component types in digital circuits.

## How It's Best Learned
Design AND, OR, and NOT using only NAND gates; repeat with NOR. Observe how the same gate type replaces different gate families.

## Common Misconceptions
Not all gates are equally universal—AND and OR alone cannot implement NOT. The order matters when stacking universal gates.
