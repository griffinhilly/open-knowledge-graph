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

## Explainer

You know binary arithmetic — how to add and subtract binary numbers using the same carry-and-borrow rules as decimal. The challenge is extending this to negative numbers without making the hardware complicated. **Two's complement** is the encoding that makes this possible, and it is used by virtually every modern processor for signed integers.

The key insight is this: in a fixed-width binary system, if you invert all the bits of a number and add one, you get its negation — and the same addition circuitry that handles unsigned numbers handles signed arithmetic correctly with no modification. Take +5 in 4 bits: `0101`. Invert all bits to get `1010`, then add 1 to get `1011`. That bit pattern, `1011`, represents -5 in two's complement. Now add +5 and -5: `0101 + 1011 = 10000`. The leading 1 overflows out of the 4-bit width, leaving `0000` — exactly zero. The adder didn't need to know anything about signs; it just added two bit patterns and got the right answer.

This "invert and add one" rule is not arbitrary — it follows from the structure of modular arithmetic. In a 4-bit system, numbers wrap around at 2^4 = 16. The two's complement of a number N is simply 2^n - N (where n is the bit width), which is the additive inverse of N modulo 2^n. So -5 is represented as 16 - 5 = 11, which is `1011` in binary. This is why addition of a positive and its two's complement always yields zero (modulo the bit width), and why the same carry-propagation hardware works for both signed and unsigned numbers.

The MSB in two's complement still indicates sign (1 = negative, 0 = non-negative), but it is **not** a separate sign bit in the way sign-magnitude uses it — it has a place value of -2^(n-1). For an 8-bit number, the MSB contributes -128 to the value rather than just flagging "negative." This means the range is **asymmetric**: an 8-bit two's complement number ranges from -128 to +127. There is one more negative number than positive because `10000000` (-128) has no positive counterpart — negating it by inverting and adding one gives `10000000` again (it overflows back to itself). This asymmetry is worth remembering because it means negating the most-negative value is an overflow condition, the one edge case where two's complement arithmetic breaks its otherwise clean guarantees.
