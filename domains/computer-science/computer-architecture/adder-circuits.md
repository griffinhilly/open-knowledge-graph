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
