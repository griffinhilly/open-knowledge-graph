---
id: thrashing-and-working-set
title: Thrashing and the Working Set Model
domain: computer-science
course: operating-systems
prerequisites:
- id: page-replacement-algorithms
  type: hard
tags:
- thrashing
- working-set
- locality
- frame-allocation
- multiprogramming-degree
stage: formal-systems
status: validated
---

# Thrashing and the Working Set Model

## Core Idea
Thrashing occurs when a system spends more time handling page faults than executing useful work — processes constantly page in and page out, and CPU utilization collapses. The cause is over-commitment: too many processes compete for too few frames. Denning's Working Set Model addresses this by tracking the set of pages a process has referenced in the last Δ time units (the working set), which captures its locality of reference. The OS should allocate each process at least its working set size worth of frames; if the sum of working sets exceeds available frames, the OS should reduce the degree of multiprogramming (suspend processes) rather than allow thrashing.

## How It's Best Learned
Plot CPU utilization against degree of multiprogramming. Explain the knee of the curve where thrashing begins. Then compute working set sizes for a sample reference string at different window sizes.

## Common Misconceptions
- Adding more processes to a thrashing system makes it worse, not better; reducing multiprogramming is the correct response.
- The working set window Δ must be chosen carefully; too small misses the current locality, too large includes stale references.

## Explainer

From your study of page replacement algorithms, you know that when a process accesses a page not currently in physical memory, a **page fault** occurs: the OS must load the page from disk, evict another page if frames are full, and then resume the process. Page faults are expensive — disk access is thousands of times slower than memory access. Page replacement algorithms like LRU and FIFO try to minimize faults by making smart eviction choices. But there is a deeper problem that no replacement algorithm can solve on its own: what happens when there simply are not enough frames to go around?

**Thrashing** is what happens when the system crosses that line. Imagine ten students trying to share three textbooks, where each student needs at least two books at any given time. They spend all their time passing books around and none of it studying. That is thrashing: processes spend more time waiting for pages to be swapped in from disk than executing instructions. CPU utilization collapses — paradoxically, the system appears idle even though it is desperately busy servicing page faults. The OS, seeing low CPU utilization, may respond by admitting more processes (increasing the degree of multiprogramming), which makes thrashing worse by further dividing the already insufficient frames.

The key insight is **locality of reference**: at any given time, a process only actively uses a small subset of its pages. A word processor editing a document is not accessing its spell-check code, print-formatting routines, and file-import modules simultaneously. **Denning's Working Set Model** captures this by defining the **working set** as the set of pages a process has referenced within the last Δ time units (a sliding window over the reference string). If a process's working set contains 50 pages, it needs at least 50 frames to run without excessive page faults. The window parameter Δ must be tuned: too small and the working set misses pages the process will need momentarily; too large and it includes stale pages from a previous phase of execution.

The operating system's job is to sum up the working set sizes of all active processes and compare that total to the number of available physical frames. If the total exceeds capacity, thrashing is imminent. The correct response is counterintuitive: **reduce** the degree of multiprogramming by suspending one or more processes entirely (swapping them out to disk), freeing their frames for the remaining processes. Fewer processes each running efficiently produces more useful work than many processes all thrashing. This is the critical lesson — adding more work to an overloaded system does not just slow it down linearly; it can cause a catastrophic collapse in throughput where almost no useful computation occurs.
