---
id: process-concept
title: Processes and the Process Control Block
domain: computer-science
course: operating-systems
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: system-calls
  type: soft
- id: assembly-language-basics
  type: soft
builds-toward:
- process-states-lifecycle
- threads-and-concurrency
- inter-process-communication
- os-security-basics
tags:
- process
- PCB
- program-counter
- address-space
stage: formal-systems
status: draft
---

# Processes and the Process Control Block

## Core Idea
A process is a program in execution — an active entity that includes the program code, current activity (program counter, registers), stack, heap, and data segment. The operating system represents each process with a Process Control Block (PCB), a data structure storing process state, PID, register values, memory maps, open file descriptors, and scheduling information. Multiple processes may run the same program but maintain separate address spaces, so they do not interfere with each other's data. The PCB is saved and restored during context switches.

## How It's Best Learned
Inspect /proc/<pid>/ on Linux to see the live PCB-equivalent data. Write a fork() program and observe how parent and child diverge despite sharing the same code.

## Common Misconceptions
- A process is not the same as a program; the same program can have many simultaneous processes.
- Processes are isolated by default; sharing memory requires explicit IPC mechanisms.
