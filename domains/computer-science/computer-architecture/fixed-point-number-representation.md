---
id: fixed-point-number-representation
title: Fixed-Point Number Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: binary-arithmetic
  type: soft
builds-toward:
- floating-point-representation
- arithmetic-logic-units-design
tags:
- representation
- numbers
- fixed-point
stage: formal-systems
status: draft
---

# Fixed-Point Number Representation

## Core Idea
Fixed-point representation stores numbers with a fixed number of digits before and after the decimal point, encoded as integers scaled by a power of 2. This approach trades range for precision and is simpler to implement in hardware than floating-point arithmetic.

## How It's Best Learned
Start with decimal fixed-point (e.g., 2 digits after decimal), convert to binary, then implement basic arithmetic operations.

## Common Misconceptions
Fixed-point precision is uniform across all values, unlike floating-point. The decimal point location is implicit, not stored.

## Questions

```yaml
- question: "A system uses Q8.8 fixed-point format (8 integer bits, 8 fractional bits). The stored integer value is 640. What real number does this represent?"
  type: multiple-choice
  options:
    - "640.0 — the stored value is the real value"
    - "2.5 — divide by 2⁸ = 256 to convert from stored integer to real number"
    - "160.0 — divide by 2² = 4 because there are 2 fractional bits per byte"
    - "0.0025 — multiply by 2⁻⁸ twice because the format has 8 fractional bits on each side"
  answer: 1
  explanation: "In Q8.8 format, the real value equals the stored integer divided by 2⁸ = 256, because the binary point sits 8 positions from the right. 640 / 256 = 2.5. You can verify: 2 in binary is 00000010.00000000, which is stored as 512; 0.5 in binary is 0.10000000, which is stored as 128; 512 + 128 = 640. The stored integer is not the real value — it is the real value scaled up by 2⁸. This scaling convention is the core of fixed-point representation."

- question: "When would fixed-point arithmetic be preferred over floating-point arithmetic?"
  type: multiple-choice
  options:
    - "When the program needs to represent very large and very small numbers simultaneously"
    - "When maximum numerical precision is required regardless of magnitude"
    - "When hardware simplicity, low power consumption, or deterministic timing matters more than dynamic range — such as in embedded systems, DSP, or motor control"
    - "When the range of values is unpredictable at design time"
  answer: 2
  explanation: "Fixed-point is preferred when you can commit to a known value range at design time and when a floating-point unit is unacceptable due to cost, power, or timing requirements. Fixed-point arithmetic uses the standard integer ALU — no dedicated FPU is needed. This is why early gaming hardware (original PlayStation), audio DSPs, and microcontrollers often use fixed-point. When the value range is unpredictable or spans many orders of magnitude, floating-point is the better choice — it adjusts precision based on magnitude. Fixed-point's uniform precision is a feature when the range is known, a liability when it isn't."

- question: "In a fixed-point number system, the position of the binary point is stored explicitly in each number so that the hardware knows how to interpret the bits."
  type: true-false
  answer: false
  explanation: "The binary point position is implicit — an agreed-upon convention that exists only in the programmer's interpretation of the bit pattern, not in the stored data itself. The hardware stores and manipulates an ordinary integer; it has no awareness of where the 'decimal point' lies. This is both the strength and the danger of fixed-point: arithmetic is simple (just integer operations), but if two values with different binary point positions are added without alignment, the result is silently wrong. Floating-point, by contrast, stores the exponent explicitly, allowing the hardware to handle numbers at different scales automatically."

- question: "Fixed-point arithmetic provides uniform precision across all representable values, unlike floating-point which has higher precision near zero."
  type: true-false
  answer: true
  explanation: "In a Q8.8 format, the spacing between adjacent representable values is always 1/256 ≈ 0.004, whether the value is near 0 or near 255. This uniform spacing means the absolute error of any fixed-point value is at most 0.002 (half the spacing). Floating-point sacrifices this uniformity for dynamic range: it is highly precise near zero (small exponent, many significant mantissa bits available) and increasingly imprecise for large values. For applications where uniform error distribution matters — such as audio sample arithmetic — fixed-point's regularity is an advantage."

- question: "Why must programmers perform 'scaling analysis' before using fixed-point arithmetic, and what can go wrong if they skip it?"
  type: short-answer
  answer: "Scaling analysis is the process of choosing the binary point position (the Q format) by analyzing the full expected range of every variable in the computation. The chosen format must represent the maximum value without overflow and the minimum meaningful value without losing it to rounding. If the range is underestimated, computed values overflow silently — the upper bits wrap around and produce garbage. If the format uses too many integer bits, fractional precision is wasted on representing a range that never occurs. Unlike floating-point, fixed-point gives no warning when values go out of range; the programmer must guarantee correctness by design."
  explanation: "This discipline is why fixed-point code is harder to write correctly than floating-point code, even though the hardware is simpler. Every intermediate calculation must be tracked through its possible range. Multiplying two Q8.8 values produces a Q16.16 intermediate result that must be right-shifted to return to Q8.8, and the programmer must ensure the pre-shift value fits in the available bits. In audio and DSP applications, scaling errors produce audible artifacts or silent corruption — which is why fixed-point software requires careful mathematical analysis, not just implementation."
```

## Explainer

From your understanding of the binary number system, you know how to represent integers as sequences of bits: each bit position represents a power of 2, and the value is the sum of those powers. **Fixed-point representation** extends this idea to fractional numbers by declaring that some of those bit positions represent negative powers of 2 — that is, fractions like 1/2, 1/4, 1/8. The key insight is that the hardware still stores and manipulates an ordinary integer; the "decimal point" (really a **binary point**) is a convention agreed upon by the programmer, not something encoded in the data itself.

Consider a 16-bit fixed-point format with 8 integer bits and 8 fractional bits, often written as **Q8.8** or **8.8 format**. The stored integer value 256 (binary `00000001.00000000`) represents the real number 1.0, because the binary point sits between bit 7 and bit 8. The stored value 384 (`00000001.10000000`) represents 1.5, since the fractional part `10000000` equals 1 × 2⁻¹ = 0.5. To convert from a real number to its fixed-point representation, you multiply by 2⁸ (256) and round: 3.14 × 256 = 803.84, stored as 803, which represents 803/256 ≈ 3.1367. The small error (3.1367 vs 3.14) is the quantization cost of fixed precision.

The great advantage of fixed-point is that **arithmetic maps directly to integer operations**. Adding two Q8.8 numbers is just integer addition — the binary points are aligned by construction. Subtraction is the same. Multiplication requires one extra step: multiplying two Q8.8 values produces a Q16.16 result (the fractional bits double), so you shift right by 8 to get back to Q8.8 format. No floating-point unit is needed; the standard integer ALU handles everything. This is why fixed-point dominates in embedded systems, DSP chips, and any hardware where a floating-point unit would be too expensive, too slow, or too power-hungry. Audio processing, motor control, and early 3D graphics (the original PlayStation used fixed-point exclusively) all relied on this approach.

The tradeoff compared to floating-point is **dynamic range**. A Q8.8 format can represent values from 0 to roughly 255.996 with uniform precision of about 0.004 everywhere. Floating-point, by contrast, adjusts its precision based on magnitude — very precise near zero, less precise for large values — and covers an enormous range. Fixed-point forces you to choose your range and precision at design time and stick with it. If a computation produces a value outside the representable range, it overflows silently. If values are very small, you waste the upper bits. The programmer must carefully analyze the expected range of every variable and choose formats accordingly — a discipline called **scaling analysis**. This manual effort is the price of fixed-point's hardware simplicity.
