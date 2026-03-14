---
id: twos-complement-signed-integers
title: Two's Complement and Signed Integer Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: binary-arithmetic
  type: hard
builds-toward:
- arithmetic-overflow-detection
- multiply-and-divide-circuits
tags:
- number-representation
- signed-arithmetic
- integer-encoding
stage: formal-systems
status: draft
---

# Two's Complement and Signed Integer Representation

## Core Idea
Two's complement is the standard encoding for negative integers in digital systems, where the most significant bit is the sign bit. To negate a number, invert all bits and add one. This representation allows addition and subtraction to use the same hardware circuits, and has a unique zero (unlike sign-magnitude).

## How It's Best Learned
Start with small examples (4-bit numbers): represent +5 and -5, verify addition works, observe how overflow is detected. Practice conversions and observe how subtraction becomes addition of a negated operand.

## Common Misconceptions
- Thinking two's complement is just 'sign bit + magnitude'
- Forgetting that the range is asymmetric: -2^(n-1) to 2^(n-1)-1
- Confusing one's complement (invert all bits) with two's complement
