---
id: floating-point-representation
title: Floating-Point Representation (IEEE 754)
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: scientific-notation-intro
  type: soft
- id: exponents-intro
  type: soft
builds-toward:
- arithmetic-logic-unit
tags:
- floating-point
- IEEE-754
- real-numbers
- precision
stage: formal-systems
status: draft
---

# Floating-Point Representation (IEEE 754)

## Core Idea
IEEE 754 floating-point represents real numbers in binary scientific notation: a sign bit, a biased exponent, and a significand (mantissa). A 32-bit single-precision float has 1 sign bit, 8 exponent bits, and 23 mantissa bits. The format can represent very large and very small numbers but introduces rounding errors because most real numbers cannot be represented exactly in a finite number of bits. Special values like infinity, negative zero, and NaN (Not a Number) handle edge cases in computation.

## How It's Best Learned
Encode and decode several floating-point values by hand using the IEEE 754 formula. Explore precision loss by computing (1.0 + epsilon == 1.0) in a programming language. Use visualization tools to see the distribution of representable values.

## Common Misconceptions
- Floating-point rounding errors are not bugs in the processor; they are inherent to finite-precision real-number approximation.
- 0.1 cannot be represented exactly in binary floating point, just as 1/3 cannot be represented exactly in decimal.
