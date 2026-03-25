---
id: context-switching-and-cpu-dispatch
title: Context Switching and CPU Dispatch
domain: computer-science
course: operating-systems
prerequisites:
- id: process-states-and-transitions
  type: hard
builds-toward:
- cpu-scheduling-basics
tags:
- scheduling
- performance
- cpu-management
stage: formal-systems
status: validated
---

# Context Switching and CPU Dispatch

## Core Idea
Context switching is the OS mechanism to pause one process and resume another. The OS saves registers, memory management state, and other CPU context to the process control block, loads another process's context, and branches to its instruction pointer. Context switching overhead is critical to OS performance and responsiveness.

## How It's Best Learned
Instrument a kernel or OS simulator to trace context switches and measure overhead such as cache misses and TLB flushes.

## Questions

```yaml
- question: "After a context switch from process A to process B, process B's first several memory accesses are unusually slow. The most likely cause is:"
  type: multiple-choice
  options:
    - "The dispatcher incorrectly saved process A's registers into process B's PCB"
    - "Switching address spaces flushed the TLB, forcing full page table lookups for each of process B's memory accesses"
    - "Process B's program counter was set to a wrong instruction during the dispatch"
    - "Process B's data had to be reloaded from disk rather than from RAM"
  answer: 1
  explanation: "When the OS switches between processes, it loads the new process's page table base register, which changes the virtual-to-physical address mappings the CPU uses. This invalidates the TLB (translation lookaside buffer) — the cache of recent address translations. Every subsequent memory access by process B must now walk the full page table to translate virtual addresses, which is much slower than a TLB hit. Additionally, B's working data is unlikely to be in the CPU cache, causing cache misses. These indirect costs — TLB cold start and cache cold start — often dominate the actual cost of context switching."

- question: "An OS designer is choosing between very short time slices (frequent context switching) and longer time slices (infrequent context switching). Which best captures the core tradeoff?"
  type: multiple-choice
  options:
    - "Short time slices give better responsiveness to interactive processes but waste CPU time on context switch overhead; longer time slices reduce overhead but hurt responsiveness"
    - "Short time slices reduce TLB misses by keeping each process's address translations warm; longer time slices cause more TLB invalidation"
    - "Longer time slices always produce better total throughput regardless of workload type"
    - "The tradeoff is irrelevant because modern CPUs perform context switches in nanoseconds with no measurable overhead"
  answer: 0
  explanation: "Each context switch imposes overhead: saving/restoring registers, flushing the TLB, and losing cache warmth. Very short time slices mean the CPU spends a significant fraction of its time on these overhead operations rather than useful computation. Very long time slices minimize overhead but mean processes wait a long time before getting CPU time, hurting responsiveness for interactive workloads. The scheduler's time quantum directly manages this tradeoff — there is no universally correct value."

- question: "Switching between two threads within the same process is cheaper than switching between two separate processes, because threads share the same address space and no TLB flush is required."
  type: true-false
  answer: true
  explanation: "The most expensive part of a context switch between processes is switching address spaces — loading a new page table base register, which invalidates the TLB. Threads within the same process share the same virtual address space, so thread switches don't require a page table switch and don't flush the TLB. Much of the CPU cache also remains valid because the threads share the same data. Only registers and the stack pointer need to be saved and restored. This is why threading is a more efficient concurrency mechanism than multi-processing for tasks that share data."

- question: "The primary cost of a context switch is the time taken to save and restore CPU registers, which typically takes several milliseconds on modern hardware."
  type: true-false
  answer: false
  explanation: "Register save and restore is fast — on the order of microseconds, not milliseconds. The dominant costs of context switching are indirect: the TLB flush (which forces expensive page table walks on subsequent memory accesses) and the cache cold start (the new process's working data is likely not in the CPU cache, causing cache misses that stall the pipeline). These indirect costs can be orders of magnitude larger than the direct register save/restore time. This is why minimizing context switch frequency matters even though the mechanical switch operation itself is quick."

- question: "Why is a context switch between two threads in the same process cheaper than a context switch between two separate processes, even though both require saving and restoring CPU registers?"
  type: short-answer
  answer: "Both types of switches require saving and restoring registers — that cost is the same. The difference is in address space management. Switching between processes requires loading a new page table base register, which changes the virtual-to-physical address mapping the CPU uses. This invalidates the entire TLB (translation lookaside buffer), so every subsequent memory access incurs a slow page table walk instead of a fast TLB hit. It also cold-starts the CPU cache for the new process's data. Thread switches within the same process skip this: threads share the same address space and page table, so no TLB flush occurs and cache remains largely valid. The shared address space is what makes threads a fundamentally cheaper unit of CPU switching."
  explanation: "This distinction explains the architectural motivation for threads: if you want concurrent execution with frequent task switching, threads within a shared address space pay only the register overhead, while processes pay the full cost including TLB invalidation. For data-sharing workloads, threads also avoid the interprocess communication overhead that separate processes would require."
```

## Explainer

From your study of process states and transitions, you know that a process can be in states like running, ready, or blocked, and that the OS moves processes between these states. Context switching is the mechanism that makes those transitions physically happen on the CPU. When the OS decides that process A should stop running and process B should start, it must perform a **context switch** — saving everything about A's execution state and loading everything about B's.

The "context" in a context switch is everything the CPU needs to resume a process exactly where it left off. This includes all **general-purpose registers** (the values the process was computing with), the **program counter** (which instruction it was about to execute), the **stack pointer** (where its call stack is), and **processor status flags** (like whether the last comparison was equal or the carry flag is set). It also includes memory management state: the page table base register that tells the CPU which virtual-to-physical address mappings to use. All of this is saved to a data structure called the **process control block (PCB)**, which the OS maintains for every process. When switching to process B, the OS loads B's PCB values into the CPU registers and jumps to B's program counter. From B's perspective, it never stopped running.

The **dispatcher** is the OS component that performs the actual context switch. When the scheduler decides which process should run next, the dispatcher does the low-level work: it saves the current context, restores the new process's context, switches to the new process's address space (updating the page table register), and transfers control to the new process. The time this takes — the **dispatch latency** — is pure overhead during which no useful work is done. On modern hardware, the register save/restore itself is fast (microseconds), but the indirect costs are significant: switching address spaces invalidates the **translation lookaside buffer (TLB)**, forcing expensive page table lookups on subsequent memory accesses, and the new process's data is unlikely to be in the **CPU cache**, causing cache misses that stall the pipeline.

This overhead is why context switch frequency matters for system design. An OS that switches too aggressively (very short time slices) spends a disproportionate amount of time on overhead rather than useful computation. An OS that switches too rarely keeps processes waiting and hurts responsiveness. The scheduler's time quantum — which you will encounter in scheduling algorithms — represents this tradeoff directly. Context switching also explains why threads within the same process are cheaper to switch between than separate processes: threads share an address space, so the TLB does not need to be flushed and much of the cache remains valid.
