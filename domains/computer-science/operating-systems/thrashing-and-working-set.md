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

## Questions

```yaml
- question: "An OS notices CPU utilization has dropped to 3% despite having many active processes. Processes are constantly blocked waiting for I/O. What is the most likely cause, and what is the correct response?"
  type: multiple-choice
  options:
    - "The CPU is mostly idle — admit more processes to increase utilization and throughput"
    - "Thrashing — too many processes competing for too few frames; suspend some processes to free their frames for the remaining ones"
    - "The page replacement algorithm is choosing poor eviction victims; switch to LRU"
    - "The disk is the bottleneck; upgrading to an SSD will solve the problem"
  answer: 1
  explanation: "Low CPU utilization combined with constant I/O blocking is the signature of thrashing: processes are spending all their time waiting for pages to be swapped in from disk, not executing instructions. Option A is the classic wrong response — the OS might see low CPU utilization and admit more processes, but this makes thrashing catastrophically worse by further dividing the insufficient frames. The correct fix is to reduce multiprogramming: suspend processes entirely to free their frames, allowing the remaining processes to each hold their working sets. Option C is wrong because no replacement algorithm helps when frames are simply insufficient."

- question: "The working set model defines a process's working set W(t, Δ) as..."
  type: multiple-choice
  options:
    - "All pages the process has ever accessed during its entire lifetime"
    - "The maximum number of frames the OS should ever allocate to this process"
    - "The set of pages referenced by the process within the last Δ time units"
    - "Pages currently loaded in physical memory that belong to this process"
  answer: 2
  explanation: "The working set is a sliding window over recent memory references: W(t, Δ) is the set of distinct pages referenced in the interval (t−Δ, t). This captures the process's current locality — the pages it actively needs right now, not all pages it has ever used. The window size Δ must be tuned carefully: too small and the working set misses pages the process will need momentarily; too large and it includes stale pages from an earlier execution phase. The key use of the working set is to determine minimum frame allocation: a process needs at least |W(t, Δ)| frames to run without excessive faults."

- question: "When a system is thrashing, the correct response is to reduce the degree of multiprogramming by suspending processes, not to switch to a better page replacement algorithm."
  type: true-false
  answer: true
  explanation: "Page replacement algorithms (LRU, FIFO, Clock) choose which page to evict when a fault occurs — they assume frames are scarce and do the best possible with what exists. But thrashing occurs precisely when total frame demand exceeds total supply: no replacement algorithm can conjure frames that don't exist. The only real fix is to reduce demand by suspending one or more processes, freeing their frames. A better replacement algorithm reduces fault *rate* within a given allocation; it cannot solve the fundamental over-commitment that causes thrashing."

- question: "During thrashing, CPU utilization is very high because the CPU is constantly busy handling page fault interrupts."
  type: true-false
  answer: false
  explanation: "This is the counterintuitive part of thrashing: CPU utilization collapses. When processes are thrashing, they spend almost all their time blocked waiting for pages to be swapped in from disk. The CPU is sitting idle while the disk does endless swap I/O. The system appears slow AND underutilized simultaneously. This is what makes thrashing easy to misdiagnose: low CPU utilization looks like there's spare capacity, tempting the OS to admit more processes — exactly the wrong response."

- question: "A system begins thrashing. Explain why reducing the degree of multiprogramming solves the problem when better page replacement algorithms cannot."
  type: short-answer
  answer: "Thrashing occurs because the sum of all active processes' working set sizes exceeds available physical frames — there simply aren't enough frames to satisfy everyone's locality needs simultaneously. Page replacement algorithms choose optimally among bad options (which page to evict), but they cannot create new frames. Reducing multiprogramming by suspending processes frees their entire frame allocation, allowing the remaining processes to each hold their working sets in memory. Each remaining process can now run without constant faulting, and total useful throughput rises even though fewer processes are 'active.'"
  explanation: "The key insight is that thrashing is a supply/demand problem, not an allocation strategy problem. Page replacement is an allocation strategy; it works within a fixed supply. The working set model addresses supply: it tells the OS how much supply each process needs, and if total need exceeds supply, the OS must reduce demand (suspend processes) rather than reallocate the insufficient supply."
```

## Explainer

From your study of page replacement algorithms, you know that when a process accesses a page not currently in physical memory, a **page fault** occurs: the OS must load the page from disk, evict another page if frames are full, and then resume the process. Page faults are expensive — disk access is thousands of times slower than memory access. Page replacement algorithms like LRU and FIFO try to minimize faults by making smart eviction choices. But there is a deeper problem that no replacement algorithm can solve on its own: what happens when there simply are not enough frames to go around?

**Thrashing** is what happens when the system crosses that line. Imagine ten students trying to share three textbooks, where each student needs at least two books at any given time. They spend all their time passing books around and none of it studying. That is thrashing: processes spend more time waiting for pages to be swapped in from disk than executing instructions. CPU utilization collapses — paradoxically, the system appears idle even though it is desperately busy servicing page faults. The OS, seeing low CPU utilization, may respond by admitting more processes (increasing the degree of multiprogramming), which makes thrashing worse by further dividing the already insufficient frames.

The key insight is **locality of reference**: at any given time, a process only actively uses a small subset of its pages. A word processor editing a document is not accessing its spell-check code, print-formatting routines, and file-import modules simultaneously. **Denning's Working Set Model** captures this by defining the **working set** as the set of pages a process has referenced within the last Δ time units (a sliding window over the reference string). If a process's working set contains 50 pages, it needs at least 50 frames to run without excessive page faults. The window parameter Δ must be tuned: too small and the working set misses pages the process will need momentarily; too large and it includes stale pages from a previous phase of execution.

The operating system's job is to sum up the working set sizes of all active processes and compare that total to the number of available physical frames. If the total exceeds capacity, thrashing is imminent. The correct response is counterintuitive: **reduce** the degree of multiprogramming by suspending one or more processes entirely (swapping them out to disk), freeing their frames for the remaining processes. Fewer processes each running efficiently produces more useful work than many processes all thrashing. This is the critical lesson — adding more work to an overloaded system does not just slow it down linearly; it can cause a catastrophic collapse in throughput where almost no useful computation occurs.
