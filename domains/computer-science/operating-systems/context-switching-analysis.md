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

## Questions

```yaml
- question: "On a system where context switches happen every 1ms, what performance problem is most likely to dominate?"
  type: multiple-choice
  options:
    - "Increased memory usage from storing too many PCBs simultaneously"
    - "Cache and TLB warming overhead that reduces effective CPU time for useful work"
    - "Longer average wait times because processes are preempted too often"
    - "Excessive kernel memory allocations for page table entries"
  answer: 1
  explanation: "When switches are very frequent, the indirect costs dominate: each switch invalidates TLB entries and evicts the outgoing process's working set from cache. The incoming process then experiences a burst of cache misses and TLB misses until both warm up. Processes spend a disproportionate fraction of their time recovering from cold starts rather than executing useful work. PCB storage and page table memory are small fixed costs per process, not per-switch costs."

- question: "A developer proposes replacing a multi-process server (one process per connection) with a multi-threaded server (one thread per connection). Which aspect of context switching best justifies this change?"
  type: multiple-choice
  options:
    - "Threads have larger register files, so save/restore takes less time"
    - "Thread switches within the same process don't require changing the page table or flushing TLB entries, since threads share an address space"
    - "The OS scheduler is specifically optimized for threads, not processes"
    - "Threads eliminate the need to save floating-point registers"
  answer: 1
  explanation: "The key advantage is shared address space. Process switches require loading the new process's page table base register and (often) flushing TLB entries, because each process has a distinct virtual address space. Thread switches within the same process skip this entirely — the address space is unchanged. This eliminates the most expensive indirect cost of context switching: TLB invalidation and the cold-start penalty that follows."

- question: "TLB flushes after a context switch cause the incoming process to experience many slow page table walks until the TLB warms up again."
  type: true-false
  answer: true
  explanation: "True. The TLB caches virtual-to-physical address translations. When the page table changes (new process's address space), cached TLB entries are invalid and must be flushed. The incoming process's first memory accesses find an empty TLB and incur full page table walks — significantly slower than TLB hits. This cold-start penalty persists until the TLB repopulates with the new process's working set. ASIDs can reduce (but not eliminate) this penalty."

- question: "The direct cost of saving and restoring registers is typically the dominant performance cost of a context switch."
  type: true-false
  answer: false
  explanation: "False. Register save/restore (the direct cost) involves hundreds of bytes of memory operations and takes only a few microseconds — relatively small. The indirect costs typically dominate: TLB invalidation forces slow page table walks on subsequent memory accesses, and cache pollution means the incoming process's working set must be refetched, imposing thousands of cycles of penalty. This is why frequent context switching is so harmful to throughput even on fast processors."

- question: "Why do thread switches within the same process cost less than process switches between different processes?"
  type: short-answer
  answer: "Thread switches don't require changing the memory management context: all threads in a process share the same virtual address space and page table. The page table base register is unchanged, and TLB entries remain valid for the new thread. Process switches must load the new process's page table (different address space), which may flush TLB entries and forces the incoming process to rebuild its TLB cache — the most expensive indirect cost of context switching."
  explanation: "Context-switch cost scales with how much 'context' actually changes. Threads share address space, so address-translation context is fully preserved. Process switches break address-translation context completely, incurring TLB and cache cold-start penalties that can cost thousands of cycles."
```

## Explainer

You already understand context switching at a conceptual level from your prerequisites: the OS stops one process, saves its state, and loads another process's state so the CPU can run it. What this topic examines is *how that mechanism actually works at the hardware level* and *why it costs more than you might initially think*. The direct costs are only part of the story — the indirect costs often dominate.

The **direct cost** is the work the OS must do during the switch itself. The kernel saves the outgoing process's **register file** — the program counter (where execution was), the stack pointer, general-purpose registers, floating-point registers, and any special status registers — into a kernel data structure called the **process control block** (PCB) or task struct. It then loads the incoming process's registers from its PCB. On a modern x86-64 processor with dozens of general-purpose, floating-point, and vector registers, this is hundreds of bytes of memory reads and writes. The OS must also update memory management structures: loading the new process's page table base register, which tells the MMU how to translate virtual addresses to physical addresses. This direct work typically takes a few microseconds.

The **indirect costs** are far more significant. When the page table changes, the **TLB** (Translation Lookaside Buffer) — a cache of recent virtual-to-physical address translations — becomes invalid, because the new process has a different address space. The CPU must flush some or all TLB entries, meaning the new process starts with a "cold" TLB and every memory access triggers a slow page table walk until the TLB warms up. Modern CPUs mitigate this with **ASIDs** (Address Space Identifiers) that tag TLB entries by process, allowing some entries to survive across switches. But the CPU's data and instruction **caches** suffer the same warming problem: the incoming process's working set is almost certainly not in cache, so it experiences a burst of cache misses as it resumes. This "cache pollution" can slow the incoming process for thousands of cycles after the switch.

These costs directly affect scheduling decisions. If the OS switches too frequently (short time quanta), processes spend a significant fraction of their time paying switching overhead rather than doing useful work. If it switches too rarely (long time quanta), interactive responsiveness suffers — a user typing at a terminal doesn't want to wait 100ms for their keystroke to be processed. Thread switches within the same process are cheaper than process switches because threads share an address space, so the page table and TLB don't need to change. This is one reason why multithreaded designs are favored over multiprocess designs for workloads that require frequent concurrency switches. Understanding these costs is essential for analyzing scheduling algorithms: a scheduler that minimizes context switches (like SJF) gains a real performance advantage beyond just the theoretical reduction in average wait time.
