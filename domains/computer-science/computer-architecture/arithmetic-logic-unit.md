---
id: arithmetic-logic-unit
title: Arithmetic Logic Unit (ALU)
domain: computer-science
course: computer-architecture
prerequisites:
- id: adder-circuits
  type: hard
- id: twos-complement
  type: hard
- id: boolean-algebra
  type: soft
- id: floating-point-representation
  type: soft
builds-toward:
- cpu-datapath
- cpu-control-unit
tags:
- ALU
- arithmetic
- logic-operations
- CPU
stage: formal-systems
status: validated
---
# Arithmetic Logic Unit (ALU)

## Core Idea
The Arithmetic Logic Unit (ALU) is the computational core of a CPU, performing arithmetic operations (addition, subtraction, comparison) and bitwise logic operations (AND, OR, XOR, NOT, shifts) on binary data. An n-bit ALU takes two n-bit operands and a function-select code, producing a result and status flags (zero, carry, overflow, negative). The ALU is built from a combination of adder circuits and logic gates unified by a multiplexer that selects the output based on the operation code.

## How It's Best Learned
Design a simple 1-bit ALU that supports ADD, AND, and OR, then extend to 4 bits. Implement status flags and trace how they are set by different operations. Examine an open-source CPU design to see how the ALU fits into the full datapath.

## Common Misconceptions
- The ALU does not perform multiplication and division directly in most designs; these are handled by separate units or by repeated addition in software.
- The ALU does not know what operation to perform on its own — it relies entirely on the control unit sending the correct function-select signals.
