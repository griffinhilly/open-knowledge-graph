---
id: exception-handling-architecture
title: Exception and Interrupt Handling Architecture
domain: computer-science
course: computer-architecture
prerequisites:
- id: interrupt-exception-handling
  type: hard
- id: processor-status-flags-and-conditions
  type: soft
builds-toward:
- multi-core-system-design
tags:
- exceptions
- interrupts
- exception-handling
stage: formal-systems
status: draft
---

# Exception and Interrupt Handling Architecture

## Core Idea
Exceptions (page faults, divide-by-zero, illegal instructions) and interrupts (I/O devices, timers) divert control to exception handlers. The processor saves the current instruction pointer and processor state, jumps to a handler address (from an interrupt vector table), and restores state upon return. Nested exceptions and priority schemes handle multiple simultaneous events.

## Explainer

From your study of basic interrupt and exception handling, you know that processors need a mechanism to respond to unexpected events — a key press, a division by zero, a page not in memory. **Exception handling architecture** is the hardware-level infrastructure that makes this possible reliably, even when exceptions arrive at inconvenient moments during instruction execution. The challenge is not just jumping to a handler; it is doing so in a way that preserves the processor's ability to resume exactly where it left off.

When an exception occurs, the processor must save enough state to return later. At minimum, this means saving the **program counter** (the address of the interrupted or faulting instruction) and the **processor status register** (which includes the condition flags and interrupt-enable bits you studied). Many architectures save these into dedicated registers (like MIPS's EPC and Cause registers) or push them onto a kernel stack (like x86). The processor then consults an **interrupt vector table** — an array of handler addresses in memory, indexed by exception type. Exception type 0 might point to the divide-by-zero handler, type 14 to the page fault handler, and so on. The processor loads the appropriate address from the table and begins executing the handler code.

The architecture must handle a subtle problem: **what happens when an exception occurs while another exception is being handled?** This requires a **priority scheme**. Hardware interrupts are typically assigned priority levels, and a higher-priority interrupt can preempt a lower-priority handler — this is a **nested exception**. A timer interrupt might preempt a keyboard handler, but a keyboard interrupt should not preempt a critical page fault handler. The processor's interrupt-enable flag and priority-level register control this nesting. When entering a handler, the processor may automatically disable lower-priority interrupts to prevent chaotic reentrance.

A particularly tricky aspect is **precise exceptions**: when an exception fires, the processor must appear as if all instructions before the faulting one have completed and none after it have started. In a simple single-cycle processor, this is trivial — one instruction is in flight at a time. But in pipelined and out-of-order processors, multiple instructions are in various stages of execution. Achieving precise exceptions requires the pipeline to flush partially completed instructions and restore the architectural state to the exact point of the fault. This is one of the most complex parts of modern processor design, but it is essential: the operating system's page fault handler, for example, must be able to fix the missing page and then re-execute the faulting instruction as if nothing happened. Without precise exceptions, virtual memory and debuggers would not work correctly.
