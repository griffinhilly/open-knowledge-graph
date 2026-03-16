---
id: binary-adders
title: 'Binary Adders: Half-Adders and Full-Adders'
domain: computer-science
course: computer-architecture
prerequisites:
- id: adder-circuits
  type: hard
- id: boolean-algebra-and-laws
  type: soft
- id: boolean-algebra
  type: soft
- id: binary-arithmetic
  type: soft
builds-toward:
- arithmetic-logic-units-design
- fixed-point-number-representation
tags:
- adders
- binary
- arithmetic
stage: formal-systems
status: draft
---

# Binary Adders: Half-Adders and Full-Adders

## Core Idea
Half-adders add two bits without carry-in; full-adders add three bits (two operands plus carry-in). Cascading full-adders creates ripple-carry adders for multi-bit addition, the basis of arithmetic in processors.

## Explainer

You already know how binary arithmetic works on paper — adding columns of 1s and 0s, carrying a 1 when a column sums to 2 or 3. Binary adder circuits do exactly this in hardware, and they are built from the Boolean logic gates you studied in Boolean algebra. The simplest building block is the **half-adder**, which adds two single-bit inputs (A and B) and produces two outputs: a **sum** bit and a **carry** bit. The sum is A XOR B (1 when the inputs differ), and the carry is A AND B (1 only when both inputs are 1). This mirrors the paper algorithm perfectly: 0+0=00, 0+1=01, 1+0=01, 1+1=10.

The half-adder has a limitation: it has no input for an incoming carry from a previous column. When you add multi-bit numbers, every column beyond the least significant one must handle a carry-in from the column to its right. The **full-adder** solves this by accepting three inputs: A, B, and a carry-in (Cin). It produces a sum bit (A XOR B XOR Cin) and a carry-out (Cout). You can build a full-adder from two half-adders and an OR gate: the first half-adder adds A and B, the second adds that result to Cin, and the OR gate combines both carry outputs. This modularity — building complex circuits from simpler ones — is a recurring pattern in digital design.

To add two *n*-bit numbers, you chain *n* full-adders together in a **ripple-carry adder**. The carry-out of bit position 0 feeds into the carry-in of bit position 1, which feeds into bit position 2, and so on — the carry "ripples" through the chain. The least significant bit can use a half-adder (or a full-adder with Cin tied to 0). This design is simple and correct, but it has a speed problem: bit position *n*-1 cannot compute its final sum until the carry has propagated through all *n*-1 preceding stages. Each stage adds a small gate delay, and for a 64-bit adder, that delay accumulates.

This propagation delay is why faster adder designs exist — carry-lookahead adders compute carries in parallel rather than sequentially, and carry-select adders speculatively compute both possible results (carry=0 and carry=1) and select the correct one. But the ripple-carry adder remains the conceptual foundation: it makes the connection between the binary arithmetic you do on paper and the physical gates that execute it in silicon, and every more advanced adder design is ultimately an optimization of the same underlying addition algorithm.
