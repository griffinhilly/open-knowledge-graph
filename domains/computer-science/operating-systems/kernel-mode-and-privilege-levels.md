---
id: kernel-mode-and-privilege-levels
title: Kernel Mode and Privilege Levels
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
builds-toward:
- system-calls
- process-creation-fork-exec
- interrupt-exception-handling
tags:
- security
- hardware-abstraction
- privilege
- protection
stage: formal-systems
status: draft
---

# Kernel Mode and Privilege Levels

## Core Idea
Modern CPUs support multiple privilege levels (typically user and kernel modes) to protect the OS from applications. Kernel mode allows unrestricted hardware access and is used for OS operations. User mode restricts operations to prevent applications from interfering with each other or the OS. Privilege transitions occur via system calls or interrupts.

## How It's Best Learned
Use system call tracing tools (strace, ltrace) to observe transitions between user and kernel mode during application execution.

## Common Misconceptions
Applications can do nothing in user mode (they perform computation and I/O via system calls). Kernel mode is always secure (it requires careful validation to prevent bugs).

## Explainer

From your introduction to operating systems, you know that the OS manages hardware resources and provides services to applications. But a natural question arises: what stops a buggy or malicious application from directly accessing hardware, overwriting another process's memory, or corrupting the OS itself? The answer is **hardware-enforced privilege levels** — a mechanism built into the CPU that divides execution into restricted and unrestricted modes.

Most processors implement at least two privilege levels. In **kernel mode** (also called supervisor mode or ring 0 on x86), the CPU can execute any instruction: access any memory address, interact directly with hardware devices, modify page tables, and disable interrupts. The OS kernel runs in this mode. In **user mode** (ring 3 on x86), certain instructions are forbidden — any attempt to execute a privileged instruction (like writing to an I/O port or modifying the interrupt table) triggers a hardware exception that transfers control to the kernel. This means an application literally cannot bypass the OS, not because of software rules it promises to follow, but because the hardware will not let it.

The transition between modes happens through a controlled gateway: the **system call**. When an application needs to perform a privileged operation — opening a file, allocating memory, sending a network packet — it cannot do so directly. Instead, it places the request parameters in agreed-upon registers and executes a special trap instruction (like `syscall` on x86-64 or `svc` on ARM). This instruction atomically switches the CPU to kernel mode and jumps to a predefined kernel entry point. The kernel validates the request, performs the operation on the application's behalf, and returns the result by switching back to user mode. The key security property is that the application never chooses where in the kernel to jump — the hardware forces entry through a fixed vector table set up at boot time.

**Interrupts** provide the other path into kernel mode. When a hardware device needs attention — a disk completing a read, a network card receiving a packet, a timer firing — it signals the CPU, which suspends the current user-mode process and transfers control to the kernel's interrupt handler. This is essential for the OS to remain in control even when a user process is running: the timer interrupt, for example, allows the scheduler to preempt a process that has used its time slice. Together, system calls and interrupts ensure that the kernel mediates every interaction between applications and hardware, enforcing isolation and protection without relying on applications to behave correctly.
