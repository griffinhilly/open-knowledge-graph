---
id: multiplication-circuits
title: Multiplication Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: full-adder-circuit-design
  type: hard
tags:
- multiplier
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Multiplication Circuit Design

## Core Idea
Binary multiplication uses shift-and-add: each multiplier bit masks partial products (via AND), which are accumulated and shifted. Booth's algorithm and other optimizations reduce partial products and improve speed.

## Explainer

If you can build a full adder, you already have the core component needed for multiplication. Binary multiplication works exactly like the longhand multiplication you learned in grade school, except it is far simpler because each digit is either 0 or 1. When you multiply 1011 by 1101, you take each bit of the multiplier, multiply it by the entire multiplicand, and shift the result left by the appropriate number of positions. Multiplying any number by a single binary digit is trivial: if the bit is 1, the result is the number itself; if 0, the result is zero. This "multiply by one bit" operation is just an AND gate applied to each bit of the multiplicand.

The **shift-and-add** method implements this directly in hardware. For an n-bit multiplication, you generate n **partial products** — each one is the multiplicand ANDed with one bit of the multiplier, shifted left by that bit's position. Then you add all the partial products together using the adder circuits you already know how to build. A simple implementation uses a single adder and a shift register, processing one multiplier bit per clock cycle: check the lowest multiplier bit, conditionally add the multiplicand to a running accumulator, then shift. After n cycles, the accumulator holds the product. This is slow but uses minimal hardware.

The speed problem is clear: an n-bit multiply takes n addition steps. **Booth's algorithm** is an optimization that reduces the number of additions by looking at pairs of adjacent multiplier bits. When the multiplier contains runs of consecutive 1s (like 01110), Booth's encoding replaces the four separate additions with a subtraction at the start of the run and an addition at the end — turning four operations into two. The key insight is that a string of 1s like 0111...10 equals 1000...00 minus 0000...10, so you can subtract the partial product at the run's start and add at the run's end.

For high-performance processors, even Booth's algorithm isn't fast enough when multiplication must complete in a single cycle. Hardware multipliers use **array multipliers** or **Wallace trees** that generate and sum all partial products simultaneously using massive parallel adder networks. A Wallace tree arranges carry-save adders in a tree structure that reduces n partial products to just two numbers in logarithmic time, then a single fast adder produces the final result. These designs trade enormous chip area for speed — a tradeoff that makes sense inside a modern CPU where multiplication is one of the most performance-critical operations.
