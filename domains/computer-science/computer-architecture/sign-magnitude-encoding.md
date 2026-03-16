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

## Explainer

You already understand binary numbers — how a sequence of bits represents a value using powers of two. But standard binary only represents non-negative numbers: 0000 through 1111 gives you 0 through 15 in a 4-bit system. To represent negative numbers, we need a convention for encoding sign. **Sign-magnitude** is the most intuitive approach because it mirrors how humans write signed numbers: a sign followed by a magnitude.

In sign-magnitude, the **most significant bit (MSB)** serves as the sign bit: 0 means positive, 1 means negative. The remaining bits represent the magnitude (absolute value) in ordinary binary. For example, in a 4-bit sign-magnitude system, +5 is `0101` (sign=0, magnitude=101=5) and -5 is `1101` (sign=1, magnitude=101=5). The range of an n-bit sign-magnitude number is -(2^(n-1) - 1) to +(2^(n-1) - 1). For 8 bits, that's -127 to +127.

The simplicity of sign-magnitude comes with two serious drawbacks. First, it has **two representations of zero**: `0000` (+0) and `1000` (-0). This wastes one bit pattern and complicates equality comparisons — hardware must treat both patterns as equivalent. Second, and more importantly, **arithmetic is awkward**. To add two sign-magnitude numbers, you cannot simply feed them into a binary adder. Instead, the hardware must first compare the signs: if both signs match, add the magnitudes and keep the sign; if the signs differ, subtract the smaller magnitude from the larger and take the sign of the larger. This comparison-and-branch logic requires significantly more circuitry than a straightforward adder.

Because of these complications, sign-magnitude is rarely used for integer arithmetic in modern processors. Its main historical use is in the mantissa (significand) of IEEE 754 floating-point numbers, where the sign bit is stored separately and magnitude arithmetic is already the norm. For general-purpose signed integers, two's complement has become the universal standard precisely because it avoids both the dual-zero problem and the arithmetic complexity that makes sign-magnitude impractical at the hardware level.
