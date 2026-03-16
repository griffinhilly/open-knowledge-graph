---
id: adder-circuits
title: 'Adder Circuits: Half Adder, Full Adder, and Carry-Ripple'
domain: computer-science
course: computer-architecture
prerequisites:
- id: combinational-circuit-design
  type: hard
- id: binary-arithmetic
  type: hard
- id: twos-complement
  type: soft
builds-toward:
- arithmetic-logic-unit
tags:
- adder
- carry
- ripple-carry
- combinational-circuits
stage: formal-systems
status: validated
---
# Adder Circuits: Half Adder, Full Adder, and Carry-Ripple

## Core Idea
A half adder computes the sum and carry-out of two single bits. A full adder extends this to accept a carry-in, enabling chaining. A ripple-carry adder chains n full adders to add n-bit numbers, with each carry propagating from the least significant to the most significant bit. While simple and correct, ripple-carry adders are slow for large n because carry propagation is sequential. Faster designs like carry-lookahead adders compute carries in parallel.

## How It's Best Learned
Draw the gate-level implementation of a half adder and full adder from their truth tables. Chain four full adders into a 4-bit ripple-carry adder and trace a sample addition. Count gate delays to understand why speed degrades with wider adders.

## Common Misconceptions
- A half adder cannot be chained to build multi-bit adders because it lacks a carry-in input.
- The 'ripple' in ripple-carry refers to carry propagation delay, not any visible signal rippling — the circuit is purely combinational.

## Explainer

You know from binary arithmetic that adding two binary numbers works column by column from right to left, just like decimal addition, and that a carry can propagate from one column to the next. You also know from combinational circuit design that any Boolean function can be implemented with logic gates. Adder circuits are where these two ideas converge: they implement binary addition in hardware, starting from the simplest possible case and scaling up.

A **half adder** handles the simplest scenario: adding two single-bit inputs, A and B, with no incoming carry. The truth table has four rows, and inspection reveals that the sum output equals A XOR B (it is 1 when exactly one input is 1) and the carry output equals A AND B (it is 1 only when both inputs are 1). That is the entire circuit — one XOR gate and one AND gate. The half adder works perfectly for the least significant bit of an addition, where there is no carry coming in from a previous column.

A **full adder** extends the half adder by accepting a third input: the **carry-in** (Cin) from the previous column. Its truth table has eight rows, and the outputs are: Sum = A XOR B XOR Cin, and Carry-out = (A AND B) OR (Cin AND (A XOR B)). You can think of a full adder as two half adders chained together with an OR gate collecting the carries. The full adder is the fundamental building block for multi-bit addition because it can both receive and produce a carry.

To add two n-bit numbers, you chain n full adders into a **ripple-carry adder**. The carry-out of bit position 0 feeds into the carry-in of bit position 1, and so on up to bit position n-1. The circuit is simple and correct, but it has a critical performance limitation: bit position k cannot produce its final sum until the carry from position k-1 has arrived, which in turn waits for position k-2, and so on back to position 0. For a 32-bit adder, the carry must ripple through 32 full adders in sequence. If each full adder has a gate delay of 2 gates for the carry path, the total delay is 64 gate delays — far too slow for a modern processor that needs to add numbers in a single clock cycle. This is why faster adder designs like carry-lookahead exist: they compute the carries in parallel rather than waiting for the ripple, trading more gates for dramatically less delay.
