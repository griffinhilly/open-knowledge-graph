---
id: logic-gates-fundamentals
title: Logic Gates Fundamentals
domain: computer-science
course: computer-architecture
prerequisites:
- id: boolean-algebra-and-laws
  type: soft
- id: boolean-algebra
  type: soft
builds-toward:
- boolean-function-implementation
- combinational-circuit-design
tags:
- gates
- digital-logic
- fundamentals
stage: formal-systems
status: draft
---

# Logic Gates Fundamentals

## Core Idea
Logic gates implement basic Boolean operations: AND (true when all inputs are true), OR (true when any input is true), and NOT (inverts input). These three gates form the foundation for all digital circuits.

## Explainer

From Boolean algebra, you already know that logical expressions can be built from AND, OR, and NOT operations. Logic gates are the physical realization of these operations — tiny electronic circuits that take one or more binary inputs (high voltage = 1, low voltage = 0) and produce a binary output according to a fixed rule. The jump from abstract algebra to physical hardware happens here: every Boolean expression you can write corresponds directly to a circuit you can build from gates.

The three fundamental gates are **AND**, **OR**, and **NOT**. An AND gate outputs 1 only when *all* its inputs are 1 — think of it as two switches wired in series, where both must be closed for current to flow. An OR gate outputs 1 when *any* input is 1 — like two switches in parallel, where either one lets current through. A NOT gate (also called an **inverter**) has a single input and flips it: 0 becomes 1, 1 becomes 0. These three operations are **functionally complete**, meaning any Boolean function, no matter how complex, can be built using only these gates.

In practice, two derived gates appear constantly: **NAND** (AND followed by NOT) and **NOR** (OR followed by NOT). Each of these is individually functionally complete — you can build AND, OR, and NOT gates entirely from NAND gates alone, or entirely from NOR gates alone. This matters for manufacturing because chip fabricators can standardize on a single gate type. Two other common gates are **XOR** (exclusive OR, which outputs 1 when inputs differ) and **XNOR** (outputs 1 when inputs match). XOR is particularly important in arithmetic circuits because it captures the behavior of binary addition without the carry.

Each gate's behavior is fully specified by its **truth table**, which lists every possible input combination and the corresponding output. For a 2-input AND gate, the truth table has four rows (00→0, 01→0, 10→0, 11→1). As you connect gates together, the truth table of the combined circuit grows exponentially — an n-input circuit has 2^n rows. This is exactly why Boolean algebra's simplification laws matter: they let you reduce complex expressions before building them in hardware, using fewer gates, less power, and less chip area. The bridge between Boolean algebra on paper and working digital circuits runs directly through these gates.
