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

## Explainer

You already know what happens when a process accesses a page not currently in physical memory: a **page fault** fires, the OS fetches the page from disk, and execution resumes. A few page faults are normal — they are the cost of virtual memory's illusion that every process has unlimited address space. But what determines whether a process experiences a tolerable trickle of page faults or a catastrophic flood?

The answer lies in the **working set** — the collection of pages a process is actively using during a recent window of time. Think of it like the books you have open on your desk right now. You might own hundreds of books (your full address space), but at any given moment you are referencing only a handful (your working set). If your desk is big enough to hold all the books you need, you work efficiently. If your desk is too small, you constantly get up to retrieve books from the shelf — and your productivity collapses. The working set model, introduced by Peter Denning, formalizes this intuition. It defines the working set as the set of pages referenced in the last Δ time units (or last *n* memory references), where Δ is the **working set window**.

**Thrashing** is what happens when the system cannot keep each process's working set in memory simultaneously. Suppose five processes each need 200 frames to hold their working sets, but the system has only 800 frames total. At least one process will be short on frames. It page-faults constantly, and each fault means a slow disk read. While it waits for disk I/O, the CPU is idle, so the OS scheduler — trying to keep the CPU busy — may load yet another process, making the frame shortage worse. The system enters a vicious cycle: more processes competing for fewer frames, more page faults, more disk I/O, and CPU utilization paradoxically drops toward zero even though the system is fully loaded. This is thrashing, and it can bring a server to its knees.

The practical remedy is to monitor each process's working set size and ensure the system has enough total frames to accommodate all active working sets. If it does not, the OS should **suspend** (swap out) one or more processes entirely rather than let everyone thrash. This is called **medium-term scheduling** or load control. The working set model gives the OS a principled way to make that decision: measure working set sizes, sum them, and compare to available physical memory. If the sum exceeds capacity, reduce the degree of multiprogramming until the remaining processes can run without thrashing.
