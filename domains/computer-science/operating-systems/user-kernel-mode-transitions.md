---
id: user-kernel-mode-transitions
title: User-Kernel Mode Transitions
domain: computer-science
course: operating-systems
prerequisites:
- id: kernel-mode-and-privilege-levels
  type: hard
- id: instruction-set-architecture
  type: soft
builds-toward:
- system-call-semantics
- interrupt-vector-dispatch
tags:
- privilege
- transitions
- security
stage: formal-systems
status: draft
---

# User-Kernel Mode Transitions

## Core Idea
CPUs support two execution modes: privileged (kernel) mode for OS code and unprivileged (user) mode for applications. Transitions between modes are tightly controlled through special instructions (SYSCALL, SYSRET) and hardware exceptions to prevent unauthorized access to protected resources.
