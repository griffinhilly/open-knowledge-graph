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

## Questions

```yaml
- question: "Why must a multi-bit adder use full adders (not half adders) for bit positions above bit 0?"
  type: multiple-choice
  options:
    - "Half adders can only process inputs of 0 or 1, which is insufficient for multi-bit numbers"
    - "A half adder has no carry-in input, so it cannot accept the carry produced by the previous bit position"
    - "Full adders use fewer gates per position, making them more efficient for chaining"
    - "Half adders require a clock signal, making them incompatible with the combinational logic of ripple-carry"
  answer: 1
  explanation: "A half adder accepts exactly two inputs (A and B) and has no carry-in. Multi-bit addition requires each bit position to incorporate the carry-out of the previous position as a third input. Without carry-in, the carry from position k-1 has nowhere to go, and the addition is incorrect for any case where a carry propagates. Full adders add a third input (Cin) explicitly to handle this, making them the correct building block for all positions except potentially bit 0."

- question: "A 16-bit ripple-carry adder has 3 gate delays per full adder in the carry path. What is the worst-case carry propagation delay?"
  type: multiple-choice
  options:
    - "3 gate delays — all carries are computed simultaneously in parallel"
    - "16 gate delays — one full adder's carry delay per bit position"
    - "48 gate delays — the carry must ripple sequentially through all 16 stages"
    - "8 gate delays — alternating stages can share carry logic"
  answer: 2
  explanation: "In a ripple-carry adder, carry-out from bit k cannot be computed until carry-in from bit k-1 arrives. This creates a serial chain: bit 0 finishes first, then bit 1 waits, through bit 15. The worst-case delay is 16 × 3 = 48 gate delays — linear in bit width. This is the defining limitation of ripple-carry architecture and the reason carry-lookahead adders exist."

- question: "A full adder's carry-out is 1 whenever at least two of its three inputs (A, B, Cin) are 1."
  type: true-false
  answer: true
  explanation: "Carry-out represents the 'overflow' when the sum of three single-bit inputs reaches 2 or 3. It equals 1 in exactly four of eight cases: (1,1,0), (1,0,1), (0,1,1), and (1,1,1) — all cases where two or more inputs are 1. This can be expressed as (A AND B) OR (B AND Cin) OR (A AND Cin), or equivalently (A AND B) OR (Cin AND (A XOR B)), which reuses the propagate term already computed for the Sum output."

- question: "A ripple-carry adder produces incorrect results for large binary inputs because the carry logic becomes inaccurate at higher bit positions."
  type: true-false
  answer: false
  explanation: "Ripple-carry adders are always logically correct — they produce the right answer for any input size. The limitation is speed, not accuracy. The final settled output is always correct; the problem is timing: higher-order bits cannot commit to their final values until the carry from lower positions has propagated through. This is a performance constraint, not a logic error, and it motivates carry-lookahead designs."

- question: "Explain why ripple-carry adder delay grows linearly with bit width, and what principle carry-lookahead uses to improve this."
  type: short-answer
  answer: "In a ripple-carry adder, each stage depends on the carry-out of the previous stage, creating a serial chain of n gate delays for n bits. Carry-lookahead breaks this serial dependency by pre-computing each carry directly from the original inputs using 'generate' (G_i = A_i AND B_i, meaning this stage will definitely produce a carry) and 'propagate' (P_i = A_i XOR B_i, meaning this stage will pass a carry through if one arrives) signals. With all G and P values known simultaneously, all carries can be resolved in parallel in O(log n) logic levels."
  explanation: "The bottleneck in ripple-carry is data dependency — each stage must wait for information from its predecessor. Carry-lookahead eliminates this by recomputing what each stage would do based on the original inputs alone, allowing all carries to be determined simultaneously. This trades additional gate area for dramatically reduced delay."
```

## Explainer

You know from binary arithmetic that adding two binary numbers works column by column from right to left, just like decimal addition, and that a carry can propagate from one column to the next. You also know from combinational circuit design that any Boolean function can be implemented with logic gates. Adder circuits are where these two ideas converge: they implement binary addition in hardware, starting from the simplest possible case and scaling up.

A **half adder** handles the simplest scenario: adding two single-bit inputs, A and B, with no incoming carry. The truth table has four rows, and inspection reveals that the sum output equals A XOR B (it is 1 when exactly one input is 1) and the carry output equals A AND B (it is 1 only when both inputs are 1). That is the entire circuit — one XOR gate and one AND gate. The half adder works perfectly for the least significant bit of an addition, where there is no carry coming in from a previous column.

A **full adder** extends the half adder by accepting a third input: the **carry-in** (Cin) from the previous column. Its truth table has eight rows, and the outputs are: Sum = A XOR B XOR Cin, and Carry-out = (A AND B) OR (Cin AND (A XOR B)). You can think of a full adder as two half adders chained together with an OR gate collecting the carries. The full adder is the fundamental building block for multi-bit addition because it can both receive and produce a carry.

To add two n-bit numbers, you chain n full adders into a **ripple-carry adder**. The carry-out of bit position 0 feeds into the carry-in of bit position 1, and so on up to bit position n-1. The circuit is simple and correct, but it has a critical performance limitation: bit position k cannot produce its final sum until the carry from position k-1 has arrived, which in turn waits for position k-2, and so on back to position 0. For a 32-bit adder, the carry must ripple through 32 full adders in sequence. If each full adder has a gate delay of 2 gates for the carry path, the total delay is 64 gate delays — far too slow for a modern processor that needs to add numbers in a single clock cycle. This is why faster adder designs like carry-lookahead exist: they compute the carries in parallel rather than waiting for the ripple, trading more gates for dramatically less delay.
