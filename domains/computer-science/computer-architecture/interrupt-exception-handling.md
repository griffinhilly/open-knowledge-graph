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

## Questions

```yaml
- question: "A program accesses a memory address whose page has been swapped to disk. The OS loads the page and the program continues as if nothing happened, re-executing the same instruction. What type of exception is this?"
  type: multiple-choice
  options:
    - "An abort — the unrecoverable error is silently corrected by the OS before the program notices"
    - "A trap — execution resumes at the instruction after the exception, as with a system call"
    - "A fault — it is recoverable, and the handler re-executes the faulting instruction after resolving the condition"
    - "A maskable interrupt — the OS can suppress this temporarily during critical sections"
  answer: 2
  explanation: "A page fault is the classic example of a fault: a recoverable exception where the handler can fix the condition (loading the missing page from disk) and then re-execute the original instruction as if nothing happened. This is precisely what makes demand paging transparent to programs. A trap resumes at the next instruction (used for intentional events like system calls). An abort signals an unrecoverable error. Calling it an interrupt is wrong because it is triggered by the current instruction (synchronous), not by an external device (asynchronous)."

- question: "Why must the processor save its state — program counter, status registers, general-purpose registers — before jumping to an interrupt handler?"
  type: multiple-choice
  options:
    - "So the interrupt vector table knows which handler routine address to load"
    - "Because the handler code will use the same registers as the interrupted program, and without saving them, the original program's data would be destroyed"
    - "So the priority level of the new interrupt can be determined from the interrupted program's status"
    - "Because non-maskable interrupts require the full register set to verify their authenticity"
  answer: 1
  explanation: "The handler is just another piece of code running on the same processor using the same registers. If the processor jumped to the handler without saving the interrupted program's register contents, the handler would overwrite them — and when the original program resumed, its data would be garbage. The save/restore cycle (context switch) is what makes it possible for interrupt handling to be transparent to the interrupted program. This is the architectural guarantee that makes I/O devices, timers, and OS services coexist with user programs."

- question: "A divide-by-zero error is classified as an exception rather than an interrupt because it is triggered by the currently executing instruction, not by an external device."
  type: true-false
  answer: true
  explanation: "This is the core distinction: exceptions are synchronous — they are caused by the instruction currently being executed (divide-by-zero, invalid memory access, illegal instruction). Interrupts are asynchronous — they are caused by external events (keyboard presses, network packets, timer ticks) that arrive independently of which instruction is executing. A divide-by-zero will always fault at exactly the same point in program execution; a keyboard interrupt can arrive at any time. This distinction determines how the processor's response is designed."

- question: "Maskable interrupts are the appropriate mechanism for handling the most critical hardware failures, such as power-supply faults, because they can be prioritized above all other events."
  type: true-false
  answer: false
  explanation: "Non-maskable interrupts (NMIs) are reserved for truly critical, unignorable hardware events precisely because maskable interrupts can be disabled by software. During a critical OS kernel section, software may mask interrupts — if power-supply faults or catastrophic hardware failures used maskable interrupts, they could be silently ignored at the worst possible moment. NMIs bypass the masking mechanism entirely: they cannot be disabled, ensuring the processor always responds to the most critical events regardless of software state."

- question: "What is the key difference between an interrupt and an exception, and why does the distinction matter for how the processor responds?"
  type: short-answer
  answer: "An interrupt is asynchronous — triggered by an external event (I/O device, timer) independent of the currently executing instruction. An exception is synchronous — triggered by the instruction currently executing (divide-by-zero, page fault, illegal opcode). The distinction matters for response design: synchronous exceptions are tied to a specific instruction and the processor knows exactly what was executing and can potentially re-execute it (faults) or continue from the next instruction (traps). Asynchronous interrupts arrive at unpredictable points and must be handled by saving full program state before doing anything."
  explanation: "The interrupt/exception distinction shapes the entire interrupt-handling architecture. Faults must be restartable, which requires saving the faulting instruction's address and restoring it exactly so the instruction re-executes after the handler resolves the condition. Traps continue from the next instruction. Asynchronous interrupts must save state without knowing what the program was about to do next. These are different contracts with the interrupted program, implemented differently at the hardware level."
```

## Explainer

From your study of interrupts and DMA, you know that external devices need a way to get the processor's attention without the CPU constantly polling every peripheral. Interrupt and exception handling is the complete mechanism that makes this possible — not just the signal itself, but the entire sequence the processor follows when something demands immediate attention. The key distinction to internalize is between **interrupts** (asynchronous, caused by external events like a keyboard press or a network packet arriving) and **exceptions** (synchronous, triggered by the instruction currently executing, such as dividing by zero or accessing an invalid memory address).

When either event occurs, the processor must perform a precise **context switch**. It saves the current state — the program counter, status registers, and sometimes general-purpose registers — onto a stack or into dedicated save areas. This is critical because the handler code will use the same registers the interrupted program was using, and without saving them, the original program's data would be destroyed. After saving state, the processor jumps to a **handler routine** whose address is found through an **interrupt vector table** — essentially an array of function pointers indexed by the interrupt or exception number.

Not all interrupts are equally urgent. A timer tick should not preempt a handler dealing with a critical hardware fault. This is where **priority levels** and **masking** come in. Each interrupt source is assigned a priority, and the processor only services a new interrupt if its priority exceeds that of the currently running handler. **Maskable interrupts** can be temporarily disabled — for example, during a critical section of an operating system kernel — while **non-maskable interrupts** (NMIs) cannot be ignored and are reserved for events like hardware failures or watchdog timeouts.

The distinction between faults, traps, and aborts further refines exception handling. A **fault** is recoverable and restartable — the classic example is a page fault, where the OS loads the missing page from disk and then re-executes the faulting instruction as if nothing happened. A **trap** is intentional, triggered by instructions like system calls, and execution continues at the next instruction after the trap. An **abort** signals an unrecoverable error, typically terminating the process. Understanding these categories explains why your operating system can seamlessly handle missing memory pages while simultaneously crashing a program that corrupts its own stack — both are exceptions, but the handler's response differs based on the type.
