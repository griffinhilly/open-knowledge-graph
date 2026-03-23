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
status: validated
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

## Questions

```yaml
- question: "A hardware designer needs circuits for both unsigned integer addition and signed (two's complement) integer addition. How many distinct adder circuits are required?"
  type: multiple-choice
  options:
    - "Two — one for unsigned, one that checks the sign bit before adding"
    - "One — the same binary addition hardware handles both correctly without modification"
    - "Two — two's complement requires a separate borrow-propagation unit"
    - "One, but it must flip the MSB before processing negative numbers"
  answer: 1
  explanation: "The central insight of two's complement is that the same carry-propagation adder hardware handles signed and unsigned arithmetic identically. The hardware doesn't 'know' about signs — it just adds bit patterns. Because two's complement represents negatives as 2^n - N (modular arithmetic), the carry-out of the MSB position handles overflow the same way in both cases. This is why two's complement was universally adopted over sign-magnitude, which would require separate circuits."

- question: "A programmer stores -128 in an 8-bit two's complement variable and writes `x = -x` to negate it. What value does x hold after this operation?"
  type: multiple-choice
  options:
    - "+128 — negating -128 produces its positive counterpart"
    - "-128 — the negation overflows back to the same bit pattern"
    - "+127 — the result saturates at the maximum representable positive value"
    - "0 — a value negated with itself always produces zero"
  answer: 1
  explanation: "To negate in two's complement, invert all bits and add 1. -128 is represented as 10000000. Inverting gives 01111111 (+127). Adding 1 gives 10000000 — which is -128 again. This is the one edge case where two's complement breaks: the range is asymmetric (-128 to +127 for 8 bits), so the most-negative value has no positive counterpart. Negating -128 is an overflow condition. Option A is the intuitive but wrong answer — +128 cannot be stored in an 8-bit two's complement variable."

- question: "In two's complement, the most significant bit acts as a separate 'sign flag' with no numeric place value — it simply marks the number as negative."
  type: true-false
  answer: false
  explanation: "This describes sign-magnitude encoding, not two's complement. In two's complement, the MSB has a place value of -2^(n-1). For an 8-bit number, the MSB contributes -128 to the total value if set. This is why the representation is asymmetric (one more negative value than positive) and why it works with standard adder hardware — every bit, including the MSB, participates in arithmetic normally."

- question: "In an 8-bit two's complement system, for every representable positive integer there is a corresponding negative integer of equal magnitude."
  type: true-false
  answer: false
  explanation: "The range of 8-bit two's complement is -128 to +127 — there is one more negative number than positive. The bit pattern 10000000 represents -128, but +128 cannot be represented in 8 bits. Negating -128 overflows back to -128. This asymmetry follows directly from the modular arithmetic definition: 2^8 = 256 values split as 128 negatives (-128 to -1), zero, and 127 positives (+1 to +127)."

- question: "Why does inverting all bits and adding one give the negation of a two's complement number? Explain the underlying mathematical principle."
  type: short-answer
  answer: "Two's complement represents the negation of N as 2^n - N (where n is the bit width), which is the additive inverse of N modulo 2^n. The bitwise inverse of an n-bit number N is (2^n - 1) - N (since inverting every bit subtracts each bit from 1). Adding 1 gives (2^n - 1) - N + 1 = 2^n - N, which is exactly the two's complement negation. So the 'invert and add one' rule is a fast way to compute 2^n - N using standard binary arithmetic."
  explanation: "The key insight is that 'invert all bits' computes (2^n - 1) - N, not 2^n - N. The extra +1 closes that gap. This also explains why negating -128 in 8 bits overflows: 2^8 - (-128) = 256 + 128 = 384, which exceeds the 8-bit range, so it wraps to 128 mod 256 = -128 in two's complement."
```

## Explainer

You know binary arithmetic — how to add and subtract binary numbers using the same carry-and-borrow rules as decimal. The challenge is extending this to negative numbers without making the hardware complicated. **Two's complement** is the encoding that makes this possible, and it is used by virtually every modern processor for signed integers.

The key insight is this: in a fixed-width binary system, if you invert all the bits of a number and add one, you get its negation — and the same addition circuitry that handles unsigned numbers handles signed arithmetic correctly with no modification. Take +5 in 4 bits: `0101`. Invert all bits to get `1010`, then add 1 to get `1011`. That bit pattern, `1011`, represents -5 in two's complement. Now add +5 and -5: `0101 + 1011 = 10000`. The leading 1 overflows out of the 4-bit width, leaving `0000` — exactly zero. The adder didn't need to know anything about signs; it just added two bit patterns and got the right answer.

This "invert and add one" rule is not arbitrary — it follows from the structure of modular arithmetic. In a 4-bit system, numbers wrap around at 2^4 = 16. The two's complement of a number N is simply 2^n - N (where n is the bit width), which is the additive inverse of N modulo 2^n. So -5 is represented as 16 - 5 = 11, which is `1011` in binary. This is why addition of a positive and its two's complement always yields zero (modulo the bit width), and why the same carry-propagation hardware works for both signed and unsigned numbers.

The MSB in two's complement still indicates sign (1 = negative, 0 = non-negative), but it is **not** a separate sign bit in the way sign-magnitude uses it — it has a place value of -2^(n-1). For an 8-bit number, the MSB contributes -128 to the value rather than just flagging "negative." This means the range is **asymmetric**: an 8-bit two's complement number ranges from -128 to +127. There is one more negative number than positive because `10000000` (-128) has no positive counterpart — negating it by inverting and adding one gives `10000000` again (it overflows back to itself). This asymmetry is worth remembering because it means negating the most-negative value is an overflow condition, the one edge case where two's complement arithmetic breaks its otherwise clean guarantees.
