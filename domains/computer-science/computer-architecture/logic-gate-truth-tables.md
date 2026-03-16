---
id: logic-gate-truth-tables
title: Logic Gates and Truth Tables
domain: computer-science
course: computer-architecture
prerequisites:
- id: boolean-algebra-and-laws
  type: hard
- id: logical-operators-and-gates
  type: hard
builds-toward:
- combinational-logic-implementation
- boolean-function-minimization
tags:
- digital-logic
- gates
- truth-tables
stage: formal-systems
status: draft
---

# Logic Gates and Truth Tables

## Core Idea
Truth tables enumerate all possible input combinations and their corresponding outputs for a logic gate. AND, OR, NOT, XOR, NAND, and NOR gates form the building blocks of digital circuits. Each gate implements a Boolean function and has a defined propagation delay.

## Explainer

You already know that Boolean algebra defines operations like AND, OR, and NOT over binary values, and that logic gates are the physical components that implement these operations. A **truth table** is the bridge between the abstract algebra and the concrete circuit — it exhaustively lists every possible combination of inputs alongside the output the gate produces for each one. For a gate with n inputs, the truth table has 2^n rows, covering every possible binary pattern. This completeness is what makes truth tables so powerful: they leave no ambiguity about how the gate behaves.

Consider the **AND gate** with two inputs, A and B. Its truth table has four rows (00, 01, 10, 11), and the output is 1 only when both A and B are 1. Compare this to the **OR gate**, which outputs 1 when at least one input is 1. The **NOT gate** (inverter) is the simplest — one input, two rows, and the output is always the opposite of the input. These three gates correspond directly to the Boolean operations you studied in Boolean algebra, but now each row of the truth table maps to a real electrical scenario where voltage levels represent 0 and 1.

The gates that prove most useful in practice are often the compound ones. A **NAND gate** is an AND followed by a NOT — its output is 0 only when all inputs are 1, and 1 otherwise. A **NOR gate** is an OR followed by NOT. These are called **universal gates** because any Boolean function can be built using only NAND gates or only NOR gates. The **XOR gate** (exclusive OR) outputs 1 when its inputs differ and 0 when they match, making it essential for arithmetic circuits and parity checking.

To use truth tables in practice, you read them as a specification. If you need a circuit that turns on a warning light when pressure is high AND temperature is high, you write the truth table first — two inputs, one output, and only one row where the output is 1. From there you can identify which gate implements that function (AND), or for more complex functions, combine gates into a circuit. As you move toward combinational logic design and Boolean minimization, truth tables become the starting point: you write the desired behavior as a truth table, then derive the simplest circuit that produces it.
