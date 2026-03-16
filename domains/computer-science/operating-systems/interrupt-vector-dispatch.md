---
id: interrupt-vector-dispatch
title: Interrupt Vector Tables and Dispatch
domain: computer-science
course: operating-systems
prerequisites:
- id: interrupt-exception-handling
  type: hard
- id: cpu-control-path-design
  type: soft
builds-toward:
- exception-handling-os-internals
tags:
- interrupts
- hardware
- dispatch
stage: formal-systems
status: draft
---

# Interrupt Vector Tables and Dispatch

## Core Idea
When a hardware interrupt or exception occurs, the CPU consults an interrupt vector table indexed by interrupt number to find the handler address. This enables the OS to dispatch control rapidly without querying what caused the interrupt.

## Explainer

From your study of interrupt and exception handling, you know that hardware devices signal the CPU when they need attention — a keyboard press, a disk transfer completing, a timer tick. The CPU must stop what it is doing and jump to the appropriate handler code in the operating system. The question is: how does the CPU know *where* to jump? It cannot run a search through kernel code looking for the right handler. Interrupts happen millions of times per second, so the dispatch mechanism must be essentially instant.

The answer is the **interrupt vector table** (IVT), sometimes called the **interrupt descriptor table** (IDT) on x86 processors. This is simply an array stored at a known memory address, where each entry corresponds to a specific interrupt number. Entry 0 might point to the divide-by-zero exception handler. Entry 14 points to the page fault handler. Entry 32 might point to the timer interrupt handler. When interrupt number *k* fires, the CPU indexes into the table at position *k*, reads the address stored there, and jumps to that address. The entire dispatch is a single array lookup — no conditionals, no searching, just one indexed memory access followed by a jump.

The operating system populates the interrupt vector table during boot. For each interrupt number, the kernel writes the address of the corresponding handler function into the table. Some entries are fixed by the hardware architecture — for instance, on x86, interrupts 0–31 are reserved for CPU exceptions (divide error, page fault, general protection fault, etc.). The remaining entries (32–255 on x86) are available for hardware devices and software interrupts. When a device like a network card is initialized, its driver registers a handler by writing the handler's address into the appropriate slot. The CPU itself knows the table's base address because the OS loads it into a special register (the IDTR on x86) during startup.

The dispatch process involves more than just jumping to a handler. When an interrupt fires, the CPU automatically saves critical state — at minimum the instruction pointer and flags register — onto the stack so it can resume the interrupted code later. On x86, the CPU also switches to a kernel stack if the interrupt occurred while running user code, enforcing the privilege boundary you studied in kernel mode and privilege levels. After the handler finishes (typically by executing an `iret` instruction), the saved state is restored and execution resumes exactly where it left off. This save-dispatch-handle-restore cycle is the fundamental mechanism by which the OS responds to hardware events while maintaining the illusion that user programs run uninterrupted.
