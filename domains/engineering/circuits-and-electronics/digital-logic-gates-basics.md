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

## Explainer

From your study of MOSFETs, you know that a transistor is a voltage-controlled switch: the gate voltage determines whether the channel conducts (ON) or blocks (OFF). **Digital logic gates** exploit this directly. Instead of operating MOSFETs in continuous voltage ranges as amplifiers, digital design snaps them to one of two states: HIGH (close to V_DD, representing logical 1) and LOW (close to ground, representing logical 0). The entire goal is to process discrete binary information using transistors as switches.

The simplest gate is the **NOT gate (inverter)**: input HIGH → output LOW; input LOW → output HIGH. A CMOS inverter uses exactly two transistors in a complementary pair. The NMOS transistor connects the output to ground and conducts when the input is HIGH (pulling the output LOW). The PMOS transistor connects the output to V_DD and conducts when the input is LOW (pulling the output HIGH). Since exactly one is always ON and the other always OFF, the output is always driven strongly to either V_DD or ground, with no static current path between them. This complementary design—CMOS stands for Complementary MOS—is why modern chips can contain billions of transistors without melting: they draw significant current only during switching transitions, not while holding a steady state.

**NAND and NOR gates** extend this logic to multiple inputs. A **NAND gate** produces LOW only when all inputs are HIGH (it is the complement of AND). In CMOS, the pull-down network places NMOS transistors in *series*—all must be ON simultaneously to pull the output to ground—while the pull-up network places PMOS transistors in *parallel*—any one being ON pulls the output to V_DD. A **NOR gate** reverses this arrangement: NMOS in parallel, PMOS in series. Importantly, AND and OR gates each require an extra inverter stage in CMOS, making NAND and NOR the natural implementation primitives. This is why NAND and NOR are called **universal gates**: every Boolean function can be constructed from NAND gates alone, or from NOR gates alone.

**Truth tables** and **Boolean algebra** are the mathematical language of gate design. De Morgan's theorems—the complement of (A AND B) equals (NOT A) OR (NOT B), and vice versa—let you transform freely between gate types. Simplifying a Boolean expression before building it in hardware directly reduces transistor count. The standard workflow of logic design—write the truth table, simplify with Boolean algebra, map to gates—is the combinational design methodology that all of digital systems builds upon.
