---
id: processor-status-flags-and-conditions
title: Processor Status Flags and Condition Codes
domain: computer-science
course: computer-architecture
prerequisites:
- id: arithmetic-logic-unit-design-details
  type: hard
builds-toward:
- branch-instruction-execution
- exception-handling-architecture
tags:
- status-flags
- condition-codes
- program-status-register
stage: formal-systems
status: draft
---

# Processor Status Flags and Condition Codes

## Core Idea
Condition codes (stored in the processor status register) indicate the outcome of ALU operations: zero flag (result is zero), negative flag (sign bit set), overflow flag (signed arithmetic overflow), and carry flag (unsigned overflow). Conditional branch instructions test these flags to alter control flow. Some flags are set only on certain instruction types.

## Explainer

From your study of ALU design, you know that the arithmetic logic unit produces a numerical result for every operation. But a result alone is not enough — the processor also needs to know *what kind* of result it was. Did the subtraction produce zero? Did the addition overflow? These questions are answered by **status flags**, single-bit indicators that the ALU sets automatically as a side effect of each operation. They are collected in a special register called the **processor status register** (PSR), sometimes called the flags register or condition code register.

The four fundamental flags are the **zero flag (Z)**, **negative flag (N)**, **carry flag (C)**, and **overflow flag (V)**. The zero flag is set to 1 when the result of an operation is exactly zero — this is how the processor detects equality, since subtracting two equal numbers yields zero. The negative flag copies the most significant bit of the result, which in two's complement representation indicates a negative number. The carry flag captures the carry-out from the most significant bit during unsigned arithmetic — it signals that an unsigned addition exceeded the representable range or that an unsigned subtraction required a borrow. The overflow flag detects signed arithmetic overflow: it is set when the carry into the most significant bit differs from the carry out, meaning two positive numbers produced a negative result or two negative numbers produced a positive one.

These flags become powerful through **conditional branch instructions**. A branch instruction like "branch if equal" (BEQ) checks the zero flag: if Z=1, the processor jumps to a new address; if Z=0, it continues to the next instruction. Comparison instructions (CMP) are typically implemented as subtractions that set flags but discard the numerical result. So `CMP R1, R2` subtracts R2 from R1, sets the flags, and throws away the difference. A subsequent `BEQ target` branches if R1 equaled R2 (Z=1). A `BLT target` (branch if less than, signed) checks a combination of N and V flags. This two-step pattern — compare then branch — is how processors implement every if-statement, loop condition, and switch case in high-level languages.

An important subtlety is that not all instructions update all flags, and this varies by architecture. On x86, most arithmetic and logical instructions set flags, but moves and loads do not. On ARM, flags are only set when the instruction explicitly requests it (using an 'S' suffix). This means a flag can retain its value across multiple instructions, and programmers must be careful about which instruction actually set the flags being tested. Understanding which operations affect which flags is essential for writing correct assembly code and for reasoning about how compilers translate conditional logic into machine instructions.
