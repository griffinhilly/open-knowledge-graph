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
status: draft
---

# Two's Complement Representation

## Core Idea
Two's complement is the standard way to represent signed integers in binary. In an n-bit two's complement number, the most significant bit has a place value of −2^(n-1) rather than +2^(n-1), so the range is −2^(n-1) to 2^(n-1)−1. To negate a number, flip all bits and add 1. The key advantage is that addition and subtraction hardware works identically for signed and unsigned numbers, eliminating the need for separate circuits.

## How It's Best Learned
Convert small positive integers to their two's complement negatives by hand. Verify that adding a number and its negative produces zero with carry discarded. Check boundary values like the minimum negative number, which has no positive counterpart.

## Common Misconceptions
- There is only one representation of zero in two's complement, unlike sign-magnitude representation.
- The 'flip-and-add-1' method is a shortcut derived from the algebraic definition, not the definition itself.
