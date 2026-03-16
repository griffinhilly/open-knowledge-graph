---
id: full-adder-circuit-design
title: Full Adder Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: half-adder-circuit-design
  type: hard
builds-toward:
- ripple-carry-adder-design
tags:
- adder
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Full Adder Circuit Design

## Core Idea
A full adder adds two bits plus a carry-in, producing sum and carry-out. Composed of two half adders and an OR gate, full adders cascade to form multi-bit adders.

## Explainer

You already know the half adder — it takes two single-bit inputs (A and B) and produces a sum bit and a carry bit. The half adder works perfectly for the least significant bit of a multi-bit addition, where there's no incoming carry. But for every other bit position, there are three inputs to consider: the two bits being added *plus* a carry-in from the previous position. This is exactly what a **full adder** handles: it computes the sum of three single-bit values (A, B, and C_in) and produces both a **sum** output and a **carry-out**.

The elegant construction uses two half adders chained together. The first half adder adds A and B, producing a partial sum and a partial carry. The second half adder adds that partial sum to C_in, producing the final sum bit and another partial carry. The final carry-out is the OR of the two partial carries — a carry is generated if either the first addition (A + B) produced a carry, or the second addition (partial sum + C_in) produced one. It's impossible for both to generate carries simultaneously (that would require a sum of 4 in binary, which can't happen with three single-bit inputs), so OR correctly combines them.

To verify the logic, trace through the case A=1, B=1, C_in=1. The first half adder computes 1+1: sum=0, carry=1. The second half adder computes 0+1 (partial sum plus carry-in): sum=1, carry=0. The final carry-out is 1 OR 0 = 1. The result is sum=1, carry=1, representing the binary value 11 — which is decimal 3, the correct sum of three 1s.

The real power of the full adder is **cascading**. To build an n-bit adder, you chain n full adders together, connecting each stage's carry-out to the next stage's carry-in. The least significant bit can use either a half adder or a full adder with C_in tied to 0. This structure — called a **ripple carry adder** — directly mirrors how you do long addition by hand: add each column, write down the digit, carry the 1 to the next column. The limitation is speed — each bit position must wait for the carry from the previous position — but the full adder itself is the fundamental arithmetic building block from which all more sophisticated adder designs (carry lookahead, carry select, carry save) are constructed.
