---
id: code-emission-target-generation
title: Code Emission and Target Generation
domain: computer-science
course: compilers
prerequisites:
- id: graph-coloring-register-allocation
  type: hard
builds-toward:
- calling-conventions-abi
tags:
- code-generation
- backend
- assembly
stage: advanced
status: draft
---

# Code Emission and Target Generation

## Core Idea
After instruction selection and register allocation, the compiler must emit target assembly or machine code. Code emission must handle instruction encoding, relocation information for jumps and calls, and proper instruction ordering. Modern emitters also generate debugging information.

## How It's Best Learned
Implement a code emitter producing assembly code from allocated instructions. Generate position-independent code and handle relocations.
