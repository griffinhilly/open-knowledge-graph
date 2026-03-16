---
id: exception-handling-os-internals
title: 'Exception Handling: OS Internals'
domain: computer-science
course: operating-systems
prerequisites:
- id: interrupt-vector-dispatch
  type: hard
- id: system-call-semantics
  type: hard
builds-toward:
- page-fault-processing
tags:
- exceptions
- handlers
- internals
stage: formal-systems
status: draft
---

# Exception Handling: OS Internals

## Core Idea
When an exception (fault, trap, or abort) occurs, the handler must save the interrupted context, diagnose the cause, take corrective action (e.g., allocate memory, terminate the process), and either resume or terminate execution.

## Explainer

From your prerequisites on interrupt vectors and system call semantics, you know that the CPU can be diverted from its current instruction stream by events that require kernel attention, and that a vector table maps event numbers to handler addresses. **Exceptions** are a specific class of these events: they are generated *by the CPU itself* in response to conditions encountered during instruction execution, as opposed to external hardware interrupts. Understanding how the OS handles exceptions is essential because exceptions are the mechanism behind page faults, segmentation faults, divide-by-zero errors, and even system calls on some architectures.

Exceptions fall into three categories based on severity and restartability. A **fault** is a potentially recoverable condition detected *before* the instruction completes — the classic example is a page fault, where the process accesses a valid virtual address whose page isn't currently in physical memory. The CPU saves the address of the faulting instruction (not the next one), transfers control to the fault handler, and the handler can fix the problem (load the page from disk) and *restart the same instruction*. A **trap** is an intentional exception triggered *after* an instruction completes — the most common examples are breakpoints (used by debuggers) and system calls (the `int 0x80` or `syscall` instruction). The saved address points to the *next* instruction, so execution continues forward after the handler returns. An **abort** signals an unrecoverable hardware error (like a parity error in memory); the handler typically terminates the process or panics the kernel.

The exception handling sequence follows a precise protocol. When the CPU detects the exception condition, it immediately stops the current instruction stream. Hardware automatically saves critical state onto the kernel stack: at minimum the instruction pointer, the stack pointer, and the processor status flags. The CPU then indexes into the **interrupt descriptor table** (IDT) using the exception number to find the handler's address and jumps to it. The handler's first job is to save any additional register state that the hardware didn't preserve — this is the same context-saving operation you've seen in context switching, but here it's triggered by an unexpected event rather than a scheduler decision. The handler then examines hardware status registers to diagnose what happened: which address caused the fault, what type of access was attempted, whether the process had permission.

The handler's response depends on the exception type and cause. For a page fault on a valid address, the handler allocates a physical frame, loads the page from disk or swap, updates the page table, and returns — the CPU restarts the faulting instruction, which now succeeds. For an illegal memory access (dereferencing a null pointer, writing to read-only memory), the handler delivers a signal to the offending process (SIGSEGV on Unix), which typically terminates it. For a divide-by-zero, the handler delivers SIGFPE. The crucial design principle is that exception handlers run in kernel mode with full privilege, even though the exception was caused by user-mode code. This is what allows the kernel to maintain control: a buggy user program can't crash the system, because its faults are caught by kernel handlers that decide the appropriate response — fix it, signal the process, or terminate it cleanly.
