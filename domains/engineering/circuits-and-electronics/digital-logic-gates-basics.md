---
id: digital-logic-gates-basics
title: Digital Logic Gates Basics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: mosfet-transistor-fundamentals
  type: hard
builds-toward:
- adc-dac-fundamentals
tags:
- logic-gates
- AND
- OR
- NOT
- NAND
- NOR
- CMOS
- truth-table
- boolean-algebra
- inverter
stage: abstract-reasoning
status: draft
---

# Digital Logic Gates Basics

## Core Idea
Digital logic gates implement Boolean functions in hardware, mapping binary input voltages (HIGH/LOW) to binary outputs. The fundamental gates are NOT (inverter), AND, and OR, from which all other logic functions can be constructed. In CMOS technology, gates are built from complementary pairs of NMOS and PMOS transistors: a CMOS inverter uses one NMOS (pull-down, conducts when input is HIGH) and one PMOS (pull-up, conducts when input is LOW), ensuring that one transistor is always off so no static current flows — the key advantage of CMOS over earlier technologies. NAND and NOR gates are the universal gates: any Boolean function can be implemented using only NAND gates (or only NOR gates). A CMOS NAND gate uses series NMOS transistors in the pull-down network and parallel PMOS transistors in the pull-up network; a CMOS NOR gate reverses this arrangement. Truth tables define the input-output mapping for each gate, and Boolean algebra (De Morgan's theorems, distributive/associative laws) enables simplification of logic expressions. The voltage transfer characteristic of a CMOS inverter shows the sharp transition between output HIGH and LOW, with noise margins defined by the voltage thresholds V_IL, V_IH, V_OL, and V_OH.

## How It's Best Learned
Build a CMOS inverter from one NMOS and one PMOS transistor and trace the current path for each input state. Verify that exactly one transistor is on at a time. Extend to NAND and NOR by reasoning about series versus parallel combinations in pull-up and pull-down networks. Construct truth tables for each gate, then use De Morgan's theorems to show that NAND and NOR are universal.

## Common Misconceptions
- Thinking AND and OR are the most fundamental gates in hardware — NAND and NOR are actually simpler to implement in CMOS (fewer transistors for basic functions) and are the building blocks from which AND and OR are constructed (by adding an inverter).
- Assuming digital signals are truly binary — real signals have finite rise/fall times, noise margins, and undefined regions between logic levels; understanding the analog behavior of the CMOS inverter transfer curve is essential.
- Confusing NMOS and PMOS roles — NMOS transistors are used in pull-down networks (connecting output to ground) and PMOS in pull-up networks (connecting output to V_DD); reversing them does not produce correct logic levels due to threshold voltage drops.
