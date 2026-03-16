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
- id: binary-arithmetic
  type: soft
builds-toward:
- arithmetic-logic-unit
tags:
- floating-point
- IEEE-754
- real-numbers
- precision
stage: formal-systems
status: validated
---

# Floating-Point Representation (IEEE 754)

## Core Idea
IEEE 754 floating-point represents real numbers in binary scientific notation: a sign bit, a biased exponent, and a significand (mantissa). A 32-bit single-precision float has 1 sign bit, 8 exponent bits, and 23 mantissa bits. The format can represent very large and very small numbers but introduces rounding errors because most real numbers cannot be represented exactly in a finite number of bits. Special values like infinity, negative zero, and NaN (Not a Number) handle edge cases in computation.

## How It's Best Learned
Encode and decode several floating-point values by hand using the IEEE 754 formula. Explore precision loss by computing (1.0 + epsilon == 1.0) in a programming language. Use visualization tools to see the distribution of representable values.

## Common Misconceptions
- Floating-point rounding errors are not bugs in the processor; they are inherent to finite-precision real-number approximation.
- 0.1 cannot be represented exactly in binary floating point, just as 1/3 cannot be represented exactly in decimal.

## Explainer

You already know how two's complement represents signed integers by fixing a set number of bits and interpreting them with positional place values. But integers cannot represent fractions or very large numbers like 6.022 × 10²³. **Floating-point representation** extends the idea of binary encoding to approximate real numbers, using the same principle as scientific notation: separate a number into a **significand** (the meaningful digits) and an **exponent** (the scale). In decimal scientific notation, 0.0042 becomes 4.2 × 10⁻³. IEEE 754 does the same thing in binary: a number is stored as ±1.mantissa × 2^exponent.

A 32-bit single-precision float divides its bits into three fields: 1 **sign bit** (0 for positive, 1 for negative), 8 **exponent bits**, and 23 **mantissa bits**. The exponent uses a **biased** encoding — the stored value is the actual exponent plus 127, so a stored exponent of 130 means an actual exponent of 3. This avoids the need for two's complement in the exponent field and makes comparison simpler. The mantissa stores only the fractional part of the significand because the leading 1 is implicit — since any nonzero binary number in scientific notation starts with 1 (there is only one nonzero digit in binary), there is no need to store it. This trick gives you 24 bits of precision from 23 stored bits.

The consequence of finite precision is **rounding error**. The representable floating-point values are not evenly distributed across the number line — they are densely packed near zero and increasingly sparse as magnitude grows. Between 1.0 and 2.0, there are 2²³ (about 8 million) representable values. Between 2.0 and 4.0, there are the same 2²³ values spread over twice the range, so the gap between consecutive representable numbers doubles. This means that adding a tiny number to a large number can produce no change at all: if the small number falls below the gap size at the large number's magnitude, it gets rounded away. The expression `1.0 + 1e-8 == 1.0` evaluates to true in single precision, not because of a bug, but because 10⁻⁸ is smaller than the spacing between representable values near 1.0.

IEEE 754 also defines **special values** to handle exceptional cases gracefully. Positive and negative **infinity** result from operations like dividing a positive number by zero. **NaN** (Not a Number) represents undefined results like 0/0 or √(−1) and has the unique property that NaN ≠ NaN. **Negative zero** exists because the sign bit is independent of the magnitude — it compares equal to positive zero but preserves sign information for certain mathematical operations. These special values ensure that floating-point arithmetic never traps or halts unexpectedly; every operation produces a defined result, even if that result is "this computation is undefined."
