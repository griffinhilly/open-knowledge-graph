---
id: instruction-set-architecture
title: Instruction Set Architecture (ISA)
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: registers-and-register-files
  type: soft
- id: twos-complement
  type: soft
builds-toward:
- assembly-language-basics
- cpu-datapath
- cpu-control-unit
tags:
- ISA
- RISC
- CISC
- instruction-format
- opcodes
stage: formal-systems
status: validated
---

# Instruction Set Architecture (ISA)

## Core Idea
The Instruction Set Architecture (ISA) is the contract between hardware and software: it specifies the instructions a CPU can execute, the registers visible to programs, data types, addressing modes, and the binary encoding of each instruction. RISC designs use few, simple, fixed-length instructions; CISC designs provide many complex, variable-length instructions. Major ISAs include x86 (CISC), ARM and RISC-V (RISC). The ISA determines what machine code is valid for a given processor family and is independent of the underlying microarchitecture.

## How It's Best Learned
Study a simple ISA like MIPS or RISC-V. Encode a few instructions by hand into their binary format. Write a short program in assembly and trace how each instruction is fetched, decoded, and executed. Compare instruction formats across RISC and CISC designs.

## Common Misconceptions
- The ISA is not the microarchitecture — the same ISA can be implemented in many different ways with very different performance characteristics.
- RISC CPUs are not simply 'simpler' CPUs; modern RISC processors are highly complex internally but expose a clean, simple instruction interface.
