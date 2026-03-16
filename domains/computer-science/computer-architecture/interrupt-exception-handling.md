---
id: interrupt-exception-handling
title: Interrupt and Exception Handling
domain: computer-science
course: computer-architecture
prerequisites:
- id: interrupts-and-dma
  type: hard
- id: instruction-fetch-decode-execute
  type: soft
builds-toward:
- io-architecture-system-integration
- power-thermal-performance-metrics
tags:
- interrupts
- exceptions
- handling
- synchronization
stage: formal-systems
status: draft
---

# Interrupt and Exception Handling

## Core Idea
Interrupts signal asynchronous events (I/O, timer); exceptions signal synchronous faults (divide-by-zero, page fault). Both cause context switches, saving processor state and jumping to handler code. Priority and masking manage multiple simultaneous events.

## Explainer

From your study of interrupts and DMA, you know that external devices need a way to get the processor's attention without the CPU constantly polling every peripheral. Interrupt and exception handling is the complete mechanism that makes this possible — not just the signal itself, but the entire sequence the processor follows when something demands immediate attention. The key distinction to internalize is between **interrupts** (asynchronous, caused by external events like a keyboard press or a network packet arriving) and **exceptions** (synchronous, triggered by the instruction currently executing, such as dividing by zero or accessing an invalid memory address).

When either event occurs, the processor must perform a precise **context switch**. It saves the current state — the program counter, status registers, and sometimes general-purpose registers — onto a stack or into dedicated save areas. This is critical because the handler code will use the same registers the interrupted program was using, and without saving them, the original program's data would be destroyed. After saving state, the processor jumps to a **handler routine** whose address is found through an **interrupt vector table** — essentially an array of function pointers indexed by the interrupt or exception number.

Not all interrupts are equally urgent. A timer tick should not preempt a handler dealing with a critical hardware fault. This is where **priority levels** and **masking** come in. Each interrupt source is assigned a priority, and the processor only services a new interrupt if its priority exceeds that of the currently running handler. **Maskable interrupts** can be temporarily disabled — for example, during a critical section of an operating system kernel — while **non-maskable interrupts** (NMIs) cannot be ignored and are reserved for events like hardware failures or watchdog timeouts.

The distinction between faults, traps, and aborts further refines exception handling. A **fault** is recoverable and restartable — the classic example is a page fault, where the OS loads the missing page from disk and then re-executes the faulting instruction as if nothing happened. A **trap** is intentional, triggered by instructions like system calls, and execution continues at the next instruction after the trap. An **abort** signals an unrecoverable error, typically terminating the process. Understanding these categories explains why your operating system can seamlessly handle missing memory pages while simultaneously crashing a program that corrupts its own stack — both are exceptions, but the handler's response differs based on the type.
