---
id: arithmetic-logic-unit-design-details
title: Arithmetic Logic Unit (ALU) Design and Operation Selection
domain: computer-science
course: computer-architecture
prerequisites:
- id: arithmetic-logic-unit
  type: hard
- id: carry-lookahead-adder-design
  type: soft
builds-toward:
- cpu-datapath-structural-design
tags:
- alu
- arithmetic
- logic-operations
stage: formal-systems
status: draft
---

# Arithmetic Logic Unit (ALU) Design and Operation Selection

## Core Idea
The ALU performs arithmetic (add, subtract, multiply, divide) and logic (AND, OR, XOR, NOT) operations on two operands. Control inputs select which operation to perform. Modern ALUs incorporate shifters and may use carry-lookahead or other optimization techniques. The ALU also sets condition code flags (zero, negative, overflow, carry) used by branch instructions.

## Explainer

From your introduction to the ALU concept, you know it is the part of the processor that performs computation. Now consider how it is actually built. An ALU is not a single circuit — it is a collection of parallel functional units (an adder, a logic unit, a shifter) whose outputs are fed into a **multiplexer** controlled by an operation select signal. When the control unit issues an ADD instruction, the select lines route the adder's output to the ALU result bus. When it issues an AND instruction, the same select lines route the logic unit's output instead. All units compute simultaneously on every cycle; the mux simply chooses which result to use.

The arithmetic section centers on an **adder circuit**, often a carry-lookahead adder for speed, as you studied previously. Subtraction is implemented by complementing the second operand (flipping all bits) and adding one — the two's complement trick that converts subtraction into addition with minimal extra hardware. Multiplication and division, when included directly in the ALU, require more complex iterative or combinational circuits and often take multiple clock cycles. The logic section is simpler: AND, OR, XOR, and NOT operations are computed independently for each bit position, since these operations have no carry propagation between bits. A **barrel shifter** handles shift and rotate operations, moving all bits simultaneously rather than shifting one position per clock cycle.

A critical output of the ALU is its **condition code flags**, also called status flags. After every operation, the ALU sets flags that describe the result: the **zero flag** (Z) indicates the result is all zeros, the **negative flag** (N) captures the most significant bit (indicating a negative result in two's complement), the **overflow flag** (V) detects when a signed operation produces a result too large for the word size, and the **carry flag** (C) captures the carry-out of the most significant bit position. These flags are stored in a status register and are read by conditional branch instructions — a "branch if zero" instruction checks the Z flag to decide whether to jump. This is the mechanism that connects arithmetic to control flow in every processor.

The **operation select** input is the interface between the ALU and the rest of the CPU. In a typical design, a 3- or 4-bit control field selects among 8 or 16 operations. This field comes from the control unit, which decodes the current instruction's opcode to determine what the ALU should do. The width of the ALU — 8-bit, 32-bit, 64-bit — determines how many bits are processed in parallel and directly affects the processor's data-handling capability. Designing an ALU means balancing the number of supported operations, the speed of the critical path (usually the adder), and the silicon area budget, since every additional operation adds hardware that must fit on the chip.
