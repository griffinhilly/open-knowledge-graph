---
id: runtime-function-calls
title: Runtime Function Calls and Stack Frames
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: memory-organization
  type: hard
builds-toward:
- garbage-collection-algorithms
tags:
- calling-conventions
- stack-frames
- runtime-support
stage: advanced
status: draft
---

# Runtime Function Calls and Stack Frames

## Core Idea
Function calls must maintain a call stack: each activation creates a stack frame storing return address, parameters, local variables, and saved registers. Calling conventions specify register allocation, parameter passing (registers vs. stack), and caller/callee save responsibilities. Proper calling conventions are essential for correctness and interoperability between separately compiled code.
