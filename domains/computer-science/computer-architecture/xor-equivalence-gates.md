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

## Questions

```yaml
- question: "Two 4-bit binary numbers, 1010 and 1011, are compared bit-by-bit using XOR gates. What is the 4-bit XOR output?"
  type: multiple-choice
  options:
    - "1111 — XOR outputs 1 for every bit in the first number"
    - "0001 — only the least significant bits differ"
    - "0000 — the two numbers are equal"
    - "1010 — XOR passes the first number through unchanged"
  answer: 1
  explanation: "XOR outputs 1 only when the corresponding bits *differ*. Comparing position by position: 1⊕1=0, 0⊕0=0, 1⊕1=0, 0⊕1=1. So the output is 0001 — only the last bit differs. This is exactly how equality comparators are built: XOR all corresponding bit pairs; if any output is 1, the numbers differ at that position. The result 0000 would mean the numbers are identical."

- question: "In a half-adder computing 1 + 1, the XOR gate produces the sum bit. What is that sum bit, and why is XOR the correct gate rather than OR?"
  type: multiple-choice
  options:
    - "Sum = 1, because OR(1,1) = 1 and addition gives a nonzero result"
    - "Sum = 0, because binary addition of 1 + 1 = 10₂ (zero with carry 1), and XOR(1,1) = 0"
    - "Sum = 2, because 1 + 1 = 2 in decimal"
    - "Sum = 1, because both inputs are 1 and the output should reflect that"
  answer: 1
  explanation: "Binary addition modulo 2: 1 + 1 = 0 (with a carry of 1 into the next column). XOR correctly computes this: XOR(1,1) = 0, matching the sum bit. OR gives OR(1,1) = 1, which is wrong. This reveals the deep connection between XOR and binary arithmetic: XOR *is* addition modulo 2, which is precisely what the sum bit of binary addition computes. The carry bit is handled separately by an AND gate."

- question: "XOR and OR produce the same output for every possible combination of two binary inputs."
  type: true-false
  answer: false
  explanation: "XOR and OR differ on exactly one input combination: when both inputs are 1. OR(1,1) = 1, but XOR(1,1) = 0. XOR is 'exclusive' OR — it outputs 1 only when *exactly one* input is 1, not when both are 1. This single difference makes XOR fundamentally different from OR: it detects when inputs differ, while OR detects when at least one input is 1."

- question: "XOR-ing any value with itself always produces 0, regardless of what that value is."
  type: true-false
  answer: true
  explanation: "A ⊕ A = 0 for any bit value A. If A = 0: 0 ⊕ 0 = 0. If A = 1: 1 ⊕ 1 = 0. This self-inverting property is fundamental to XOR's usefulness: it means 'comparing a value against itself' always yields 0 (no difference). This property underlies parity checking (XOR all bits together to detect whether the count of 1s is odd or even) and is also used in cryptography and hash functions."

- question: "Explain why XOR is the correct gate for the sum bit of a half-adder, connecting this to what XOR fundamentally computes."
  type: short-answer
  answer: "XOR computes addition modulo 2 — it produces 1 when exactly one input is 1, and 0 when both inputs match (both 0 or both 1). Binary single-bit addition follows the same rule: 0+0=0, 0+1=1, 1+0=1, and 1+1=0 (with a carry). The sum bit is always the XOR of the two operands. OR would be wrong because OR(1,1)=1, but the sum bit of 1+1 is 0. XOR captures the 'different-ness' that binary addition measures at each bit position, while the carry (AND gate) handles the overflow."
  explanation: "This connection is not coincidental — XOR is literally the definition of addition in GF(2) (the two-element field), the algebraic structure underlying binary arithmetic. Understanding this makes XOR's appearance in adders, checksums, error-correcting codes, and cryptographic operations all fit together as instances of the same operation."
```

## Explainer

You already know the basic logic gates — AND, OR, NOT, NAND, NOR — and how they combine inputs to produce outputs according to truth tables. **XOR** (exclusive OR) and **XNOR** (exclusive NOR) extend this family with a behavior that none of the basic gates provide: detecting whether two inputs are the same or different.

The **XOR gate** outputs 1 when its inputs *differ* — specifically, when exactly one input is 1. For two inputs A and B: XOR outputs 1 when A=0,B=1 or A=1,B=0, and outputs 0 when both inputs match (both 0 or both 1). In Boolean algebra, this is written as A ⊕ B, and it can be decomposed into basic gates as A·B' + A'·B. Think of XOR as answering the question "are these two bits different?" This makes it indispensable for **comparison circuits**: to check whether two multi-bit numbers are equal, you XOR corresponding bits — if any XOR output is 1, the numbers differ at that position.

The **XNOR gate** is simply the complement of XOR: it outputs 1 when the inputs are the *same*. XNOR implements **logical equivalence** — the operation that tests whether A and B have the same truth value. In Boolean algebra, A ⊙ B = A·B + A'·B'. You can think of XNOR as answering "are these two bits equal?" Every XOR output inverted is an XNOR output, so the two gates always appear as a complementary pair.

Beyond comparison, XOR has several properties that make it uniquely useful in digital design. It is **self-inverting**: A ⊕ A = 0 (any value XORed with itself is 0) and A ⊕ 0 = A (XORing with 0 preserves the value). This makes XOR the core of **parity checking** — XOR all the bits together, and the result tells you whether the total number of 1s is odd (result=1) or even (result=0). Error detection codes like parity bits rely on this directly. XOR also appears in **binary addition**: the sum bit of a half-adder is exactly A ⊕ B, because 0+0=0, 0+1=1, 1+0=1, and 1+1=0 (with a carry). This connection between XOR and addition is not a coincidence — addition modulo 2 is precisely the XOR operation. You will see XOR appear repeatedly as you move into more complex combinational circuits, from adders to checksums to cryptographic building blocks.
