---
id: binary-coded-decimal-encoding
title: Binary Coded Decimal (BCD)
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
tags:
- number-systems
- encoding
stage: formal-systems
status: draft
---

# Binary Coded Decimal (BCD)

## Core Idea
BCD represents each decimal digit (0–9) as a separate 4-bit binary code. Used in systems requiring direct decimal interfacing, though less efficient than pure binary for computation.

## Explainer

You already understand the binary number system — how any value can be represented using combinations of 1s and 0s, with each position representing a power of 2. **Binary Coded Decimal** takes a different approach: instead of converting an entire number into binary, it converts each decimal digit separately into its 4-bit binary equivalent. The decimal number 47 in pure binary is 101111 (32 + 8 + 4 + 2 + 1). In BCD, it becomes 0100 0111 — the digit 4 encoded as 0100, and the digit 7 encoded as 0111, stored side by side. Each group of 4 bits represents exactly one decimal digit, never exceeding 1001 (decimal 9).

This means BCD wastes some representational capacity. Four bits can encode 16 values (0000 through 1111), but BCD only uses 10 of them (0000 through 1001). The combinations 1010 through 1111 are invalid in BCD — they don't correspond to any decimal digit. An 8-bit byte in pure binary can represent values 0–255, but an 8-bit BCD representation holds only two decimal digits (0–99). The tradeoff is clear: BCD is less space-efficient than pure binary, using roughly 20% more bits for the same numeric range.

So why does BCD exist? The answer is **decimal-exact representation and display**. Financial systems, calculators, and digital clocks need to display and compute with decimal numbers without rounding errors. Converting between binary and decimal requires division and modulo operations — relatively expensive in hardware. With BCD, each digit maps directly to a display segment or decimal output with no conversion needed. A seven-segment display driver can take a 4-bit BCD group and activate the right segments directly. Financial calculations avoid the problem where binary floating-point cannot exactly represent values like 0.10 (one-tenth has no finite binary expansion), which is why COBOL and banking systems historically relied on BCD arithmetic.

**BCD arithmetic** requires special handling. When you add two BCD digits and the result exceeds 9, you must apply a correction: add 6 (0110) to the result to skip over the six invalid codes and carry into the next digit. For example, 7 + 8 = 15 in decimal. In BCD, 0111 + 1000 = 1111, which is an invalid BCD code. Adding the correction factor 0110 gives 10101 — which splits into 0001 0101, correctly representing 15 in BCD (1 and 5). Many older processors included a dedicated "decimal adjust" instruction (like x86's DAA) specifically for this correction step. Modern systems generally use pure binary arithmetic and convert to decimal only for display, but BCD remains relevant in embedded systems, financial hardware, and anywhere exact decimal behavior is non-negotiable.
