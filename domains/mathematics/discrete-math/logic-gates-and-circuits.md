---
id: logic-gates-and-circuits
title: Logic Gates and Combinational Circuits
domain: mathematics
course: discrete-math
prerequisites:
- id: boolean-algebra
  type: hard
tags:
- logic-gates
- AND
- OR
- NOT
- NAND
- XOR
- combinational-circuits
- functional-completeness
stage: formal-systems
status: validated
---

# Logic Gates and Combinational Circuits

## Core Idea
Logic gates are physical realizations of Boolean operations: AND, OR, NOT, NAND, NOR, and XOR. A combinational circuit is a directed acyclic network of gates computing a Boolean function of its inputs with no feedback. Any Boolean function can be implemented using only NAND gates (or only NOR gates), making each set functionally complete — a fact crucial for hardware manufacturing. Circuit design translates a truth table to a Boolean expression, simplifies it to minimize gates, and then maps to a gate network. The half adder and full adder demonstrate how arithmetic emerges from Boolean primitives.

## How It's Best Learned
Design simple circuits — half adder, full adder, 2-to-1 multiplexer — starting from truth tables. Practice both sum-of-products and product-of-sums implementations. Prove NAND universality by constructing NOT, AND, and OR from NAND alone.

## Common Misconceptions
- Confusing combinational circuits (stateless, no memory) with sequential circuits (with feedback and state).
- Thinking you need all gate types — NAND alone suffices to implement any Boolean function.
- Conflating XOR with OR: XOR outputs 1 only when inputs differ; OR outputs 1 when at least one input is 1.
