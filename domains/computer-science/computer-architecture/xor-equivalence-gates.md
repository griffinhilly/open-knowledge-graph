---
id: xor-equivalence-gates
title: XOR and XNOR Gates
domain: computer-science
course: computer-architecture
prerequisites:
- id: logic-gates-fundamentals
  type: hard
builds-toward:
- boolean-function-implementation
tags:
- gates
- xor
- comparison
stage: formal-systems
status: draft
---

# XOR and XNOR Gates

## Core Idea
XOR outputs true when inputs differ; XNOR outputs true when inputs are equal. XOR is essential for comparators and parity checking, while XNOR implements logical equivalence.

## Explainer

You already know the basic logic gates — AND, OR, NOT, NAND, NOR — and how they combine inputs to produce outputs according to truth tables. **XOR** (exclusive OR) and **XNOR** (exclusive NOR) extend this family with a behavior that none of the basic gates provide: detecting whether two inputs are the same or different.

The **XOR gate** outputs 1 when its inputs *differ* — specifically, when exactly one input is 1. For two inputs A and B: XOR outputs 1 when A=0,B=1 or A=1,B=0, and outputs 0 when both inputs match (both 0 or both 1). In Boolean algebra, this is written as A ⊕ B, and it can be decomposed into basic gates as A·B' + A'·B. Think of XOR as answering the question "are these two bits different?" This makes it indispensable for **comparison circuits**: to check whether two multi-bit numbers are equal, you XOR corresponding bits — if any XOR output is 1, the numbers differ at that position.

The **XNOR gate** is simply the complement of XOR: it outputs 1 when the inputs are the *same*. XNOR implements **logical equivalence** — the operation that tests whether A and B have the same truth value. In Boolean algebra, A ⊙ B = A·B + A'·B'. You can think of XNOR as answering "are these two bits equal?" Every XOR output inverted is an XNOR output, so the two gates always appear as a complementary pair.

Beyond comparison, XOR has several properties that make it uniquely useful in digital design. It is **self-inverting**: A ⊕ A = 0 (any value XORed with itself is 0) and A ⊕ 0 = A (XORing with 0 preserves the value). This makes XOR the core of **parity checking** — XOR all the bits together, and the result tells you whether the total number of 1s is odd (result=1) or even (result=0). Error detection codes like parity bits rely on this directly. XOR also appears in **binary addition**: the sum bit of a half-adder is exactly A ⊕ B, because 0+0=0, 0+1=1, 1+0=1, and 1+1=0 (with a carry). This connection between XOR and addition is not a coincidence — addition modulo 2 is precisely the XOR operation. You will see XOR appear repeatedly as you move into more complex combinational circuits, from adders to checksums to cryptographic building blocks.
