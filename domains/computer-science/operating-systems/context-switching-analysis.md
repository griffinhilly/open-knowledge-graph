---
id: context-switching-analysis
title: 'Context Switching: Mechanism and Cost'
domain: computer-science
course: operating-systems
prerequisites:
- id: context-switching-and-cpu-dispatch
  type: hard
- id: process-model-formalization
  type: hard
builds-toward:
- scheduling-algorithm-analysis
- cpu-cache-implications
tags:
- context-switch
- scheduling
- performance
stage: formal-systems
status: draft
---

# Context Switching: Mechanism and Cost

## Core Idea
Context switching saves the current process state (registers, program counter, memory management info) and loads the next process's state. The cost includes register save/restore, TLB flushes, and cache pollution; designers must balance responsiveness with switching overhead.

## Explainer

You already understand context switching at a conceptual level from your prerequisites: the OS stops one process, saves its state, and loads another process's state so the CPU can run it. What this topic examines is *how that mechanism actually works at the hardware level* and *why it costs more than you might initially think*. The direct costs are only part of the story — the indirect costs often dominate.

The **direct cost** is the work the OS must do during the switch itself. The kernel saves the outgoing process's **register file** — the program counter (where execution was), the stack pointer, general-purpose registers, floating-point registers, and any special status registers — into a kernel data structure called the **process control block** (PCB) or task struct. It then loads the incoming process's registers from its PCB. On a modern x86-64 processor with dozens of general-purpose, floating-point, and vector registers, this is hundreds of bytes of memory reads and writes. The OS must also update memory management structures: loading the new process's page table base register, which tells the MMU how to translate virtual addresses to physical addresses. This direct work typically takes a few microseconds.

The **indirect costs** are far more significant. When the page table changes, the **TLB** (Translation Lookaside Buffer) — a cache of recent virtual-to-physical address translations — becomes invalid, because the new process has a different address space. The CPU must flush some or all TLB entries, meaning the new process starts with a "cold" TLB and every memory access triggers a slow page table walk until the TLB warms up. Modern CPUs mitigate this with **ASIDs** (Address Space Identifiers) that tag TLB entries by process, allowing some entries to survive across switches. But the CPU's data and instruction **caches** suffer the same warming problem: the incoming process's working set is almost certainly not in cache, so it experiences a burst of cache misses as it resumes. This "cache pollution" can slow the incoming process for thousands of cycles after the switch.

These costs directly affect scheduling decisions. If the OS switches too frequently (short time quanta), processes spend a significant fraction of their time paying switching overhead rather than doing useful work. If it switches too rarely (long time quanta), interactive responsiveness suffers — a user typing at a terminal doesn't want to wait 100ms for their keystroke to be processed. Thread switches within the same process are cheaper than process switches because threads share an address space, so the page table and TLB don't need to change. This is one reason why multithreaded designs are favored over multiprocess designs for workloads that require frequent concurrency switches. Understanding these costs is essential for analyzing scheduling algorithms: a scheduler that minimizes context switches (like SJF) gains a real performance advantage beyond just the theoretical reduction in average wait time.
