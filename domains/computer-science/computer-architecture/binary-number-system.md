---
id: binary-number-system
title: Binary Number System
domain: computer-science
course: computer-architecture
prerequisites:
- id: place-value-whole-numbers
  type: soft
- id: number-base-conversion-operations
  type: soft
builds-toward:
- hexadecimal-number-system
- binary-arithmetic
- twos-complement
tags:
- binary
- number-systems
- representation
stage: abstract-reasoning
status: validated
---

# Binary Number System

## Core Idea
The binary number system uses only two digits (0 and 1) to represent all numbers, using powers of 2 as place values. Each digit position corresponds to 2^n for some n ≥ 0, so the binary number 1011 equals 1×8 + 0×4 + 1×2 + 1×1 = 11 in decimal. Computers use binary because electronic circuits naturally represent two states: on (1) and off (0). Converting between binary and decimal is a core skill for understanding how data is stored and processed.

## How It's Best Learned
Practice converting between binary and decimal in both directions. Start with small numbers (0–15) to build intuition about powers of 2, then extend to larger values. Use the doubling/halving method for quick conversions.

## Common Misconceptions
- Binary numbers are not just 'computer code' — they are a complete positional number system with the same arithmetic properties as decimal.
- Leading zeros do not change a binary number's value (0101 = 101) but are often written for alignment to fixed bit-widths.

## Questions

```yaml
- question: "What is the decimal value of the binary number 1101?"
  type: multiple-choice
  options: ["10", "11", "13", "14"]
  answer: 2
  explanation: "Each bit position is a power of 2: 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = 13. A common error is reading the bits as if they were decimal digits (1101 = 1,101 in decimal), which confuses binary representation with its decimal meaning."

- question: "Leading zeros change the value of a binary number (e.g., 0101 has a different value than 101)."
  type: true-false
  answer: false
  explanation: "Just as 007 equals 7 in decimal, 0101 equals 101 in binary — both represent the value 5. Leading zeros are only written for practical reasons like aligning numbers to a fixed bit-width (e.g., writing 8-bit values always as 8 digits)."

- question: "Why do computers use binary rather than decimal to represent all data?"
  type: short-answer
  answer: "Electronic circuits have two stable physical states — high voltage and low voltage (or on and off) — which map directly to 1 and 0. Reliably distinguishing ten voltage levels for decimal would be far more error-prone and expensive to engineer."
  explanation: "Binary is not just a convention but a physical match to how transistors work. A transistor is either conducting or not — two states. Encoding more states per circuit element would require finer voltage discrimination, making hardware more complex, slower, and less reliable."
```

## Explainer

If you have studied place value in decimal, you already understand the core idea of binary — the systems work identically, just with a different base. In decimal (base 10), each position is worth ten times the one to its right: the number 253 means 2×100 + 5×10 + 3×1. Binary (base 2) works the same way, but each position is worth *two* times the one to its right: the positions represent 1, 2, 4, 8, 16, 32, and so on — successive powers of 2.

To convert binary to decimal, multiply each bit by its place value and sum the results. The binary number 1011 means 1×8 + 0×4 + 1×2 + 1×1 = 11. To convert decimal to binary, repeatedly divide by 2 and record the remainders from bottom to top: 11 ÷ 2 = 5 R1, 5 ÷ 2 = 2 R1, 2 ÷ 2 = 1 R0, 1 ÷ 2 = 0 R1 — reading remainders upward gives 1011. Both directions are worth practicing until they feel mechanical.

Computers use binary because of physics, not convention. A transistor — the fundamental building block of all modern processors — is a switch that is either open or closed, conducting or not. That's two states, which map naturally to 0 and 1. Every piece of data your computer handles — integers, text, images, programs — is ultimately stored and processed as sequences of these bits. Understanding binary lets you reason about what's actually happening at the hardware level.

One thing that trips up beginners: binary numbers follow all the same arithmetic rules as decimal. You can add, subtract, multiply, and divide in binary just like in decimal — carrying and borrowing work the same way, just with 2 as the threshold instead of 10. For example, 1 + 1 in binary equals 10 (zero with a carry), exactly as 9 + 1 equals 10 in decimal. This isn't a new kind of math; it's the same math in a new base.
