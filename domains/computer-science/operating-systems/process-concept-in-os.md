---
id: process-concept-in-os
title: The Process Concept
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
- id: kernel-mode-and-privilege-levels
  type: soft
builds-toward:
- process-creation-fork-exec
- process-states-and-transitions
- thread-model-user-vs-kernel
tags:
- process-management
- abstraction
- isolation
stage: formal-systems
status: draft
---

# The Process Concept

## Core Idea
A process is an instance of a program in execution, isolated from other processes with its own address space, registers, and file descriptors. The OS maintains a process control block (PCB) containing process state, priority, memory maps, and other metadata. Processes provide strong isolation and enable concurrent execution.

## How It's Best Learned
Examine process tables using system tools (ps, Task Manager) and observe how multiple instances of the same program run as distinct processes with separate memory.
