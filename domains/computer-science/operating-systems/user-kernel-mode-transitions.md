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

## Explainer

You already understand from studying privilege levels that the CPU operates in at least two modes: **kernel mode**, where every instruction and every memory address is accessible, and **user mode**, where the hardware restricts what code can do. The critical question is: how does a program running in user mode request something that only the kernel can do — like reading a file, sending a network packet, or allocating memory? The answer is the **mode transition**, and it is one of the most carefully engineered boundaries in all of computing.

When a user program needs an OS service, it cannot simply call a kernel function the way it calls its own subroutines. If it could, any program could jump to arbitrary kernel code and take over the machine. Instead, the program executes a special instruction — on x86-64, this is **SYSCALL**. This instruction does several things atomically: it saves the current instruction pointer and stack pointer, switches the CPU from user mode to kernel mode by flipping the privilege bit in the processor status register, and jumps to a predetermined entry point in the kernel (the **system call handler**). The key security property is that the user program controls *which* system call number it requests (placed in a register), but it cannot control *where* in the kernel execution begins. The entry point is fixed by the kernel at boot time.

Inside the kernel, the system call handler looks up the requested call number in a dispatch table, validates the arguments (because they came from untrusted user code), and executes the appropriate kernel function. When the work is done, the kernel executes **SYSRET** (or the equivalent return instruction), which restores the saved user-mode state and flips the CPU back to unprivileged mode. The program resumes exactly where it left off, with the result of the system call placed in a register. From the program's perspective, it made a function call and got a result back — but underneath, the CPU crossed a hardware security boundary and back.

Mode transitions are not free. Each transition requires saving and restoring registers, potentially flushing CPU pipeline state, and switching stacks (the kernel uses its own stack, never the user program's stack, for security). A single system call typically costs hundreds of nanoseconds to a few microseconds — orders of magnitude more than a regular function call. This cost is why high-performance programs batch operations (reading large blocks of data at once rather than one byte at a time) and why techniques like memory-mapped files exist to reduce the number of transitions needed. The other path into kernel mode is involuntary: **hardware interrupts** and **exceptions** (like page faults or division by zero) trigger mode transitions that the program did not request, allowing the kernel to handle hardware events and error conditions.
