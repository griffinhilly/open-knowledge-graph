---
id: bytecode-and-vm-design
title: Bytecode Intermediate Representation and Virtual Machines
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: jit-compilation
  type: hard
builds-toward:
- interpreter-design-and-tradeoffs
tags:
- bytecode
- VM
- interpretation
stage: advanced
status: draft
---

# Bytecode Intermediate Representation and Virtual Machines

## Core Idea
Bytecode is a compact, machine-independent intermediate representation executed by a virtual machine. The compiler targets bytecode for portability, and the VM interprets it (slow but flexible) or JIT-compiles it to native code (fast). Trade-off between deployment simplicity and runtime performance.
