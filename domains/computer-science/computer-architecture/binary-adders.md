---
id: binary-adders
title: 'Binary Adders: Half-Adders and Full-Adders'
domain: computer-science
course: computer-architecture
prerequisites:
- id: boolean-algebra-and-laws
  type: soft
- id: boolean-algebra
  type: soft
- id: binary-arithmetic
  type: soft
builds-toward:
- arithmetic-logic-unit
- fixed-point-number-representation
tags:
- adders
- binary
- arithmetic
stage: formal-systems
status: validated
---

# Binary Adders: Half-Adders and Full-Adders

## Core Idea
Half-adders add two bits without carry-in; full-adders add three bits (two operands plus carry-in). Cascading full-adders creates ripple-carry adders for multi-bit addition, the basis of arithmetic in processors.

## Questions

```yaml
- question: "A half-adder receives inputs A=1 and B=1. What are its Sum and Carry outputs?"
  type: multiple-choice
  options:
    - "Sum=1, Carry=1"
    - "Sum=0, Carry=1"
    - "Sum=1, Carry=0"
    - "Sum=0, Carry=0"
  answer: 1
  explanation: "Sum = A XOR B = 1 XOR 1 = 0; Carry = A AND B = 1 AND 1 = 1. This mirrors binary arithmetic: 1 + 1 = 10 in binary, which is sum bit 0 with a carry of 1. The XOR gate produces 1 when inputs differ (which is false when both are 1), and the AND gate produces 1 only when both inputs are 1. Option A (Sum=1, Carry=1) is the most common wrong answer — students mistakenly apply OR logic to the sum."

- question: "What is the fundamental performance limitation of a 64-bit ripple-carry adder?"
  type: multiple-choice
  options:
    - "The carry-out of the most significant bit cannot be computed until the carry has propagated sequentially through all 64 stages"
    - "The XOR gates used for sum bits are inherently slower than the AND gates used for carry bits"
    - "Each full-adder must read both 64-bit operands simultaneously, creating a memory bottleneck"
    - "The half-adder at bit position 0 introduces a one-stage delay that compounds across the chain"
  answer: 0
  explanation: "In a ripple-carry adder, each stage's carry-out feeds into the next stage's carry-in. Stage n-1 cannot produce its final sum until it receives the carry from stage n-2, which can't compute until it receives from n-3, and so on all the way back to stage 0. This sequential dependency means the total delay grows linearly with bit width — 64 gate delays in series. This is why carry-lookahead and carry-select adders were developed: they break the sequential dependency by computing carries in parallel."

- question: "A full-adder with inputs A=1, B=0, Cin=1 produces a carry-out of 1."
  type: true-false
  answer: true
  explanation: "Cout = 1 if two or more of the three inputs are 1. Here A=1 and Cin=1 (two inputs are 1), so Cout=1. The Sum = A XOR B XOR Cin = 1 XOR 0 XOR 1 = 0, giving a full result of 10 in binary (sum=0, carry=1). Equivalently: 1 + 0 + 1 = 2 = 10₂."

- question: "In a multi-bit ripple-carry adder, a half-adder can be used at every bit position because all bit positions have the same inputs."
  type: true-false
  answer: false
  explanation: "A half-adder only accepts two inputs (A and B) and cannot accept a carry-in. Only the least significant bit position (bit 0) has no carry-in (or a carry-in fixed at 0), so a half-adder is valid there. Every other bit position must receive the carry-out from the previous stage, requiring a full-adder with three inputs (A, B, Cin). Using a half-adder at bit position 1 or higher would silently discard the carry, producing wrong results for any addition that generates a carry from lower bits."

- question: "Explain why a full-adder is necessary for multi-bit addition, and why the ripple-carry adder becomes slower as the number of bits increases."
  type: short-answer
  answer: "A full-adder is necessary because every column beyond the least significant one must accept a carry from the column to its right. A half-adder has no carry-in input, so it can only add two bits — it cannot account for the carry produced by the previous column. The full-adder's three inputs (A, B, Cin) allow it to handle this. In a ripple-carry adder, the carry-out of each stage feeds into the carry-in of the next stage sequentially. The most significant bit's result depends on the carry propagating through every preceding stage. With n stages each introducing a gate delay, the worst-case propagation time grows linearly with n — a 64-bit adder is 64 times slower than a 1-bit adder."
  explanation: "The sequential carry dependency is the root cause of ripple-carry's speed limitation. Carry-lookahead adders solve this by pre-computing whether each stage will 'generate' or 'propagate' a carry, enabling parallel carry computation. But the ripple-carry design remains the conceptual baseline because it directly maps the paper algorithm to hardware."
```

## Explainer

You already know how binary arithmetic works on paper — adding columns of 1s and 0s, carrying a 1 when a column sums to 2 or 3. Binary adder circuits do exactly this in hardware, and they are built from the Boolean logic gates you studied in Boolean algebra. The simplest building block is the **half-adder**, which adds two single-bit inputs (A and B) and produces two outputs: a **sum** bit and a **carry** bit. The sum is A XOR B (1 when the inputs differ), and the carry is A AND B (1 only when both inputs are 1). This mirrors the paper algorithm perfectly: 0+0=00, 0+1=01, 1+0=01, 1+1=10.

The half-adder has a limitation: it has no input for an incoming carry from a previous column. When you add multi-bit numbers, every column beyond the least significant one must handle a carry-in from the column to its right. The **full-adder** solves this by accepting three inputs: A, B, and a carry-in (Cin). It produces a sum bit (A XOR B XOR Cin) and a carry-out (Cout). You can build a full-adder from two half-adders and an OR gate: the first half-adder adds A and B, the second adds that result to Cin, and the OR gate combines both carry outputs. This modularity — building complex circuits from simpler ones — is a recurring pattern in digital design.

To add two *n*-bit numbers, you chain *n* full-adders together in a **ripple-carry adder**. The carry-out of bit position 0 feeds into the carry-in of bit position 1, which feeds into bit position 2, and so on — the carry "ripples" through the chain. The least significant bit can use a half-adder (or a full-adder with Cin tied to 0). This design is simple and correct, but it has a speed problem: bit position *n*-1 cannot compute its final sum until the carry has propagated through all *n*-1 preceding stages. Each stage adds a small gate delay, and for a 64-bit adder, that delay accumulates.

This propagation delay is why faster adder designs exist — carry-lookahead adders compute carries in parallel rather than sequentially, and carry-select adders speculatively compute both possible results (carry=0 and carry=1) and select the correct one. But the ripple-carry adder remains the conceptual foundation: it makes the connection between the binary arithmetic you do on paper and the physical gates that execute it in silicon, and every more advanced adder design is ultimately an optimization of the same underlying addition algorithm.
