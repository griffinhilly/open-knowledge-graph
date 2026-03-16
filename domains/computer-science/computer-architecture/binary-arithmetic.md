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
status: validated
---

# Binary Arithmetic

## Core Idea
Binary arithmetic follows the same rules as decimal arithmetic but with carries occurring at 2 rather than 10. Adding two 1-bits produces a sum of 0 and a carry of 1 into the next position. Overflow occurs when the result of an operation exceeds the number of bits available to represent it. Binary subtraction can be performed using addition with negated operands, which motivates the two's complement representation used in hardware.

## How It's Best Learned
Work through 4-bit and 8-bit addition problems by hand, tracking carries carefully. Intentionally create overflow scenarios to understand when results wrap around. Compare binary addition to decimal to reinforce structural similarity.

## Common Misconceptions
- Overflow is not an error in hardware; the carry-out bit is simply discarded unless the programmer checks for it.
- Binary multiplication is not more complex in principle — it uses the same shift-and-add approach as long multiplication in decimal.

## Explainer

If you can add in decimal, you can add in binary — the rules are structurally identical, just simpler. In decimal, each digit ranges from 0 to 9, and you carry to the next column when a sum reaches 10. In binary, each digit (called a **bit**) is either 0 or 1, and you carry when a sum reaches 2. The complete addition table for one bit position has only four entries: 0+0=0, 0+1=1, 1+0=1, and 1+1=10 (that is, 0 with a carry of 1). This simplicity is exactly why computers use binary — the addition rules map directly onto simple logic gates.

To add multi-bit numbers, you work column by column from right to left, just as in decimal long addition. Consider adding 0110 (6) and 0011 (3) in four bits. The rightmost column: 0+1=1, no carry. Next: 1+1=10, write 0 and carry 1. Next: 1+0 plus the carry 1 = 10, write 0 and carry 1. Leftmost: 0+0 plus the carry 1 = 1. Result: 1001 (9). The **carry chain** — the sequence of carries rippling from right to left — is the critical path in binary addition, and it directly determines how fast hardware adders can operate.

**Overflow** occurs when the result of an arithmetic operation cannot be represented in the available number of bits. In unsigned 4-bit arithmetic, the largest representable value is 1111 (15). Adding 1000 (8) and 1001 (9) gives 10001 (17), but only four bits are stored, so the result wraps to 0001 (1) and the carry-out is lost. The hardware does not raise an error — it simply discards the extra bit. Detecting overflow is the programmer's responsibility, typically by checking a carry flag or an overflow flag set by the processor.

Binary subtraction works by the same columnar method, borrowing instead of carrying. But hardware designers prefer to avoid building separate subtraction circuits. Instead, subtraction is performed as addition with a negated operand: to compute A - B, you negate B and add. This insight motivates **two's complement** representation, which you will study next. In two's complement, negation is a simple bit manipulation (invert all bits and add 1), so the same adder circuit handles both addition and subtraction — an elegant unification that keeps hardware simple and fast.
