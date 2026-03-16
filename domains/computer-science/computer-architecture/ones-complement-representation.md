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
status: draft
---

# One's Complement Number Representation

## Core Idea
One's complement represents negative numbers by inverting all bits. Unlike two's complement, it has two zero representations and makes arithmetic more complicated, though it was used historically.

## Explainer

From your study of the binary number system, you know how to represent positive integers as sequences of bits — for example, 5 as 0101 in a 4-bit system. But what about negative numbers? There is no minus sign in hardware, so the encoding itself must convey sign information. **One's complement** is one of the earliest schemes for representing signed integers, and understanding its strengths and weaknesses illuminates why modern systems chose a different approach.

The rule is simple: to negate a number in one's complement, **flip every bit**. If +5 is 0101, then −5 is 1010. The most significant bit (MSB) serves as a sign indicator — 0 for positive, 1 for negative — but unlike a simple sign-magnitude scheme, the remaining bits are not the same as the positive version. Instead, each bit is inverted. This means you can negate a number using nothing more than a row of NOT gates, which made one's complement attractive to early hardware designers because inverters are among the cheapest and fastest logic components.

The scheme has an elegant symmetry but a frustrating quirk: **two representations of zero**. Positive zero is 0000, and negative zero is 1111 (all bits flipped). Both represent the value zero, but they are different bit patterns. This creates complications in comparison logic — checking whether a value is zero now requires testing for two patterns instead of one. It also complicates arithmetic. When you add two one's complement numbers and the carry bit overflows past the MSB, you must wrap that carry back around and add it to the least significant bit, a step called **end-around carry**. Without this correction, sums that cross zero produce answers that are off by one.

These complications are exactly why one's complement fell out of favor. Two's complement, which you will likely encounter next, solves both problems: it has a single zero representation and does not need end-around carry. Nevertheless, one's complement survives in certain niches — notably, the Internet checksum used in TCP and IP headers is a one's complement sum, chosen because its error-detection properties and the symmetry of positive and negative zero simplify incremental checksum updates when header fields change.
