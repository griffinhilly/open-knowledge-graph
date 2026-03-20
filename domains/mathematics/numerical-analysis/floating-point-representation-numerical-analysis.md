---
id: floating-point-representation-numerical-analysis
title: Floating Point Representation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: machine-epsilon
  type: soft
builds-toward:
- machine-epsilon
- rounding-errors
tags:
- floating-point
- representation
- computer-arithmetic
stage: formal-systems
status: draft
---
# Floating Point Representation

## Core Idea
Floating point numbers are represented in computers using a fixed number of bits: a sign bit, an exponent, and a mantissa (fractional part). The IEEE 754 standard defines how these are encoded and how arithmetic operations are performed. This limited precision representation allows computers to store a wide range of values but introduces systematic errors in computation.

## Explainer

Computers must represent real numbers using a finite string of bits, which immediately poses a problem: there are uncountably many real numbers and only finitely many bit patterns. Floating point is the engineering solution — instead of trying to represent all numbers, it represents a carefully chosen finite set that covers a wide range of magnitudes while maintaining consistent *relative* precision. The key insight is that scientific computation usually cares about significant digits rather than absolute position of the decimal point. A measurement of 6.022 × 10^23 has four significant digits whether expressed as a large integer or not.

**IEEE 754 double precision** (the default in most languages) uses 64 bits: 1 sign bit, 11 exponent bits, and 52 **mantissa** bits. The number stored is (−1)^s × 1.f × 2^(e−1023), where s is the sign, e is the stored exponent, and 1.f is the mantissa with an implicit leading 1 bit (since every normalized binary number starts with 1, this bit is free). The 52 mantissa bits give about 15–16 significant decimal digits of precision. The 11 exponent bits allow a range from roughly 10^−308 to 10^308. This is the same idea as scientific notation in base 2: the exponent controls the scale, the mantissa controls the significant digits.

The critical consequence is that most real numbers cannot be represented exactly. Consider the decimal 0.1: in binary it is a repeating fraction 0.0001100110011..., so it gets truncated. This means that `0.1 + 0.2 ≠ 0.3` in floating point arithmetic — a famous surprise for beginners. The gap between any representable number and the next representable one (relative to the number's magnitude) is bounded by **machine epsilon** ε ≈ 2.22 × 10^−16. Every arithmetic operation introduces a **rounding error** of at most ε/2 relative error. Individually tiny, these errors can accumulate dramatically over many operations — a phenomenon you will study when analyzing numerical algorithms.

Special values complete the system: IEEE 754 reserves patterns for **±infinity** (for overflow, e.g., 1.0/0.0) and **NaN** (Not a Number, for undefined results like 0.0/0.0 or √(−1)). These allow computations to continue and propagate failure information rather than crashing. Recognizing a NaN in your output signals that something went wrong upstream — it is a diagnostic, not a valid result. Understanding how floating point works is prerequisite to understanding why numerical algorithms must be designed carefully: operations that are mathematically equivalent may behave very differently when computed in finite precision.
