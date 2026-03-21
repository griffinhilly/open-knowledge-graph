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

## Questions

```yaml
- question: "In an 8-bit two's complement system, what is the result of adding 01111111 (+127) and 00000001 (+1)?"
  type: multiple-choice
  options:
    - "10000000, which represents +128 — the largest positive value in the range"
    - "10000000, which represents −128 — this is a signed overflow"
    - "11111111, which represents −1"
    - "00000000, which represents 0 due to wraparound"
  answer: 1
  explanation: "In 8-bit two's complement, the MSB has place value −128. The bit pattern 10000000 = −128, not +128. Adding +127 and +1 should give +128, but that value is outside the representable range (−128 to +127). The result 10000000 is interpreted as −128 — a signed overflow. This is detected by hardware when two positive inputs produce a negative result. The correct answer reveals why two's complement range is asymmetric: the MSB's negative place value means one extra negative value fits."

- question: "Why does 8-bit two's complement represent numbers from −128 to +127 rather than the symmetric range −127 to +127?"
  type: multiple-choice
  options:
    - "One bit pattern (10000000) is reserved as an error or undefined value"
    - "There is exactly one representation of zero, so the 256 bit patterns split into 127 positive values, zero, and 128 negative values"
    - "Hardware designers chose this range to match ASCII character encoding"
    - "The range is actually symmetric — there is a +128 that is rarely used"
  answer: 1
  explanation: "With 8 bits, there are exactly 256 bit patterns. Two's complement uses exactly one pattern for zero (00000000). The remaining 255 patterns divide into 127 positive values (00000001 through 01111111) and 128 negative values (10000000 through 11111111). The asymmetry is a direct consequence of single-zero representation. Sign-magnitude has two zeros (+0 and −0), which is why it achieves a symmetric ±127 range with 8 bits — but at the cost of requiring special handling of two zeros."

- question: "In two's complement, the 'flip all bits and add 1' method for negating a number is a convenient shortcut derived from the algebraic definition, not the definition itself."
  type: true-false
  answer: true
  explanation: "The definition of two's complement is that the MSB has a negative place value. The flip-and-add-1 shortcut follows algebraically: if N + flip(N) = all-ones = −1, then flip(N) = −N − 1, so flip(N) + 1 = −N. The shortcut works because of the underlying place-value definition — it is not a defining axiom. Understanding this matters because the shortcut breaks down at one edge case: the most negative number (10000000) flipped is 01111111 (+127), and adding 1 gives back 10000000 (−128). That's not a bug in the definition — it's an unavoidable consequence of the asymmetric range."

- question: "Two's complement uses two distinct bit patterns to represent zero, which is why it can represent one more negative number than positive numbers."
  type: true-false
  answer: false
  explanation: "This describes sign-magnitude representation, not two's complement. In sign-magnitude, the patterns 00000000 (+0) and 10000000 (−0) both represent zero, giving two zero representations and a symmetric ±127 range. Two's complement has exactly one zero (00000000), and the pattern 10000000 represents −128 — a genuine negative value. The single zero is one of two's complement's key advantages over sign-magnitude, eliminating the need to special-case equality comparisons involving zero."

- question: "Why does two's complement allow a single adder circuit to handle both signed and unsigned addition without any special cases?"
  type: short-answer
  answer: "In two's complement, the place values of bits 0 through n−2 are identical for signed and unsigned interpretation — only the MSB differs (−2^(n-1) for signed, +2^(n-1) for unsigned). When you add two numbers, the adder produces the same bit pattern regardless of whether the operands are treated as signed or unsigned. Whether that pattern represents a valid signed or unsigned result is an interpretation question, not a hardware question. For example, adding +3 (00000011) and −1 (11111111) uses the same binary addition as unsigned 3 + 255, producing 100000010, and discarding the carry gives 00000010 = 2 in both interpretations. The hardware does one thing; the programmer decides what it means."
  explanation: "This is the fundamental elegance of two's complement: the carry-propagating adder is agnostic to signedness. Sign-magnitude and ones' complement require the ALU to check sign bits and handle special cases, requiring more transistors and slower operation. Two's complement eliminates all of this — which is why it became universal in computer hardware."
```

## Explainer

You already know how to represent positive integers in binary using place values: in an 8-bit number, the bits represent 128, 64, 32, 16, 8, 4, 2, 1 from left to right. Two's complement extends this system to handle negative numbers by making one simple change: the **most significant bit** (MSB) gets a *negative* place value. In an 8-bit two's complement number, the leftmost bit represents −128 instead of +128. So the bit pattern 10000000 equals −128 + 0 = −128, and 11111111 equals −128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = −1. If the MSB is 0, the number is non-negative and reads exactly like unsigned binary. If the MSB is 1, the number is negative.

The brilliant property of two's complement is that **addition works identically for signed and unsigned numbers**. Consider adding +3 (00000011) and −1 (11111111) in 8 bits: the binary sum is 100000010, but the leading 1 overflows beyond 8 bits and is discarded, leaving 00000010 = +2. The correct answer, with no special hardware needed. This is not a coincidence — it is the reason two's complement was chosen over alternatives like sign-magnitude (where a dedicated sign bit flags negative numbers) or ones' complement (where negation means flipping all bits without adding 1). Those systems require the ALU to check signs and handle special cases; two's complement lets a single adder circuit handle all signed and unsigned arithmetic.

To **negate** a two's complement number, you flip every bit and add 1. Why does this work? Consider the number +5 = 00000101. Flipping all bits gives 11111010. Notice that a number plus its bitwise complement always equals 11111111 (all ones), which in two's complement is −1. So if N + flip(N) = −1, then flip(N) = −N − 1, and flip(N) + 1 = −N. For +5: flip gives 11111010 (which is −6), and adding 1 gives 11111011 (which is −5). You can verify: −128 + 64 + 32 + 16 + 8 + 0 + 2 + 1 = −5. This trick works for every value except the most negative number: −128 (10000000) flipped is 01111111 (+127), and adding 1 gives 10000000 (−128 again). This asymmetry — the range is −128 to +127, not ±127 — is an inherent consequence of having an even number of bit patterns but wanting to include zero.

Understanding two's complement is essential for everything that follows in computer architecture. When you study adder circuits, you will see that subtraction is implemented as addition of the negated value — the ALU flips the bits of the second operand, sets the carry-in to 1, and uses the same adder. When you encounter the ALU's overflow detection, it checks whether two positive inputs produced a negative result (or two negatives produced a positive) — a condition that only makes sense through the lens of two's complement interpretation. And when you reach floating-point representation, you will see two's complement used again for the exponent field's bias encoding. The system is simple, elegant, and universal — which is why every modern processor uses it.
