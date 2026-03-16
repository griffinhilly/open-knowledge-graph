---
id: addressing-modes-instruction-format
title: Addressing Modes and Instruction Format
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-set-architecture
  type: hard
builds-toward:
- instruction-pipeline-organization
- memory-management-paging-segmentation
tags:
- addressing
- modes
- instruction
- format
stage: formal-systems
status: draft
---

# Addressing Modes and Instruction Format

## Core Idea
Addressing modes specify how to locate an instruction's operands: immediate (literal value), register (from register), direct (from memory at given address), indirect (from memory at address in a register), and indexed (address modified by an index). Instruction format encodes opcode and addressing mode in fixed or variable-length fields.

## Explainer

From your study of instruction set architecture, you know that every machine instruction specifies an operation and its operands. But *how* the operands are specified varies enormously, and the choice has deep consequences for code density, performance, and flexibility. **Addressing modes** are the different ways an instruction can say "here is where to find the data." Understanding them is understanding the bridge between high-level data access patterns (variables, arrays, pointers, structures) and the hardware's actual capabilities.

The simplest modes are **immediate** and **register**. In immediate mode, the operand value is embedded directly in the instruction itself — `ADD R1, #5` means "add the literal value 5 to register R1." This is fast because no memory access is needed, but the value must be small enough to fit in the instruction's operand field. Register mode is equally fast — `ADD R1, R2` fetches the operand from a CPU register, which takes essentially zero extra time. These two modes handle constants and local variables that the compiler has placed in registers.

When data lives in memory, the modes become more interesting. **Direct** (or absolute) addressing gives a fixed memory address: `LOAD R1, [0x4000]` fetches from address 0x4000. This works for global variables at known locations. **Register indirect** addressing uses a register as a pointer: `LOAD R1, [R2]` means "go to the address stored in R2 and fetch the value there." This is how pointer dereferencing works at the hardware level. **Indexed** addressing adds an offset: `LOAD R1, [R2 + 8]` accesses a memory location at a fixed displacement from a base address, which is exactly what you need for accessing structure fields or array elements. Some architectures support **scaled indexed** mode — `LOAD R1, [R2 + R3*4]` — where the index register is multiplied by the element size, directly supporting array indexing without extra multiply instructions.

The **instruction format** determines how all of this information — opcode, addressing mode, register numbers, immediate values, offsets — is packed into binary. In a **fixed-length** format (like ARM's 32-bit instructions), every instruction occupies the same number of bits, which simplifies instruction fetch and pipeline design but limits how much information each instruction can carry. In a **variable-length** format (like x86), instructions range from 1 to 15 bytes, allowing more addressing modes and larger immediate values at the cost of more complex decoding logic. This tradeoff between decode simplicity and code expressiveness is one of the fundamental design decisions in processor architecture, and it directly affects the pipeline organization you will study next.
