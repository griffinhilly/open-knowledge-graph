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

## Questions

```yaml
- question: "A circuit must output 1 when exactly one of its two inputs is 1, but output 0 when both are 1 or both are 0. A student proposes using an OR gate. Which truth table row reveals the error?"
  type: multiple-choice
  options:
    - "A=0, B=0 → OR outputs 0, but the circuit should output 0 (no error here)"
    - "A=1, B=1 → OR outputs 1, but the circuit should output 0"
    - "A=0, B=1 → OR outputs 1, but the circuit should output 0"
    - "There is no error — OR is the correct gate for this requirement"
  answer: 1
  explanation: "An OR gate outputs 1 whenever at least one input is 1, including when both inputs are 1. The described function requires output 0 when both are 1 — that's XOR (exclusive OR), not OR. The critical difference between OR and XOR is exactly the A=1, B=1 row: OR outputs 1, XOR outputs 0. Students frequently conflate OR ('at least one') with XOR ('exactly one')."

- question: "A designer needs to implement any arbitrary logic function using only a single type of gate. Which choice or choices make this possible?"
  type: multiple-choice
  options:
    - "AND gates only, since AND is the most fundamental Boolean operation"
    - "AND gates and OR gates together, since these cover the two main operations"
    - "NAND alone, or NOR alone — either is sufficient"
    - "XOR alone, since XOR can simulate other gates through cascading"
  answer: 2
  explanation: "NAND and NOR are each called 'universal gates' because any Boolean function can be implemented using only NAND gates, or only NOR gates. AND alone cannot implement NOT (and thus cannot implement many functions). OR alone is similarly limited. XOR alone cannot implement AND or OR. Universality is what makes NAND and NOR so important in practical digital circuit design — entire chip families are built from a single gate type."

- question: "A logic gate with 3 inputs requires a truth table with 8 rows."
  type: true-false
  answer: true
  explanation: "A truth table must enumerate every possible combination of inputs. With n binary inputs, there are 2^n combinations. For 3 inputs: 2^3 = 8. This completeness is what makes truth tables an exhaustive specification — no input scenario is left ambiguous. For 4 inputs: 16 rows; for 8 inputs: 256 rows."

- question: "An XOR gate with two inputs outputs 1 when both inputs are 1."
  type: true-false
  answer: false
  explanation: "XOR (exclusive OR) outputs 1 when its inputs *differ* and 0 when they *match*. So A=1, B=1 produces output 0 because both inputs are the same. The rows where XOR outputs 1 are A=0,B=1 and A=1,B=0. This differs from OR precisely at the both-inputs-1 case — a subtle but critical distinction for circuits like half-adders and parity checkers."

- question: "What does it mean for a truth table to be an 'exhaustive specification' of a gate's behavior, and why is this property useful when designing circuits from truth tables?"
  type: short-answer
  answer: "Exhaustive means the truth table lists every possible input combination (all 2^n rows for n inputs), leaving no case undefined. This is useful because you can write the desired behavior as a truth table first — specifying exactly what output you want for each input scenario — and then derive a gate circuit that produces it. The truth table becomes the contract between intent and implementation."
  explanation: "Truth tables are the bridge from abstract requirements to concrete circuits. When designing a circuit (say, a warning light that activates under specific sensor combinations), you first write the truth table from the specification, then use Boolean algebra or Karnaugh maps to find the simplest circuit that matches all rows. Because the truth table is complete, if your circuit agrees on every row, it is correct by definition."
```

## Explainer

You already know that Boolean algebra defines operations like AND, OR, and NOT over binary values, and that logic gates are the physical components that implement these operations. A **truth table** is the bridge between the abstract algebra and the concrete circuit — it exhaustively lists every possible combination of inputs alongside the output the gate produces for each one. For a gate with n inputs, the truth table has 2^n rows, covering every possible binary pattern. This completeness is what makes truth tables so powerful: they leave no ambiguity about how the gate behaves.

Consider the **AND gate** with two inputs, A and B. Its truth table has four rows (00, 01, 10, 11), and the output is 1 only when both A and B are 1. Compare this to the **OR gate**, which outputs 1 when at least one input is 1. The **NOT gate** (inverter) is the simplest — one input, two rows, and the output is always the opposite of the input. These three gates correspond directly to the Boolean operations you studied in Boolean algebra, but now each row of the truth table maps to a real electrical scenario where voltage levels represent 0 and 1.

The gates that prove most useful in practice are often the compound ones. A **NAND gate** is an AND followed by a NOT — its output is 0 only when all inputs are 1, and 1 otherwise. A **NOR gate** is an OR followed by NOT. These are called **universal gates** because any Boolean function can be built using only NAND gates or only NOR gates. The **XOR gate** (exclusive OR) outputs 1 when its inputs differ and 0 when they match, making it essential for arithmetic circuits and parity checking.

To use truth tables in practice, you read them as a specification. If you need a circuit that turns on a warning light when pressure is high AND temperature is high, you write the truth table first — two inputs, one output, and only one row where the output is 1. From there you can identify which gate implements that function (AND), or for more complex functions, combine gates into a circuit. As you move toward combinational logic design and Boolean minimization, truth tables become the starting point: you write the desired behavior as a truth table, then derive the simplest circuit that produces it.
