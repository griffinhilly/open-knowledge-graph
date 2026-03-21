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

## Questions

```yaml
- question: "Which correctly represents the decimal number 93 in BCD?"
  type: multiple-choice
  options:
    - "1011101 — the pure binary representation of 93"
    - "1001 0011 — the digits 9 and 3 each encoded separately as 4-bit groups"
    - "0101 1101 — a compact encoding using partial binary conversion"
    - "1111 0011 — using the maximum 4-bit value for the tens digit"
  answer: 1
  explanation: "In BCD, each decimal digit is encoded separately: 9 → 1001, 3 → 0011, giving 1001 0011. Option A is pure binary (93 = 64+16+8+4+1 = 1011101), which treats the entire number as one binary value rather than encoding digit by digit. BCD never encodes the whole number at once — it encodes one digit per 4-bit group. Options C and D include 4-bit patterns above 1001, which are invalid BCD codes."

- question: "When adding 7 + 8 in BCD arithmetic, the raw 4-bit result is 1111 (decimal 15), which is an invalid BCD code. The correct procedure is:"
  type: multiple-choice
  options:
    - "Subtract 6 (0110) from 1111 to get back to a valid BCD digit"
    - "Add 6 (0110) to 1111, producing 10101, which encodes BCD 15 as 0001 0101"
    - "Use the raw result 1111 and flag it as an overflow error"
    - "Divide the result by 10 to extract the carry digit"
  answer: 1
  explanation: "When a BCD addition result exceeds 9 (valid codes are 0000–1001; invalid codes are 1010–1111), add 6 (0110) to skip over the six invalid codes. Here: 0111 + 1000 = 1111. Adding 0110: 1111 + 0110 = 10101, which splits into carry 1 and remainder 0101, giving BCD 0001 0101 — correctly representing 15 as '1' and '5.' The +6 correction works because the 4-bit system has 16 states but BCD uses only 10, leaving a gap of 6 that must be jumped on overflow."

- question: "In BCD encoding, exactly 6 of the 16 possible 4-bit patterns are invalid and never represent a decimal digit."
  type: true-false
  answer: true
  explanation: "Four bits can represent 16 values: 0000 through 1111. BCD uses only 10 of these — 0000 (0) through 1001 (9). The six patterns 1010 (10), 1011 (11), 1100 (12), 1101 (13), 1110 (14), and 1111 (15) are invalid BCD codes. This waste of 6 out of 16 patterns per digit is exactly why BCD requires more bits than pure binary for the same numeric range, and why BCD addition needs the +6 correction step."

- question: "BCD is more storage-efficient than pure binary because it avoids the conversion step between decimal and binary representations."
  type: true-false
  answer: false
  explanation: "BCD is less space-efficient than pure binary, not more. An 8-bit byte in pure binary represents 0–255 (256 values); an 8-bit BCD representation holds only two decimal digits (0–99, or 100 values). BCD requires roughly 20% more bits than pure binary to represent the same numeric range, because each 4-bit group encodes only 10 of its 16 possible values. BCD's advantage is decimal-exact representation and easy display conversion — not storage efficiency."

- question: "Why does BCD exist as an encoding scheme despite being less space-efficient than pure binary? What types of applications justify this tradeoff?"
  type: short-answer
  answer: "BCD exists because some applications require decimal-exact computation and direct decimal display without conversion overhead. Financial systems need to represent values like $0.10 exactly — pure binary floating-point cannot represent 1/10 as a finite binary fraction, causing rounding errors in banking calculations. BCD avoids this entirely. Display hardware (seven-segment displays, digital clocks, calculators) can drive decimal outputs directly from BCD groups without binary-to-decimal conversion, simplifying hardware design. Embedded and real-time systems also benefit from the direct decimal mapping."
  explanation: "The classic example: 0.10 + 0.20 = 0.30000000000000004 in IEEE 754 floating-point, but always exactly 0.30 in BCD. This is why COBOL and many financial processors historically use BCD or decimal floating-point. The tradeoff — more bits in exchange for decimal exactness and display simplicity — is justified wherever decimal accuracy is non-negotiable."
```

## Explainer

You already understand the binary number system — how any value can be represented using combinations of 1s and 0s, with each position representing a power of 2. **Binary Coded Decimal** takes a different approach: instead of converting an entire number into binary, it converts each decimal digit separately into its 4-bit binary equivalent. The decimal number 47 in pure binary is 101111 (32 + 8 + 4 + 2 + 1). In BCD, it becomes 0100 0111 — the digit 4 encoded as 0100, and the digit 7 encoded as 0111, stored side by side. Each group of 4 bits represents exactly one decimal digit, never exceeding 1001 (decimal 9).

This means BCD wastes some representational capacity. Four bits can encode 16 values (0000 through 1111), but BCD only uses 10 of them (0000 through 1001). The combinations 1010 through 1111 are invalid in BCD — they don't correspond to any decimal digit. An 8-bit byte in pure binary can represent values 0–255, but an 8-bit BCD representation holds only two decimal digits (0–99). The tradeoff is clear: BCD is less space-efficient than pure binary, using roughly 20% more bits for the same numeric range.

So why does BCD exist? The answer is **decimal-exact representation and display**. Financial systems, calculators, and digital clocks need to display and compute with decimal numbers without rounding errors. Converting between binary and decimal requires division and modulo operations — relatively expensive in hardware. With BCD, each digit maps directly to a display segment or decimal output with no conversion needed. A seven-segment display driver can take a 4-bit BCD group and activate the right segments directly. Financial calculations avoid the problem where binary floating-point cannot exactly represent values like 0.10 (one-tenth has no finite binary expansion), which is why COBOL and banking systems historically relied on BCD arithmetic.

**BCD arithmetic** requires special handling. When you add two BCD digits and the result exceeds 9, you must apply a correction: add 6 (0110) to the result to skip over the six invalid codes and carry into the next digit. For example, 7 + 8 = 15 in decimal. In BCD, 0111 + 1000 = 1111, which is an invalid BCD code. Adding the correction factor 0110 gives 10101 — which splits into 0001 0101, correctly representing 15 in BCD (1 and 5). Many older processors included a dedicated "decimal adjust" instruction (like x86's DAA) specifically for this correction step. Modern systems generally use pure binary arithmetic and convert to decimal only for display, but BCD remains relevant in embedded systems, financial hardware, and anywhere exact decimal behavior is non-negotiable.
