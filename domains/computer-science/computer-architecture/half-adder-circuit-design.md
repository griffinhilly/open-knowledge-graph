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
builds-toward:
- full-adder-circuit-design
tags:
- adder
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Half Adder Circuit Design

## Core Idea
A half adder adds two single bits, producing sum (via XOR) and carry (via AND). It lacks a carry-in input, limiting use to the least significant bit of multi-bit addition.

## Explainer

You already know how individual logic gates — AND, OR, XOR — work, and specifically that XOR outputs 1 when its inputs differ. The **half adder** is your first encounter with combining gates into a circuit that performs arithmetic, and it is satisfyingly minimal: just two gates that add two single-bit numbers.

Start from the truth table for single-bit addition. When you add A and B, there are four cases: 0+0=00, 0+1=01, 1+0=01, and 1+1=10 (writing the result as a two-bit number: carry and sum). Look at the sum column: it is 1 exactly when A and B differ — that is the XOR function. Look at the carry column: it is 1 exactly when both A and B are 1 — that is the AND function. So the entire half adder is one XOR gate producing the **sum bit** and one AND gate producing the **carry bit**. Two gates, two inputs, two outputs, and you have performed binary addition.

The name "half" adder reflects its limitation: it handles only two inputs, with no provision for a **carry-in** from a previous column. When you add multi-bit numbers column by column, every column except the rightmost must account for a possible carry from the column to its right. A half adder cannot do this — it would need a third input. This is exactly the gap that the **full adder** fills by accepting A, B, and a carry-in. You can think of a full adder as two half adders connected in series: the first adds A and B, the second adds that partial sum to the carry-in, and an OR gate combines the two carry outputs. The half adder is therefore the conceptual and literal building block of all binary addition hardware — too limited to do the whole job on its own, but essential as the component from which more capable adders are composed.
