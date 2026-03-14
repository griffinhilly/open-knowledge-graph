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
