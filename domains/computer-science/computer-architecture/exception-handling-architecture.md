---
id: exception-handling-architecture
title: Exception and Interrupt Handling Architecture
domain: computer-science
course: computer-architecture
prerequisites:
- id: interrupts-and-dma
  type: hard
- id: processor-status-flags-and-conditions
  type: soft
tags:
- exceptions
- interrupts
- exception-handling
stage: formal-systems
status: validated
---

# Exception and Interrupt Handling Architecture

## Core Idea
Exceptions (page faults, divide-by-zero, illegal instructions) and interrupts (I/O devices, timers) divert control to exception handlers. The processor saves the current instruction pointer and processor state, jumps to a handler address (from an interrupt vector table), and restores state upon return. Nested exceptions and priority schemes handle multiple simultaneous events.

## Questions

```yaml
- question: "A page fault fires while an instruction is partway through execution in a pipelined processor. The OS loads the missing page and returns. What must the processor guarantee for this sequence to work correctly?"
  type: multiple-choice
  options:
    - "The faulting instruction is skipped and execution resumes at the next instruction."
    - "The processor must guarantee precise exception semantics: all prior instructions appear complete, the faulting instruction appears as if it never started, and it will be re-executed from scratch after the handler returns."
    - "The pipeline flushes all in-flight instructions and the program restarts from its beginning."
    - "The exception handler runs within the same pipeline stage where the fault was detected."
  answer: 1
  explanation: "Precise exceptions require the processor to present a clean architectural state at the point of the fault: all instructions before the faulting one have completed their effects, and no effects of the faulting instruction or any instruction after it are visible. The faulting instruction is then re-executed once the OS has fixed the problem. This is essential for virtual memory — the instruction must be able to succeed on the second attempt. Option A would silently skip a computation; option C would destroy all prior work; option D misunderstands where handlers execute."

- question: "When a keyboard interrupt arrives, the processor indexes into the interrupt vector table using the interrupt's type number. What does the table entry at that index contain?"
  type: multiple-choice
  options:
    - "A saved copy of the interrupted program's register values."
    - "A priority level number indicating whether the interrupt should preempt the current handler."
    - "The memory address of the handler routine to be executed for this interrupt type."
    - "A flag indicating whether the I/O device has already been acknowledged."
  answer: 2
  explanation: "The interrupt vector table is an array of handler addresses indexed by exception type. When the processor receives interrupt type N, it loads the address stored at entry N and jumps to that handler. This is how the processor knows where to find the keyboard handler, the page fault handler, the divide-by-zero handler, and so on — each type maps to a distinct handler address. Register saving (option A) typically happens before the table lookup, pushed onto a kernel stack or into dedicated registers."

- question: "Achieving precise exceptions in a pipelined processor requires flushing partially-completed instructions that followed the faulting instruction and restoring the architectural state to the exact point of the fault."
  type: true-false
  answer: true
  explanation: "True. In a pipeline, multiple instructions are in flight simultaneously. When an exception fires, instructions younger than the faulting instruction may have partially modified registers or memory. Precise exceptions require squashing all of these in-progress effects and rolling the architectural state back to the exact snapshot before the faulting instruction began. This is one of the most demanding aspects of processor design, particularly for out-of-order and deeply pipelined processors."

- question: "After an exception handler finishes, the processor always resumes execution at the instruction immediately following the one that caused the exception."
  type: true-false
  answer: false
  explanation: "False — whether to resume at the same instruction or the next depends on the exception type. For faults (page faults, divide-by-zero), the handler corrects the problem and the processor re-executes the faulting instruction — resuming at the next instruction would skip it and lose its result. For traps (intentional software interrupts like system calls), execution resumes at the instruction after the trap. The processor saves either the faulting PC or PC+1 depending on the exception class, and the handler uses this to determine where to return."

- question: "Why do pipelined processors face a significantly harder problem achieving precise exceptions than single-cycle processors?"
  type: short-answer
  answer: "In a single-cycle processor, exactly one instruction is in flight at a time — when an exception fires, no other instruction has been partially modified, so the processor simply saves the PC and jumps to the handler. In a pipelined processor, multiple instructions are simultaneously in different stages. If instruction I faults at stage 4, instructions I+1 and I+2 may already be in earlier stages having partially read or written registers. Achieving precise exceptions requires detecting the fault, preventing younger instructions from committing their results, and restoring the architectural state to the snapshot before instruction I — all without losing the pipeline's throughput advantage."
  explanation: "Out-of-order processors face an even harder version: instructions may complete out of order, so maintaining a precise exception point requires re-order buffers that track which results have been architecturally committed versus speculatively executed. This hardware complexity is the direct cost of supporting precise exceptions in high-performance designs — but it is a cost modern processors pay because virtual memory and debuggers depend on it."
```

## Explainer

From your study of basic interrupt and exception handling, you know that processors need a mechanism to respond to unexpected events — a key press, a division by zero, a page not in memory. **Exception handling architecture** is the hardware-level infrastructure that makes this possible reliably, even when exceptions arrive at inconvenient moments during instruction execution. The challenge is not just jumping to a handler; it is doing so in a way that preserves the processor's ability to resume exactly where it left off.

When an exception occurs, the processor must save enough state to return later. At minimum, this means saving the **program counter** (the address of the interrupted or faulting instruction) and the **processor status register** (which includes the condition flags and interrupt-enable bits you studied). Many architectures save these into dedicated registers (like MIPS's EPC and Cause registers) or push them onto a kernel stack (like x86). The processor then consults an **interrupt vector table** — an array of handler addresses in memory, indexed by exception type. Exception type 0 might point to the divide-by-zero handler, type 14 to the page fault handler, and so on. The processor loads the appropriate address from the table and begins executing the handler code.

The architecture must handle a subtle problem: **what happens when an exception occurs while another exception is being handled?** This requires a **priority scheme**. Hardware interrupts are typically assigned priority levels, and a higher-priority interrupt can preempt a lower-priority handler — this is a **nested exception**. A timer interrupt might preempt a keyboard handler, but a keyboard interrupt should not preempt a critical page fault handler. The processor's interrupt-enable flag and priority-level register control this nesting. When entering a handler, the processor may automatically disable lower-priority interrupts to prevent chaotic reentrance.

A particularly tricky aspect is **precise exceptions**: when an exception fires, the processor must appear as if all instructions before the faulting one have completed and none after it have started. In a simple single-cycle processor, this is trivial — one instruction is in flight at a time. But in pipelined and out-of-order processors, multiple instructions are in various stages of execution. Achieving precise exceptions requires the pipeline to flush partially completed instructions and restore the architectural state to the exact point of the fault. This is one of the most complex parts of modern processor design, but it is essential: the operating system's page fault handler, for example, must be able to fix the missing page and then re-execute the faulting instruction as if nothing happened. Without precise exceptions, virtual memory and debuggers would not work correctly.
