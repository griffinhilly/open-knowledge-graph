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

## Questions

```yaml
- question: "A programmer writes `if (0.1 + 0.2 == 0.3)` in a language using IEEE 754, and the condition evaluates to false. The most accurate explanation is:"
  type: multiple-choice
  options:
    - "The processor has a bug in its floating-point arithmetic unit that affects certain decimal fractions"
    - "0.1, 0.2, and 0.3 cannot be represented exactly in binary, so 0.1 + 0.2 produces a slightly different approximation than the stored value of 0.3"
    - "Floating-point addition is not commutative, so the result depends on operand order"
    - "The equality operator is inherently unreliable for all numeric comparisons in IEEE 754"
  answer: 1
  explanation: "This is the fundamental consequence of finite-precision binary representation. 0.1 in binary is a repeating fraction (like 1/3 in decimal), so the stored value is an approximation. Adding the approximations of 0.1 and 0.2 produces a slightly different value than the stored approximation of 0.3. The error is inherent to the representation — not a hardware bug. Floating-point addition is commutative (option C is false). The correct practice is to check approximate equality: `abs(a - b) < epsilon`."

- question: "In IEEE 754 single-precision format, the exponent field stores the value 130. What actual exponent does this represent?"
  type: multiple-choice
  options:
    - "130 — the stored value is used directly as the exponent"
    - "3 — the actual exponent is the stored value minus the bias of 127"
    - "2 — the stored exponent uses two's complement, so 130 encodes 2"
    - "257 — the bias is added to the stored value to get the actual exponent"
  answer: 1
  explanation: "IEEE 754 uses biased (excess-127) exponent encoding: actual exponent = stored value − 127. A stored exponent of 130 represents actual exponent 130 − 127 = 3, meaning the number is ±1.mantissa × 2³. The bias avoids needing two's complement for the exponent field and makes floating-point magnitude comparison possible using integer comparison hardware. Option D inverts the relationship: you subtract the bias from the stored value, not add it."

- question: "In IEEE 754 single-precision, the leading 1 of the significand is implicit and not stored, giving 24 bits of effective precision from only 23 stored mantissa bits."
  type: true-false
  answer: true
  explanation: "In binary scientific notation, every normalized nonzero number has the form 1.xxx...x × 2^e — the leading digit is always 1 because 1 is the only nonzero binary digit. Since this leading 1 is guaranteed to be present in any normalized number, it need not be stored. The 23 mantissa bits store only the fractional part. When the number is reconstructed, hardware implicitly prepends the 1, giving 24 bits of significand precision. This implicit leading bit is a free precision bonus inherent to the binary format."

- question: "Floating-point rounding errors indicate a poorly designed processor and can be eliminated by using more careful arithmetic circuit design."
  type: true-false
  answer: false
  explanation: "Floating-point rounding errors are a mathematical inevitability of representing an infinite set of real numbers using a finite number of bits — not hardware bugs. Most real numbers, including simple decimals like 0.1, require infinitely many bits to represent exactly in binary. Any finite representation must round. Better hardware can reduce error (double precision uses 64 bits instead of 32), but cannot eliminate it without infinite storage. IEEE 754 specifies correct rounding rules so every operation produces the best possible approximation; the errors come from the limits of finite representation, not imprecision in the circuits."

- question: "Explain why adding a very small floating-point number to a very large one might produce no change at all, using the concept of how representable values are spaced."
  type: short-answer
  answer: "Floating-point values are not evenly spaced across the number line — they are densely packed near zero and increasingly sparse at larger magnitudes. Between consecutive powers of 2, there are exactly 2²³ representable values (single precision), so the gap between adjacent representable numbers grows as magnitude increases. If the small number is smaller than the gap between the large number and its nearest representable neighbor, the result rounds back to the large number unchanged. For example, if the gap near 1.0 is about 1.2 × 10⁻⁷, adding 10⁻⁸ to 1.0 has no effect because 10⁻⁸ falls below the resolution of the representation at that magnitude."
  explanation: "This phenomenon — sometimes called absorption — has real consequences in numerical algorithms. A running sum of many small values accumulated into a large total can lose precision as each addition falls below the representable gap. Algorithms like Kahan compensated summation address this by tracking the accumulated rounding error in a separate variable. Understanding representable value spacing is essential for diagnosing and preventing precision loss in numerical computing."
```

## Explainer

You already know how two's complement represents signed integers by fixing a set number of bits and interpreting them with positional place values. But integers cannot represent fractions or very large numbers like 6.022 × 10²³. **Floating-point representation** extends the idea of binary encoding to approximate real numbers, using the same principle as scientific notation: separate a number into a **significand** (the meaningful digits) and an **exponent** (the scale). In decimal scientific notation, 0.0042 becomes 4.2 × 10⁻³. IEEE 754 does the same thing in binary: a number is stored as ±1.mantissa × 2^exponent.

A 32-bit single-precision float divides its bits into three fields: 1 **sign bit** (0 for positive, 1 for negative), 8 **exponent bits**, and 23 **mantissa bits**. The exponent uses a **biased** encoding — the stored value is the actual exponent plus 127, so a stored exponent of 130 means an actual exponent of 3. This avoids the need for two's complement in the exponent field and makes comparison simpler. The mantissa stores only the fractional part of the significand because the leading 1 is implicit — since any nonzero binary number in scientific notation starts with 1 (there is only one nonzero digit in binary), there is no need to store it. This trick gives you 24 bits of precision from 23 stored bits.

The consequence of finite precision is **rounding error**. The representable floating-point values are not evenly distributed across the number line — they are densely packed near zero and increasingly sparse as magnitude grows. Between 1.0 and 2.0, there are 2²³ (about 8 million) representable values. Between 2.0 and 4.0, there are the same 2²³ values spread over twice the range, so the gap between consecutive representable numbers doubles. This means that adding a tiny number to a large number can produce no change at all: if the small number falls below the gap size at the large number's magnitude, it gets rounded away. The expression `1.0 + 1e-8 == 1.0` evaluates to true in single precision, not because of a bug, but because 10⁻⁸ is smaller than the spacing between representable values near 1.0.

IEEE 754 also defines **special values** to handle exceptional cases gracefully. Positive and negative **infinity** result from operations like dividing a positive number by zero. **NaN** (Not a Number) represents undefined results like 0/0 or √(−1) and has the unique property that NaN ≠ NaN. **Negative zero** exists because the sign bit is independent of the magnitude — it compares equal to positive zero but preserves sign information for certain mathematical operations. These special values ensure that floating-point arithmetic never traps or halts unexpectedly; every operation produces a defined result, even if that result is "this computation is undefined."
