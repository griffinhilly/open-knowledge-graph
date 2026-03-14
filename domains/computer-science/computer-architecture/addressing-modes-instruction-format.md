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
