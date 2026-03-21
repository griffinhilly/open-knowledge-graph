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

## Questions

```yaml
- question: "A programmer writes CMP R1, R2 followed by BLT target (branch if less than, signed). The branch is taken. What can we conclude?"
  type: multiple-choice
  options:
    - "R1 is numerically smaller than R2 in unsigned binary representation"
    - "R1 is less than R2 in signed (two's complement) interpretation, based on the N and V flags set by the subtraction R1 − R2"
    - "The zero flag was set to 1 because R1 and R2 are equal"
    - "R2 − R1 produced a carry out from the most significant bit, setting the carry flag"
  answer: 1
  explanation: "BLT (branch if less than, signed) checks a combination of the negative flag (N) and the overflow flag (V) to detect signed less-than after a subtraction. CMP computes R1 − R2 and sets flags but discards the result. The branch being taken tells us R1 < R2 in signed arithmetic. This is distinct from unsigned comparison (which uses the carry flag) — the subtlety is that the same binary subtraction is interpreted differently for signed vs unsigned comparison."

- question: "Why does the CMP instruction compute a subtraction but discard the numerical result, storing nothing in any general-purpose register?"
  type: multiple-choice
  options:
    - "CMP is more efficient than SUB because it skips the register write-back stage in the pipeline"
    - "For conditional branching, only the flags (zero, negative, carry, overflow) matter — the numerical difference itself is not needed, so discarding it avoids consuming a destination register"
    - "CMP uses the carry flag while SUB uses the overflow flag, making them fundamentally different operations"
    - "The difference is stored implicitly in the status register rather than truly discarded"
  answer: 1
  explanation: "The entire purpose of CMP is to set flags for a subsequent branch instruction. Whether R1 = R2, R1 > R2, or R1 < R2 is encoded completely in the flags — you don't need the number (R1 − R2) itself. Discarding the difference frees the programmer from needing a spare register to hold a temporary value they'll never use. This is a design choice that makes assembly code cleaner."

- question: "A single CMP instruction sets all four status flags simultaneously, so subsequent branch instructions (BEQ, BLT, BGT, BVS) can each check the result of the same comparison."
  type: true-false
  answer: true
  explanation: "The CMP/comparison instruction performs a subtraction that updates all relevant flags (Z, N, C, V) at once. Multiple conditional branch instructions can then test whichever flag combination is relevant — BEQ tests Z=1, BLT tests N≠V, BCS tests C=1, and so on. This means one comparison sets up multiple possible branch outcomes without any repeated computation."

- question: "On all processor architectures, every instruction automatically updates all four status flags (zero, negative, carry, overflow) as a side effect of execution."
  type: true-false
  answer: false
  explanation: "Flag update behavior is architecture-dependent. On x86, most arithmetic and logical instructions set flags, but moves and loads do not. On ARM, flags are only updated when the instruction explicitly includes an 'S' suffix (e.g., ADDS vs ADD). This means flags can retain their values across multiple instructions, and programmers must carefully track which instruction most recently set the flags being tested — a common source of bugs in assembly programming."

- question: "Explain the difference between the carry flag and the overflow flag, and give an example of when you would care about each."
  type: short-answer
  answer: "The carry flag signals unsigned overflow: a carry out of the most significant bit during addition, or a borrow during subtraction, indicating the result exceeded the unsigned range. The overflow flag signals signed overflow: the carry into and out of the MSB differ, meaning two same-sign values produced an opposite-sign result. Care about carry when adding unsigned integers (e.g., 255 + 1 in 8-bit unsigned). Care about overflow when adding signed integers (e.g., 127 + 1 in 8-bit two's complement produces −128)."
  explanation: "The distinction matters because the same bit pattern can represent different values depending on whether you treat it as signed or unsigned. After an 8-bit addition of 0xFF + 0x01: the carry flag is set (unsigned result 256 exceeds 8 bits), but the overflow flag is not (in signed interpretation, −1 + 1 = 0, which is correct). Conversely, 0x7F + 0x01 in signed arithmetic sets the overflow flag (127 + 1 = −128, wrong sign) but not the carry flag in isolation."
```

## Explainer

From your study of ALU design, you know that the arithmetic logic unit produces a numerical result for every operation. But a result alone is not enough — the processor also needs to know *what kind* of result it was. Did the subtraction produce zero? Did the addition overflow? These questions are answered by **status flags**, single-bit indicators that the ALU sets automatically as a side effect of each operation. They are collected in a special register called the **processor status register** (PSR), sometimes called the flags register or condition code register.

The four fundamental flags are the **zero flag (Z)**, **negative flag (N)**, **carry flag (C)**, and **overflow flag (V)**. The zero flag is set to 1 when the result of an operation is exactly zero — this is how the processor detects equality, since subtracting two equal numbers yields zero. The negative flag copies the most significant bit of the result, which in two's complement representation indicates a negative number. The carry flag captures the carry-out from the most significant bit during unsigned arithmetic — it signals that an unsigned addition exceeded the representable range or that an unsigned subtraction required a borrow. The overflow flag detects signed arithmetic overflow: it is set when the carry into the most significant bit differs from the carry out, meaning two positive numbers produced a negative result or two negative numbers produced a positive one.

These flags become powerful through **conditional branch instructions**. A branch instruction like "branch if equal" (BEQ) checks the zero flag: if Z=1, the processor jumps to a new address; if Z=0, it continues to the next instruction. Comparison instructions (CMP) are typically implemented as subtractions that set flags but discard the numerical result. So `CMP R1, R2` subtracts R2 from R1, sets the flags, and throws away the difference. A subsequent `BEQ target` branches if R1 equaled R2 (Z=1). A `BLT target` (branch if less than, signed) checks a combination of N and V flags. This two-step pattern — compare then branch — is how processors implement every if-statement, loop condition, and switch case in high-level languages.

An important subtlety is that not all instructions update all flags, and this varies by architecture. On x86, most arithmetic and logical instructions set flags, but moves and loads do not. On ARM, flags are only set when the instruction explicitly requests it (using an 'S' suffix). This means a flag can retain its value across multiple instructions, and programmers must be careful about which instruction actually set the flags being tested. Understanding which operations affect which flags is essential for writing correct assembly code and for reasoning about how compilers translate conditional logic into machine instructions.
