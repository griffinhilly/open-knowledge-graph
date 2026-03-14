---
id: process-creation-fork-exec
title: 'Process Creation: fork() and exec()'
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: kernel-mode-and-privilege-levels
  type: soft
builds-toward:
- process-termination-and-cleanup
- process-states-and-transitions
tags:
- system-calls
- process-lifecycle
- unix-api
stage: formal-systems
status: draft
---

# Process Creation: fork() and exec()

## Core Idea
Processes are created via system calls like fork() (Unix/Linux) or CreateProcess() (Windows). fork() creates a child process as a copy of the parent; exec() replaces the current process image with a new program. Together, they enable process spawning and program execution in Unix-like systems.

## Common Misconceptions
fork() returns twice (it does: once in the parent returning the child's PID, once in the child returning 0). exec() returns on error (it never returns on success; the process image is replaced).
