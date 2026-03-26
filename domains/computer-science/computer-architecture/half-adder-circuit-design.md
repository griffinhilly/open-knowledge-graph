---
id: half-adder-circuit-design
title: Half Adder Circuit Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: xor-equivalence-gates
  type: hard
- id: logic-gates-fundamentals
  type: hard
- id: carry-lookahead-adder-design
  type: soft
builds-toward:
- full-adder-and-carry-logic
tags:
- adder
- arithmetic-circuits
stage: formal-systems
status: validated
---
# Half Adder Circuit Design

## Core Idea
A half adder adds two single bits, producing sum (via XOR) and carry (via AND). It lacks a carry-in input, limiting use to the least significant bit of multi-bit addition.

## Questions

```yaml
- question: "A half adder receives inputs A=1 and B=1. What are the sum and carry outputs?"
  type: multiple-choice
  options:
    - "Sum=0, Carry=1"
    - "Sum=1, Carry=0"
    - "Sum=1, Carry=1"
    - "Sum=0, Carry=0"
  answer: 0
  explanation: "1+1 in binary equals 10 (decimal 2): a sum bit of 0 and a carry bit of 1. The XOR gate (sum) outputs 0 when both inputs are identical; the AND gate (carry) outputs 1 when both inputs are 1. This is the one case where the carry is generated."

- question: "Why can't half adders alone be chained to build a multi-bit binary adder?"
  type: multiple-choice
  options:
    - "Because XOR gates cannot be cascaded in sequence"
    - "Because a half adder has no carry-in input to accept a carry from the previous bit position"
    - "Because a half adder produces two outputs, which confuses downstream gates"
    - "Because AND gates are too slow for multi-bit arithmetic"
  answer: 1
  explanation: "Every bit position beyond the least significant must handle a potential carry arriving from the column to its right. A half adder only accepts two inputs (A and B) — it has nowhere to plug in an incoming carry. The full adder solves this by adding a third input (carry-in), allowing it to be placed in any bit position. The half adder can only correctly handle the rightmost bit, where there is no prior carry."

- question: "In a half adder, the XOR gate produces the carry bit and the AND gate produces the sum bit."
  type: true-false
  answer: false
  explanation: "The assignments are reversed. The XOR gate produces the sum bit — it outputs 1 exactly when the two inputs differ (one 1 and one 0), which matches the sum column of the addition truth table. The AND gate produces the carry bit — it outputs 1 only when both inputs are 1, which is the only case where a carry is generated (1+1=10)."

- question: "A half adder is sufficient for the second-least-significant bit position (bit 1) of a multi-bit adder, since carries primarily propagate from that position forward."
  type: true-false
  answer: false
  explanation: "Bit position 1 must accept a possible carry-out from bit position 0. A half adder has no carry-in input, so it cannot incorporate that carry — it would silently drop it, producing wrong results. Only the least significant bit (bit 0) can use a half adder; all higher positions require full adders that accept carry-in."

- question: "Why does XOR implement the sum bit and AND implement the carry bit in a half adder? Explain in terms of what each gate computes."
  type: short-answer
  answer: "XOR outputs 1 when its inputs differ — exactly when one input is 1 and the other is 0, giving a sum of 1 with no carry. AND outputs 1 only when both inputs are 1, the case that produces a sum of 0 and a carry of 1. Together they replicate the complete truth table for 1-bit binary addition: 0+0=00, 0+1=01, 1+0=01, 1+1=10."
  explanation: "The elegance of the half adder is that the truth tables of XOR and AND perfectly match the two output columns (sum, carry) of single-bit binary addition. No complex logic is needed — the arithmetic structure and the gate structure coincide exactly. This mapping is why single-bit addition requires only two gates and is the foundational building block from which all larger adder circuits are constructed."
```

## Explainer

You already know how individual logic gates — AND, OR, XOR — work, and specifically that XOR outputs 1 when its inputs differ. The **half adder** is your first encounter with combining gates into a circuit that performs arithmetic, and it is satisfyingly minimal: just two gates that add two single-bit numbers.

Start from the truth table for single-bit addition. When you add A and B, there are four cases: 0+0=00, 0+1=01, 1+0=01, and 1+1=10 (writing the result as a two-bit number: carry and sum). Look at the sum column: it is 1 exactly when A and B differ — that is the XOR function. Look at the carry column: it is 1 exactly when both A and B are 1 — that is the AND function. So the entire half adder is one XOR gate producing the **sum bit** and one AND gate producing the **carry bit**. Two gates, two inputs, two outputs, and you have performed binary addition.

The name "half" adder reflects its limitation: it handles only two inputs, with no provision for a **carry-in** from a previous column. When you add multi-bit numbers column by column, every column except the rightmost must account for a possible carry from the column to its right. A half adder cannot do this — it would need a third input. This is exactly the gap that the **full adder** fills by accepting A, B, and a carry-in. You can think of a full adder as two half adders connected in series: the first adds A and B, the second adds that partial sum to the carry-in, and an OR gate combines the two carry outputs. The half adder is therefore the conceptual and literal building block of all binary addition hardware — too limited to do the whole job on its own, but essential as the component from which more capable adders are composed.
