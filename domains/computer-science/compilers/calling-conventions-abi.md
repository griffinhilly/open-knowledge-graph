---
id: calling-conventions-abi
title: Calling Conventions and ABI
domain: computer-science
course: compilers
prerequisites:
- id: code-emission-target-generation
  type: hard
tags:
- abi
- calling-conventions
- function-calls
stage: advanced
status: draft
---

# Calling Conventions and ABI

## Core Idea
A calling convention specifies how functions are called: how arguments are passed (registers vs stack), where the return value goes, which registers are caller/callee-saved, and how the stack frame is organized. ABIs formalize these conventions so different compilers generate compatible code.

## How It's Best Learned
Study the ABI for your target platform (x86-64 System V ABI, ARM EABI, etc.). Implement function calls that interoperate with system libraries.
