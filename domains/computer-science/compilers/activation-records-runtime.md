---
id: activation-records-runtime
title: Activation Records and Stack Frames
domain: computer-science
course: compilers
prerequisites:
- id: memory-management-basics
  type: hard
- id: calling-conventions-abi
  type: hard
builds-toward:
- exception-handling-compilation
tags:
- runtime
- memory
- function-calls
stage: advanced
status: draft
---

# Activation Records and Stack Frames

## Core Idea
An activation record (or stack frame) stores a function's return address, parameters, local variables, saved registers, and temporary values. The compiler generates code to build these frames on function entry and dismantle them on exit, managing the runtime call stack and enabling recursion.

## How It's Best Learned
Examine assembly code for a simple recursive function, trace stack frame construction, and verify that parameters and locals are accessible at known offsets from the frame pointer.
