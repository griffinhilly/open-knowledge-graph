---
id: ones-complement-representation
title: One's Complement Number Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
tags:
- number-representation
- signed-integers
stage: formal-systems
status: validated
---

# One's Complement Number Representation

## Core Idea
One's complement represents negative numbers by inverting all bits. Unlike two's complement, it has two zero representations and makes arithmetic more complicated, though it was used historically.

## Questions

```yaml
- question: "In a 4-bit one's complement system, you add +5 (0101) and -3 (1100). The raw binary result is 10001. What is the correct final answer?"
  type: multiple-choice
  options:
    - "0001 (+1) — the carry simply wraps the result back to 4 bits"
    - "0010 (+2) — end-around carry adds the overflow bit back to the LSB"
    - "1110 (-1) — the carry inverts the sign"
    - "0000 (0) — the carry cancels the result"
  answer: 1
  explanation: "End-around carry is the correction step unique to one's complement. When a carry overflows past the MSB, it must be added back to the least-significant bit: 0001 + 1 = 0010 = +2. Without this step, sums crossing zero are off by one. This is one of the key reasons one's complement fell out of favor — two's complement requires no such correction."

- question: "Why does one's complement have two representations of zero, while two's complement has only one?"
  type: multiple-choice
  options:
    - "Because one's complement uses fewer bits and cannot distinguish all values"
    - "Because flipping all bits of 0000 gives 1111, a different pattern that also represents zero"
    - "Because the MSB is reserved for the sign and cannot encode magnitude"
    - "Because one's complement was designed before hardware could reliably represent zero"
  answer: 1
  explanation: "In one's complement, negation = flip all bits. Applying this to +0 (0000) produces 1111, which represents −0. Both 0000 and 1111 evaluate to zero, but are distinct bit patterns. This forces comparison logic to test two patterns when checking for zero. Two's complement avoids this: flipping all bits of 0000 gives 1111, but then adding 1 wraps back to 0000, so there is only one zero."

- question: "In one's complement, end-around carry is mainly needed when the two operands have opposite signs."
  type: true-false
  answer: false
  explanation: "End-around carry is needed whenever a carry overflows out of the MSB position, regardless of the signs of the operands. This can happen in mixed-sign addition or in other arithmetic operations. The rule is structural: any overflow carry past the MSB must be added back to the LSB. Limiting it to opposite-sign cases would miss legitimate corrections."

- question: "The Internet checksum used in TCP/IP headers is computed using one's complement arithmetic, partly because the symmetry of positive and negative zero simplifies incremental updates."
  type: true-false
  answer: true
  explanation: "This is one of the few modern uses of one's complement. The Internet checksum sums 16-bit words in one's complement and takes the one's complement of the result. The dual-zero symmetry is actually a feature here: because +0 and -0 both represent 'no error,' incremental checksum updates (when a header field changes) remain consistent without special-casing zero. It's a rare case where one's complement's quirk becomes a design advantage."

- question: "Why does one's complement require end-around carry for addition, and what problem does this solve?"
  type: short-answer
  answer: "When two one's complement numbers are added and produce a carry out of the MSB, that carry must be added back to the LSB. Without this correction, results that cross zero (from positive to negative or vice versa) are off by one. The problem arises because the two-zero representation leaves a 'gap' in the number line: going from +0 to -0 consumes one position, so arithmetic without correction lands one unit away from the true sum."
  explanation: "The root cause is the two-zero representation. The numbers from -0 to +0 span one extra position compared to two's complement. End-around carry compensates for this by adding the escaped carry bit back into the low end. Two's complement eliminates this entirely by having only one zero, which is why it replaced one's complement in essentially all general-purpose hardware."
```

## Explainer

From your study of the binary number system, you know how to represent positive integers as sequences of bits — for example, 5 as 0101 in a 4-bit system. But what about negative numbers? There is no minus sign in hardware, so the encoding itself must convey sign information. **One's complement** is one of the earliest schemes for representing signed integers, and understanding its strengths and weaknesses illuminates why modern systems chose a different approach.

The rule is simple: to negate a number in one's complement, **flip every bit**. If +5 is 0101, then −5 is 1010. The most significant bit (MSB) serves as a sign indicator — 0 for positive, 1 for negative — but unlike a simple sign-magnitude scheme, the remaining bits are not the same as the positive version. Instead, each bit is inverted. This means you can negate a number using nothing more than a row of NOT gates, which made one's complement attractive to early hardware designers because inverters are among the cheapest and fastest logic components.

The scheme has an elegant symmetry but a frustrating quirk: **two representations of zero**. Positive zero is 0000, and negative zero is 1111 (all bits flipped). Both represent the value zero, but they are different bit patterns. This creates complications in comparison logic — checking whether a value is zero now requires testing for two patterns instead of one. It also complicates arithmetic. When you add two one's complement numbers and the carry bit overflows past the MSB, you must wrap that carry back around and add it to the least significant bit, a step called **end-around carry**. Without this correction, sums that cross zero produce answers that are off by one.

These complications are exactly why one's complement fell out of favor. Two's complement, which you will likely encounter next, solves both problems: it has a single zero representation and does not need end-around carry. Nevertheless, one's complement survives in certain niches — notably, the Internet checksum used in TCP and IP headers is a one's complement sum, chosen because its error-detection properties and the symmetry of positive and negative zero simplify incremental checksum updates when header fields change.
