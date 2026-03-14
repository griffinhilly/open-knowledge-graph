---
id: code-generation
title: Code Generation from IR
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: instruction-set-architecture
  type: hard
builds-toward:
- runtime-function-calls
- jit-compilation
tags:
- code-generation
- machine-code
- code-emission
stage: advanced
status: draft
---

# Code Generation from IR

## Core Idea
Code generation transforms optimized IR into executable machine code. For each IR instruction, emit corresponding assembly or bytecode. This involves instruction selection (choosing target instructions), operand allocation (assigning registers/memory), and instruction scheduling (reordering for performance). Modern code generators use pattern matching, templates, or dynamic programming to select instructions.
