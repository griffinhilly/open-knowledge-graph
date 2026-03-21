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
stage: advanced
status: draft
---

# Exception Handling: OS Internals

## Core Idea
When an exception (fault, trap, or abort) occurs, the handler must save the interrupted context, diagnose the cause, take corrective action (e.g., allocate memory, terminate the process), and either resume or terminate execution.

## Questions

```yaml
- question: "A page fault occurs when the CPU tries to execute an instruction at virtual address X. After the OS handler loads the missing page from disk, execution resumes at..."
  type: multiple-choice
  options:
    - "The instruction after address X, since the faulting instruction has already been attempted"
    - "The entry point of the fault handler, to re-run the diagnostic logic"
    - "Address X itself — the faulting instruction is retried"
    - "The start of the current function, which must re-run from a clean state"
  answer: 2
  explanation: "A fault saves the address of the faulting instruction, not the next one. This is intentional: the instruction could not complete because a prerequisite (the page) was missing. Once the handler provides what was missing, it is correct to retry the exact same instruction — it will now succeed. If the CPU saved the next address instead, the faulting instruction would be silently skipped, producing incorrect behavior. This restart-on-fix design is what makes virtual memory and on-demand paging work transparently."

- question: "A user program executes the 'syscall' instruction to request kernel services. What type of exception is this, and where does execution resume after the handler returns?"
  type: multiple-choice
  options:
    - "A fault; execution restarts the syscall instruction so the request can be re-evaluated"
    - "A trap; execution resumes at the instruction after the syscall"
    - "An abort; the process is terminated as the hardware assumes the system call failed"
    - "A hardware interrupt; execution resumes where it was interrupted, which may be anywhere"
  answer: 1
  explanation: "System calls are traps — intentional exceptions triggered after the instruction completes. The saved return address points to the next instruction because the syscall instruction itself has fully executed; the OS processes the request and returns to the instruction that follows. This is fundamentally different from a fault (which saves the current address for retry) and from an interrupt (which is asynchronous, triggered by external hardware rather than by the program itself)."

- question: "Exception handlers can run in user mode if the faulting process has sufficient privileges, allowing fast, OS-bypass handling."
  type: true-false
  answer: false
  explanation: "Exception handlers always run in kernel mode, regardless of the privilege level of the code that triggered the exception. This is a hardware-enforced invariant, not an OS policy. When an exception occurs, the CPU unconditionally switches to kernel mode and loads the handler address from the interrupt descriptor table (IDT), which only the kernel can modify. This design ensures that a buggy user program cannot corrupt the OS or other processes — the kernel intercepts every fault and decides the response."

- question: "A fault saves the instruction pointer to the address of the faulting instruction so that, after the handler resolves the problem, the same instruction can be retried."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of a fault. A page fault is the canonical example: the instruction that accessed an unmapped virtual address is saved, the handler loads the needed page, and the CPU returns to execute that same instruction again. If faults saved the next instruction's address (as traps do), the faulting instruction would be skipped and the program would execute in a corrupt or incomplete state. The save-and-retry design makes transparent demand paging possible."

- question: "What is the difference between a fault and a trap in terms of the saved return address, and why does this distinction matter for the correct behavior of virtual memory?"
  type: short-answer
  answer: "A fault saves the address of the faulting instruction itself; a trap saves the address of the instruction that follows. For virtual memory, this distinction is essential: when a page fault occurs, the OS must be able to retry the exact instruction that caused the fault after loading the missing page. If it resumed at the next address, the memory access that triggered the fault would never complete, leaving the program in an undefined state. Traps (like system calls) don't need retrying because the triggering instruction has already completed its work before the exception is raised."
  explanation: "The saved address is the handler's return ticket. For faults, the problem exists because the instruction couldn't finish — fix the problem, restart the instruction. For traps, the instruction is finished — the OS does the requested service and moves on. This difference is why virtual memory works transparently: from the user program's perspective, accessing a paged-out address just takes a bit longer, with no visible effect, because the faulting instruction is silently retried after the page is loaded."
```

## Explainer

From your prerequisites on interrupt vectors and system call semantics, you know that the CPU can be diverted from its current instruction stream by events that require kernel attention, and that a vector table maps event numbers to handler addresses. **Exceptions** are a specific class of these events: they are generated *by the CPU itself* in response to conditions encountered during instruction execution, as opposed to external hardware interrupts. Understanding how the OS handles exceptions is essential because exceptions are the mechanism behind page faults, segmentation faults, divide-by-zero errors, and even system calls on some architectures.

Exceptions fall into three categories based on severity and restartability. A **fault** is a potentially recoverable condition detected *before* the instruction completes — the classic example is a page fault, where the process accesses a valid virtual address whose page isn't currently in physical memory. The CPU saves the address of the faulting instruction (not the next one), transfers control to the fault handler, and the handler can fix the problem (load the page from disk) and *restart the same instruction*. A **trap** is an intentional exception triggered *after* an instruction completes — the most common examples are breakpoints (used by debuggers) and system calls (the `int 0x80` or `syscall` instruction). The saved address points to the *next* instruction, so execution continues forward after the handler returns. An **abort** signals an unrecoverable hardware error (like a parity error in memory); the handler typically terminates the process or panics the kernel.

The exception handling sequence follows a precise protocol. When the CPU detects the exception condition, it immediately stops the current instruction stream. Hardware automatically saves critical state onto the kernel stack: at minimum the instruction pointer, the stack pointer, and the processor status flags. The CPU then indexes into the **interrupt descriptor table** (IDT) using the exception number to find the handler's address and jumps to it. The handler's first job is to save any additional register state that the hardware didn't preserve — this is the same context-saving operation you've seen in context switching, but here it's triggered by an unexpected event rather than a scheduler decision. The handler then examines hardware status registers to diagnose what happened: which address caused the fault, what type of access was attempted, whether the process had permission.

The handler's response depends on the exception type and cause. For a page fault on a valid address, the handler allocates a physical frame, loads the page from disk or swap, updates the page table, and returns — the CPU restarts the faulting instruction, which now succeeds. For an illegal memory access (dereferencing a null pointer, writing to read-only memory), the handler delivers a signal to the offending process (SIGSEGV on Unix), which typically terminates it. For a divide-by-zero, the handler delivers SIGFPE. The crucial design principle is that exception handlers run in kernel mode with full privilege, even though the exception was caused by user-mode code. This is what allows the kernel to maintain control: a buggy user program can't crash the system, because its faults are caught by kernel handlers that decide the appropriate response — fix it, signal the process, or terminate it cleanly.
