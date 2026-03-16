---
id: arithmetic-logic-units-design
title: Arithmetic-Logic Unit (ALU) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-adders
  type: hard
- id: arithmetic-logic-unit
  type: soft
builds-toward:
- cpu-datapath
- instruction-fetch-decode-execute
tags:
- alu
- arithmetic
- logic
- operations
stage: formal-systems
status: draft
---

# Arithmetic-Logic Unit (ALU) Design

## Core Idea
An ALU integrates multiple arithmetic and logical operations (add, subtract, AND, OR, shift, etc.) and uses control signals to select which operation to perform. It is the computational core of every CPU's datapath.

## How It's Best Learned
Design a simple ALU with 4 operations (add, subtract, AND, OR); trace through execution with sample inputs.

## Common Misconceptions
ALUs do not store state; they are purely combinational. Operation selection requires log₂(N) control bits for N operations.

## Explainer

From your study of binary adders, you know how to build a circuit that takes two binary numbers and produces their sum using a chain of full adders with carry propagation. An ALU generalizes this idea: instead of a single hardwired operation, it is a combinational circuit that can perform *any one of several operations* on the same pair of inputs, selected by a set of **control signals**. Think of it as a Swiss Army knife — the inputs stay the same, but the control bits tell the ALU which blade to open.

The simplest ALU design places multiple operation circuits in parallel — an adder, a subtractor, an AND gate array, an OR gate array — all connected to the same two input buses. Each circuit computes its result simultaneously, and a **multiplexer** at the output selects which result to pass through based on the control signals. For four operations, you need a 4-to-1 multiplexer controlled by 2 bits: `00` might select AND, `01` might select OR, `10` might select addition, and `11` might select subtraction. Subtraction typically reuses the adder by inverting one input and setting the carry-in to 1, exploiting the two's complement identity `A - B = A + NOT(B) + 1`. This means the adder and subtractor share hardware, and a single control bit toggles between addition and subtraction.

Beyond the primary result, a well-designed ALU produces **condition flags** that report properties of the output: a **zero flag** (is the result all zeros?), a **negative flag** (is the sign bit set?), a **carry flag** (did the addition overflow the word width?), and an **overflow flag** (did a signed addition produce an incorrect sign?). These flags cost almost nothing to generate — a zero flag is just a wide NOR gate across all result bits — but they are essential for the processor's control logic. Branch instructions like "branch if equal" simply test the zero flag after a subtraction, which is why comparison and subtraction are really the same ALU operation.

The ALU is purely **combinational**: it has no memory, no clock input, and no internal state. You present inputs and control signals, and after a propagation delay the outputs stabilize. This is a critical property because it means the ALU fits cleanly into a clocked datapath — registers capture inputs at the start of a clock cycle, the ALU computes during the cycle, and registers capture the result at the end. When you build a full CPU datapath, the ALU sits at the center, connected to the register file on both sides, with the control unit deciding which operation to perform on each clock cycle based on the current instruction.
