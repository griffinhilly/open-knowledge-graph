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

## Questions

```yaml
- question: "A programmer writes `if (0.1 + 0.2 == 0.3)` in a language using IEEE 754 double precision. What will happen, and why?"
  type: multiple-choice
  options:
    - "The condition evaluates to true — 0.1 + 0.2 equals 0.3 exactly in double precision"
    - "The condition evaluates to false — neither 0.1 nor 0.2 has an exact binary representation, so their sum differs slightly from the stored value of 0.3"
    - "The condition evaluates to true only on CPUs with a hardware floating-point unit"
    - "The expression raises an overflow exception since 0.3 cannot be represented"
  answer: 1
  explanation: "The decimal 0.1 is a repeating fraction in binary (0.000110011...) and cannot be stored exactly. The error introduced when storing 0.1 and the error introduced when storing 0.2 do not perfectly cancel, so their sum differs from the separately-stored representation of 0.3 — typically by about 5.5 × 10⁻¹⁷. This is not a bug in the computer; it is a fundamental consequence of representing real numbers with finite binary precision. The correct practice is to compare floating-point numbers with a tolerance: `|a − b| < ε`."

- question: "Why does IEEE 754 floating point maintain approximately the same number of significant decimal digits across its entire representable range — whether storing a number near 10⁻³⁰⁰ or near 10³⁰⁰?"
  type: multiple-choice
  options:
    - "Because the hardware allocates more mantissa bits to smaller numbers to compensate for their tiny magnitude"
    - "Because relative precision — bounded by machine epsilon — is constant regardless of magnitude"
    - "Because the exponent bits grow larger as the number grows, maintaining absolute error"
    - "Because the mantissa is stored in decimal form internally, independent of the binary exponent"
  answer: 1
  explanation: "Floating point is designed for relative, not absolute, precision. The mantissa stores the significant digits and the exponent scales the magnitude. Whether the number is 6.022 × 10²³ or 6.022 × 10⁻⁵, the same 52 mantissa bits represent the same ~15–16 significant decimal digits. Machine epsilon ε ≈ 2.22 × 10⁻¹⁶ bounds the relative error of any single operation: the absolute error scales with the magnitude of the number, but the relative error is always at most ε/2."

- question: "The decimal number 0.1 cannot be represented exactly in IEEE 754 binary floating point because it requires an infinitely repeating binary fraction."
  type: true-false
  answer: true
  explanation: "In binary, 0.1 = 0.000110011001100110011... — a repeating pattern analogous to 1/3 = 0.333... in decimal. Since the 52 mantissa bits must truncate this infinite sequence, the stored value differs from the true 0.1 by approximately 5.5 × 10⁻¹⁸. This is unavoidable in binary floating point and applies to many 'simple' decimals: 0.2, 0.3, 0.6, 0.7 all have repeating binary representations."

- question: "Floating-point arithmetic errors are unpredictable and random, so numerical analysts cannot systematically bound or control their effect on a computation."
  type: true-false
  answer: false
  explanation: "Floating-point errors are systematic and bounded, not random. Each arithmetic operation introduces a relative error of at most machine epsilon ε/2 ≈ 1.11 × 10⁻¹⁶. Numerical analysis provides rigorous frameworks — condition number analysis, backward error analysis, interval arithmetic — for bounding how errors accumulate across a computation. Algorithms can be designed (or avoided) based on their error amplification behavior. The challenge is not unpredictability but the potential for systematic amplification in ill-conditioned computations."

- question: "Explain why floating point uses relative precision rather than absolute precision, and what practical consequence this has for comparing floating-point numbers for equality."
  type: short-answer
  answer: "Floating point maintains relative precision because scientific computation usually cares about significant digits, not absolute position. A measurement of 6.022 × 10²³ has the same meaningful precision as 6.022 × 10⁻⁵ — the scale differs but the information content is similar. Absolute precision (a fixed number of decimal places) would waste bits for large numbers and provide useless precision for tiny ones. The practical consequence for equality comparison is that you cannot use ==: since most decimals cannot be represented exactly, two values that should be 'equal' often differ by a tiny rounding error. The correct test is |a − b| < δ for some tolerance δ appropriate to the problem."
  explanation: "The relative-precision design is what makes floating point powerful for scientific computing but dangerous for financial calculations (where absolute precision at a fixed decimal place is required). Equality comparison failures are the most common practical pitfall encountered by programmers new to floating point, and they arise directly from this fundamental design choice."
```

## Explainer

Computers must represent real numbers using a finite string of bits, which immediately poses a problem: there are uncountably many real numbers and only finitely many bit patterns. Floating point is the engineering solution — instead of trying to represent all numbers, it represents a carefully chosen finite set that covers a wide range of magnitudes while maintaining consistent *relative* precision. The key insight is that scientific computation usually cares about significant digits rather than absolute position of the decimal point. A measurement of 6.022 × 10^23 has four significant digits whether expressed as a large integer or not.

**IEEE 754 double precision** (the default in most languages) uses 64 bits: 1 sign bit, 11 exponent bits, and 52 **mantissa** bits. The number stored is (−1)^s × 1.f × 2^(e−1023), where s is the sign, e is the stored exponent, and 1.f is the mantissa with an implicit leading 1 bit (since every normalized binary number starts with 1, this bit is free). The 52 mantissa bits give about 15–16 significant decimal digits of precision. The 11 exponent bits allow a range from roughly 10^−308 to 10^308. This is the same idea as scientific notation in base 2: the exponent controls the scale, the mantissa controls the significant digits.

The critical consequence is that most real numbers cannot be represented exactly. Consider the decimal 0.1: in binary it is a repeating fraction 0.0001100110011..., so it gets truncated. This means that `0.1 + 0.2 ≠ 0.3` in floating point arithmetic — a famous surprise for beginners. The gap between any representable number and the next representable one (relative to the number's magnitude) is bounded by **machine epsilon** ε ≈ 2.22 × 10^−16. Every arithmetic operation introduces a **rounding error** of at most ε/2 relative error. Individually tiny, these errors can accumulate dramatically over many operations — a phenomenon you will study when analyzing numerical algorithms.

Special values complete the system: IEEE 754 reserves patterns for **±infinity** (for overflow, e.g., 1.0/0.0) and **NaN** (Not a Number, for undefined results like 0.0/0.0 or √(−1)). These allow computations to continue and propagate failure information rather than crashing. Recognizing a NaN in your output signals that something went wrong upstream — it is a diagnostic, not a valid result. Understanding how floating point works is prerequisite to understanding why numerical algorithms must be designed carefully: operations that are mathematically equivalent may behave very differently when computed in finite precision.
