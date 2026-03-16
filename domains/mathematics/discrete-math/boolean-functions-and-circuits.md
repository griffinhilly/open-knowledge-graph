---
id: boolean-functions-and-circuits
title: Boolean Functions, Logic Gates, and Digital Circuits
domain: mathematics
course: discrete-math
prerequisites:
- id: boolean-algebra
  type: hard
builds-toward:
- algorithm-complexity-discrete
tags:
- Boolean-functions
- logic-gates
- circuits
- DNF-CNF
stage: formal-systems
status: draft
---

# Boolean Functions, Logic Gates, and Digital Circuits

## Core Idea
A Boolean function f: {0,1}ⁿ → {0,1} is computed by a logic circuit using AND, OR, NOT gates. Every Boolean function can be expressed in disjunctive normal form (DNF) or conjunctive normal form (CNF). Circuit complexity measures the minimum gates or depth needed.

## How It's Best Learned
Build truth tables for Boolean functions. Express functions in DNF (OR of ANDs) and CNF (AND of ORs). Apply Boolean algebra identities to simplify circuits. Design circuits for arithmetic (adders, multipliers).

## Common Misconceptions
DNF and CNF are normal forms, not canonical until further specified. A Boolean function can have multiple minimal representations. Circuit complexity depends on depth and gate count—it's not unique.

## Explainer

A Boolean function takes n binary inputs (each 0 or 1) and produces a single binary output. You've already learned Boolean algebra — the rules governing AND, OR, and NOT on individual values. A Boolean function simply extends this systematically: for all 2ⁿ possible input combinations, it specifies the output for each one. A **truth table** is the most direct definition of any Boolean function — list all 2ⁿ rows and record the output for each.

The connection to circuits is direct: any Boolean function can be computed by wiring AND, OR, and NOT gates together. The systematic translation uses **Disjunctive Normal Form (DNF)** — also called sum-of-products. Identify every row of the truth table where the output is 1. For each such row, write an AND term (a "minterm") that is satisfied only by that exact input combination. Then OR all those terms together. For example, if f(x,y,z) = 1 only when (x=1, y=0, z=1), the DNF minterm is (x ∧ ¬y ∧ z). **Conjunctive Normal Form (CNF)** — product-of-sums — works dually: identify all rows where the output is 0 and write OR terms (maxterms) that exclude those combinations, then AND everything together.

DNF and CNF guarantee that every Boolean function has a circuit representation — a completeness result. But the circuits produced this way can be large and redundant. The Boolean algebra identities you already know let you simplify: (x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ z) simplifies to (¬y ∧ z) by factoring out ¬y ∧ z. **Circuit complexity** measures how efficient a circuit can be — specifically, the minimum number of gates (circuit size) or the fewest gate-layers from inputs to output (circuit depth). Different circuits can compute the same function, so there is no single canonical representation; the interesting question is how small the optimal circuit is.

The most instructive design exercise is building a circuit for addition. A **half adder** adds two 1-bit inputs: the sum bit is XOR(A,B) (the inputs differ) and the carry bit is AND(A,B) (both are 1). A **full adder** takes three bits — two inputs plus a carry-in — and produces a sum and carry-out. Chain n full adders together and you have a circuit that adds two n-bit binary numbers — the same operation a CPU performs billions of times per second. This shows how the abstract machinery of Boolean functions and normal forms connects directly to the arithmetic hardware at the heart of every computer.
