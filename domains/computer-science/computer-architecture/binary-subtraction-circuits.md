---
id: binary-subtraction-circuits
title: Binary Subtraction Using Two's Complement
domain: computer-science
course: computer-architecture
prerequisites:
- id: twos-complement
  type: hard
- id: full-adder-circuit-design
  type: hard
tags:
- subtraction
- arithmetic-circuits
stage: formal-systems
status: draft
---

# Binary Subtraction Using Two's Complement

## Core Idea
Subtraction is implemented by negating the subtrahend (inverting bits and adding 1) then adding. This unifies subtraction and addition in hardware, requiring only one arithmetic unit.

## Explainer

From your study of two's complement, you know that negating a binary number means inverting all its bits and adding 1. And from full adder circuit design, you know how to build hardware that adds two n-bit numbers with a carry-in. Binary subtraction circuits exploit a beautiful connection between these two ideas: **A − B is the same as A + (−B)**, and since −B in two's complement is ~B + 1, subtraction becomes A + ~B + 1. This means you can perform subtraction using the same adder you already have — you just need to invert B and set the carry-in to 1.

The hardware implementation is elegant in its simplicity. Each bit of the subtrahend B passes through a **controlled inverter** — typically an XOR gate with a control signal called SUB. When SUB = 0 (addition mode), the XOR gate passes B through unchanged. When SUB = 1 (subtraction mode), the XOR gate flips every bit of B, producing ~B. The same SUB signal is wired to the carry-in of the least significant full adder, providing the +1 needed to complete the two's complement negation. The result is a single circuit — an **adder-subtractor** — that performs addition when SUB = 0 and subtraction when SUB = 1, with no additional arithmetic hardware.

This unification is why virtually every processor has a single arithmetic unit for both addition and subtraction rather than separate circuits. It also extends naturally to detecting overflow: in two's complement, overflow occurs when the carry into the most significant bit differs from the carry out of it. The adder-subtractor can check this condition with a single XOR gate on those two carry signals. Understanding this design also clarifies why two's complement is the universal choice for signed integer representation in hardware — it is the only signed number system where subtraction reduces to addition with bit inversion, keeping the circuit simple and fast.
