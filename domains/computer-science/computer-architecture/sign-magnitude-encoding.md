---
id: sign-magnitude-encoding
title: Sign-Magnitude Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
tags:
- number-representation
- signed-integers
stage: formal-systems
status: draft
---

# Sign-Magnitude Representation

## Core Idea
Sign-magnitude uses the most significant bit for sign (0=positive, 1=negative) and remaining bits for magnitude. Intuitive but cumbersome for arithmetic because operations depend on comparing signs.

## Questions

```yaml
- question: "A hardware engineer wants to add two 8-bit sign-magnitude numbers, +35 (00100011) and -35 (10100011). What must the hardware do before it can complete this addition?"
  type: multiple-choice
  options:
    - "XOR the sign bits and add the magnitude bits directly in a standard binary adder"
    - "Compare the sign bits; since they differ, subtract the smaller magnitude from the larger and assign the sign of the larger"
    - "Invert all bits of the negative number and add 1, then add the result to the positive number"
    - "Convert both numbers to positive, add them, then set the sign bit of the result based on which input had the larger absolute value"
  answer: 1
  explanation: "Sign-magnitude arithmetic cannot simply feed numbers into a standard binary adder. When signs differ, the hardware must compare them, determine which magnitude is larger, subtract the smaller from the larger, and assign the sign of the larger-magnitude operand — a multi-step conditional operation. Option C describes two's complement negation (not sign-magnitude). Option D is close but incomplete — when adding +35 and -35, magnitudes are equal and the result is zero regardless. Option B correctly captures the comparison-and-branch logic that makes sign-magnitude hardware-unfriendly."

- question: "In an 8-bit sign-magnitude system, how many distinct values can be represented?"
  type: multiple-choice
  options:
    - "256, because 8 bits give 2^8 possible bit patterns"
    - "255, because one bit pattern (+0) duplicates another (-0) and both represent the same value"
    - "254, because both +0 and -0 must be excluded from the useful range"
    - "128, because the sign bit halves the available magnitude"
  answer: 1
  explanation: "An 8-bit system has 2^8 = 256 bit patterns, but sign-magnitude wastes one on a duplicate representation of zero: 00000000 (+0) and 10000000 (-0) represent the same value. This leaves 255 distinct values (-127 through -1, zero, +1 through +127). By contrast, two's complement also has 256 patterns but represents 256 distinct values — it has only one zero and uses the 'extra' pattern for -128. The dual-zero problem is one of the key reasons sign-magnitude is impractical."

- question: "In sign-magnitude representation, the most significant bit encodes the sign of the number, and the remaining bits encode the absolute value in standard binary."
  type: true-false
  answer: true
  explanation: "This is the defining property of sign-magnitude: the MSB is 0 for positive and 1 for negative, while the remaining bits represent the magnitude exactly as they would in unsigned binary. So +5 is 00000101 and -5 is 10000101 — the magnitude bits are identical; only the sign bit differs. This intuitive structure is what makes sign-magnitude easy to understand but difficult for arithmetic hardware."

- question: "Because sign-magnitude uses a dedicated sign bit, negating a sign-magnitude number requires a multi-step arithmetic operation similar to two's complement negation."
  type: true-false
  answer: false
  explanation: "Negation in sign-magnitude is trivially simple: just flip the MSB. Changing 00000101 (+5) to 10000101 (-5) requires only a single bit inversion. This is actually easier than two's complement negation, which requires inverting all bits and adding 1. The difficulty with sign-magnitude lies not in negation but in addition and subtraction, which require sign comparison before the operation can proceed."

- question: "Why was sign-magnitude largely abandoned for representing signed integers in modern processors, despite being the most intuitive encoding scheme?"
  type: short-answer
  answer: "Two problems make sign-magnitude impractical: (1) it has two representations of zero (+0 and -0), complicating equality comparisons in hardware; (2) addition and subtraction require comparing signs first, then either adding or subtracting based on the result — a conditional operation requiring significantly more circuitry than a simple binary adder. Two's complement eliminates both problems: it has one zero, and unsigned binary adder hardware works correctly for signed arithmetic without modification."
  explanation: "The elegance of two's complement is that it folds sign handling into the binary arithmetic system itself rather than making it a separate operation. A single adder works for both signed and unsigned two's complement arithmetic. This hardware simplicity — not any advantage in range or conceptual clarity — is the decisive reason two's complement became universal."
```

## Explainer

You already understand binary numbers — how a sequence of bits represents a value using powers of two. But standard binary only represents non-negative numbers: 0000 through 1111 gives you 0 through 15 in a 4-bit system. To represent negative numbers, we need a convention for encoding sign. **Sign-magnitude** is the most intuitive approach because it mirrors how humans write signed numbers: a sign followed by a magnitude.

In sign-magnitude, the **most significant bit (MSB)** serves as the sign bit: 0 means positive, 1 means negative. The remaining bits represent the magnitude (absolute value) in ordinary binary. For example, in a 4-bit sign-magnitude system, +5 is `0101` (sign=0, magnitude=101=5) and -5 is `1101` (sign=1, magnitude=101=5). The range of an n-bit sign-magnitude number is -(2^(n-1) - 1) to +(2^(n-1) - 1). For 8 bits, that's -127 to +127.

The simplicity of sign-magnitude comes with two serious drawbacks. First, it has **two representations of zero**: `0000` (+0) and `1000` (-0). This wastes one bit pattern and complicates equality comparisons — hardware must treat both patterns as equivalent. Second, and more importantly, **arithmetic is awkward**. To add two sign-magnitude numbers, you cannot simply feed them into a binary adder. Instead, the hardware must first compare the signs: if both signs match, add the magnitudes and keep the sign; if the signs differ, subtract the smaller magnitude from the larger and take the sign of the larger. This comparison-and-branch logic requires significantly more circuitry than a straightforward adder.

Because of these complications, sign-magnitude is rarely used for integer arithmetic in modern processors. Its main historical use is in the mantissa (significand) of IEEE 754 floating-point numbers, where the sign bit is stored separately and magnitude arithmetic is already the norm. For general-purpose signed integers, two's complement has become the universal standard precisely because it avoids both the dual-zero problem and the arithmetic complexity that makes sign-magnitude impractical at the hardware level.
