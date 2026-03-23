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
status: validated
---

# Full Adder Circuit Design

## Core Idea
A full adder adds two bits plus a carry-in, producing sum and carry-out. Composed of two half adders and an OR gate, full adders cascade to form multi-bit adders.

## Questions

```yaml
- question: "A full adder receives inputs A=1, B=1, C_in=1. What are the correct sum and carry-out outputs?"
  type: multiple-choice
  options:
    - "Sum=0, Carry-out=0"
    - "Sum=1, Carry-out=0"
    - "Sum=0, Carry-out=1"
    - "Sum=1, Carry-out=1"
  answer: 3
  explanation: "Three 1-bit inputs each equal to 1 sum to decimal 3, which is binary 11 — so sum=1 and carry-out=1. Tracing through the circuit: the first half adder computes 1+1, giving partial sum=0 and partial carry=1. The second half adder computes 0+1 (partial sum + C_in), giving final sum=1 and second carry=0. The carry-out is partial_carry1 OR carry2 = 1 OR 0 = 1. Result: sum=1, carry-out=1."

- question: "Why does a full adder use an OR gate (not AND, XOR, or NAND) to combine the two partial carry signals?"
  type: multiple-choice
  options:
    - "Because OR has the lowest propagation delay among all gate types"
    - "Because a carry-out is generated whenever *either* partial carry is 1, and both cannot be 1 simultaneously"
    - "Because AND would only produce a carry when both partial carries are 1, which never happens"
    - "Because the two partial carries always have opposite values, so OR selects the non-zero one"
  answer: 1
  explanation: "A carry-out must be generated if *either* half-adder stage produced a carry — that's an OR condition. Crucially, both partial carries cannot be 1 simultaneously: the first half adder carries when A=1 and B=1, giving partial sum=0; the second then adds 0 + C_in, which cannot carry unless C_in=1 — but if the first half adder carries and C_in=1, the second gets 0+1=1, no carry. The OR gate is correct because this mutual exclusion means OR and XOR would give identical results here, but OR is the logically meaningful choice."

- question: "A full adder can be constructed from two half adders and one OR gate."
  type: true-false
  answer: true
  explanation: "This is the standard construction. The first half adder takes A and B as inputs and produces a partial sum and partial carry. The second half adder takes the partial sum and C_in, producing the final sum bit and a second partial carry. The OR gate combines both partial carries to produce the final carry-out. Since both partial carries cannot be 1 simultaneously, OR correctly implements the carry-out logic."

- question: "A half adder is sufficient for every bit position in a multi-bit ripple carry adder."
  type: true-false
  answer: false
  explanation: "A half adder handles only two inputs (A and B) with no carry-in. It can only be used for the least significant bit position, where there is no incoming carry. Every other bit position receives a carry-out from the previous stage as a third input. For these positions, a full adder — which accepts A, B, and C_in — is required. This is why multi-bit adders are built from n full adders (with the first stage's carry-in tied to 0), not from half adders."

- question: "In the two-half-adder construction of a full adder, why is it impossible for both partial carries to equal 1 at the same time?"
  type: short-answer
  answer: "The first half adder computes A + B. If it generates a carry (A=1, B=1), the partial sum is 0. The second half adder then adds 0 + C_in — which produces at most a sum of 1 with no carry. If the first half adder does not generate a carry, the partial sum is A XOR B (0 or 1); the second half adder can only carry if both its inputs are 1, which requires the partial sum to be 1 *and* C_in to be 1. In no case can both stages simultaneously generate carries, because the maximum value of A + B + C_in with each 0 or 1 is 3 (binary 11) — one sum bit and one carry bit, never two carries."
  explanation: "Formally: the maximum sum of three single-bit values is 3, representable as one sum bit and one carry-out bit. Two carry bits would require a sum of 4 or more, which is impossible with three single-bit inputs. The OR gate correctly captures the carry-out, and the mutual exclusion guarantees OR produces the right answer."
```

## Explainer

You already know the half adder — it takes two single-bit inputs (A and B) and produces a sum bit and a carry bit. The half adder works perfectly for the least significant bit of a multi-bit addition, where there's no incoming carry. But for every other bit position, there are three inputs to consider: the two bits being added *plus* a carry-in from the previous position. This is exactly what a **full adder** handles: it computes the sum of three single-bit values (A, B, and C_in) and produces both a **sum** output and a **carry-out**.

The elegant construction uses two half adders chained together. The first half adder adds A and B, producing a partial sum and a partial carry. The second half adder adds that partial sum to C_in, producing the final sum bit and another partial carry. The final carry-out is the OR of the two partial carries — a carry is generated if either the first addition (A + B) produced a carry, or the second addition (partial sum + C_in) produced one. It's impossible for both to generate carries simultaneously (that would require a sum of 4 in binary, which can't happen with three single-bit inputs), so OR correctly combines them.

To verify the logic, trace through the case A=1, B=1, C_in=1. The first half adder computes 1+1: sum=0, carry=1. The second half adder computes 0+1 (partial sum plus carry-in): sum=1, carry=0. The final carry-out is 1 OR 0 = 1. The result is sum=1, carry=1, representing the binary value 11 — which is decimal 3, the correct sum of three 1s.

The real power of the full adder is **cascading**. To build an n-bit adder, you chain n full adders together, connecting each stage's carry-out to the next stage's carry-in. The least significant bit can use either a half adder or a full adder with C_in tied to 0. This structure — called a **ripple carry adder** — directly mirrors how you do long addition by hand: add each column, write down the digit, carry the 1 to the next column. The limitation is speed — each bit position must wait for the carry from the previous position — but the full adder itself is the fundamental arithmetic building block from which all more sophisticated adder designs (carry lookahead, carry select, carry save) are constructed.
