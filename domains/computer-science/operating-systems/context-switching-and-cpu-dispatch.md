---
id: context-switching-and-cpu-dispatch
title: Context Switching and CPU Dispatch
domain: computer-science
course: operating-systems
prerequisites:
- id: process-states-and-transitions
  type: hard
builds-toward:
- cpu-scheduling-basic-concepts
tags:
- scheduling
- performance
- cpu-management
stage: formal-systems
status: draft
---

# Context Switching and CPU Dispatch

## Core Idea
Context switching is the OS mechanism to pause one process and resume another. The OS saves registers, memory management state, and other CPU context to the process control block, loads another process's context, and branches to its instruction pointer. Context switching overhead is critical to OS performance and responsiveness.

## How It's Best Learned
Instrument a kernel or OS simulator to trace context switches and measure overhead such as cache misses and TLB flushes.

## Explainer

From your study of process states and transitions, you know that a process can be in states like running, ready, or blocked, and that the OS moves processes between these states. Context switching is the mechanism that makes those transitions physically happen on the CPU. When the OS decides that process A should stop running and process B should start, it must perform a **context switch** — saving everything about A's execution state and loading everything about B's.

The "context" in a context switch is everything the CPU needs to resume a process exactly where it left off. This includes all **general-purpose registers** (the values the process was computing with), the **program counter** (which instruction it was about to execute), the **stack pointer** (where its call stack is), and **processor status flags** (like whether the last comparison was equal or the carry flag is set). It also includes memory management state: the page table base register that tells the CPU which virtual-to-physical address mappings to use. All of this is saved to a data structure called the **process control block (PCB)**, which the OS maintains for every process. When switching to process B, the OS loads B's PCB values into the CPU registers and jumps to B's program counter. From B's perspective, it never stopped running.

The **dispatcher** is the OS component that performs the actual context switch. When the scheduler decides which process should run next, the dispatcher does the low-level work: it saves the current context, restores the new process's context, switches to the new process's address space (updating the page table register), and transfers control to the new process. The time this takes — the **dispatch latency** — is pure overhead during which no useful work is done. On modern hardware, the register save/restore itself is fast (microseconds), but the indirect costs are significant: switching address spaces invalidates the **translation lookaside buffer (TLB)**, forcing expensive page table lookups on subsequent memory accesses, and the new process's data is unlikely to be in the **CPU cache**, causing cache misses that stall the pipeline.

This overhead is why context switch frequency matters for system design. An OS that switches too aggressively (very short time slices) spends a disproportionate amount of time on overhead rather than useful computation. An OS that switches too rarely keeps processes waiting and hurts responsiveness. The scheduler's time quantum — which you will encounter in scheduling algorithms — represents this tradeoff directly. Context switching also explains why threads within the same process are cheaper to switch between than separate processes: threads share an address space, so the TLB does not need to be flushed and much of the cache remains valid.
