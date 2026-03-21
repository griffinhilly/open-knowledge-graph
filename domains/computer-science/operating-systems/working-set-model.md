---
id: working-set-model
title: Working Set Model and Thrashing
domain: computer-science
course: operating-systems
prerequisites:
- id: page-fault-processing
  type: hard
- id: memory-hierarchy-overview
  type: soft
tags:
- virtual-memory
- working-set
- thrashing
stage: advanced
status: draft
---

# Working Set Model and Thrashing

## Core Idea
The working set of a process is the pages it actively uses in a time window. Temporal and spatial locality mean programs reuse nearby pages; keeping the working set resident minimizes page faults. Thrashing occurs when working set exceeds available frames, causing excessive disk I/O and performance collapse.

## Questions

```yaml
- question: "A system has 1000 physical frames. Five processes are running, and their working sets require 150, 200, 250, 180, and 300 frames respectively. The OS tries to keep all five running. What happens?"
  type: multiple-choice
  options:
    - "The system runs efficiently — 1000 frames is close enough to the total demand of 1080 frames"
    - "The system enters thrashing because total working set demand (1080 frames) exceeds available physical memory (1000 frames)"
    - "The OS automatically compresses the largest working sets to fit within 1000 frames"
    - "Page fault rates increase moderately but performance stays acceptable with a good replacement algorithm"
  answer: 1
  explanation: "Total working set demand is 150+200+250+180+300 = 1080 frames, but only 1000 are available. Some process (or multiple processes) will be short on frames and page-fault constantly. While waiting for disk I/O, those processes block, the CPU appears idle, and the scheduler loads more processes — which are also short on frames. The system enters a vicious cycle where disk I/O dominates, CPU utilization collapses, and throughput falls catastrophically. No page replacement algorithm fixes a structural frame deficit."

- question: "The OS detects thrashing. Which action best addresses the root cause according to the working set model?"
  type: multiple-choice
  options:
    - "Switch to LRU page replacement to better approximate the working set"
    - "Increase the page size so fewer frames are needed to hold the same data"
    - "Suspend one or more processes entirely to reduce total working set demand below available physical memory"
    - "Increase the working set window Δ so each process has a larger, more stable resident set"
  answer: 2
  explanation: "Thrashing is a structural mismatch: total working set demand exceeds physical memory. Changing page replacement algorithms cannot fix this — the faulted pages are genuinely needed. Larger pages worsen internal fragmentation and don't solve the frame deficit. Increasing Δ makes each working set *larger*, worsening the mismatch. The only correct fix is to suspend one or more processes entirely, freeing their frames for the remaining processes so each active process can keep its working set fully resident."

- question: "Thrashing can be solved by using a more sophisticated page replacement algorithm that keeps the most important pages in memory."
  type: true-false
  answer: false
  explanation: "This is the core misconception about thrashing. Page replacement algorithms optimize within a given frame allocation — they decide which page to evict when a new one must be loaded. But thrashing occurs because the total number of frames is insufficient for all active working sets combined. Even a perfect oracle replacement algorithm cannot solve the problem: if a process needs 200 frames and has only 100, it will fault on every access to the other half of its working set, regardless of replacement strategy. The fix must be at the level of reducing the number of active processes."

- question: "Temporal locality — the tendency for programs to reuse recently accessed pages — is the property that makes the working set concept useful as a predictor of future page demand."
  type: true-false
  answer: true
  explanation: "The working set model depends on locality of reference: during any phase of execution, a program repeatedly uses only a small subset of its total pages (temporal locality), and those pages tend to be adjacent in address space (spatial locality). Because of temporal locality, the pages accessed in the last Δ time units are likely to be needed again in the next Δ time units. Without this property, the working set would change completely between measurements, making it useless as a prediction. Real programs exhibit strong locality due to loops, data structures, and function call patterns."

- question: "Why does CPU utilization paradoxically drop toward zero during thrashing, even though the system appears fully loaded and active?"
  type: short-answer
  answer: "During thrashing, processes spend almost all their time blocked waiting for disk I/O to satisfy page faults, not executing instructions. When a process page-faults, it blocks and the CPU idles. The scheduler, seeing the CPU idle, loads another process — which also immediately page-faults and blocks. Nearly all processes are simultaneously waiting for disk, the disk is flooded with page-fault requests, and the CPU has nothing runnable. CPU utilization is the fraction of time spent executing instructions, and since no process can execute until its pages are loaded, CPU utilization collapses."
  explanation: "This counterintuitive relationship — CPU utilization drops as system load increases beyond the thrashing threshold — is why CPU-only monitoring can miss thrashing. The correct diagnostic metrics are page fault rate, disk I/O queue depth, and I/O wait time. An OS monitoring working set sizes can detect when total demand exceeds physical memory before thrashing begins and preemptively suspend a process."
```

## Explainer

You already know what happens when a process accesses a page not currently in physical memory: a **page fault** fires, the OS fetches the page from disk, and execution resumes. A few page faults are normal — they are the cost of virtual memory's illusion that every process has unlimited address space. But what determines whether a process experiences a tolerable trickle of page faults or a catastrophic flood?

The answer lies in the **working set** — the collection of pages a process is actively using during a recent window of time. Think of it like the books you have open on your desk right now. You might own hundreds of books (your full address space), but at any given moment you are referencing only a handful (your working set). If your desk is big enough to hold all the books you need, you work efficiently. If your desk is too small, you constantly get up to retrieve books from the shelf — and your productivity collapses. The working set model, introduced by Peter Denning, formalizes this intuition. It defines the working set as the set of pages referenced in the last Δ time units (or last *n* memory references), where Δ is the **working set window**.

**Thrashing** is what happens when the system cannot keep each process's working set in memory simultaneously. Suppose five processes each need 200 frames to hold their working sets, but the system has only 800 frames total. At least one process will be short on frames. It page-faults constantly, and each fault means a slow disk read. While it waits for disk I/O, the CPU is idle, so the OS scheduler — trying to keep the CPU busy — may load yet another process, making the frame shortage worse. The system enters a vicious cycle: more processes competing for fewer frames, more page faults, more disk I/O, and CPU utilization paradoxically drops toward zero even though the system is fully loaded. This is thrashing, and it can bring a server to its knees.

The practical remedy is to monitor each process's working set size and ensure the system has enough total frames to accommodate all active working sets. If it does not, the OS should **suspend** (swap out) one or more processes entirely rather than let everyone thrash. This is called **medium-term scheduling** or load control. The working set model gives the OS a principled way to make that decision: measure working set sizes, sum them, and compare to available physical memory. If the sum exceeds capacity, reduce the degree of multiprogramming until the remaining processes can run without thrashing.
