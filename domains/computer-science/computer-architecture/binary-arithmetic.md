---
id: binary-arithmetic
title: Binary Arithmetic
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
builds-toward:
- twos-complement
- adder-circuits
- arithmetic-logic-unit
tags:
- binary
- arithmetic
- overflow
- addition
stage: formal-systems
status: draft
---

# Binary Arithmetic

## Core Idea
Binary arithmetic follows the same rules as decimal arithmetic but with carries occurring at 2 rather than 10. Adding two 1-bits produces a sum of 0 and a carry of 1 into the next position. Overflow occurs when the result of an operation exceeds the number of bits available to represent it. Binary subtraction can be performed using addition with negated operands, which motivates the two's complement representation used in hardware.

## How It's Best Learned
Work through 4-bit and 8-bit addition problems by hand, tracking carries carefully. Intentionally create overflow scenarios to understand when results wrap around. Compare binary addition to decimal to reinforce structural similarity.

## Common Misconceptions
- Overflow is not an error in hardware; the carry-out bit is simply discarded unless the programmer checks for it.
- Binary multiplication is not more complex in principle — it uses the same shift-and-add approach as long multiplication in decimal.
