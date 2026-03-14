---
id: assembly-language-basics
title: Assembly Language Basics
domain: computer-science
course: computer-architecture
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: hexadecimal-number-system
  type: soft
- id: variables-and-assignment
  type: soft
builds-toward:
- cpu-datapath
- memory-organization
tags:
- assembly
- machine-code
- mnemonics
- addressing-modes
stage: formal-systems
status: validated
---

# Assembly Language Basics

## Core Idea
Assembly language is a human-readable representation of machine code, where each instruction mnemonic (like ADD, LOAD, BRANCH) maps directly to a binary opcode. Programmers work with registers by name, specify memory addresses, and use labels for branch targets. Addressing modes — immediate, register, direct, indirect, base+offset — determine how operands are located. Assembly is compiled by an assembler into machine code, and understanding assembly is essential for reverse engineering, performance tuning, and interpreting compiler output.

## How It's Best Learned
Write and run short MIPS or RISC-V assembly programs in a simulator such as MARS or Ripes. Trace register and memory values through each instruction. Examine compiler output at the assembly level using gcc -S or an online tool like Godbolt.

## Common Misconceptions
- Assembly language is not machine code — it is a text-based representation that an assembler translates into binary.
- Writing assembly is not always faster than compiled code; modern optimizing compilers often produce more efficient code than hand-written assembly.
