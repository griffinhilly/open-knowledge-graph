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

## Explainer

From your understanding of the binary number system, you know how to represent integers as sequences of bits: each bit position represents a power of 2, and the value is the sum of those powers. **Fixed-point representation** extends this idea to fractional numbers by declaring that some of those bit positions represent negative powers of 2 — that is, fractions like 1/2, 1/4, 1/8. The key insight is that the hardware still stores and manipulates an ordinary integer; the "decimal point" (really a **binary point**) is a convention agreed upon by the programmer, not something encoded in the data itself.

Consider a 16-bit fixed-point format with 8 integer bits and 8 fractional bits, often written as **Q8.8** or **8.8 format**. The stored integer value 256 (binary `00000001.00000000`) represents the real number 1.0, because the binary point sits between bit 7 and bit 8. The stored value 384 (`00000001.10000000`) represents 1.5, since the fractional part `10000000` equals 1 × 2⁻¹ = 0.5. To convert from a real number to its fixed-point representation, you multiply by 2⁸ (256) and round: 3.14 × 256 = 803.84, stored as 803, which represents 803/256 ≈ 3.1367. The small error (3.1367 vs 3.14) is the quantization cost of fixed precision.

The great advantage of fixed-point is that **arithmetic maps directly to integer operations**. Adding two Q8.8 numbers is just integer addition — the binary points are aligned by construction. Subtraction is the same. Multiplication requires one extra step: multiplying two Q8.8 values produces a Q16.16 result (the fractional bits double), so you shift right by 8 to get back to Q8.8 format. No floating-point unit is needed; the standard integer ALU handles everything. This is why fixed-point dominates in embedded systems, DSP chips, and any hardware where a floating-point unit would be too expensive, too slow, or too power-hungry. Audio processing, motor control, and early 3D graphics (the original PlayStation used fixed-point exclusively) all relied on this approach.

The tradeoff compared to floating-point is **dynamic range**. A Q8.8 format can represent values from 0 to roughly 255.996 with uniform precision of about 0.004 everywhere. Floating-point, by contrast, adjusts its precision based on magnitude — very precise near zero, less precise for large values — and covers an enormous range. Fixed-point forces you to choose your range and precision at design time and stick with it. If a computation produces a value outside the representable range, it overflows silently. If values are very small, you waste the upper bits. The programmer must carefully analyze the expected range of every variable and choose formats accordingly — a discipline called **scaling analysis**. This manual effort is the price of fixed-point's hardware simplicity.
