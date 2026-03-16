---
id: twos-complement
title: Two's Complement Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-arithmetic
  type: hard
- id: integers-and-number-line
  type: soft
- id: adding-integers
  type: soft
builds-toward:
- adder-circuits
- arithmetic-logic-unit
- floating-point-representation
tags:
- signed-integers
- twos-complement
- representation
- negative-numbers
stage: formal-systems
status: validated
---

# Two's Complement Representation

## Core Idea
Two's complement is the standard way to represent signed integers in binary. In an n-bit two's complement number, the most significant bit has a place value of −2^(n-1) rather than +2^(n-1), so the range is −2^(n-1) to 2^(n-1)−1. To negate a number, flip all bits and add 1. The key advantage is that addition and subtraction hardware works identically for signed and unsigned numbers, eliminating the need for separate circuits.

## How It's Best Learned
Convert small positive integers to their two's complement negatives by hand. Verify that adding a number and its negative produces zero with carry discarded. Check boundary values like the minimum negative number, which has no positive counterpart.

## Common Misconceptions
- There is only one representation of zero in two's complement, unlike sign-magnitude representation.
- The 'flip-and-add-1' method is a shortcut derived from the algebraic definition, not the definition itself.

## Explainer

You already know how to represent positive integers in binary using place values: in an 8-bit number, the bits represent 128, 64, 32, 16, 8, 4, 2, 1 from left to right. Two's complement extends this system to handle negative numbers by making one simple change: the **most significant bit** (MSB) gets a *negative* place value. In an 8-bit two's complement number, the leftmost bit represents −128 instead of +128. So the bit pattern 10000000 equals −128 + 0 = −128, and 11111111 equals −128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = −1. If the MSB is 0, the number is non-negative and reads exactly like unsigned binary. If the MSB is 1, the number is negative.

The brilliant property of two's complement is that **addition works identically for signed and unsigned numbers**. Consider adding +3 (00000011) and −1 (11111111) in 8 bits: the binary sum is 100000010, but the leading 1 overflows beyond 8 bits and is discarded, leaving 00000010 = +2. The correct answer, with no special hardware needed. This is not a coincidence — it is the reason two's complement was chosen over alternatives like sign-magnitude (where a dedicated sign bit flags negative numbers) or ones' complement (where negation means flipping all bits without adding 1). Those systems require the ALU to check signs and handle special cases; two's complement lets a single adder circuit handle all signed and unsigned arithmetic.

To **negate** a two's complement number, you flip every bit and add 1. Why does this work? Consider the number +5 = 00000101. Flipping all bits gives 11111010. Notice that a number plus its bitwise complement always equals 11111111 (all ones), which in two's complement is −1. So if N + flip(N) = −1, then flip(N) = −N − 1, and flip(N) + 1 = −N. For +5: flip gives 11111010 (which is −6), and adding 1 gives 11111011 (which is −5). You can verify: −128 + 64 + 32 + 16 + 8 + 0 + 2 + 1 = −5. This trick works for every value except the most negative number: −128 (10000000) flipped is 01111111 (+127), and adding 1 gives 10000000 (−128 again). This asymmetry — the range is −128 to +127, not ±127 — is an inherent consequence of having an even number of bit patterns but wanting to include zero.

Understanding two's complement is essential for everything that follows in computer architecture. When you study adder circuits, you will see that subtraction is implemented as addition of the negated value — the ALU flips the bits of the second operand, sets the carry-in to 1, and uses the same adder. When you encounter the ALU's overflow detection, it checks whether two positive inputs produced a negative result (or two negatives produced a positive) — a condition that only makes sense through the lens of two's complement interpretation. And when you reach floating-point representation, you will see two's complement used again for the exponent field's bias encoding. The system is simple, elegant, and universal — which is why every modern processor uses it.
