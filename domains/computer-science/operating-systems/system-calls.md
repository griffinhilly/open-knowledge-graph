---
id: system-calls
title: System Calls and User/Kernel Mode
domain: computer-science
course: operating-systems
prerequisites:
- id: instruction-set-architecture
  type: hard
- id: kernel-architecture
  type: soft
builds-toward:
- process-concept
- inter-process-communication
- io-management
tags:
- system-call
- user-mode
- kernel-mode
- trap
- privilege
stage: formal-systems
status: validated
---

# System Calls and User/Kernel Mode

## Core Idea
CPUs operate in at least two privilege levels: user mode (restricted) and kernel mode (unrestricted). A system call is the controlled mechanism by which user-space programs request privileged services from the kernel, such as reading a file, spawning a process, or allocating memory. The call triggers a software interrupt or trap instruction that switches the CPU into kernel mode, executes the requested service, and returns control to user mode. The POSIX API (read, write, fork, exec, etc.) defines the standard system call interface on Unix-like systems.

## How It's Best Learned
Use strace on Linux to observe which system calls a program makes. Then inspect how a simple write() call propagates from C library through libc wrapper, into the kernel, and back.

## Common Misconceptions
- Calling a C standard library function (printf) is NOT a system call itself; it eventually wraps one (write).
- System calls are expensive relative to function calls because mode-switching flushes CPU pipeline state.
