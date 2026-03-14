---
id: system-call-semantics
title: System Call Semantics and ABI
domain: computer-science
course: operating-systems
prerequisites:
- id: user-kernel-mode-transitions
  type: hard
- id: calling-conventions-abi
  type: soft
builds-toward:
- interrupt-vector-dispatch
tags:
- system-calls
- abi
- interface
stage: formal-systems
status: draft
---

# System Call Semantics and ABI

## Core Idea
System calls are the formal interface for requesting OS services. The Application Binary Interface (ABI) specifies calling conventions: which registers hold arguments and return values, stack layout, and parameter passing. This standardization enables portable user programs.
